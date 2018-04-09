
# class="infobox"
from bs4 import BeautifulSoup
import requests
import os
import pandas as pd
import openpyxl
from ezprint import p

url = 'https://ru.wikipedia.org/wiki/'

c1 = []
c2 = []

def search():
	global url
	value = input('Input request: ')
	url = url + value


# def p(value):
# 	print(value)


def cls():
	os.system('cls')


def get_html(url):
	r = requests.get(url)
	return r.text


def parse():
	global c1
	global c2
	infobox = []
	html = get_html(url)
	soup = BeautifulSoup(html, 'lxml')

	table = soup.find('table', class_ = "infobox")
	try:

		trs = table.find_all('tr')
	except:
		print('Search Error!')
		exit()
	for i in trs:
		try:
			cols = i.find('th').getText()
			cols = cols.replace('\n', '')
			c1.append(cols)
		except:
			c1.append('None')
		try:
			cols1 = i.find('td').getText()
			cols1 = cols1.replace('\n', '')
			c2.append(cols1)
		except:
			c2.append('None')

	df = pd.DataFrame({
		'Quests' : c1,
		'Info'   : c2
		})
	print(df)

	p('dfffffffffffff')
	df.to_excel('wiki.xlsx')
if __name__ == '__main__':
	search()
	cls()
	parse()