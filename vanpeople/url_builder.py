# -*- coding: utf-8 -*-


def rentForumPage(page_number):
    """
    get main page url

    :param page_number: int
    :return: string
    """
    return "http://www.vanpeople.com/c/s_/1/0/0/0/" + str(page_number) + ".html"


def post(post_id):
    """
    get post page url

    :param post_id: int
    :return: string
    """
    return "http://www.vanpeople.com/c/" + str(post_id) + ".html"
