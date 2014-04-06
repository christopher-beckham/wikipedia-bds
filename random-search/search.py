import sys
import urllib2
import re
from random import randint



def geturl(st,agent=None):
	headers = { 'User-Agent' : agent }
	req = urllib2.Request(st, None, headers)
	html = urllib2.urlopen(req).read()
	return html
	
def getbetween2(body,start,end):
	strs = re.findall( re.escape(start) + \
		"(.*?)" + \
		re.escape(end), \
		body, re.DOTALL)
	return strs

def successors(url):
	page = geturl( url['url'] )
	page = page[ 0 : page.find('<h2><span class="mw-headline" id="References">References</span>') ]
	links = getbetween2(page, '<a href="/wiki', '"')
	clean_links = []
	for elem in links:
		if ':' not in elem and \
		'Main_Page' not in elem and \
		'Geographic_coordinate_system' not in elem:
			clean_links.append( {'url': "http://en.wikipedia.org/wiki" + elem, 'parent': url } )
	return clean_links
	

def getRandomArticle():
	page = geturl("http://en.wikipedia.org/wiki/Special:Random")
	link = getbetween2(page, '<link rel="canonical" href="', '"')[0]
	return link

def randomSearch(start_url,num_iters=20):

	start_node = {'url': start_url, 'parent': None}
	succ = successors(start_node)
	
	for k in range(0, num_iters-1):
		new = succ[ randint(0, len(succ)-1) ]
		print new['url']
		succ = successors(new)
		
PREFIX = "http://en.wikipedia.org/wiki/"


randomSearch( getRandomArticle(), num_iters=100 )

#print getRandomArticle()
