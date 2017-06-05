import requests
import json


# search text in Google Books API
def search(text):
    # replace spaces with '+' for url
    text = ['+' if x == ' ' else x for x in list(text)]
    text = ''.join(text)

    # create url for getting request from Google Books API
    url = 'https://www.googleapis.com/books/v1/volumes?q='+text
    # get json from url
    r = requests.get(url)
    data = json.loads(r.text)
    return data


# returns lists of dictionaries with title, subtitle and list of authors
def search_json(data):
    books = []
    # print(data['items'])

    # get needed elements from json
    for item in data['items']:
        info = item['volumeInfo']
        title = info.get('title', None)
        subtitle = info.get('subtitle', None)
        authors = info.get('authors', None)  # list of authors
        books.append({'title': title, 'subtitle': subtitle, 'authors': authors})

    return books


# compares titles - if equal returns true, if not false
def compare_title(item, title):
    item_title = item['title']
    item_subtitle = item['subtitle']

    if item_title is None:
        return False
    else:
        return item_title == title or \
               item_title+str(item_subtitle) == title or \
               item_title+' '+str(item_subtitle) == title


# compares authors - if equal true, if not false
def compare_author(item, author):
    item_authors = item['authors']
    if item_authors is None:
        return False

    # comparison of words
    author_data = author.split(' ', 1)
    if len(author_data) == 1:
        for a in item_authors:
            for word in a.split(' ', 1):
                if word == author_data[0]:
                    return True
        return False

    # direct comparison
    for a in item_authors:
        if a == author:
            return True
    return False


# checks whether quote might be said to have origin in the book or the author
def test_credibility(arg):
    text = arg['quote'][0]
    factor = arg['factor'][0]
    t_type = arg['type'][0]

    search_result = search(text)
    books = search_json(search_result)

    # functions to call
    compare = {
        'title': lambda x, y: compare_title(x, y),
        'author': lambda x, y: compare_author(x, y)
    }
    compare_function = compare.get(t_type, None)

    for item in books:
        res = compare_function(item, factor)
        if res is True:
            return True
    return False
