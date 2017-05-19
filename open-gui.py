#! /usr/bin/env python3
from bs4 import BeautifulSoup
import urllib.request, pytest
url = "https://yandex.ru/search/xml?user=axel-hilmi&key=03.190607486:a7ef6ecff735248e5b74a6fc09dd7809&query=yandex"

def get_data ():
    try:
        response = urllib.request.urlopen(url)
        return response.read()
    except urllib.error.URLError as e:
        print(e.reason)

def test_get_data():
	response = get_data()
	parsed = BeautifulSoup(response, "lxml")
	res = int(parsed.find('found', attrs={'priority':'all'}).text)
	if res > 1000:
		assert True
	else : False

