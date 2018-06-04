import argparse
from collections import Counter

NUMBER_OF_WORDS = 10


def load_data(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        text = file.read().lower().split()
    return text


def get_most_frequent_words(text, number=NUMBER_OF_WORDS):
    return Counter(text).most_common(number)


def argparser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--filepath', help='full path to text file')
    parser.add_argument('-n', '--number', help='number of words')
    args = parser.parse_args()
    return args


def main():
    args = argparser()
    if args.filepath is not None:
        path = args.filepath
    else:
        path = input('Enter full path to text file: ')
    text = load_data(path)
    if args.number is not None:
        most_frequent_words = get_most_frequent_words(text, number=int(args.number))
    else:
        most_frequent_words = get_most_frequent_words(text)
    print("The most popular words:")
    print("-----------------------")
    for number, (word, amount) in enumerate(most_frequent_words, 1):
        print("{} \t {} \t {}".format(number, word, amount))
    print("_______________________")


if __name__ == '__main__':
    main()
