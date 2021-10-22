# Use the example from the class presentation to extract and print the IP address from http://checkip.dyndns.org

# Use the HTMLParser methods to look for a unique piece of information that precedes the data you’re interested in.

# Split the data apart with string methods.

# Print only the IP portion, no leading/trailing spaces or new lines.
from html.parser import HTMLParser
import urllib.request


# class MyHTMLParser(HTMLParser):
#     def handle_starttag(self, tag, attrs):
#         print("Found a start tag:", tag)

#     def handle_endtag(self, tag):
#         print("Found end tag :", tag)

#     def handle_data(self, data):
#         print("Found some data  :", data)


# myparser = MyHTMLParser()
# myparser.feed("<html><head><title>My Crazy Document Title</title></head>"
#               "<body><h1>My views on rainbow unicorns...</h1>"
#               "<p>Unicorns are like the elusive Yeti.</p></body></html>")


class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        print("Found a start tag:", tag)

    def handle_endtag(self, tag):
        print("Found end tag :", tag)

    def handle_data(self, data):
        print("Found some data  :", data)


myparser = MyHTMLParser()

with urllib.request.urlopen('http://checkip.dyndns.org') as response:
    html = str(response.read())

myparser.feed(html)
print(myparser.get_starttag_text())
