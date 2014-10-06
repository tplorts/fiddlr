import urllib.request
import time
import random


def pageContent(url):
    response = urllib.request.urlopen(url)
    data = response.read()
    text = data.decode(encoding='utf-8', errors='ignore')
    return text


def randomPause():
    time.sleep(2 + 3*random.random())
