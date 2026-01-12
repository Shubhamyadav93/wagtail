from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-$!=@2(ogq_8td591)9ey(y@j)sexc5pn$n^zk^_6l+7yl#7sqn"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# Enable Wagtail internationalisation (translations)
WAGTAIL_I18N_ENABLED = True

LANGUAGES = [
    ("en", "English"),
    ("fr", "French"),
]

# Enable automatic page alias creation for translations
WAGTAILSIMPLETRANSLATION_SYNC_PAGE_TREE = True


try:
    from .local import *
except ImportError:
    pass 

