#Yuzhuang Chen
#yuzhuangchen1@gmail.com

import sys
import urllib2
import re
import os
from bs4 import BeautifulSoup
import subprocess
import robotparser
import urlparse


def get_robots(url):
    rp = robotparser.RobotFileParser()
    rp.set_url(urlparse.urljoin(url, '/robots.txt'))
    rp.read()
    return rp	


def third_level(url, key):
	info = urllib2.urlopen(url).read()

	soup = BeautifulSoup(info,'lxml')
	for link in soup.find_all(name="span"):		
		if 'class' in  link.attrs:
			if 'itemprop' in link.attrs:
				temp_name = str(link.contents)
				if key in temp_name:
					print 'Here are the results matched your key'
					print temp_name								
					f.write(str(temp_name))		
		
	return	None
	

def second_level(url, key):
	info = urllib2.urlopen(url).read()

	soup = BeautifulSoup(info,'lxml')
	for link in soup.find_all(name="a"):
		if 'href' in  link.attrs:	
			x = str(link.attrs['href']) 			
			if x.startswith('http://dblp.uni-trier.de/db/journals/'):
				third_level(x, key)
				
	return	None		

def first_level(num_count, key, user_agent):
	url = "http://dblp.uni-trier.de/db/journals/" + '?pos=' + str(num_count)
	info = urllib2.urlopen(url).read()
	rp = get_robots(url)

	if user_agent:
		headers['User-agent'] = 'BadCrawler'
	soup = BeautifulSoup(info,'lxml')
	for link in soup.find_all(name="a"):
		if rp.can_fetch(user_agent, url):
			if 'href' in  link.attrs:	
				x = str(link.attrs['href']) 
				if x.startswith('http://dblp.uni-trier.de/db/journals/'):				
					second_level(x, key)
	
		else:
			print 'This website has been blocked: ', url 	
	return num_count	

	
user_agent =''
key = raw_input('Searching in DBLP? ')
f = file('result.txt','w')
num_count = 1			
web = num_count    #there are more pid to be found

while web != 0 :
	web = first_level(num_count, key, user_agent)
	num_count = 100 + num_count

#while num_count < 4300 :
#	first_level(num_count, key, user_agent)
#	num_count = 100 + num_count

f.close()	


