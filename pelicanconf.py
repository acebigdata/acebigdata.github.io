#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Isaac Zhou'
SITENAME = "Ace Big Data"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['./plugins']
PLUGINS = ['ipynb.markup']

# Themes
BS3_URL = 'https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/css/bootstrap.min.css'
BS3_JS  = 'https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/js/bootstrap.min.js'
BS3_THEME = 'https://bootswatch.com/default/bootstrap.min.css'

MENUITEMS = [
    ('Home', '/'),
    ('Posts By', [
        ('Categories', '/categories.html'),
        ('Chronological', '/archives.html'),
        ('Tags', '/tags.html'),
        ]),
    ('DLND', [
        ('Neural Networks', '/dlnd-nn.html'),
        ('Convolutional Neural Networks', '/dlnd-cnn.html'),
        ('Recurrent Neural Networks', '/dlnd-rnn.html'),
        ('Generative Adversarial Networks', '/dlnd-gan.html'),
        ]),
    ('Analytics Edge', [
        ('Intro to Analytics', '/ae-intro.html'),
        ('Linear Regression', '/ae-linear-regression.html'),
        ('Logistics Regression', '/ae-logistics-regression.html'), 
        ('Tree', '/ae-tree.html'),
        ('Text Analytics', '/ae-text-analytics.html'),
        ('Clustering', '/ae-clustering.html'),
        ('Visualization', '/ae-visualization.html'),        
        ]),
    ('DataCamp Python', [
        ('Intro to Python', '/dc-intro-python.html'),
        ('Intermediate Python', '/dc-intermediate-python.html'),
        ('Python Data Science Toolbox', '/dc-data-science-toolbox.html'),
        ('Importing Data Python', '/dc-import-data-python.html'),
        ('Cleaning Data Python', '/dc-clean-data-python.html'),
        ('Pandas', '/dc-pandas.html'),
        ('Database in Python', '/dc-database-python.html'),
        ('Visualization in Python', '/dc-visualization-python.html'),
        ('Bokeh', '/dc-bokeh.html'),
        ('Statistical Thinking', '/dc-stat.html'),
        ('Supervised Learning', '/dc-supervised-learning.html'),
        ('Unsupervised Learning', '/dc-unsupervised-learning.html'),
        ('Deep Learning', '/dc-deep-learning.html'),
        ('Network Analysis', '/dc-network-analysis.html'),
        ]),
    ('Others', [
        ('DataCamp SQL', '/dc-sql.html'),
        ('Natural Language Processing', '/nlp.html'),        
        ]),    
    ('Search', '008288081600836329244:fdefrs0jhtk'),
    ]

FAVICON = u'https://photos-5.dropbox.com/t/2/AAApnB-1cvGXYPU5TzIpWjw2XO8gopGCMRMDpPUgANgneg/12/669394314/png/32x32/1/_/1/2/primerpyfavicon.png/EJzL47sFGI7MEyACKAI/ifTZBqf1Hxef7jG8ne_8la0vY3YzQTcFZUJL0Th_vi4?size=2048x1536&size_mode=3'

FAVICON_TYPE = u'png'

STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}
