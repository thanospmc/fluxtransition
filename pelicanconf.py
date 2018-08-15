#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = 'Thanos Poulos'
SITENAME = 'Flux Transition'
SITEURL = 'https://thanospmc.github.io/'

THEME = '../theme'


PATH = 'content'

TIMEZONE = 'Europe/Brussels'

DEFAULT_LANG = 'English'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Home', '/index.html'),
         ('About', '/pages/about.html'),
         ('Cases', '/pages/cases.html'),
         ('Publications', '/pages/publications.html'),
         )

# Social widget
SOCIAL = (('LinkedIn', 'https://www.linkedin.com/in/thanospoulos/'),
          ('Twitter', 'https://twitter.com/ThanosPoulos'),
          ('Github', 'https://github.com/thanospmc'),
          ('Email', 'mailto:thanos@thanospoulos.org')
          )

DEFAULT_PAGINATION = 10

USE_LOGO = False
USE_SITEMAP = False
USE_PRIVACY_POLICY = True
REUSE_LINKS = True
#USE_LOGO_URL

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
STATIC_PATHS = ['extra/robots.txt']
EXTRA_PATH_METADATA = {'extra/robots.txt':{'path': 'robots.txt'}}

TAGS_ARCHIVES_URL = False

PLUGINS = ['assets']
PLUGIN_PATHS = [os.path.join(THEME, "plugins")]
