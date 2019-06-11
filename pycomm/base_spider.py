#! /bin/python
#-*-coding: utf-8-*-
import bs4
from bs4 import BeautifulSoup as Soup
from log import Log
import urllib2
import chardet

class BaseSpider(object):

    def __init__(self, url):
        self.url = url
        self.headers = {    
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
            }
        self.keyWords = []
            
    def add_header(self, key, value):
        self.headers[key] = value

    def fetch_page(self):
        req = urllib2.Request(self.url)

        for key, val in self.headers.items():
            req.add_header(key, val)
            
        try:
            resp = urllib2.urlopen(req)
            
        except urllib2.HTTPError as e:
            code = e.code
            reason = e.reason
            Log("Get %s fail, errcode: %d, msg: %s"%(self.url, code, reason),
                "red")
            return ""

        data = resp.read()

        try:
            page = data.decode("utf-8")

        except Exception as e:
            Log(str(e) + " try gbk", "red")
            page = data.decode("gbk")

        Log("Fetch page of %s succ"%self.url, "green")

        return page

    def parse_html(self, htmlPage):
        assert isinstance(htmlPage, str) or isinstance(htmlPage, unicode)

        soup = Soup(htmlPage, features="html.parser")

        return soup


    def FindTagByClass(self, soup, tag, cls):
        if isinstance(soup, bs4.BeautifulSoup):
            tags = soup.find_all(tag)

        elif isinstance(soup, bs4.element.Tag):
            tags = soup.find_all(tag)

        #list
        else:
            assert isinstance(soup, list)
            tags = []
            for item in soup:
                tags.extend(item.find_all(tag))
        
        targets = []
        for item in tags:
            if not cls or cls in item.attrs.get("class", []):
                targets.append(item)

        return targets

    def process_soup(self):
        page = self.fetch_page()
        if not page:
            Log("page empty" "red")
            return False

        soup = self.parse_html(page)

        return self.extract_from_soup(soup)

    def process_raw(self):
        """
        利用特定接口获得的数据，不需要解析网页
        """
        data = self.fetch_page()
        if not data:
            Log("page empty", "red")
            return False

        return extract_from_str(data)

    def extract_from_soup(self, soup):
        pass


    def extract_from_str(self, rawStr):
        pass
