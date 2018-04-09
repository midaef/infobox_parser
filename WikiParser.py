
#class="infobox"
from bs4 import BeautifulSoup
import requests
import os
import pandas as pd
import openpyxl
from ezprint import p #print('Hello, World') = p('Hello, World')

url = 'https://ru.wikipedia.org/wiki/' #const

c1 = []
c2 = []


def search():
	global url
	value = input('Input request: ')
	url = url + value #search quest


def cls():
	os.system('cls') #cls console


def get_html(url):
	r = requests.get(url)
	return r.text #Get html 


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
		p('Search Error!')
		exit()
	for i in trs:
		try:
			cols = i.find('th').getText()
			cols = cols.replace('\n', '')
			c1.append(cols)
		except:
			c1.append('NoneData')
		try:
			cols1 = i.find('td').getText()
			cols1 = cols1.replace('\n', '')
			c2.append(cols1)
		except:
			c2.append('NoneData')

	df = pd.DataFrame({
		'Quests' : c1,
		'Info'   : c2
		})
	p(df)
	df.to_excel('wiki.xlsx')


if __name__ == '__main__':
	search()
	cls()
	parse()
	p('Save page!')