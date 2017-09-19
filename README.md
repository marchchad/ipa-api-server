# ipa-api-server

# Developer Environment Setup

## Linux - Ubuntu 17.04

Make sure to install:

  * `python-dev`
  * `libmysqlclient-dev`
  
## Windows - 10

Make sure to install the wheel in `python_dependencies/windows` using `pip`

## Miscellaneous

Django OAuth Toolkit getting started is out of date. See [this StackOverflow post](https://stackoverflow.com/a/45029747/1783650) for the necessary modifications to the `settings.py` in order to get everything initially setup.

# Deployments

## Third Party Libraries

To use libraries such as Django Rest Framework, see how to handle installing and packaging third party libraries here: https://cloud.google.com/appengine/docs/standard/python/tools/using-libraries-python-27#installing_a_third-party_library

## Static Files

Don't forget to run `manage.py collectstatic` before deploying

## To Deploy

Haven't figured out how to set up a hook into GitHub commits. For now, use `gcloud app deploy`.

## SSL

Google App Engine now provides Let's Encrypt certs for all custom domains once ownership is proven. To enforce HTTPS only, update the `app.yaml` to include `secure: always`