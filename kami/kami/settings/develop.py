#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

from .base import * # NOQA


DEBUG = True


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
