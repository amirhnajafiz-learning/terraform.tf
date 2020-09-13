from bs4 import BeautifulSoup # using BeautifulSoup to scrap the web page
import urllib.request

import datetime as dt

from file_utils import dir_check, create_csv

"""
If you directly use "urlopen" method, it blocks you with 403 error code.
Definitely it's blocking because of use of urllib based on the user agent.
We create a new class called AppURLopener
which overrides the user-agent with Mozilla.
"""
class AppURLopener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0"


SCRIPT_EX_TIME = dt.datetime.now()
MAIN_DIR_PATH = "./output/"
MONTH_DIR_PATH = SCRIPT_EX_TIME.strftime("%B") + "/"
FILE_NAME = "Top200Of_" + SCRIPT_EX_TIME.strftime("%d_%Y")
PATH = MAIN_DIR_PATH + MONTH_DIR_PATH + FILE_NAME +".csv"

# page url
URL = "https://spotifycharts.com/regional"

# opening connection
opener = AppURLopener()
web_page = opener.open(URL)

# normally the return string is an undefined thing
# so we change it to a utf-8 format string and we now have the
# page source.
html = web_page.read().decode("utf-8")

# get the page soup
soup = BeautifulSoup(html, "html.parser")

# the division of the tracks
divisions = soup.findAll("td", {"class":"chart-table-track"})
links = soup.findAll("td", {"class":"chart-table-image"})
streams = soup.findAll("td", {"class":"chart-table-streams"})

dir_check(MAIN_DIR_PATH, MONTH_DIR_PATH)
create_csv(PATH, divisions, links, streams)
