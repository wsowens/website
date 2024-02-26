#!/usr/bin/env python
# -*- coding: utf-8 -*- #
# required for some blog posts:  pelican-plugins/simple-footnotes
# pip install pelican-simple-footnotes

AUTHOR = 'Will Owens'
SITENAME = 'Et cetera'
SITEURL = 'https://ovvens.com/etc'

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = ()

# Social widget
# SOCIAL = ()

# I'll enable this later
DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# disable creating pages for category and author
AUTHOR_SAVE_AS = ''
CATEGORY_SAVE_AS = ''

SUMMARY_MAX_LENGTH = 10
SUMMARY_END_SUFFIX = "... (Read more)"
