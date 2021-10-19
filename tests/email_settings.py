#!/usr/bin/env python

# Copyright (C) 2020 Intel Corporation
#
# SPDX-License-Identifier: MIT

from cvat.settings.production import *


# https://github.com/pennersr/django-allauth
ACCOUNT_AUTHENTICATION_METHOD = 'username'
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'

# Email backend settings for Django
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_HOST_USER = "keshavadk@gmail.com"
# EMAIL_HOST_PASSWORD = ""
# EMAIL_USE_TLS = True
# EMAIL_USE_SSL = True
# # EMAIL_TIMEOUT
# # EMAIL_SSL_KEYFILE
# # EMAIL_SSL_CERTFILE

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'keshavadk@gmail.com'
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = 587