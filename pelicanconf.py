#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Homer White'
SITENAME = "Homer's Pelican Site"
SITEURL = 'https://homerhanumat.github.io/pelican'
THEME = "gum"

PATH = 'content'
PAGE_PATHS = ['pages']

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

DISPLAY_PAGES_ON_MENU = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Links (in default theme)
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)
         
# for bootstrap theme, need some pages, like this:
#MENUITEMS = (('About', 'pages/about.md'),('Vita', 'pages/vita.md'),)

GITHUB_URL = 'https://github.com/homerhanumat'
TWITTER_URL = 'https://twitter.com/homerhanumat'
FACEBOOK_URL = 'https://plus.google.com/+HomerWhitehomerhanumat'
GOOGLEPLUS_URL = 'https://www.facebook.com/homer.white1'

# Social widget
SOCIAL = (('Gihub', 'GITHUB-URL'),
          ('Facebook', 'FACEBOOK-URL'),)


DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['./plugins']
PLUGINS = ['ipynb.markup']



