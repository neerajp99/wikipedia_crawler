from bs4 import BeautifulSoup
import requests

# Initial random wikipedia url
initial_url = "https://en.wikipedia.org/wiki/Special:Random"

# Targeted url
final_url = "https://en.wikipedia.org/wiki/Computer_science"

# details of the browser, that's acting as a user
headers = {
    "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
}

# Make a call to the wikipedia url and the provided header
wikipedia = requests.get(initial_url, headers = headers)
wikipedia_text = wikipedia.text

# Scrape the data from the provided url
soup = BeautifulSoup(wikipedia_text, 'html-parser')

# Find the exact first link field with an id
target_link = soup.find(id = "mw-content-text").find(class_ = "mw-parser-output")

# initialise the first link in the current wikipedia page with None
first_link = None
