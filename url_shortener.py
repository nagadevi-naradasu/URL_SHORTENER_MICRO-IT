import pyshorteners

def shorten_url():
    url = input("Enter the long URL: ")
    shortener = pyshorteners.Shortener()
    short_url = shortener.tinyurl.short(url)
    print("Shortened URL:", short_url)

shorten_url()
