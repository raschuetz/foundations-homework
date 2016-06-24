
# coding: utf-8

# # Reddit Part One: Getting Data
# 
# You're going to scrape the front page of https://www.reddit.com! Reddit is a magic land made of many many semi-independent kingdoms, called subreddits. We need to find out which are the most powerful.
# 
# You are going to scrape the front page of reddit every 4 hours, saving a CSV file that includes:
# * The title of the post
# * The number of votes it has (the number between the up and down arrows)
# * The number of comments it has
# * What subreddit it is from (e.g. /r/AskReddit, /r/todayilearned)
# * When it was posted (get a TIMESTAMP, e.g. 2016-06-22T12:33:58+00:00, not "4 hours ago")
# * The URL to the post itself
# * The URL of the thumbnail image associated with the post
# 
# Note:
# 
# <p>Ugh, reddit is horrible when it hasn't been customized to your tastes. If you would like something more exciting/less idiotic, try scraping a multireddit page - https://www.reddit.com/r/multihub/top/?sort=top&t=year - they're subreddits clustered by topics.
# 
# <p>For example, you could scrape https://www.reddit.com/user/CrownReserve/m/improveyoself which is all self-improvement subreddits. You can follow the links at https://www.reddit.com/r/multihub/top/?sort=top&t=year or use the "Find Multireddits" link on the Multireddit page to find more.

# In[83]:

from bs4 import BeautifulSoup
import requests

user_agent = {'User-agent': 'Mozilla/5.0'}
html_str = requests.get('https://www.reddit.com/', headers = user_agent).text


# In[85]:

document = BeautifulSoup(html_str, 'html.parser')


# In[86]:

# The title of the post
    # The whole post is under `<div>` class = ' thing id-t3_4 ....'
        # <div> class = 'entry unvoted'
        # <p> class = 'title'
        # `<a>` class = 'title may-blank '
# The number of votes it has (the number between the up and down arrows)
    # The number of votes is in <div> class = 'score unvoted'
    # sometimes this is &bull;
# The number of comments it has
    # There's a
        # <div> class = 'entry unvoted'
        # <ul> class = 'flat-list buttons'
        # <li> class = 'first'
        # <a> class = 'bylink comments may-blank'
# What subreddit it is from (e.g. /r/AskReddit, /r/todayilearned)
    # <div> class = 'entry unvoted'
    # <p> class='tagline'
    # <a> class = 'subreddit hover may-blank'
# When it was posted (get a TIMESTAMP, e.g. 2016-06-22T12:33:58+00:00, not "4 hours ago")
    # <div> class = 'entry unvoted'
    # <p> class='tagline'
    # <time> it's actually in the tag
# The URL to the post itself
    # This is in two places. Both inside the main <div> tag and in the same tag with the title.
# The URL of the thumbnail image associated with the post
    # There are two thumbnail urls—the one I guess it's from orginially and the reddit thumbnail. Here's how to get the reddit thumbnail:
        # <a> class = 'thumbnail may-blank'
        # <img> it's actually in the tag
# What I eventually want: 
#     posts_today = [
#         {'title': '"Two clowns in the same circus" 16 x 12s oil on linen'},
#         {'votes': 4246},
#         {'comments': 372},
#         {'subreddit': '/r/Art'},
#         {'timestamp': '2016-06-22T12:33:58+00:00'},
#         {'url': 'https://www.reddit.com/r/Art/comments/4pbvk5/two_clowns_in_the_same_circus_16_x_12s_oil_on/'},
#         {'thumb_url': 'https://b.thumbs.redditmedia.com/p32PnbLD9t9hqvw9Q5X7eZS2tI7Ygqnh5K5MTxOERSE.jpg'}
#     ]


# In[148]:

import re


# In[272]:

non_ads = document.find('div', {'id': 'siteTable'})
one_sibling_up = non_ads.find_all('div', {'class': 'clearleft'})


# In[89]:

# troubleshooting
# document


# In[273]:

# because only every other clearleft has a post in it:
posts = [tag.find_next_sibling('div') for tag in one_sibling_up if tag.find_next_sibling('div')]


# In[97]:

