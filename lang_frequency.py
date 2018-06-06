import re
import argparse
from collections import Counter


def load_data(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()
    return text


def get_words(text):
    return re.findall(r'\w+', text)


def get_most_frequent_words(words, number):
    return Counter(words).most_common(number)


def create_argparser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--filepath',
                        help='full path to text file', required=True)
    parser.add_argument('-n', '--number', help='number of words',
                        default=10, type=int)
    args = parser.parse_args()
    return args


def main():
    argparser = create_argparser()
    path = argparser.filepath
    loaded_text = load_data(path)
    lowercase_text = loaded_text.lower()
    words = get_words(lowercase_text)
    most_frequent_words = get_most_frequent_words(words, number=argparser.number)
    print('The most popular words:')
    print('-----------------------')
    for number, (word, amount) in enumerate(most_frequent_words, 1):
        print('{} \t {} \t {}'.format(number, word, amount))
    print('_______________________')


if __name__ == '__main__':
    main()
