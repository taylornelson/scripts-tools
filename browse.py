import argparse

BASE_URL = 'http://slo.craigslist.org/search/'
?query=
SORT_STYLE = '&sort=rel'
if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument('category', type=str, default='jjj')
	parser.add_argument('query', type=str, default='programming')
	#parser.add_argument('region', type=str, default='slo')
	args = parser.parse_args()




def browse_list(category, query):
	res = urllib2.urloppen(BASE_URL + category + '/' + '?query=' + query + SORT_STYLE).read()
	return res
	
