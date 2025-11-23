from django.shortcuts import render
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

def scrape(request,name=None):
    import requests
    from bs4 import BeautifulSoup

    Headline.objects.all().delete()  # optional, for clean reloads
    
    url = "https://www.theonion.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    articles = soup.find_all('article')

    for a in articles:
        title_tag = a.find('h2')
        if not title_tag:
            continue
        
        title = title_tag.get_text()
        link = title_tag.find('a')['href']

        # extract image
        img_tag = a.find('img')

        if img_tag:
            if img_tag.get('data-src'):
                img_url=img_tag.get('data-src')
            elif img_tag.get('src'):
                img_url=img_tag.get('src')
            else:
                img_url=""
        else:
            img_url=""
        

        Headline.objects.create(
            title=title,
            url=link,
            image=img_url
        )

    return redirect('/')


def news_list(request):
    headlines = Headline.objects.all()[::-1]
    context = {
        "object_list": headlines,
    }
    return render(request, "news/home.html", context)
