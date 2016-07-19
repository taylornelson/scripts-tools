#AKA ineedajob.py 2-4pm 7/19/16

import argparse
import urllib2
import xml
import lxml
from lxml import etree
from lxml import html

BASE_URL = 'http://slo.craigslist.org'
BASE_SEARCH_URL = 'http://slo.craigslist.org/search/'
#todo ^^ 1 
SORT_STYLE = '&sort=rel'
#jjj = jobs
#ggg = gigs

def browse_list(category, query):
	res = urllib2.urlopen(BASE_SEARCH_URL + category + '/' + '?query=' + query + SORT_STYLE).read()
	return res

def parse_list(list_res):
	tree = html.fromstring(list_res)
	#r = tree.xpath('//p[@class="row"]')
	titles = tree.xpath('//span[@id="titletextonly"]')	
	locations = tree.xpath('//span[@class="pnr"]')	
	urls = 	tree.xpath('//a[@class="i gallery"]')
	times = tree.xpath('//time')
	
	ctr = 1
	if len(titles) > 0:
		for title,url,time,location in zip(titles,urls,times,locations):
			if ctr < 20 and ('San Luis Obispo' or 'slo' or 'san luis obispo') in str(location.xpath('string()')):
				print '[%s]:|  %s  |:%s' % (ctr,time.xpath('string()'),title.xpath('string()'))
				print url.attrib['href']
				print location.xpath('string()')
			ctr += 1

	return urls	

def quick_view_entries(urls):
	while True:
		entry_no = int(raw_input("Enter entry number to view\n"))
		data = urllib2.urlopen(BASE_URL + urls[entry_no].attrib['href']).read()
		tree = html.fromstring(data)
		postingbody = tree.xpath('//section[@id="postingbody"]')
		print postingbody[0].xpath('string()')
if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument('-c', dest='category', action='store', default='jjj')
	parser.add_argument('-q', dest='query', action='store', default='massage')
	#parser.add_argument('region', type=str, default='slo')
	args = parser.parse_args()
	list_res = browse_list(args.category, args.query)
	urls = parse_list(list_res)
	quick_view_entries(urls)

