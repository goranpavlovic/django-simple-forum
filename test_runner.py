#!/usr/bin/env python
import os
import sys
import django
from django.conf import settings
from django.test.utils import get_runner
from django.conf.urls import include, url


if __name__ == "__main__":
    os.environ['DJANGO_SETTINGS_MODULE'] = 'tests.test_settings'
    django.setup()
    TestRunner = get_runner(settings)
    test_runner = TestRunner()
    failures = test_runner.run_tests(["django_simple_forum"])
    sys.exit(bool(failures))


urlpatterns = [
    url(r'^', include(('django_simple_forum.urls', 'django_simple_forum'), )),
]
