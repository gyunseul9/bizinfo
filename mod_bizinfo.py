import re
import time
import urllib.request
import os
from datetime import datetime

class Tag:

	def mainpage(soup,keyword):

		wrapper = soup.find('div',{'id':'wrapper'})
		contents = wrapper.find('div',{'id':'contents'})
		articleWrap = contents.find('div',{'id':'articleWrap'})
		content = articleWrap.find('div',{'id':'content'})
		boardBusiness = contents.find('div',{'class':'boardBusiness'})
		bbsTable = boardBusiness.find('div',{'class':'bbsTable'})
		bbsStyle1 = bbsTable.find('table',{'class':'bbsStyle1'})
		tbody = bbsStyle1.find('tbody')
		tr = tbody.find('tr')	

		if keyword == 'seq':
			tmp = []
			tmp2 = []
			td = tr.find_all('td')
			seq = td[1].find('a').attrs['onclick']
			tmp = Utilities.make_array(str(seq),';')
			tmp2 = Utilities.make_array(str(tmp[0]),'\'')
			seq = re.compile('[^ 0-9|]+')
			seq = seq.sub('', str(tmp2[1]))			
			value = seq
		elif keyword == 'title':
			td = tr.find_all('td')
			title = td[1].find('a')
			title = title.find('span').get_text().strip()	
			value = title	
		elif keyword == 'period':
			td = tr.find_all('td')
			period = td[2].get_text().strip()	
			value = period	
		elif keyword == 'goverment':
			td = tr.find_all('td')
			goverment = td[3].get_text().strip()	
			value = goverment		
		elif keyword == 'posted':
			td = tr.find_all('td')
			posted = td[4].get_text().strip()	
			value = posted								

		#print('value:',value)
		return value

	def subpage(soup,keyword):

		wrapper = soup.find('div',{'id':'wrapper'})
		container = wrapper.find('div',{'id':'container'})
		contents = container.find('div',{'id':'contents'})
		boardBusiness = contents.find('div',{'class':'boardBusiness'})
		bodCont = boardBusiness.find('div', {'class':'bodCont'})

		if keyword == 'kind':
			value = 'bizinfo'
		elif keyword == 'summary':
			summary = '-'
			value = summary
							
		#print('value:',value)
		return value		

class Utilities:

	def make_array(string,keyword): 
		arr = []
		arr = string.split(keyword)
		return arr

	def remove_certaion_tag(string):
		string = re.sub('<span.*?>.*?</span>', '', str(string), 0, re.I|re.S)
		return string

	def remove_all_tag(string):
		string = re.sub('<[^<]+?>', '', string)
		return string

	def remove_keyword(string):
		string = string.replace('>', '')
		string = string.replace('\'', '')
		return string		

	def tokenize(string, token):
		arr = []
		arr = string.split(token)
		return arr	
