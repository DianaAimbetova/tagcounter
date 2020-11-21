from html.parser import HTMLParser
tags = {}

class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        global tags
        if tag not in tags:
            tags[tag] = 0
        tags[tag] += 1

    def handle_endtag(self, tag):
        if tag not in tags:
            tags[tag] = 0
        tags[tag] += 1


def get_tags():
    return tags