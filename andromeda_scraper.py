from bs4 import BeautifulSoup
import re
import sys 
import os
import csv

#the csv may have duplicates
oFile = open('andromeda.csv', 'ab')
writer = csv.writer(oFile)

#for d in args:
#	for f in os.listdir(d):
#		process(f)
#try:
#	directory_name = sys.argv[1]
#	print(directory_name)

#except:
#	print('please pass')

def parse_zero_sellers(soup):
	soup = soup
	countr = 0
	countdrug = 0
	countprice = 0
	listings = []
	prices = []
	users = [] 
	drug_type = []
	date = []
	for listing in soup.find_all('a', href=re.compile('^listing')):
		if listing.string is not None:
			countr += 1
			#this appends the odd numbers, which are the  drug names in this file
			if countr % 2 == 1:
				countdrug += 1
				#print countdrug, 'drug' + listing.string
				listings.append(listing.string.encode('utf-8'))
			#this appends the even numbers, which in this file format is the prices
			else:
				countprice += 1
				prices.append(listing.string.encode('utf-8'))
				#print countprice,'price' + listing.string
	countablah = 0
	for username in soup.find_all('a', href=re.compile('^profile')):
		if (username.string is not None) & (username.string!='gwern') & (username.string!='Andromeda') & (username.string!='View Profile') & (username.string!='Profile'):
			countablah += 1
			users.append(username.string.encode('utf-8'))
			#print countablah, username.string
	#print countdrug, countprice, countablah
	#turn arrays into rows and then create writer file
	for row in range(len(listings)):
		drug_type.append(sys.argv[1])
		date.append(fname)
	rows = zip(listings, prices, users, drug_type, date)
	#oFile = open('andromeda2.csv', 'w')
	#writer = csv.writer(oFile)
	
	if countdrug == countprice & countprice == countablah:
			#pass
			#print 'true'
			for row in rows:
				writer.writerow(row)
			#print count
	else:
		#pass
		#print 'false'
		print fname, count, counta, countb	
def parse_ten_extra_names(soup):
	#print 'hey'
	soup = soup
	count = 0
	listings = []
	prices = []
	users = [] 
	drug_type = []
	date = []
	for listing in soup.find_all('a', href=re.compile('^listing')):
		if listing.string is not None:	
			count += 1
			listings.append(listing.string.encode('utf-8'))
			#print count, listing.string

	counta = 0
	
	regex_paren = re.compile('[(]')

	for username in soup.find_all('a', href=re.compile('^profile')):
		if (username.string is not None) & (username.string!='gwern') & (username.string!='Andromeda') & (username.string!='View Profile') & (username.string!='Profile'):
			if regex_paren.search(username.string) is not None:
				counta += 1
				users.append(username.string.encode('utf-8'))
				#print counta, username.string
	countb = 0
	for div in soup.find_all('div', id='submit'):
		countb += 1
		prices.append(div.text.encode('utf-8'))		
		#print countb, div.text
	for row in range(len(listings)):
		drug_type.append( sys.argv[1])
		date.append(fname)
	rows = zip(listings, prices, users, drug_type, date)
	#oFile = open('andromeda.csv', 'w')			
	#print rows
	if count == counta & counta == countb:
		#pass
		print 'true'
		for row in rows:
			#print row
			writer.writerow(row)
		#print count
	else:
		#pass
		#print 'false'
		print fname, count, counta, countb		
def parse_double_counting_items(soup):
	soup = soup
	count = 0
	countdrug = 0
	countprice = 0
	listings = []
	prices = []
	users = [] 
	drug_type = []
	date = []
	for listing in soup.find_all('a', href=re.compile('^listing')):
		if listing.string is not None:
			count += 1
			if count % 2 ==1:
				countdrug += 1
				listings.append(listing.string.encode('utf-8'))
		#		print countdrug, listing.string
			
	counta = 0
	for username in soup.find_all('a', href=re.compile('^profile')):
		if (username.string is not None) & (username.string!='gwern') & (username.string!='Andromeda') & (username.string!='View Profile') & (username.string!='Profile'):
			counta += 1
			users.append(username.string.encode('utf-8'))
		#	print counta, username.string
	countb = 0
	for div in soup.find_all('div', id='submit'):
		countb += 1
		prices.append(div.text.encode('utf-8'))
		#print countb, div.text
	for row in range(len(listings)):
		drug_type.append( sys.argv[1])
		date.append(fname)
	rows = zip(listings, prices, users, drug_type, date)
	#oFile = open('andromeda.csv', 'w')
	#writer = csv.writer(oFile)
	if countdrug == counta & counta == countb:
		#pass
		print 'true'
		for row in rows:
			writer.writerow(row)
		#print count
	else:
		#pass
		#print 'false'
		print fname, countdrug, counta, countb
