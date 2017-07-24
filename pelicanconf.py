#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Isaac Zhou'
SITENAME = 'Ace Big Data'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Do not publish articles set in the future
WITH_FUTURE_DATES = False
TEMPLATE_PAGES = {'blog.html': 'blog.html'}
STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'}}

# Feed generation is usually not desired when developing
FEED_RSS = 'feed/index.html'
FEED_ATOM = 'feed/atom/index.html'
FEED_ALL_RSS = False
FEED_ALL_ATOM = False
TRANSLATION_FEED_RSS = False
TRANSLATION_FEED_ATOM = False

# Blogroll
LINKS = (('Isaac Zhou', 'http://isaaczhou.com'),
         ('PrimerPy', 'http://primerpy.com'))

# Social widget
SOCIAL = (
          ('linkedin', 'https://www.linkedin.com/in/isaaczhou/'),
          ('githuB', 'https://github.com/acebigdata'),
          ('envelope', 'mailto:isaaczhou85@gmail.com')
          )


DEFAULT_PAGINATION = True
PAGINATED_DIRECT_TEMPLATES = ('blog-index',)
DIRECT_TEMPLATES = ('categories', 'index', 'blog-index', 'blog')

POST_LIMIT = 3

# PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Formatting for dates

DEFAULT_DATE_FORMAT = ('%d/%b/%Y %a')

# Formatting for urls

ARTICLE_URL = "{date:%Y}/{date:%m}/{slug}/"
ARTICLE_SAVE_AS = "{date:%Y}/{date:%m}/{slug}/index.html"

# Plugins


# Specify theme

# THEME = "theme/BT3-Flat"
THEME = "/home/isaac/Dropbox/isaaczhou/pelican-themes/BT3-Flat"
# GOOGLE_SEARCH = '013542728820335073314:dcpel18vrey'
SWIFTYPE = ''
SITE_THUMBNAIL = 'http://cdn4.master-bigdata.com/wp-content/uploads/2014/12/bomb-bigdata.png.pagespeed.ce.FjLtTP9DH9.png'
SITE_THUMBNAIL_TEXT = 'Ace Big Data'
SITESUBTITLE = 'Big Data in Action'

DISQUS_SITENAME = 'acebigdata'
GOOGLE_ANALYTICS = ''
GOOGLE_ANALYTICS_DOMAIN = 'acebigdata.com'

### Plugin-specific settings

RELATED_POSTS_MAX = 5

# TODO: align default SITEMAP config to http://wordpress.org/extend/plugins/google-sitemap-generator/stats/
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}


#===theme settings===========================

FAVICON = 'http://cdn4.master-bigdata.com/wp-content/uploads/2014/12/bomb-bigdata.png.pagespeed.ce.FjLtTP9DH9.png'
ICON = 'http://cdn4.master-bigdata.com/wp-content/uploads/2014/12/bomb-bigdata.png.pagespeed.ce.FjLtTP9DH9.png'
SHORTCUT_ICON = 'http://cdn4.master-bigdata.com/wp-content/uploads/2014/12/bomb-bigdata.png.pagespeed.ce.FjLtTP9DH9.png'
HEADER_IMAGE = 'http://moveableonline.com/blog/assets/2016/02/big-data-visualization-e1456688631506-1024x671.png'
BACKGROUND_IMAGE = 'http://moveableonline.com/blog/assets/2016/02/big-data-visualization-e1456688631506-1024x671.png'
COPYRIGHT = '2017 &copy; All Rights Reserved.'
# Google fonts can be downloaded with
# https://neverpanic.de/downloads/code/2014-03-19-downloading-google-web-fonts-for-local-hosting-fetch.sh'
# Maybe you need to add missing mime types to your webserver configuration
USER_FONT = '/theme/fonts/font.css'
USER_BOOTSTRAP = '//maxcdn.bootstrapcdn.com/bootstrap/3.3.4'
#USER_FONTAWESOME = '//maxcdn.bootstrapcdn.com/font-awesome/4.3.0'
USER_JQUERY = '//code.jquery.com/jquery-1.11.2.min.js'

# About ME
PERSONAL_PHOTO = "https://media.licdn.com/mpr/mpr/shrinknp_400_400/AAEAAQAAAAAAAAgPAAAAJGQ3NGRhY2M4LTlkMTAtNGM1OC04NzlmLTk1YzQ4NjZlYTBjNA.jpg"
PERSONAL_INFO = """My name is Isaac Zhou, a data scientist and life-long learner who is working & living in New York, NY. I've spent years in building models and data products to facilitate the consulting projects within my company. I also do program work a lot as a personal hobby in my part-time. Python and R have always been my favorite. I have a master degree in finance and several years experience working as a management consultant for automotive industries. This website serves as a portfolio for all of my projects."""

# work
WORK_DESCRIPTION = ''
# items to descripe a work, "type", "cover-image link", "title", "descption", "link"
WORK_LIST = (('link', 'https://dl.dropboxusercontent.com/u/299446/BT3-Flat.png', 'BT3-Flat', 'A BT3 flat theme for pelican', 'https://github.com/acebigdatat'),)

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Used for jupyter publishing
MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['./plugins']

PLUGINS = ['ipynb.markup', 'sitemap', 'neighbors', 'related_posts']
