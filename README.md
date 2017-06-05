**BooksMachine**

BooksMachine is a program helping users verify origin of quotes for Python 3.

It takes text of quote and title or author as arguments and decides whether this text could have been written in given book or by that author or not. BooksMachine finds books using Google Books API.

Caution: If any book contains given text as a quote, the program cannot tell its proper origin but will claim that it is likely that the quote is from the book.

i. e. Michail Bulgakov starts "Master and Margarita" with quote from Goethe's "Faust":

«... who are you, then? I am part of that power which eternally wills evil and eternally works good.»

and program will agree that it is likely for that quote to come from the book if you test "Master and Margarita". Therefore it is recommended to check your sources.

Console arguments:

*quote type factor

quote* - text that is searched in Google Books API
*type* - 'title' or 'author' - is information about comparision of factor and results
*factor* - title of the book or name/names of the author - it is compared to the results 


For examples of usage go to examples.ipynb
