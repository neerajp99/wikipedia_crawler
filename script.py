from bs4 import BeautifulSoup
import requests
import urllib
import time

# Initial random wikipedia url
initial_url = "https://en.wikipedia.org/wiki/Special:Random"

# Targeted url
final_url = "https://en.wikipedia.org/wiki/Computer_science"

# Function to find the first link from a particular wikipedia page
def first_wikipedia_link(url):
    # Details of the browser, that's acting as a user
    headers = {
        "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
    }

    # Make a call to the wikipedia url and the provided header
    wikipedia = requests.get(url, headers = headers)
    wikipedia_text = wikipedia.text

    # Scrape the data from the provided url
    soup = BeautifulSoup(wikipedia_text, 'html.parser')

    # Find the exact first link field with an id
    target_link = soup.find(id = "mw-content-text").find(class_ = "mw-parser-output")

    # Initialise the first link in the current wikipedia page with None
    first_link = None

    # Check for the first <a> tag inside <p> tag
    for x in target_link.find_all("p", recursive = False):
        # check for a child anchor tag
        if x.find("a", recursive = False):
            first_link = x.find("a", recursive = False).get("href")
            break

    # If no anchor tag is found inside the paragraph tag, return
    if not first_link:
        return


    # Creating a new url each time with the new found anchor tag link
    next_link = urllib.parse.urljoin('https://en.wikipedia.org/', first_link)
    return next_link

# Function to check if the article is found or not
def check_for_destination_url(current_url, final_url, max_steps = 50):
    if current_url[-1] == final_url:
        print('Target url is found')
        return False
    elif len(current_url) > max_steps:
        print('The search has exceed the maximum count')
        return False
    elif current_url[-1] in current_url[:-1]:
        print('We have crossed the current url before.')
        return False
    else:
        return True

# Initial current url
current_url = [initial_url]

# Continue checking, until the target url is found
while check_for_destination_url(current_url, final_url):
    # Print the current url
    print(current_url[-1])

    current_link = first_wikipedia_link(current_url[-1])

    # if the function does not return anything
    if not current_link:
        print ('The target url is found!')
        break

    # If the target url is not found, append the current_link to the current_url array
    current_url.append(current_link)
    time.sleep(2)
