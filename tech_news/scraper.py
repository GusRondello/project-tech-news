from parsel import Selector
import requests
import time
from bs4 import BeautifulSoup


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
    selector = Selector(html_content)
    return selector.css("a.cs-overlay-link::attr(href)").getall() or []


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)

    next_page = selector.css("a.next.page-numbers::attr(href)").get()
    if next_page:
        return next_page

    return None


# Requisito 4
def scrape_news(html_content):
    selector = Selector(html_content)

    url = selector.css("link[rel='canonical']::attr(href)").get()
    title = selector.css("h1.entry-title::text").get().strip()
    timestamp = selector.css("li.meta-date::text").get()
    writer = selector.css("span.author a::text").get()
    comments_count = len(selector.css("ol.comment-list li").getall())
    summary = (
        BeautifulSoup(selector.css("div.entry-content p").get(), "html.parser")
        .get_text()
        .strip()
    )
    tags = selector.css("a[rel='tag']::text").getall()
    category = selector.css("span.label::text").get()

    news = {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "comments_count": comments_count,
        "summary": summary,
        "tags": tags,
        "category": category,
    }

    return news


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
