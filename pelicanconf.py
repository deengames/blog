#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'nightblade'
SITENAME = 'Deen Games Blog'
SITEURL = ''

PATH = 'content'
DEFAULT_CATEGORY = 'Other'

TIMEZONE = 'Canada/Eastern'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = "atom.xml"
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Games', 'https://www.deengames.com'),
        ('Newsletter', 'https://deengames.eo.page/8t7kx'),
        ('Discord', 'https://discord.gg/5D6XS3b'),)
        

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/deengames'),)

DEFAULT_PAGINATION = 5

THEME = 'themes/dg-from-chameleon'

USE_FOLDER_AS_CATEGORY = False
# Permalink structure
ARTICLE_SAVE_AS = '{date:%Y}/{slug}.html'
ARTICLE_URL = ARTICLE_SAVE_AS

# Add "videos" to list of directories (images) to copy to output
STATIC_PATHS = ["images"]
PLUGINS = ['plugins.open_graph']

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
