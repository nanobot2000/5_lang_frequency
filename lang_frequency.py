import argparse

NUMBER_OF_WORDS = 10

def load_data(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
    	text = file.read().lower().split()
    return text

def get_most_frequent_words(text, n=NUMBER_OF_WORDS):
    counter = {}
    {word: 1 if word not in counter and not counter.update({word: 1})
                  else counter[word] + 1
                  if not counter.update({word: counter[word] + 1}) else 1 for word in text}
    return sorted(counter.items(), key=lambda i: i[1], reverse=True)[:n]

def argparser():
	parser = argparse.ArgumentParser()
	parser.add_argument('-f','--filepath', help='full path to text file')
	parser.add_argument('-n','--number', help='number of words')
	args = parser.parse_args()
	return args

def main():
	args = argparser()
	if args.filepath is not None:
		filepath = args.filepath
	else:
		filepath = input('Enter full path to text file: ')
	text = load_data(filepath)
	if args.number is not None:
		print(get_most_frequent_words(text, int(args.number)))
	else:
		print(get_most_frequent_words(text))

if __name__ == '__main__':
    main()
