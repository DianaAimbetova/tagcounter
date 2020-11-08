# uncompyle6 version 3.7.4
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.7.3 (default, Mar 27 2019, 17:13:21) [MSC v.1915 64 bit (AMD64)]
# Embedded file name: C:\Users\diana_aimbetova\PycharmProjects\tagcounter\venv\Scripts\cmd.py
# Compiled at: 2020-11-08 18:29:26
# Size of source mod 2**32: 1060 bytes
import re, yaml, html_tag_counter, urllib.request, db_worker

def run(command):
    if 'get' in command:
        site = re.sub('--get', '', command).strip()
        get(site)
    else:
        if 'view' in command:
            site = re.sub('--view', '', command).strip()
            view(site)


def build_url(site):
    return f"http://{str(site)}"


def get_site_content(url):
    page = str(urllib.request.urlopen(url).read())
    return page


def define_site_name(site):
    with open('sites.yml') as (sites):
        sites_dict = yaml.safe_load(sites)
    if [s for s in sites_dict.keys() if s == site]:
        site = sites_dict[site]
    return site


def get(site):
    site = define_site_name(site)
    parser = html_tag_counter.MyHTMLParser()
    url = build_url(site)
    parser.feed(get_site_content(url))
    tags = html_tag_counter.get_tags()
    db_worker.insert_tags(site, url, tags)


def view(site):
    site = define_site_name(site)
    url = build_url(site)
    db_worker.select_tags(url)