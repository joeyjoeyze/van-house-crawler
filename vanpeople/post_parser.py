# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup


def parse_post(content):
    """
    parse response content

    :param content: string
    :return: Dict
    """

    # parse content
    soup = BeautifulSoup(content, 'lxml')

    # get main post information
    info = soup.find('div', {'class': 'side'})

    # get title
    title = info.find('h1').get_text().encode('utf-8')

    # get publish date time
    publish = parse_publish_time(info.find('div', {'class': 'ep_info'}))

    # get contact and location details
    details = parse_details(info.find('div', {'class': 'ep_news'}))

    # get description and image links
    desc, img_links = parse_description(info.find('div', {'class': 'desc'}).find('div', {'class': 'l'}))

    return {
        'title': title,
        'date': publish,
        'details': details,
        'description': desc,
        'images': img_links
    }


def parse_publish_time(ep_info):
    """
    get post published time

    :param ep_info: BeautifulSoup()
    :return: string
    """

    return ep_info.find('div', {'class': 'l'}).get_text().encode('utf-8')[14:33]


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
    left = ep_news.find('div', {'class': 'l'})

    # loop through all left information
    for info in left.find_all('dl'):
        # get info name and value
        name, value = info.find('dt').get_text().encode('utf-8'), info.find('dd').contents[0].encode('utf-8')

        # match values
        if name == u'价格：'.encode('utf-8'):
            information['price'] = value
        elif name == u'地区：'.encode('utf-8'):
            information['area'] = value
        elif name == u'地址：'.encode('utf-8'):
            information['address'] = value

    # contact information
    right = ep_news.find('div', {'class': 'r'})

    # loop through all right information
    for info in right.find_all('dl'):
        # get info name and value
        name, value = info.find('dt').get_text().encode('utf-8'), info.find('dd').contents[0].encode('utf-8')

        # match values
        if name == u'联系人：'.encode('utf-8'):
            information['contact'] = value
        elif name == u'电话：'.encode('utf-8'):
            information['telephone'] = value
        elif name == u'微信：'.encode('utf-8'):
            information['wechat'] = value
        elif name == u'QQ：'.encode('utf-8'):
            information['qq'] = value

    return information


def parse_description(desc):
    """
    parse description div

    :param desc: BeautifulSoup()
    :return: string, List[string]
    """

    # get pic list
    pics = desc.find('ul', {'class': 'pic_list'})

    # init picture links
    picture_links = []

    # check pic exists
    if pics:
        for pic in pics.find_all('li'):
            picture_links.append(pic.find('img').get('src'))

    # get description
    description = desc.find('div', {'class': ''}).get_text().encode('utf-8')

    return description, picture_links
