from settings import *


DEBUG = TEMPLATE_DEBUG = True

MEDIA_ROOT = ''

SESSION_COOKIE_AGE = 60 * 60 * 24 * 14

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_DIRS = (  
    # Put strings here, like "/home/html/static" or "C:/www/django/static".  
    # Always use forward slashes, even on Windows.  
    # Don't forget to use absolute paths, not relative paths.  
    "os.path.join(BASE_DIR, "static_in_pro", "our_static"),",  
)

STATICFILES_FINDERS = (  
    'django.contrib.staticfiles.finders.FileSystemFinder',  
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',  
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',  
) 

MANAGERS = ADMINS

if 'SERVER_SOFTWARE' in os.environ:
    from sae.const import (
        MYSQL_HOST, MYSQL_PORT, MYSQL_USER, MYSQL_PASS, MYSQL_DB
    )
else:
    MYSQL_HOST = 'localhost'
    MYSQL_PORT = '3306'
    MYSQL_USER = 'root'
    MYSQL_PASS = '123'
    MYSQL_DB   = 'lab_mgr'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': MYSQL_DB,                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': MYSQL_USER,
        'PASSWORD': MYSQL_PASS,
        'HOST': MYSQL_HOST,                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': MYSQL_PORT,                      # Set to empty string for default.
    }
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
#ALLOWED_HOSTS = []
ALLOWED_HOSTS = ['*']