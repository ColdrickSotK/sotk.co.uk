#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Adam Coldrick'
SITENAME = u'SotK'
SITEURL = ''
THEME = 'theme'

PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = u'en'

PAGE_URL='{slug}'
PAGE_SAVE_AS='{slug}/index.html'

AUTHOR_SAVE_AS=''
AUTHORS_SAVE_AS=''

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['tag_cloud']


# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
