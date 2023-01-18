from parsel import Selector
import requests
import time


# Requisito 1
def fetch(url):
    try:
        time.sleep(1)
        response = requests.get(url)

        if response.status_code == 200:
            return response.text

        return None

    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_updates(html_content):
    selector = Selector(text=html_content)
    return selector.css("a.cs-overlay-link::attr(href)").getall() or []


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)

    next_page = selector.css("a.next.page-numbers::attr(href)").get()
    if next_page:
        return next_page

    return None


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
