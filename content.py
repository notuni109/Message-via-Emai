import random
import csv

def get_random_quote():
    quotes_file = open('quotes.csv', 'r')
    quotes = []
    for line in csv.reader(quotes_file, delimiter='-'):
        quote = {'quote': line[0], 'author': line[1]}
        quotes.append(quote)
    
    return random.choice(quotes)

def get_random_number():
    number = random.randint(0, 100)
    return number

def get_random_link():
    links_file = open('links.csv', 'r')
    links = []
    for link in csv.reader(links_file):
        links.append(link)

    return random.choice(links)

if __name__ == '__main__':
    pass