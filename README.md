## frauk
### matekasse & more

[Mete](https://github.com/chaosdorf/mete) Clone based on Python and Flask.

#### Import from [Mete](https://github.com/chaosdorf/mete)

The import only works if no frauk db exists.

    $ mv app/dev.db app/dev.db_bak
    $ python mete_import.py /path/to/mete_database.db

That's it.

#### Roadmap
* zunächst als [Mete](https://github.com/chaosdorf/mete) Clone mit Python und Flask [95%]
* Admin Panel zum Editieren von Usern und Preisen.
* Barcode Scanner zum Scannen der Items
* User Auth über NFC Karten
* Getränkebestandsanzeige, Statistiken
* Gamification (Archivements oder so?)

#### Install Guide

Exaples work for Debian9. You might need to do things differently for other distributions. 

After login, 

Install pip

	$ sudo apt-get install python-pip
    
Install git

	$ sudo apt-get install git

clone the frauk repo
	
    $ git clone https://github.com/Maschinendeck/frauk
    
enter the directory created by git clone

	$ cd frauk

check if virtualenv is installed

	$ pip list | grep virtualenv
    
if yes fine else install it with

	$ pip install virtualenv
    
create a new virtual environment for the frauk app and activate it

	$ virtualenv venv
    $ source venv/bin/activate
    
and install the frauk python package.
the ````--editable```` installs frauk in its current location.

	(venv) $ pip install --editable .

it should now install flask and other things, including frauk.

copy the ````config.py```` and change the database path to wherever you want.

now we need to set a few environment variables. since we are in a virtual environment these are stored permanently

    (venv) $ export FLASK_APP=frauk
    (venv) $ export FLASK_DEBUG=0 # 1 when developing
    (venv) $ export FRAUK_CONFIG=/home/vann/projects/frauk/config.py

to create a new database do:

	(venv) $ python
    > from frauk import db
    > db.create_all()
    > exit()

after that you can import an sqlite database from chaosdorfs mete with

	(venv) $ python mete_import /path/to/mete.db
    
now to start everything and check if it works do:

	(venv) $ flask run

it should tell you that it's listening on ````localhost:5000````.

````(venv) $ curl localhost:5000```` to test if its working

__So far you've got a development setup. If that's your goal you can stop reading.__

If you want to put it behind a webserver, go ahead and install gunicorn and nginx

	(venv) $ pip install gunicorn
	(venv) $ sudo apt-get install nginx
    
gunicorn runns our application and sits behind nginx as reverse proxy

test if gunicorn is working\

	(venv) $ gunicorn frauk:frauk
    
then create your config for nginx at ````/etc/nginx/sites-available/frauk````

```nginx
# /etc/nginx/sites-available/frauk
# Handle requests to frauk on port 80
server {
        listen 80;
        server_name <your domain or ip>;

                # Handle all locations
        location / {
                        # Pass the request to Gunicorn
                proxy_pass http://127.0.0.1:8000;

                # Set some HTTP headers so that our app knows where the
                # request really came from
                proxy_set_header Host $host;
                proxy_set_header X-Real-IP $remote_addr;
                proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        }
}
```

this activates the config above

	$ sudo ln -s \
	/etc/nginx/sites-available/frauk \
	/etc/nginx/sites-enabled/frauk

reload the nginx config with

	(venv) $ sudo service nginx reload

now check if you can reach the app with curl

	(venv) $ curl 127.0.0.1
    
yeah, that's it congratz.
