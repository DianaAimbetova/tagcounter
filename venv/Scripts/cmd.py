import re
import html_tag_counter
import db_worker
import logging
from datetime import datetime
import site_util

def run(command):
    if 'get' in command:
        site = re.sub('--get', '', command).strip()
        get(site)
    else:
        if 'view' in command:
            site = re.sub('--view', '', command).strip()
            view(site)


def get(site):
    site = site_util.define_site_name(site)
    parser = html_tag_counter.MyHTMLParser()
    url = site_util.build_url(site)
    parser.feed(site_util.get_site_content(url))
    tags = html_tag_counter.get_tags()
    logging.info(str(datetime.now()) + ' Getting tags: ' + str(tags))
    db_worker.insert_tags(site, url, tags)


def view(site):
    site = site_util.define_site_name(site)
    url = site_util.build_url(site)
    result = db_worker.select_tags(url)
    logging.info(str(datetime.now()) + ' Getting tags: ' + result)
    print(result)