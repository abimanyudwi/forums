from hitcount.utils import get_hitcount_model
from hitcount.views import HitCountMixin
import requests
import lxml
from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib, re
from nltk.tokenize import RegexpTokenizer


def update_views(request, object):
    context = {}
    hit_count = get_hitcount_model().objects.get_for_object(object)
    hits = hit_count.hits
    hitcontext = context["hitcount"] = {"pk": hit_count.pk}
    hit_count_response = HitCountMixin.hit_count(request, hit_count)

    if hit_count_response.hit_counted:
        hits = hits + 1
        hitcontext["hitcounted"] = hit_count_response.hit_counted
        hitcontext["hit_message"] = hit_count_response.hit_message
        hitcontext["total_hits"] = hits


def custom_tag_string(tag_string):
    """takes in a string, returns a list"""
    if not tag_string:
        return []
    if "," not in tag_string:
        return [tag_string]
    return [t.strip() for t in tag_string.split(",")]


def get_link_data(url):
    parsed_uri = urllib.request.urlparse(url)
    domainName = "{uri.scheme}://{uri.netloc}/".format(uri=parsed_uri)

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
        "Accept-Language": "id",
    }
    r = requests.get(url, headers=headers)

    soup = BeautifulSoup(r.text, "lxml")

    if domainName == "https://www.cnnindonesia.com/":
        konten = soup.find("div", class_="detail_text")
        # unwanted = konten.find("div", class_="paradetail")
        classes = ["paradetail", "lihatjg"]
        for i in classes:
            for data in konten.find_all("div", {"class": i}):
                data.decompose()
        # unwanted.extract()
        konten = konten.getText(strip=True)
        title = soup.select_one(selector=".l_content .title").getText(strip=True)
        # konten = soup.find('div',class_='.detail_text').getText()

    elif "kompas.com" in domainName:
        # classToIgnore = ["lihatJuga", "inner-link-baca-juga", "class3"]
        konten = soup.find("div", class_="read__content")
        for data in konten.find_all(["a", "i"]):
            data.extract()
        konten = konten.getText(strip=True)
        title = soup.select_one(selector=".read__title").getText(strip=True)

    elif "tempo.co" in domainName:
        konten = soup.select_one(selector=".detail-in").getText(strip=True)
        title = soup.select_one(selector=".detail-title .title").getText(strip=True)

    # konten = konten.strip()
    konten = konten
    title = title.strip()
    url = url
    context = {"konten": konten, "title": title, "a_url": url, "domain": domainName}
    return context


def compare(translasi):

    with open("main/idwords.html", "r") as file:
        body = file.read()

    soup = BeautifulSoup(body, "lxml")
    word = soup.select_one(selector=".word").get_text(strip=True)
    allwords = word.split()
    text = translasi
    regx = re.sub("[^a-zA-Z]+", " ", text)

    text = regx.split()
    low_text = [lowtext.lower() for lowtext in text]
    low_allwords = [lowallwords.lower() for lowallwords in allwords]
    clean = sorted([*set(low_text)])
    allword = sorted([*set(low_allwords)])
    compared = sorted(list(set(clean) - set(allword)))
    context = {"compare": compared}
    return context


def compare_db(kata, kata_db):

    clean = sorted([*set(kata)])
    allword = sorted([*set(kata_db)])
    compared = sorted(list(set(clean) - set(allword)))
    context = {"compare": compared}
    return context


def kalimat_perbandingan(ind, mdo):
    tokenizer = RegexpTokenizer(r"[^.?!]+")
    text_compiler = re.compile("<.*?>")
    ind = re.sub(text_compiler, "", ind)
    mdo = re.sub(text_compiler, "", mdo)
    kalimat_ind = list(map(str.strip, tokenizer.tokenize(ind)))
    kalimat_mdo = list(map(str.strip, tokenizer.tokenize(mdo)))
    context = {"ind": kalimat_ind, "mdo": kalimat_mdo}
    return context


def kalimat_mdo(mdo):
    tokenizer = RegexpTokenizer(r"[^.?!]+")
    text_compiler = re.compile("<.*?>")
    mdo = re.sub(text_compiler, "", mdo)
    kalimat_mdo = list(map(str.strip, tokenizer.tokenize(mdo)))
    context = {"mdo": kalimat_mdo}
    return context
