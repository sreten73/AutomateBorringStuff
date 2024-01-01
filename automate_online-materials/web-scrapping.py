import requests
import lxml
import bs4

res = requests.get('http://quotes.toscrape.com/')
soup = bs4.BeautifulSoup(res.text,'lxml')
authors = set()
authors1 = soup.select('.author')[0].getText()
print(authors1)
for i in range(0,len(soup.select('.author'))):
    authors.add(soup.select('.author')[i].getText())
print(authors)
authors = set()
#second way to extract authors
for name in soup.select(".author"):
    authors.add(name.text)
print(authors)

quotes = []
quote1 = soup.select('.text')[0].getText()
for i in range(0,len(soup.select('.text'))):
    quotes.append(soup.select('.text')[i].getText())
print(quotes)

#second way to get all qiotes
quotes = []
for quote in soup.select('.text'):
    quotes.append(quote.text)
print(quotes)


for item in soup.select(".tag-item"):
    print(item.text)

#Solution 1 to get all the unique authors from all pages
url = 'http://quotes.toscrape.com/page/'
authors = set()

for page in range(1,10):

    # Concatenate to get new page URL
    page_url = url+str(page)
    # Obtain Request
    res = requests.get(page_url)
    # Turn into Soup
    soup = bs4.BeautifulSoup(res.text,'lxml')
    # Add Authors to our set
    for name in soup.select(".author"):
        authors.add(name.text)

print(authors)

# Solution 2 to get all the unique authors from all pages.
# We don't know how much we have pages
# Choose some huge page number we know doesn't exist
page_url = url+str(9999999)

# Obtain Request
res = requests.get(page_url)

# Turn into Soup
soup = bs4.BeautifulSoup(res.text,'lxml')
# This solution requires that the string "No quotes found!" only occurs on the last page.
# If for some reason this string was on the other pages, we would need to be more detailed.
#"No quotes found!" in res.text
page_still_valid = True
authors = set ()
page = 1

while page_still_valid:

    # Concatenate to get new page URL
    page_url = url + str ( page )

    # Obtain Request
    res = requests.get ( page_url )

    # Check to see if we're on the last page
    if "No quotes found!" in res.text:
        break

    # Turn into Soup
    soup = bs4.BeautifulSoup ( res.text, 'lxml' )

    # Add Authors to our set
    for name in soup.select ( ".author" ):
        authors.add ( name.text )

    # Go to Next Page
    page += 1
print(authors)