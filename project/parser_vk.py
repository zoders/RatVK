from bs4 import BeautifulSoup
import requests


def check_page_status_code(url):
    code = requests.get(url).status_code
    if code != 200:
        raise ValueError


def get_profile_online_status(url):
    page = requests.get(url)
    if page.status_code != 200:
        return "null"
    soup = BeautifulSoup(page.text, "html.parser")
    try:
        return soup.find('span', class_="pp_last_activity_text").text
    except Exception:
        raise IndentationError


def get_profile_pic(url):
    img_url = []
    page = requests.get(url)
    if page.status_code != 200:
        return "null"
    soup = BeautifulSoup(page.text, "html.parser")
    img_url = soup.findAll('img', class_="pp_img")
    if len(img_url) == 0:
        raise ValueError
    else:
        return img_url[0]['src']


def get_profile_name(url):
    page = requests.get(url)
    if page.status_code != 200:
        return "null"
    soup = BeautifulSoup(page.text, "html.parser")
    try:
        return soup.find('h2', class_='op_header').text
    except Exception:
        raise IndentationError


def get_profile_music(url):
    page = requests.get(url)
    if page.status_code != 200:
        return "null"
    soup = BeautifulSoup(page.text, "html.parser")
    song = soup.findAll('div', class_='pp_status')

    if len(song) == 0:
        return "щас музыку не слушает"
    else:
        return str(song[0].text)


if __name__ == "__main__":
    url = "https://vk.com/id185394982/"
    data = check_page_status_code(url)
    print(data)
    pass
