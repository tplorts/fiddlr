from bs4 import BeautifulSoup

from scraping import pageContent, randomPause


NumberOfPages = 69


def pageURL(pageNo):
    return "http://nyc.jazznearyou.com/entities.php?type=7&pg=%d" % pageNo


def pageSoup(pageNo):
    content = pageContent(pageURL(pageNo))
    return BeautifulSoup(content)


def scrapePage(pageNo):
    soup = pageSoup(pageNo)
    table = soup('table')[0]
    rows = table('tr')
    for row in rows:
        columns = row('td')
        if len(columns) >= 2:
            name = columns[0].string
            href = columns[0]('a')[0]['href']
            address = list(columns[1].children)
            street = address[0].string.strip().rstrip(',')
            city = address[1].string.strip()
            print('"{}", "{}", "{}", "{}"'.format(name, street, city, href))


def scrapeAllPages():
    for pno in range(1, NumberOfPages+1):
        scrapePage(pno)
        randomPause()


if __name__ == "__main__":
    scrapeAllPages()


