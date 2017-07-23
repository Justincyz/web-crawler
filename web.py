import sys
import urllib2
import re
import os
from bs4 import BeautifulSoup
import subprocess

def third_level(url):
	info = urllib2.urlopen(url).read()

	soup = BeautifulSoup(info,'lxml')
	for link in soup.find_all(name="span"):
		
		if 'class' in  link.attrs:
			if 'itemprop' in link.attrs:
				print link.contents
				f = file('result.txt','w')			
				f.write(str(link.contents))			
	return	None
	

def second_level(url):
	info = urllib2.urlopen(url).read()

	soup = BeautifulSoup(info,'lxml')
	for link in soup.find_all(name="a"):
		if 'href' in  link.attrs:	
			x = str(link.attrs['href']) 			
			if x.startswith('http://dblp.uni-trier.de/db/journals/'):
				#print x
				third_level(x)
				
	return	None		

def first_level(num_count):
	url = "http://dblp.uni-trier.de/db/journals/" + '?pos=' + str(num_count)
	info = urllib2.urlopen(url).read()


	soup = BeautifulSoup(info,'lxml')
	for link in soup.find_all(name="a"):
		if 'href' in  link.attrs:	
			x = str(link.attrs['href']) 
			if x.startswith('http://dblp.uni-trier.de/db/journals/'):
				#print x				
				second_level(x)


	return num_count	
		


first_level(1)



num_count = 0			
while num_count < 301:
	#print num_count
	#first_level(num_count)
	num_count = 100 + num_count


