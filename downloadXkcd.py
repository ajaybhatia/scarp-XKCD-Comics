#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#  downloadXkcd.py
#  
#  Copyright 2016 Ajay Bhatia <prof.ajaybhatia@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import os
import requests
from bs4 import BeautifulSoup

# xkcd Comics home URL
url = "http://xkcd.com"

# Make xkcd directory if not present to store comics
os.makedirs('xkcd', exist_ok=True)

while not url.endswith('#'):
	# Download the page
	print('Downloading the page {}...'.format(url))
	res = requests.get(url)
	res.raise_for_status()
	
	soup = BeautifulSoup(res.text, 'lxml')
	
	# Find the URL of comic image.
	comicElem = soup.select('#comic img')
	if comicElem == []:
		print("Couldn't find comic image.")
	else:
		try:
			comicUrl = 'http:' + comicElem[0].get('src')
			# Download the image
			print('Downloading the image {}...'.format(comicUrl))
			res = requests.get(comicUrl)
			res.raise_for_status()
		except requests.exceptions.MissingSchema:
			# Skip this comic because it doesn't have image.
			prevLink = soup.select('a[rel="prev"]')[0]
			url = 'http://xkcd.com' + prevLink.get('href')
			continue
		
		# Save the image to xkcd directory
		imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
		for chunk in res.iter_content(100000):
			imageFile.write(chunk)
			
		imageFile.close()
		
	# Get Prev Button's URL
	prevLink = soup.select('a[rel="prev"]')[0]
	url = 'http://xkcd.com' + prevLink.get('href')
	
print('Done!')
