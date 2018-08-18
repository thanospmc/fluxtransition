#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = 'Thanos Poulos'
SITENAME = 'Flux Transition'
SITEURL = 'http://localhost:8000'

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
#STATIC_PATHS = ['images','extra/robots.txt', 'extra/CNAME']
STATIC_PATHS = ['images','extra']
EXTRA_PATH_METADATA = {'extra/robots.txt':{'path': 'robots.txt'},
                       'extra/CNAME': {'path': 'CNAME'},
                       'extra/favicon.ico': {'path': 'favicon.ico'},
                       }

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'div.highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html5',
}

TAGS_ARCHIVES_URL = False

PLUGINS = ['assets']
PLUGIN_PATHS = [os.path.join(THEME, "plugins")]
