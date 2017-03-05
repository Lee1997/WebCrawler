from html.parser import HTMLParser
from urllib import parse



class LinkFinder(HTMLParser):
    def __init__(self, base_url, page_url):
        super().__init__()
        self.base_url = base_url
        self.page_url = page_url
        self.links = set()

    # When giving a sring to LinkFinder.feed(), this method will proc on start tags
    def handle_starttag(self, tag, attrs):
        if tag == 'tr':
            for (attribute, value) in attrs:
                if attribute == "onclick":
                    point = value.split("'")[1]
                    url = parse.urljoin(self.base_url, point)
                    self.links.add(url)

    def page_links(self):
        return self.links

    def error(self, message):
        pass






























