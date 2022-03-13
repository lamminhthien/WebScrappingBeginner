from requests_html import HTMLSession, HTML
from bs4 import BeautifulSoup
import math
import re

link = open('dtdd.csv','r')

for i in link:
    star = []
    session = HTMLSession()
    r = session.get(i.rstrip() + '/danh-gia')
    print(r.html)