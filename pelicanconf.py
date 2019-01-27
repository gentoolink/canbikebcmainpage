#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Tri-M Sports & Consulting Ltd'
SITENAME = u'Can-Bike BC'
SITEURL = ''
CUSTOM_LICENSE = 'Designed & Hosted by <a href="https://gentoolink.com/">Gentoolink Web Services Inc.</a>'


THEME = 'pelican-bootstrap3'
BOOTSTRAP_THEME = 'united'
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
PATH = 'content'

FAVICON = 'images/favicon.ico'
SITELOGO = 'images/logo.png'
SITELOGO_SIZE = '50x50'
BANNER = 'images/banner.jpg'
BANNER_SUBTITLE = 'Welcome to Can-Bike British Columbia'
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
LINKS = (('Courses Login', 'https://courses.canbikebc.ca'),
         ('My Blog', 'https://blog.canbikebc.ca'),
         ('Can-Bike Canada', 'http://canbikecanada.ca/'),
	('Project529', 'https://project529.com/garage'))

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/chuckglover1'),
          ('Facebook', 'https://facebook.com/ch.glover.1'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True


GOOGLE_ANALYTICS = 'put code in here'
