#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Tri-M Sports & Consulting Ltd'
SITENAME = u'CanbikeBC'
SITEURL = ''

THEME = 'pelican-bootstrap3'
BOOTSTRAP_THEME = 'united'
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
PATH = 'content'

FAVICON = 'images/favpenguin.png'

BANNER = '/images/banner.jpg'
BANNER_ALL_PAGES = True

PLUGIN_PATHS = ['/home/gentoolink/websites/pelican-plugins/']
PLUGINS = ['i18n_subsites']


TIMEZONE = 'America/Vancouver'

DEFAULT_LANG = u'en'

#This is where my blog posts will be kept.
ARTICLE_PATHS = ['blog']


# Delete the output directory, and all of its contents, before generating new files. This can be useful in preventing older, unnecessary files from persisting in your output. However, this is a destructive setting and should be handled with extreme care.
#DELETE_OUTPUT_DIRECTORY = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Bookmarks
LINKS = (('Courses', 'https://helpdesk.gentoolink.com'),
         ('Canbike', 'http://nextcloud.com/'),
         ('My Blog', 'https://blog.canbikebc.ca'),
         ('Inspire Wear Store', 'https://inspirewear.store'),)

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/chuckglover1'),
          ('Facebook', 'https://facebook.com/'),
	('Instagram', 'https://instagram.com'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True


GOOGLE_ANALYTICS = 'put code in here'
