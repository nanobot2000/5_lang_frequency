# Frequency Analysis of Words

Reads file and shows N most frequent words in it.

# Quickstart

The script requires the installed Python interpreter version 3.6
You have to start program, run the script with the -f, --filepath argument with path to text file and optional -n, --number argument (default 10). 
To call the help, run the script with the -h or --help option.
```bash
$ python3 lang_frequency.py -h
usage: lang_frequency.py [-h] -f FILEPATH [-n NUMBER]

optional arguments:
  -h, --help            show this help message and exit
  -f FILEPATH, --filepath FILEPATH
                        full path to text file
  -n NUMBER, --number NUMBER
                        number of words
```
Example of script launch on Linux, Python 3.6:

```bash
$ python3 lang_frequency.py -f /home/parallels/war.txt -n 10
The most popular words:
-----------------------
1        the     69441
2        and     44606
3        to      33510
4        of      30016
5        a       21218
6        he      20010
7        in      18072
8        that    16410
9        his     15968
10       was     14720
_______________________
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
