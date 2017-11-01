=====
django-no-last-login
=====

This is a extremely simple way to disable Django's behavior of updating a user last_login field on login.
You could use this to connect a Django app to a read-only database, such as a replica, and still having a more or less functional application.

Quick start
-----------

1. Add "nolastlogin" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'nolastlogin',
    ]

2. Add this to the settings::
    NO_UPDATE_LAST_LOGIN = True
