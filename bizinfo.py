import os
import requests
from bs4 import BeautifulSoup
import time
import datetime
import sys
from mod_bizinfo import Utilities,Tag
from config import Configuration
from db import DBConnection,Query
import urllib.request
from time import sleep

class Bizinfo:

	def __init__(self,platform):
		#print('init')
		self.platform = platform

	def set_params(self):
		#print('set_params')
		self.platform = sys.argv[1]

	def validate(self):
		#print('validate')
		default	= {
			'platform':'ubuntu'
		}

		self.platform = default.get('platform')	if self.platform == '' else self.platform.lower()

	def crawling(self):

		#print('crawling')
		self.validate()

		try:
			configuration = Configuration.get_configuration(self.platform)
			_host = configuration['host']
			_user = configuration['user']
			_password = configuration['password']
			_database = configuration['database']
			_port = configuration['port']
			_charset = configuration['charset']

			conn = DBConnection(host=_host,
				user=_user,
				password=_password,
				database=_database,
				port=_port,
				charset=_charset)

			main = 'https://www.bizinfo.go.kr/see/seea/selectSEEA100.do'

			response = requests.get(main)
			html = response.text
			soup = BeautifulSoup(html, 'html.parser')

			seq = Tag.mainpage(soup,'seq')
			title = Tag.mainpage(soup,'title')
			period = Tag.mainpage(soup,'period')
			goverment = Tag.mainpage(soup,'goverment')
			posted = Tag.mainpage(soup,'posted')			
			
			'''
			print('번호: {}'.format(seq))
			print('\r', end='')			
			print('제목: {}'.format(title))
			print('\r', end='')	
			print('기간: {}'.format(period))
			print('\r', end='')	
			print('부처: {}'.format(goverment))
			print('\r', end='')
			print('등록: {}'.format(posted))
			print('\r', end='')	
			END'''

			sub = 'https://www.bizinfo.go.kr/see/seea/selectSEEA140Detail.do?pblancId=PBLN_'+seq

			'''
			response = requests.get(sub)
			html = response.text
			soup = BeautifulSoup(html, 'html.parser')

			kind = Tag.subpage(soup,'kind')
			summary = Tag.subpage(soup,'summary')
			END'''

			kind = 'bizinfo'
			summary = sub
			support = '-'
			papers = '-'
			point = '-'
			question = '-'

			'''
			print('분류: {}'.format(kind))
			print('\r', end='')
			print('요약: {}'.format(summary))
			print('\r', end='')
			print('지원: {}'.format(support))
			print('\r', end='')
			print('서류: {}'.format(papers))
			print('\r', end='')
			print('가점: {}'.format(point))
			print('\r', end='')	
			print('문의: {}'.format(question))
			print('\r', end='')						
			END'''

			cnt = conn.exec_select_rnd(seq)

			if cnt:
				print('overlap seq: ',cnt)	
			else:	
				print('does not overlap seq: ',cnt)		
				conn.exec_insert_rnd(seq,kind,title,period,goverment,posted,summary,support,papers,point,question)
			
		except Exception as e:
			with open('./bizinfo.log','a') as file:
				file.write('{} You got an error: {}\n'.format(datetime.datetime.now().strtime('%Y-%m-%d %H:%M:%S'),str(e)))

def run():
	bizinfo = Bizinfo('')
	bizinfo.set_params()
	bizinfo.crawling()

if __name__ == "__main__":
	run()
