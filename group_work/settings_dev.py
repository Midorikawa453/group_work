from .settings_common import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-5bwhs^l5oh)a7o13d@2!r6s0ym_9%e$k!7r!n_4e&wcwzmw%uu'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition



# ロギング設定
LOGGING = {
    'version': 1,  # 1固定
    'disable_existing_loggers': False,

    # ロガーの設定
    'loggers': {
        # Djangoが利用するロガー
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
        },
        # diaryアプリケーションが利用するロガー
        'diary': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    },

    # ハンドラの設定
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'dev'
        },
    },

    # フォーマッタの設定
    'formatters': {
        'dev': {
            'format': '\t'.join([
                '%(asctime)s',
                '[%(levelname)s]',
                '%(pathname)s(Line:%(lineno)d)',
                '%(message)s'
            ])
        },
    }
}

# コンソール用
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# Gmail用
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# Gmailのメールサーバーへの接続設定
#EMAIL_HOST = 'smtp.gmail.com'
#EMAIL_PORT = 587
#EMAIL_HOST_USER = <Gmailのメールアドレス>
#EMAIL_HOST_PASSWORD = <Gmailのパスワード>
#EMAIL_USE_TLS = True

MEDIA_ROOT = os.path.join(BASE_DIR,'media')