from __future__ import print_function
import urllib
import re

symbolscode = open("symcode.txt").read()
symbolscode = symbolscode.split("\n")

for symbol in symbolscode:
	urlfile = urllib.urlopen("http://www.nasdaq.com/symbol/" +symbol)
	urltext = urlfile.read()
	regex = '<div id="qwidget_lastsale" class="qwidget-dollar">(.+?)</div>'
	pattern = re.compile(regex)
	price = re.findall(pattern, urltext)
	print("the last price for ", symbol, "is", price)