#!/usr/bin/env python
###############################################################################
# Import library's
import urllib2
from bs4 import BeautifulSoup
import argparse

###############################################################################
# Global Variables

###############################################################################
# Scripted Actions


# Commented out line that can be uncommented if manual testing needs to be done.
# port = 162

def ScreenScrape(port):
	url = "http://www.speedguide.net/port.php?port="+str(port)
	#Get the page
	req = urllib2.Request(url)
	response = urllib2.urlopen(req)
	the_page = response.read()
	#Process the page w/BS4
	soup = BeautifulSoup(the_page)
	port_data = soup.find_all("table", {"class": "port"})
	for item in port_data:
		print item.text

def Args():
	parser = argparse.ArgumentParser(
		description="Simple python script to look up port numbers from speedguide.net",
		epilog="""
		NOTE: The following pre-requisites need to be in place before this script will work.
		1.) A valid TCP or UDP port number to be provided. 
		""",
		formatter_class=argparse.RawDescriptionHelpFormatter
	)
	parser.add_argument(
		'-p', '--port',
		help='Input which port numner will be looked up',
		required=True)
	args = parser.parse_args()
	return args

def main():
	args = Args()
	ScreenScrape(args.port)


if __name__ == '__main__':
	main()

###############################################################################
