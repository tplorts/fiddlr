import re

from bs4 import BeautifulSoup

from scraping import pageContent, randomPause


if __name__ == '__main__':
    url = 'http://musicians.allaboutjazz.com/'
    soup = BeautifulSoup(pageContent(url))
    table = soup.select('div.prime-content-container table')[0]
    rows = table('tr')
    yearsRe = re.compile(r'\d{4}\s*\-\s*\d{4}')
    for row in rows:
        # The 2nd column contains the desired info
        col = row('td')[1]
        items = list(col.children)
        link = col('a')[0]
        name = link.string.strip()
        href = link['href']
        inst = items[-1].string.strip()
        alive = True
        if len(items) == 7:
            # 5 for entries with no years, 7 for those with.
            years = items[-3].string.strip()
            if yearsRe.fullmatch(years) is not None:
                # If there is a second year, we know what that means.
                alive = False
        print('"{}", "{}", "{}", "{}"'.
              format(name, href, inst, str(alive).lower()))

