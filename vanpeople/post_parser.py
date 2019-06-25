# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import re
import datetime

def parse_post(content):
    """
    parse response content

    :param content: string
    :return: Dict
    """

    # parse content
    soup = BeautifulSoup(content, 'lxml')

    # get title
    mainTitle = soup.find('div', {'id': 'mainTitle'}) 
    title = mainTitle.find('h1').text

    # get publish date time
    dateUni = u'发布时间'
    publish = mainTitle.find(text=re.compile(dateUni))[6:]

    # parse date for caller
    postDate = datetime.datetime.strptime(publish.split()[0], '%Y/%m/%d')

    # get contact and location details
    details = parse_details(soup.find('div', {'class': 'ep_news'}))

    # get description and image links
    desc, img_links = parse_description(soup.find('div', {'id': 'description'}))

    return {
        'title': title,
        'date': publish,
        'details': details,
        'description': desc,
        'images': img_links
    }, postDate



def parse_details(ep_news):
    """
    get contact and location detail

    :param ep_news: BeautifulSoup()
    :return: Dict
    """

    # instances that might be able to get from ep_news
    information = {
        'price':     None,  # 价格：
        'area':      None,  # 地区：*
        'address':   None,  # 地址：
        'contact':   None,  # 联系人：
        'telephone': None,  # 电话：*
        'wechat':    None,  # 微信：
        'qq':        None,  # QQ：
    }

    # price and location
    left = ep_news.find('ul', {'class': 'leftUlBox'})
    leftInfo = left.find_all('span')

    for i in range(len(leftInfo) - 1):
        text = leftInfo[i].text.strip()
        nextText = leftInfo[i+1].text.strip()
        if u'价' in text:
            if u'面' not in nextText:
                information['price'] = nextText
        elif u'区' in text:
            information['area'] = nextText
        elif u'址' in text:
            information['address'] = nextText

    # contact information
    right = ep_news.find('div', {'class': 'rightBox'})
    rightInfo = right.find_all('span')

    # loop through all right information
    for i in range(len(rightInfo) - 1):
        # get info name and value
        text = rightInfo[i].text.strip()
        nextText = rightInfo[i+1].text.strip()
        if u'联' in text:
            information['contact'] = nextText
        elif u'电' in text:
            information['telephone'] = nextText
        elif u'微' in text:
            information['wechat'] = nextText
        elif u'Q' in text:
            information['qq'] = nextText

    return information


def parse_description(desc):
    """
    parse description div

    :param desc: BeautifulSoup()
    :return: string, List[string]
    """

    # get description
    description = desc.find('div', {'class': 'adsContent'}).text

    picture_links = []
    for pic in desc.find_all('img'):
        picture_links.append(pic['src'])

    return description, picture_links
