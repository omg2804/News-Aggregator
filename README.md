

</p>
<h1 align = 'center'>News Aggregator</h1>
<br>

<br>



</p>

## Overview

News Aggregator is a web application built with **Python & Django** that scrapes news articles from *TheOnion.com* using Requests + BeautifulSoup, stores them in a database, and displays them in a clean UI.

Users can browse news by category, access the original article source, share via social platforms, switch between light/dark mode, and manage scraped headlines using Django Admin.


## Features

- Web scraping using BeautifulSoup
- Category-wise news extraction (Latest, Sports, Politics, Entertainment, etc.)
- SQLite storage for scraped articles
- Modern Bootstrap UI
- Light / Dark Mode toggle
- Share articles via:
  - Facebook
  - WhatsApp
  - Telegram
- Copy article link to clipboard
- Placeholder image support for missing images
- Django Admin Panel access

      
### Screenshots ###
## Latest
![](https://github.com/sam-boghara/News-Aggregator/blob/master/screenshots/latest_light_mode.PNG)
![](https://github.com/sam-boghara/News-Aggregator/blob/master/screenshots/latest_night_mode.PNG)
<img width="1918" height="896" alt="image" src="https://github.com/user-attachments/assets/72e0969c-d306-46e8-99eb-918ff1b306a8" />

## Entertainment
![](https://github.com/sam-boghara/News-Aggregator/blob/master/screenshots/entertainment_light_mode.PNG)
![](https://github.com/sam-boghara/News-Aggregator/blob/master/screenshots/entertainment_night_mode.PNG)
## Sports
![](https://github.com/sam-boghara/News-Aggregator/blob/master/screenshots/sports_light_mode.PNG)
![](https://github.com/sam-boghara/News-Aggregator/blob/master/screenshots/sports_night_mode.PNG)
## Politics
![](https://github.com/sam-boghara/News-Aggregator/blob/master/screenshots/polititcs_light_mode.PNG)
![](https://github.com/sam-boghara/News-Aggregator/blob/master/screenshots/polititcs_night_mode.PNG)
## Breaking News
![](https://github.com/sam-boghara/News-Aggregator/blob/master/screenshots/breaking_light_mode.PNG)
![](https://github.com/sam-boghara/News-Aggregator/blob/master/screenshots/breaking_night_mode.PNG)
## Opinion News
![](https://github.com/sam-boghara/News-Aggregator/blob/master/screenshots/opinion_light_mode.PNG)
![](https://github.com/sam-boghara/News-Aggregator/blob/master/screenshots/opinion_night_mode.PNG)
## Facebook share
![](https://github.com/sam-boghara/News-Aggregator/blob/master/screenshots/facebook_share.PNG)
## Whatsapp share
![](https://github.com/sam-boghara/News-Aggregator/blob/master/screenshots/whatsapp_share.PNG)
## Telegram share
![](https://github.com/sam-boghara/News-Aggregator/blob/master/screenshots/telegram_share.PNG)
## Copy to clipboard
![](https://github.com/sam-boghara/News-Aggregator/blob/master/screenshots/copy_to_clipboard.PNG)
---------------------------------------------------------------------------------------

## How To Use

#### Software Requirements

Python3

#### Installation

Install the dependencies by running:
```html  
    pip install bs4
    pip install requests
    pip install django-social-share
```

#### Run using Command Prompt

Navigate to the News-Aggregator folder which has manage.py file then run the following command on cmd

```html
python manage.py runserver
```

### Tech stack

`Backend` : Python3,Beautiful soup <br>
`Framework` : Django <br>
`Database` : Sqlite3 <br>
`Frontend` : Html,CSS,Bootstrap <br>
