Title: Running Flask with Python 3 on Ubuntu 16.04
Date: 2016-11-07 22:00
Modified: 2016-11-07 22:00
Category: Python
Tags: flask, ubuntu
Slug: flask-python3-ubuntu
Authors: Homer White
Summary: Running Flask with Python 3 on Ubuntu 16.04

## Introduction

I'm trying out Flask, thinking that I will run it with Python 3.5 rather than with 2.7.  Originally Ubuntu 16.04 Xenial was supposed to have Python 3.5 as the system default, but although it ships with 3.5 the default Python version is still 2.7.  Accordingly you have to do some extra work to get Flask apps to run with the newer Python.

The following notes record what I did to get a "Hello Wordl" flask app running on A Digial Ocean Ubuntu 16.04 droplet.

## Install Python Modules

```
sudo apt-get install python3-pip
```


```
sudo -H pip3 install --target=/usr/local/lib/python3.5/dist-packages Flask
```

## Install The Flask App

```
sudo chown -R homer /var/www
```

```
cd /var/www
mkdir firstapp
cd firstapp
git init
git clone https://github.com/homerhanumat/firstapp.git
```

Run `ls` and you'll see the app `hello.py`.

In the same directory as `hello.py` you need a `hello.wsgi` file to enable Apache to serve the app.

Run:

```
nano hello.wsgi
```

Enter this text:

```
import sys
sys.path.insert(0, "/var/www/firstapp")
from hello import app as application
```





## Install and Configure Apache

```
sudo apt-get install apache2
```

For convenience, make the  configuration directory your own:

```
sudo chown -R /etc/apache2
```

Install the `WSGI` module that enables Apache to serve your apps.  You need the one for Python 3:


```
sudo apt-get install libapache2-mod-wsgi-py3
```

Then set up the configuration for your app:

```
cd /etc/apache2/sites-available
nano hello.conf
```

Enter this text:

```
<VirtualHost *>
    ServerName example.com

    WSGIScriptAlias / /var/www/firstapp/hello.wsgi
    WSGIDaemonProcess hello
    <Directory /var/www/firstapp>
       WSGIProcessGroup hello
       WSGIApplicationGroup %{GLOBAL}
        Order deny,allow
        Allow from all
    </Directory>
</VirtualHost>
```

Disable Apache's default "It works!" app, and enable your own, then reload:

```
sudo a2dissite 000-default.conf
sudo a2ensite hello.conf
sudo service apache2 reload
```

Not aboslutely sure this is needed because the only WSGI installed is for Python 3, but for safety I'm setting the Python path for Apache.  Run:

```
nano /etc/a[ache2/modes-enabled/wsgi.conf
```

Find the line

```
#WSGIPythonPath directory|directory-1:directory-2:...
```

Modify it to read:

```
WSGIPythonPath /usr/bin/python3
```

If you do this, make sure to reload with:

```
sudo service apache2 reload
```

##  Test the App

Head to your browser and paste in the URL of the droplet.  With any luck the app will run.
