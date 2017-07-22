import sys
import urllib2
import re
import os
from bs4 import BeautifulSoup
import subprocess

num_count = 0






def first_level(num_count):
	url = "http://dblp.uni-trier.de/db/journals/" + '?pos' + str(num_count)
	info = urllib2.urlopen(url).read()

	soup = BeautifulSoup(info,'lxml')
	for link in soup.find_all(name="a"):
		if 'href' in  link.attrs:	
			x = str(link.attrs['href']) 
			if x.startswith('http://dblp.uni-trier.de/db/journals/'):
			#print x
				num_count = num_count + 1
				print num_count
			#return num_count	
		#else:
			#url2 = "http://dblp.uni-trier.de/db/journals/" + '?pos' + str(num_count)
			#info2 = urllib2.urlopen(url2).read()
			#print num_count
			#print info2

first_level(num_count)

#print num_count			

#while num_count == 0:
#				print soup.a
#				num_count = num_count - 1

