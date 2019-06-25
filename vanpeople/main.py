# -*- coding: utf-8 -*-
import url_builder
from requester import request
from list_parser import parse_list
from post_parser import parse_post
from json import dumps
from time import time
import datetime
import sys 

def get_vanpeople_posts(oldestPostDays, maxPostCount):
    """
    get vanpeople's posts

    :param page_numbers: List[int]
    :return: Dict
    """

    # init posts list
    posts = []

    today = datetime.datetime.today()
    postDate = today
    forumPageNumber = 0
    postCount = 0

    while (postDate - today).days < oldestPostDays and postCount < maxPostCount:
        requestUrl = url_builder.rentForumPage(forumPageNumber)
        postLinks = parse_list(request(requestUrl))
        
        # import pdb; pdb.set_trace()
        for post_link in postLinks:
            # assign post link
            post = {'link': post_link}

            # assign other fields to post
            postInfo, postDate = parse_post(request(post_link))
            post.update(postInfo)

            # push post into posts list
            posts.append(post)

            # print progress to screen 
            print 'Processed posts: {0}'.format(len(posts))
            sys.stdout.write("\033[F")
            sys.stdout.write("\033[K")

        # increment
        forumPageNumber = forumPageNumber + 60 
        postCount = postCount + len(postLinks)
        print postDate, today 
        print postCount, maxPostCount
    return posts


def store_locally(posts):
    with open('data/vanpeople/' + str(time()) + '.json', 'w') as f:
        data = dumps(posts, ensure_ascii=False, sort_keys=True, indent=4)
        f.write(data.encode('utf-8'))


def transform(post):
    return {
        'title': post['title'],
        'published_date': post['date'],
        'contact_info': {
            'name': post['details']['contact'],
            'telephone': post['details']['telephone'],
            'wechat': post['details']['wechat'],
            'qq': post['details']['qq']
        },
        'location_info': {
            'area': post['details']['area'],
            'address': post['details']['address']
        },
        'description': post['description'],
        'images': post['images'],
        'link': post['link']
    }
