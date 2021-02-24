# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
import datetime as dt

def scrape_all():
    # Initiate headless driver for deployment
    browser = Browser("chrome", executable_path="chromedriver", headless=True)
    news_title, news_wrapper,news_link,news_pic = county_news(browser)
    # Run all scraping functions and store results in dictionary
    data = {
       "featured_image": featured_image(browser),
       "news_title": news_title,
       "news_wrapper": news_wrapper,
       "news_link":news_link,
       "news_pic":news_pic
    }
    # Stop webdriver and return data
    browser.quit()
    return data

# ### Featured Images
def featured_image(browser):
    # Visit URL
    url = 'http://www.countymapsofwashington.com/king.shtml'
    browser.visit(url)

    # Parse the resulting html with soup
    html = browser.html
    img_soup = soup(html, 'html.parser')
    
    try:
        for x in img_soup.find_all('img', alt= True): 
            if x['alt'] == "King county Washington map": #if alt name matchs with your numbers
                 img_url_rel=x.get('src') #adding into list
        img_url_rel
    except AttributeError:
        return None

    # Use the base URL to create an absolute URL
    img_url = f'http://www.countymapsofwashington.com/{img_url_rel}'
    
    return img_url

def county_news(browser):
    # Visit the mars nasa news site
    url = 'https://patch.com/washington/seattle'
    browser.visit(url)
    
    # Optional delay for loading the page
    browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)

    # Parse the HTML
    html = browser.html
    news_soup = soup(html, 'html.parser')

    try:
        slide_elem = news_soup.select_one('article')

        # Use the parent element to find the first `a` tag and save it as `news_title`
        news_title = slide_elem.find("h2", class_="styles_Card__Title__vp17Z styles_Card__Title--Is-Serif__2ClLt").get_text()
        news_wrapper = slide_elem.find("p", class_="styles_Card__Description__3tUgd").get_text()
        news_link_rel = slide_elem.find("a", class_="styles_Card__Thumbnail__1-_Rw").get("href")
        news_link = f'https://patch.com{news_link_rel}'
        news_pic = slide_elem.find("img", class_="styles_Card__ThumbnailImage__2aX1C is-lazy-loaded").get("src")

    except AttributeError:
        return None, None
    
    return news_title,news_wrapper,news_link,news_pic

if __name__ == "__main__":
    # If running as script, print scraped data
    print(scrape_all())
