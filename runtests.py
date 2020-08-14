import sys

from django.conf import global_settings, settings

OUR_MIDDLEWARE = []
OUR_MIDDLEWARE.extend(global_settings.MIDDLEWARE)
OUR_MIDDLEWARE.extend([
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
])


settings.configure(
    DATABASES={
        'default': {'ENGINE': 'django.db.backends.sqlite3', 'NAME': ':memory;'}
    },
    INSTALLED_APPS=[
        'django.contrib.auth',
        'django.contrib.sessions',
        'django.contrib.contenttypes',
        'directmessages',
    ],
    #ROOT_URLCONF='directmessages.urls',
    MIDDLEWARE=OUR_MIDDLEWARE,
)


def runtests(*test_args):
    import django.test.utils

    if django.VERSION[0:2] >= (1, 7):
        django.setup()

    runner_class = django.test.utils.get_runner(settings)
    test_runner = runner_class(verbosity=1, interactive=True, failfast=False)
    failures = test_runner.run_tests(['directmessages'])
    sys.exit(failures)


if __name__ == '__main__':
    runtests()
