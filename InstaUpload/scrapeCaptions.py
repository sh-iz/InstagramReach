from bs4 import BeautifulSoup
import pandas as pd, requests, urllib.request,time,io


#Create lists to store the scraped data
authors = []
quotes = []
def scrape_website(page_number):
    page_num = str(page_number) #Convert the page number to a string
    URL = 'https://www.goodreads.com/quotes/tag/inspirational?page='+page_num #append the page number to complete the URL
    webpage = requests.get(URL)  #Make a request to the website
    soup = BeautifulSoup(webpage.text, "html.parser") #Parse the text from the website
    quoteText = soup.find_all('div', attrs={'class':'quoteText'}) #Get the tag and it's class
    for i in quoteText:
        quote = i.text.strip().split('\n')[0]#Get the text of the current quote, but only the sentence before a new line
        author = i.find('span', attrs={'class':'authorOrTitle'}).text.strip()
        print(quote)
        quotes.append(quote)
        print(author)
        authors.append(author)

#Loop through 'n' pages
n = 7
for num in range(0,n):
    print("n-------------------------------------------------------------------------> " +str(num))
    scrape_website(num)


#Combine the lists
combined_list = []
for i in range(len(quotes)):
    quote = quotes[i]
    quote = quote[1:len(quote)-2]
    combined_list.append(quote)

#Show the combined list
# print(combined_list)

with io.open("captions.py", "w", encoding="utf-8") as f:
    f.write("captions=[")
    for item in combined_list:
        item= f"\"{item}\",\n"
        f.write("%s" %item)