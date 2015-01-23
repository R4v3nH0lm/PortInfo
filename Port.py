#Lib's
import urllib2
from bs4 import BeautifulSoup
#Var's
port = input('Port Number? ')

#Commented out line that can be uncommented if manual testing needs to be done.
#port = 162

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