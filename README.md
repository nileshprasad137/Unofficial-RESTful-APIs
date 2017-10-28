# Unofficial-RESTful-APIs

This repository contains simple Python scripts to convert RSS Feed from popular platforms to convert them to RESTful APIs.

Flask-RESTPlus is being used for the purpose.Flask-RESTPlus is an extension for Flask that adds support for quickly building REST APIs. Flask-RESTPlus encourages best practices with minimal setup. It provides a coherent collection of decorators and tools to describe your API and expose its documentation properly (using Swagger).

- [x] Udacity
    * Official API(not REST API) at https://www.udacity.com/public-api/v0/courses 
    * Also refer - https://s3.amazonaws.com/content.udacity-data.com/techdocs/UdacityCourseCatalogAPIDocumentation-v0.pdf

- [x] EDX
    * RSS FEED from https://www.edx.org/api/v2/report/course-feed/rss

- [x] Hindustan Times 
    * RSS FEED from http://www.hindustantimes.com/rss/topnews/rssfeed.xml

- [ ] MIT OCW

- [ ] Techcrunch

## How to Run?

Flask-RestPlus requires Python 2.7+.

You can install Flask-Restplus with pip:
`$ pip install flask-restplus`
or with easy_install:
`$ easy_install flask-restplus`

In order to run an API, `cd` into the directory and in the terminal run the command - `python file_name.py`

The purpose of this repository was to learn about REST APIs. Feel free to contribue and add more APIs.