def title(post):
    if post.find('a', {'class': 'title may-blank '}):
        return post.find('a', {'class': 'title may-blank '}).string
    else:
        return 'NO TITLE'


# In[164]:

def votes(post):
    if post.find('div', {'class': 'score unvoted'}):
        return int(post.find('div', {'class': 'score unvoted'}).string)
    else:
        return 'NO INFO'


# In[156]:

def comments(post):
    if post.find('a', {'class': 'bylink comments may-blank'}):
        comment_string = post.find('a', {'class': 'bylink comments may-blank'}).text
        comment_non_int = comment_string.replace(' comments', '').replace(' comment', '')
        return int(comment_non_int)
    else:
        return 0


# In[162]:

def subreddit(post):
    if post.find('a', {'class': 'subreddit hover may-blank'}):
        return post.find('a', {'class': 'subreddit hover may-blank'}).text
    else:
        return 'NO SUBREDDIT'


# In[262]:

# Doing timestamp with regular expressions

# # When it was posted (get a TIMESTAMP, e.g. 2016-06-22T12:33:58+00:00, not "4 hours ago")
#     # <div> class = 'entry unvoted'
#     # <p> class='tagline'
#     # <time> it's actually in the tag

# # Regular Expressions only works on strings, not Beautiful Soup objects. 
# # Even document is a Beautiful Soup object, so you need to go back to html_str

# timestamps = re.findall(r'datetime="(\S+)"', html_str)
# timestamps

# # Since I want to cut out the first 9 results. First one: 2016-06-22T19:52:01+00:00
# list_number = 8
# for post in posts:
#     list_number += 1
#     print(timestamps[list_number])


# In[265]:

def timestamp(post):
    time = post.find('time')
    if time:
        return time.get('datetime')
    else:
        return 'NO TIMESTAMP'


# In[252]:

# Doing url with regular expressions
# # The URL to the post itself
#     # This is in two places. Both inside the main <div> tag and in the same tag with the title.
# urls = re.findall(r'<a class="title may-blank " href="(\S+)"', html_str)
# urls   


# In[260]:

def url(post):
    if post.get('data-url'):
        if post.get('data-url')[:2] == '/r':
            return 'https://www.reddit.com/' + post.get('data-url')
        else:
            return post.get('data-url')
    else:
        return 'NO URL'


# In[251]:

# My unfinished, really messy attempt at trying to do thumb_url with regular expressions:
        
#         #<img src="//\w.thumbs.redditmedia.com/[\w-]+.jpg"
# thumb_urls = re.findall(r'<a class=("thumbnail s*e*l*f* *may-blank a*f*f*i*l*i*a*t*e* *") href="([/:\w\._]+)" rel="\w*" ><img src=("//\w.thumbs.redditmedia.com/[\w-]+.jpg")', html_str)
# print(len(thumb_urls))
# thumb_urls


# In[248]:

def thumb_url(post):
    image = post.find('img')
    if image:
        return image.get('src')
    else:
        return 'NO THUMBNAIL'


# In[275]:

posts_today = []
post_dict = {}

for post in posts:
    post_dict['title'] = title(post)
    post_dict['votes'] = votes(post)
    post_dict['comments'] = comments(post)
    post_dict['subreddit'] = subreddit(post)
    post_dict['timestamp'] = timestamp(post)
    post_dict['url'] = url(post)
    post_dict['thumb_url'] = thumb_url(post)
    posts_today.append(post_dict)
    post_dict = {}

print(len(posts_today))
posts_today


# In[268]:

import pandas as pd


# In[276]:

posts_today_csv = pd.DataFrame(posts_today)
posts_today_csv


# # Reddit Part Two: Sending data
# 
# You'd like to get something in your inbox about what's happening on reddit every morning at 8:30AM. Using a mailgun.com account and their API, send an email to your email address with the the CSV you saved at 8AM attached. The title of the email should be something like "Reddit this morning: January, 1 1970" 
# 
# <p>TIP: How are you going to find that csv file? Well, think about how specific the datetime stamp in the filename really needs to be.

# In[270]:

import time
datestring = time.strftime('%Y-%m-%d')
filename = 'reddit-data-' + datestring + '.csv'
posts_today_csv.to_csv(filename, index=False)

