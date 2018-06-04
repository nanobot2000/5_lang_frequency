import argparse
from collections import Counter

def load_data(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        text = file.read()
    return text


def get_words(text):
    return text.lower().split()

def get_most_frequent_words(text, number):
    return Counter(text).most_common(number)


def argparser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--filepath', help='full path to text file', required=True)
    parser.add_argument('-n', '--number', help='number of words', default=10, type=int)
    args = parser.parse_args()
    return args


def main():
    args = argparser()
    if args.filepath is not None:
        path = args.filepath
    else:
        path = input('Enter full path to text file: ')
    text = load_data(path)
    words = get_words(text)
    if args.number is not None:
        most_frequent_words = get_most_frequent_words(words, number=args.number)
    else:
        most_frequent_words = get_most_frequent_words(words)
    print('The most popular words:')
    print('-----------------------')
    for number, (word, amount) in enumerate(most_frequent_words, 1):
        print('{} \t {} \t {}'.format(number, word, amount))
    print('_______________________')


if __name__ == '__main__':
    main()
