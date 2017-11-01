from django.conf import settings
from django.contrib.auth.models import update_last_login
from django.contrib.auth.signals import user_logged_in


def _readonly():
    return getattr(settings, 'NO_UPDATE_LAST_LOGIN', False)


if _readonly():
    user_logged_in.disconnect(update_last_login)
