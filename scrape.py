from requests import get
from bs4 import BeautifulSoup
from pprint import pprint

def get_custom_hacker_news(num_pages, thresh_votes):
    custom_hn_list = []
    for page_num in range(1, num_pages + 1):
        response = get('https://news.ycombinator.com/news?p=' + str(page_num))
        html_page = BeautifulSoup(response.text, 'html.parser')
        links = html_page.select('.storylink')
        subtext = html_page.select('.subtext')
        custom_hn_list += create_custom_hacker_news_list(links, subtext, thresh_votes)
    custom_hn_list.sort(key = lambda k : k['Points'], reverse = True)
    return custom_hn_list

def create_custom_hacker_news_list(links, subtext, thresh_votes):
    custom_hn_list = []
    for i, link in enumerate(links):
        score = subtext[i].select('.score')
        if score:
            points = int(score[0].getText().replace(' points', ''))
            if points >= thresh_votes:
                custom_hn_list.append({'Title' : link.getText(), 'Link' : link.get('href'), 'Points' : points})
    return custom_hn_list
    

custom_hn = get_custom_hacker_news(2, 100)

pprint(custom_hn)