#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Max Liu'
SITENAME = u'Imaginary Frequencies'
SITESUBTITLE = 'My Personal Blog'
SITEURL = ''

PATH = 'content'
STATIC_PATHS = [
    'static',
    'images',
]

EXTRA_PATH_METADATA = {
    'static/favicon.ico': {'path': 'favicon.ico'}
}

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

TYPOGRIFY = True

# Theme specific settings
THEME = 'nest'
# Add items to top menu before pages
MENUITEMS = [('Home', '/'), ('Categories', '/categories.html')]
# Add header background image from content/images : 'background.jpg'
NEST_HEADER_IMAGES = 'background1.jpg'
NEST_HEADER_LOGO = '/static/logo.png'
# Footer
NEST_SITEMAP_COLUMN_TITLE = u'Sitemap'
NEST_SITEMAP_MENU = [('Archives', '/archives.html'), ('Tags','/tags.html'), ('Authors','/authors.html')]
#NEST_SITEMAP_ATOM_LINK = u'Atom Feed'
#NEST_SITEMAP_RSS_LINK = u'RSS Feed'
NEST_SOCIAL_COLUMN_TITLE = u'Social'
NEST_LINKS_COLUMN_TITLE = u'Links'
NEST_COPYRIGHT = u'&copy; Mengjie Liu 2017'
# Footer optional
#NEST_FOOTER_HTML = ''
# index.html
NEST_INDEX_HEAD_TITLE = u'Home'
NEST_INDEX_HEADER_TITLE = u'Imaginary Frequencies'
NEST_INDEX_HEADER_SUBTITLE = u'Where chemical engineering meets programming'
NEST_INDEX_CONTENT_TITLE = u'Recent Posts'
# archives.html
NEST_ARCHIVES_HEAD_TITLE = u'Archives'
NEST_ARCHIVES_HEAD_DESCRIPTION = u'Post Archives'
NEST_ARCHIVES_HEADER_TITLE = u'Archives'
NEST_ARCHIVES_HEADER_SUBTITLE = u'Archive of all posts'
NEST_ARCHIVES_CONTENT_TITLE = u'Archives'
# article.html
NEST_ARTICLE_HEADER_BY = u'By'
NEST_ARTICLE_HEADER_MODIFIED = u'modified'
NEST_ARTICLE_HEADER_IN = u'in category'
# author.html
NEST_AUTHOR_HEAD_TITLE = u'Posts by'
NEST_AUTHOR_HEAD_DESCRIPTION = u'Posts by'
NEST_AUTHOR_HEADER_SUBTITLE = u'Post archives'
NEST_AUTHOR_CONTENT_TITLE = u'Posts'
# authors.html
NEST_AUTHORS_HEAD_TITLE = u'Author list'
NEST_AUTHORS_HEAD_DESCRIPTION = u'Author list'
NEST_AUTHORS_HEADER_TITLE = u'Author list'
NEST_AUTHORS_HEADER_SUBTITLE = u'Archives listed by author'
# categories.html
NEST_CATEGORIES_HEAD_TITLE = u'Categories'
NEST_CATEGORIES_HEAD_DESCRIPTION = u'Archives listed by category'
NEST_CATEGORIES_HEADER_TITLE = u'Categories'
NEST_CATEGORIES_HEADER_SUBTITLE = u'Archives listed by category'
# category.html
NEST_CATEGORY_HEAD_TITLE = u'Category Archive'
NEST_CATEGORY_HEAD_DESCRIPTION = u'Category archive'
NEST_CATEGORY_HEADER_TITLE = u'Category'
NEST_CATEGORY_HEADER_SUBTITLE = u'Category archive'
# pagination.html
NEST_PAGINATION_PREVIOUS = u'Previous'
NEST_PAGINATION_NEXT = u'Next'
# period_archives.html
NEST_PERIOD_ARCHIVES_HEAD_TITLE = u'Archives for'
NEST_PERIOD_ARCHIVES_HEAD_DESCRIPTION = u'Archives for'
NEST_PERIOD_ARCHIVES_HEADER_TITLE = u'Archives'
NEST_PERIOD_ARCHIVES_HEADER_SUBTITLE = u'Archives for'
NEST_PERIOD_ARCHIVES_CONTENT_TITLE = u'Archives for'
# tag.html
NEST_TAG_HEAD_TITLE = u'Tag Archive'
NEST_TAG_HEAD_DESCRIPTION = u'Tag archive'
NEST_TAG_HEADER_TITLE = u'Tag'
NEST_TAG_HEADER_SUBTITLE = u'Tag archive'
# tags.html
NEST_TAGS_HEAD_TITLE = u'Tags'
NEST_TAGS_HEAD_DESCRIPTION = u'Tag list'
NEST_TAGS_HEADER_TITLE = u'Tags'
NEST_TAGS_HEADER_SUBTITLE = u'Tag list'
NEST_TAGS_CONTENT_TITLE = u'Tag List'
NEST_TAGS_CONTENT_LIST = u'tagged'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ('Green Group', 'http://cheme.scripts.mit.edu/green-group/'),
    ('RMG', 'http://rmg.mit.edu/'),
)

# Social widget
SOCIAL = (
    ('LinkedIn', 'https://www.linkedin.com/in/liumengjie'),
    ('GitHub', 'https://github.com/mliu49')
)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
