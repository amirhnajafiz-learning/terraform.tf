import mechanicalsoup
import datetime as dt

from file_utils import dir_check, create_csv


SCRIPT_EX_TIME = dt.datetime.now()
MAIN_DIR_PATH = "./output/"
MONTH_DIR_PATH = SCRIPT_EX_TIME.strftime("%B") + "/"
FILE_NAME = "Top200Of_" + SCRIPT_EX_TIME.strftime("%d_%Y")
PATH = MAIN_DIR_PATH + MONTH_DIR_PATH + FILE_NAME +".csv"
# page url
URL = "https://spotifycharts.com/regional"

# creating a free head browser
browser = mechanicalsoup.Browser()

web_page = browser.get(URL) # opening a connection

# get the page soup
soup = web_page.soup

# the division of the tracks
divisions = soup.findAll("td", {"class":"chart-table-track"})
links = soup.findAll("td", {"class":"chart-table-image"})
streams = soup.findAll("td", {"class":"chart-table-streams"})

dir_check(MAIN_DIR_PATH, MONTH_DIR_PATH)
create_csv(PATH, divisions, links, streams)
