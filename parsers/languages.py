from bs4 import BeautifulSoup

from utils import get_soup


def parse_langs(langs_get_url: str):
    soup = get_soup(langs_get_url)
    if not isinstance(soup, BeautifulSoup):
        print("Что-то пошло не так... Попробуйте позже. Статус ошибки", soup)
        return
    lang_box = soup.find("div", class_="lang-block")
    current_lang = {
        "lang": langs_get_url,
        "lang_str": lang_box.find("div", class_="lang-current").text.strip()
    }
    other_langs = lang_box.select(".lang-list .lang-block a")
    langs_list = [current_lang]
    langs_list.extend(map(
        lambda links_soup: {
            "lang": links_soup["href"].split("/")[-1].split("?")[0],
            "lang_str": links_soup.text.strip()
        },
        other_langs
    ))
    return langs_list
