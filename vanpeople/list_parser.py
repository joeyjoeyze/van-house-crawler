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
    posts = soup.find_all('li', {'class': 'g-item f-clear'})

    # init link list
    links = []

    # loop through all posts
    for post in posts:

        # ads don't have a custom style
        if post.get('style') is None:
            postUrl = post.find('a', {'class': 'ahtitle'})['href']
            links.append(postUrl)

    return links
