from django.shortcuts import render
from .models import Headline

def home(request):
    objects = Headline.objects.all()
    return render(request, "news/home.html", {"object_list": objects})

import requests
from django.shortcuts import render, redirect
from bs4 import BeautifulSoup as BSoup
from news.models import Headline

# Create your views here.


# def scrape(request, name):
#     Headline.objects.all().delete()
#     session = requests.Session()
#     session.headers = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}
#     url = f"https://www.theonion.com/{name}"
#     content = session.get(url).content
#     soup = BSoup(content, "html.parser")

#     News = soup.find_all("div", {"class": "sc-cw4lnv-13 hHSpAQ"})

#     for article in News:
#         main = article.find_all("a", href=True)

#         linkx = article.find("a", {"class": "sc-1out364-0 dPMosf js_link"})
#         link = linkx["href"]

#         titlex = article.find("h2", {"class": "sc-759qgu-0 cvZkKd sc-cw4lnv-6 TLSoz"})
#         title = titlex.text

#         imgx = article.find("img")["data-src"]

#         new_headline = Headline()
#         new_headline.title = title
#         new_headline.url = link
#         new_headline.image = imgx
#         new_headline.save()
#     return redirect("../")

def scrape(request, name=None):
    import requests
    from bs4 import BeautifulSoup
    from .models import Headline

    category_map = {
        "latest": "https://www.theonion.com/latest",
        "entertainment": "https://www.theonion.com/entertainment",
        "sports": "https://www.theonion.com/sports",
        "politics": "https://www.theonion.com/politics",
        "opinion": "https://www.theonion.com/opinion",
        "breaking-news": "https://www.theonion.com/tag/breaking-news",
    }

    url = category_map.get(name, "https://www.theonion.com/")

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    cards = soup.find_all("article")

    temp_list = []

    for c in cards:

        title_tag = c.find("h2")
        if not title_tag:
            continue
        
        a = title_tag.find("a")
        if not a:
            continue
        
        title = a.get_text(strip=True)
        link = a["href"]

        img_tag = c.find("img")

        if img_tag:
            image = img_tag.get("data-src") or img_tag.get("src")
        else:
            image = None

        temp_list.append({
            "title": title,
            "url": link,
            "image": image
        })

    return render(request, "news/home.html", {"object_list": temp_list})




# def news_list(request):
#     headlines = Headline.objects.all()[::-1]
#     context = {
#         "object_list": headlines,
#     }
#     return render(request, "news/home.html", context)

def home(request):
    headlines = Headline.objects.all().order_by('-id')

    if not headlines.exists():
        return redirect('scrape', name='latest')
    
    return render(request, "news/home.html", {"object_list": headlines})
