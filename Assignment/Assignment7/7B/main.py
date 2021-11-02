# Use a web browser to visit:

# https://www.colorhexa.com/color-names

# Use the HTMLParser code from the class example to visit the site and look at all the tags.

# With your knowledge of the HTMLParser and urllib modules, use the HTMLParser methods to extract the colour
# names and hex values from the website. You can leave out any HTMLParser methods you don’t use,
# for easier to read code.

# Store the extracted values in a dictionary named “colours”,
# where the colour name is the key and the hex code is the value.
# There should be 746 colours in total.

# Print out the entire dictionary (746 colours), including a total at the end,
# so you get output in the following format:

# Alice blue #f0f8ff

# Almond #efdecd

# Amber #ffbf00

# ...

# Total colors: 746


# from html.parser import HTMLParser
# import urllib.request


# class MyHTMLParser(HTMLParser):
#     def handle_starttag(self, tag, attrs):
#         print("Found a start tag:", tag)

#     def handle_endtag(self, tag):
#         print("Found end tag :", tag)

#     def handle_data(self, data):
#         print("Found some data  :", data)


# myparser = MyHTMLParser()

# with urllib.request.urlopen('https://www.colorhexa.com/color-names') as response:
#     html = str(response.read())

# myparser.feed(html)
from html.parser import HTMLParser
import urllib.request


class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.isTrTagInit = False
        self.isTrTagEnd = False
        self.start = False
        self.data = []

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            self.isTrTagInit = True

    def handle_endtag(self, tag):
        if tag == 'a':
            self.isTrTagEnd = True

    def handle_data(self, data):
        if "Air Force blue" in data:
            self.start = True
        if self.isTrTagEnd == True & self.isTrTagInit == True & self.start == True:
            self.isTrTagEnd = False
            self.isTrTagInit = False
            if "#2c1608" in data:
                self.start = False
            self.data.append(data)

    def pack_data(self):
        mycolordict = dict(self.data[i:i+2]
                           for i in range(0, len(self.data), 2))
        mycolordict['count'] = str(len(self.data)/2)
        for val in mycolordict:
            print(val + ':'+mycolordict[val])


myparser = MyHTMLParser()

with urllib.request.urlopen('https://www.colorhexa.com/color-names') as response:
    html = str(response.read())
myparser.feed(html)
myparser.pack_data()