def parse_five_extra_items(soup):
	soup = soup
	count = 0
	countlisting = 0
	listings = []
	prices = []
	users = [] 
	drug_type = []
	date = []
	for listing in soup.find_all('a', href=re.compile('^listing')):
		if listing.string is not None:	
			count += 1
			if count >5: 
				countlisting += 1
				listings.append(listing.string.encode('utf-8'))
				#print count, listing.string
				#pass

	counta = 0
	for username in soup.find_all('a', href=re.compile('^profile')):
		if (username.string is not None) & (username.string!='gwern') & (username.string!='Andromeda') & (username.string!='View Profile') & (username.string!='Profile'):
			counta += 1
			users.append(username.string.encode('utf-8'))
			#print counta, username.string
	countb = 0
	for div in soup.find_all('div', id='submit'):
		countb += 1
		prices.append(div.text.encode('utf-8'))
		#print countb, div.text
	for row in range(len(listings)):
		drug_type.append( sys.argv[1])
		date.append(fname)
	rows = zip(listings, prices, users, drug_type, date)
	#oFile = open('andromeda.csv', 'w')
	#writer = csv.writer(oFile)
	if countlisting == counta & counta == countb:
		#pass
		print 'true'
		for row in rows:
			writer.writerow(row)
		#print count
	else:
		#pass
		#print 'false'
		print fname, countlisting, counta, countb
def parse_one_extra_user(soup):
	soup = soup
	count = 0
	listings = []
	prices = []
	users = [] 
	drug_type = []
	date = []
	for listing in soup.find_all('a', href=re.compile('^listing')):
		if listing.string is not None:	
			count += 1
			#print count, listing.string
			listings.append(listing.string.encode('utf-8'))
			#pass

	counta = 0
	countuser = 0
	for username in soup.find_all('a', href=re.compile('^profile')):
		if (username.string is not None) & (username.string!='gwern') & (username.string!='Andromeda') & (username.string!='View Profile') & (username.string!='Profile'):
			counta += 1
			if counta >1: 
				countuser += 1
				users.append(username.string.encode('utf-8'))
				#print counta, username.string
				#pass

	countb = 0
	for div in soup.find_all('div', id='submit'):
		countb += 1
		prices.append(div.text.encode('utf-8'))
		#print countb, div.text	
	for row in range(len(listings)):
		drug_type.append( sys.argv[1])
		date.append(fname)
	rows = zip(listings, prices, users, drug_type, date)
	#oFile = open('andromeda.csv', 'w')
	#writer = csv.writer(oFile)
	if count == countuser & countuser == countb:
		#pass
		print 'true'
		for row in rows:
			writer.writerow(row)
		#print count
	else:
		#pass
		#print 'false'
		print fname, count, countuser, countb	

def parse_five_extra_double_counting(soup):
	soup = soup
	count = 0
	countdrug = 0
	listings = []
	prices = []
	users = [] 
	drug_type = []
	date = []
	for listing in soup.find_all('a', href=re.compile('^listing')):
		if listing.string is not None:	
			count += 1
			if count >5: 
				#print count, listing.string
				if count % 2 ==0:
					countdrug += 1
					listings.append(listing.string.encode('utf-8'))
					#print countdrug, listing.string

	counta = 0
	for username in soup.find_all('a', href=re.compile('^profile')):
		if (username.string is not None) & (username.string!='gwern') & (username.string!='Andromeda') & (username.string!='View Profile') & (username.string!='Profile'):
			counta += 1
			listings.append(username.string.encode('utf-8'))
			#print counta, username.string
	countb = 0
	for div in soup.find_all('div', id='submit'):
		countb += 1
		prices.append(div.text.encode('utf-8'))
		#print countb, div.text

	for row in range(len(listings)):
		drug_type.append( sys.argv[1])
		date.append(fname)
	rows = zip(listings, prices, users, drug_type, date)
	#oFile = open('andromeda.csv', 'w')
	#writer = csv.writer(oFile)

	if countdrug == counta & counta == countb:
		#pass
		print 'true'
		for row in rows:
			writer.writerow(row)
		#print count
	else:
		#pass
		#print 'false'
		print fname, count, counta, countb

