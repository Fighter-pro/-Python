import re
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup


KEYWORDS = ["дизайн", "фото", "web", "python"]
HABR_URL = "https://habr.com/ru/articles/"


def get_html(url):
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0 Safari/537.36"
        )
    }

    response = requests.get(url, headers=headers, timeout=15)
    response.raise_for_status()
    return response.text


def has_keywords(text, keywords):
    text = text.lower()
    return any(keyword.lower() in text for keyword in keywords)


def get_article_title_and_link(article):
    title_tag = (
        article.select_one("h2 a")
        or article.select_one("a.tm-title__link")
        or article.select_one("a[href*='/ru/articles/']")
    )

    if title_tag is None:
        return None, None

    title = title_tag.get_text(" ", strip=True)
    link = urljoin(HABR_URL, title_tag.get("href"))

    return title, link


def parse_habr_articles():
    html = get_html(HABR_URL)
    soup = BeautifulSoup(html, "html.parser")

    articles = soup.find_all("article")

    for article in articles:
        preview_text = article.get_text(" ", strip=True)

        if not has_keywords(preview_text, KEYWORDS):
            continue

        title, link = get_article_title_and_link(article)

        if not title or not link:
            continue

        time_tag = article.find("time")

        if time_tag:
            date = time_tag.get("datetime") or time_tag.get_text(" ", strip=True)
        else:
            date = "Дата не найдена"

        print(f"{date} – {title} – {link}")


if __name__ == "__main__":
    parse_habr_articles()