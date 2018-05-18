# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup


def parse_list(content):
    """
    parse the list page

    :param content: string
    :return: List[string]
    """

    # parse content
    soup = BeautifulSoup(content, 'lxml')

    # get all posts
    posts = soup.find_all('div', {'class': 'show'})[1].find_all('dt')

    # init link list
    links = []

    # loop through all posts
    for post in posts:
        # get the first a tag's href as link
        links.append(post.find('a').get('href'))

    return links
