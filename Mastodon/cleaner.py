try:
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup

def parseHTML(html):
    parsed_html = BeautifulSoup(html)
    return parsed_html.p.find('a', attrs={'class': 'mention hashtag'}).span

def remove_html_tags(text):
    soup = BeautifulSoup(text, 'lxml')
    return soup.get_text()

