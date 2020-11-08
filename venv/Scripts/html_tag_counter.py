# uncompyle6 version 3.7.4
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.7.3 (default, Mar 27 2019, 17:13:21) [MSC v.1915 64 bit (AMD64)]
# Embedded file name: C:\Users\diana_aimbetova\PycharmProjects\tagcounter\venv\Scripts\html_tag_counter.py
# Compiled at: 2020-11-08 17:37:51
# Size of source mod 2**32: 407 bytes
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