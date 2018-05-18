# -*- coding: utf-8 -*-
from url_builder import main_page
from requester import request
from list_parser import parse_list
from post_parser import parse_post


def get_vanpeople_posts(page_numbers):
    """
    get vanpeople's posts

    :param page_numbers: List[int]
    :return: Dict
    """

    # init posts list
    posts = []

    # loop through each page
    for page_number in page_numbers:
        # get all posts' link in the page
        post_links = parse_list(request(main_page(page_number)))

        # parse content in each post
        for post_link in post_links:
            # assign post link
            post = {'link': post_link}

            # assign other fields to post
            post.update(parse_post(request(post_link)))

            # push post into posts list
            posts.append(post)

    return posts
