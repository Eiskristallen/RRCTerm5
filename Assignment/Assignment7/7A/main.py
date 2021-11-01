
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
# with urllib.request.urlopen('http://checkip.dyndns.org') as response:
#     html = str(response.read())
# myparser.feed(html)
# print(myparser.get_starttag_text())


# Use the HTMLParser methods to look for a unique piece of information that precedes the data you’re interested in.\
class MyuniqueData(HTMLParser):
    def handle_data(self, data):
        if data == "Current IP Check":
            print(data)


myparser = MyuniqueData()

with urllib.request.urlopen('http://checkip.dyndns.org') as response:
    html = str(response.read())
myparser.feed(html)
print(myparser.get_starttag_text())

# Split the data apart with string methods.


class MySpliteData(HTMLParser):

    def handle_data(self, data):
        result = []
        result.append(data.split(' '))
        print(result)


myparser = MySpliteData()

with urllib.request.urlopen('http://checkip.dyndns.org') as response:
    html = str(response.read())
myparser.feed(html)


# Print only the IP portion, no leading/trailing spaces or new lines.


class MyIpData(HTMLParser):

    def handle_data(self, data):
        result = ""
        if "Address" in data:
            result += data
            print(result)


myparser = MyIpData()

with urllib.request.urlopen('http://checkip.dyndns.org') as response:
    html = str(response.read())
myparser.feed(html)
print(myparser.get_starttag_text())
