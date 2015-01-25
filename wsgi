# Copyright © 2014-2015 Martin Ueding <dev@martin-ueding.de>
 
WSGIScriptAlias /shoppinglist /usr/lib/python2.7/dist-packages/shoppinglistsite/wsgi.py
WSGIPythonPath /usr/lib/python2.7/dist-packages/

<Directory /usr/lib/python2.7/dist-packages/shoppinglistsite/>
        <Files wsgi.py>
        Allow from all
        </Files>
</Directory>
