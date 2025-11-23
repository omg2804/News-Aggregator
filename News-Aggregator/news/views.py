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

    Headline.objects.all().delete()

    base = "https://www.theonion.com/"

    category_map = {
        "latest": "https://www.theonion.com/latest",
        "entertainment": "https://www.theonion.com/entertainment",
        "sports": "https://www.theonion.com/sports",
        "politics": "https://www.theonion.com/politics",
        "opinion": "https://www.theonion.com/opinion",
        "breaking-news": "https://www.theonion.com/tag/breaking-news",
    }

    # default fallback
    if name not in category_map:
        target_url = base
    else:
        target_url = category_map[name]

    response = requests.get(target_url)
    soup = BeautifulSoup(response.text, "html.parser")

    articles = soup.find_all("h2")

    for h in articles:
        a = h.find("a")
        if not a:
            continue

        title = a.get_text(strip=True)
        url = a["href"]

        # save
        Headline.objects.create(
            title=title,
            url=url,
            image=None
        )

    return redirect("/")



def news_list(request):
    headlines = Headline.objects.all()[::-1]
    context = {
        "object_list": headlines,
    }
    return render(request, "news/home.html", context)
