import os

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'messaging_app.settings')
    import django
    django.setup()
    print("Messaging app ready")
