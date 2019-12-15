#By default crud ini menggunakan databases sqlite3

#curd menggunakan databases dbms (mysql)
1.Install mysql server
2.Install mysql connector
3.Edit settings.py di derectory crud, ubah konfigurasi database seperti dibawah ini:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':'django-project',
        'USER':'root',
        'PASSWORD':'',
        'HOST':'localhost',
        'PORT':'3306',
    }
}

4.makemigration dan migrate