def process(fname):
	soup = BeautifulSoup(open(fname))
	listings = []
	prices = []
	users = [] 
	drug_type = []
	date = []
	regexp0508 = re.compile('2014-05-08-list.php[?]category') #05-08
	regexp0529 = re.compile('2014-05-29-list.php[?]category')
	regexp0522 = re.compile('2014-05-22-list.php[?]category')
	regexp0512 = re.compile('2014-05-12-list.php[?]category')
	regexp0603 = re.compile('2014-06-03-list.php[?]category')
	
	regexp0830 = re.compile('2014-08-30-list.php[?]category')
	regexp0818 = re.compile('2014-08-18-list.php[?]category')
	regexp0819 = re.compile('2014-08-19-list.php[?]category')
	regexp0824 = re.compile('2014-08-24-list.php[?]category')
	regexp0827 = re.compile('2014-08-27-list.php[?]category')

	regexp0501 = re.compile('2014-05-01-list.php[?]category')
	regexp0424 = re.compile('2014-04-24-list.php[?]category')
	regexp0420 = re.compile('2014-04-20-list.php[?]category')

	regexp0616 = re.compile('2014-06-16-list.php[?]category')

	regexp0705 = re.compile('2014-07-05-list.php[?]category')

	regexp0609 = re.compile('2014-06-09-list.php[?]category')

	regexp_scrape = re.compile('scrape')
	####testing####
	regtest = re.compile('2014-08-18-list.php[?]category')
	ragtest2 = re.compile('2014-07-16-list.php[?]category')
	######

	if regexp0508.search(fname) is not None:
		parse_zero_sellers(soup)
	
	elif regexp0512.search(fname) is not None:
		parse_zero_sellers(soup)

	elif regexp0522.search(fname) is not None:
		parse_zero_sellers(soup)

	elif regexp0529.search(fname) is not None:
		parse_zero_sellers(soup)

	elif regexp0603.search(fname) is not None:
		parse_zero_sellers(soup)

	elif regexp0830.search(fname) is not None:
		parse_ten_extra_names(soup)

	elif regexp0819.search(fname) is not None:
		parse_ten_extra_names(soup)

	elif regexp0824.search(fname) is not None:
		parse_ten_extra_names(soup)

	elif regexp0827.search(fname) is not None:
		parse_ten_extra_names(soup)

	elif regexp0818.search(fname) is not None:
		parse_ten_extra_names(soup)
	
	elif regexp0501.search(fname) is not None:
		parse_double_counting_items(soup)

	elif regexp0420.search(fname) is not None:
		parse_double_counting_items(soup)

	elif regexp0424.search(fname) is not None:
		parse_double_counting_items(soup)

	elif regexp0616.search(fname) is not None:
		parse_five_extra_items(soup)

	elif regexp0705.search(fname) is not None:
		parse_one_extra_user(soup)

	elif regexp0609.search(fname) is not None:
		parse_five_extra_double_counting(soup)

	elif regexp_scrape.search(fname) is not None:
		pass

	else: 
		prices = soup.find_all('div', id='submit')

		#print soup.find_all('a', src=re.compile(r'href'))
		#print soup.final_all('a')
		#pattern = re.compile("listing")
		#for a in soup.find_all('a', href=True):
		#	if a['href'].match(pattern):
		#		print a['href']
		count = 0
		for listing in soup.find_all('a', href=re.compile('^listing')):
			if listing.string is not None:	
				count += 1
				listings.append(listing.string.encode('utf-8'))
				#print count, listing.string

		counta = 0
		for username in soup.find_all('a', href=re.compile('^profile')):
			if (username.string is not None) & (username.string!='gwern') & (username.string!='Andromeda') & (username.string!='View Profile') & (username.string!='Profile'):
				counta += 1
				users.append(username.string.encode('utf-8'))
				#print counta, username.string
		countb = 0
		for div in soup.find_all('div', id='submit'):
			countb += 1
			prices.append(div.text.encode('utf-8'))
			#print countb, div.text

		#count += count
		for row in range(len(listings)):
			drug_type.append( sys.argv[1])
			date.append(fname)
		rows = zip(listings, prices, users, drug_type, date)
		#writer = csv.writer(oFile)
		#print fname, count, counta, countb
		if count == counta & counta == countb:
			#pass
			#print 'true'
			#print fname
			for row in rows:
				writer.writerow(row)
			#print count
		else:
			#pass
			print 'false'
			#print fname, count, counta, countb	
		#<a href="listing[.]php.[a-zA-Z,=,0-9,",>, , *, ~]+<\/a>

directory = sys.argv[1]
for fname in os.listdir(directory):
	right_name = os.path.join(directory, fname)
	
	if os.path.isfile(right_name):
		process(right_name)
		#print right_name
	else:
		print "why arent you printing"
	
	#process(fname)	
