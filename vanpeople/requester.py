# -*- coding: utf-8 -*-
import requests


def request(url):
    """
    request data from url

    :param url: string
    :return: string
    """

    # get request
    response = requests.get(url)

    # check response status
    if response.status_code != 200:
        # if encountered wrong status, write to a file
        f = open('response', 'w')
        f.write(response.content)
        f.close()
        exit('Request responses with a wrong status code')

    # the website responses in html
    return response.content
