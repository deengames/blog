#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'nightblade'
SITENAME = 'Deen Games Blog'
SITEURL = 'http://deengames.com/blog'

PATH = 'content'

TIMEZONE = 'Canada/Eastern'

DEFAULT_LANG = 'English'

# Feed generation is usually not desired when developing
FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = "atom.xml"
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Deen Games', 'http://deengames.com'),
        ('Patreon Page', 'http://patreon.com/deengames'),)

# Social widget
SOCIAL = (('Twitter (nightblade99)', 'https://twitter.com/nightblade99'),
        ('Twitter (ChemicalInk)', 'https://twitter.com/chemical_ink'),
        ('Twitter (official)', 'https://twitter.com/deengames'),)

DEFAULT_PAGINATION = False

THEME = 'dg-theme'

GOOGLE_ANALYTICS = "UA-11092514-4"

USE_FOLDER_AS_CATEGORY = False
# Permalink structure
ARTICLE_SAVE_AS = '{date:%Y}/{slug}.html'
ARTICLE_URL = ARTICLE_SAVE_AS

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
