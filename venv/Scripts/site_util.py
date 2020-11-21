import logging
from datetime import datetime
import yaml
import urllib.request

def build_url(site):
    result = f"http://{str(site)}"
    logging.info(str(datetime.now()) + ' building URL ' + result)
    return result


def get_site_content(url):
    page = str(urllib.request.urlopen(url).read())
    return page


def define_site_name(site):
    with open('sites.yml') as (sites):
        sites_dict = yaml.safe_load(sites)
    if [s for s in sites_dict.keys() if s == site]:
        site = sites_dict[site]
    logging.info(str(datetime.now()) + ' Site name defined: '+ site)
    return site