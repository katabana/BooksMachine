import argparse
import booksmachine.checker
import sys
# TODO: REPAIR PACKAGE -> in console : arguments problem


def parse():
    parser = argparse.ArgumentParser()

    # quote - text to be found
    parser.add_argument('quote', nargs=1, help='Quote to be tested.')
    # type of comparision
    parser.add_argument('type', nargs=1, help='Type of comparision: "title" or "author"')
    # factor - value to be compared
    parser.add_argument('factor', nargs=1, help='Author or full title for quote to be checked.')

    args = parser.parse_args()
    args = vars(args)

    if args['type'][0] != 'title' and args['type'][0] != "author":
        print('Type has to be "author" or "title"')
        exit(1)

    return args


def main(quote=None, t_type=None, factor=None):
    # for running main in python console
    if quote is not None and t_type is not None and factor is not None:
        sys.argv = ['__init__.py', quote, t_type, factor]
    args = parse()
    result = checker.test_credibility(args)

    if result is True:
        print('The quote is likely to be from the source you tried.')
    else:
        print('The quote is likely not to be from the source you have given.')
        print('To be 100% sure you could try longer quote.')

    sys.argv = ['__init__.py']


if __name__ == '__main__':
    main()
