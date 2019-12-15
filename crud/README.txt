#By default crud ini menggunakan databases sqlite3

#bila ingin menggunakan database dbms (mysql)
1.Install mysql server (XAMPP)
2.Install mysql client (pip install "mysqlclient==1.3.12") versi menyesuaikan mysql server
2.Install mysql connector (versi menyesuaikan mysql server)
3.Edit settings.py di derectory crud, ubah konfigurasi database seperti dibawah ini:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':'django_project',
        'USER':'root',
        'PASSWORD':'',
        'HOST':'localhost',
        'PORT':'3306',
    }
}

4.migrate
