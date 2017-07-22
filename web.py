import sys
import urllib2
import re
import os
from bs4 import BeautifulSoup
import subprocess


#url = "http://dblp.uni-trier.de/db/journals/" + '?pos=' + str(200)
#info = urllib2.urlopen(url).read()
#print info

def first_level(num_count):
	
	
	url = "http://dblp.uni-trier.de/db/journals/" + '?pos=' + str(num_count)
	info = urllib2.urlopen(url).read()

	soup = BeautifulSoup(info,'lxml')
	for link in soup.find_all(name="a"):
		if 'href' in  link.attrs:	
			x = str(link.attrs['href']) 
			if x.startswith('http://dblp.uni-trier.de/db/journals/'):
				print x
				num_count = num_count + 1
				
	return num_count	
		#else:
			#url2 = "http://dblp.uni-trier.de/db/journals/" + '?pos' + str(num_count)
			#info2 = urllib2.urlopen(url2).read()
			#print num_count
			#print info2
num_count = 0			
while num_count < 301:
	print num_count
	first_level(num_count)
	num_count = 100 + num_count


#print num_count			

#while num_count == 0:
#				print soup.a
#				num_count = num_count - 1

