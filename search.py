import sys
import urllib2
import re
import networkx as nx
from Queue import Queue

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
	
def findParents(elem):
	arr = []
	while elem['parent'] != None:
		arr.append( elem['url'] )
		elem = elem['parent']
	arr.append( elem['url'] )
	return arr

def BFS(start_url, end_url, draw_graph=False):

	start_node = {'url': start_url, 'parent': None}
	end_node = {'url': end_url, 'parent': None}

	Q_a = Queue()
	V_a = dict()
	Q_a.put(start_node)
	V_a[ start_node['url'] ] = start_node
	
	Q_b = Queue()
	V_b = dict()
	Q_b.put(end_node)
	V_b[ end_node['url'] ] = end_node
	
	while Q_a.empty() == False or Q_b.empty() == False:

		node = Q_a.get()
		#print url
		for successor in successors(node):
			if successor['url'] not in V_a:
				V_a[ successor['url'] ] = successor
				Q_a.put(successor)
				
		node = Q_b.get()
		#print url
		for successor in successors(node):
			if successor['url'] not in V_b:
				V_b[ successor['url'] ] = successor
				Q_b.put(successor)
			
		intersect = list( set( V_a.keys() ).intersection( set( V_b.keys() ) ) ) # seems a bit inefficient?
		if len(intersect) > 0:
			left = V_a[ intersect[0] ]
			right = V_b[ intersect[0] ]
			for p in findParents(left)[::-1]:
				print p
			for p in findParents(right)[1::]:
				print p
			break
	
BFS("http://en.wikipedia.org/wiki/Support_vector_machine", "http://en.wikipedia.org/wiki/Miley_Cyrus")