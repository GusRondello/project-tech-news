from tech_news.database import search_news
from datetime import datetime


# Requisito 6
def search_by_title(title):
    news_title = search_news({"title": {"$regex": title, "$options": "i"}})

    return [(news["title"], news["url"]) for news in news_title]


# Requisito 7
def search_by_date(date):
    date_type = "%Y-%m-%d"
    try:
        raw_date = datetime.strptime(date, date_type)
        formated_date = datetime.strftime(raw_date, "%d/%m/%Y")
        date_news = search_news({"timestamp": formated_date})
        return [(news["title"], news["url"]) for news in date_news]
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_tag(tag):
    tag_news = search_news({"tags": {"$regex": tag, "$options": "i"}})

    return [(news["title"], news["url"]) for news in tag_news]


# Requisito 9
def search_by_category(category):
    category_news = search_news(
        {"category": {"$regex": category, "$options": "i"}}
    )

    return [(news["title"], news["url"]) for news in category_news]
