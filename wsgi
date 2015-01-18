# Copyright © 2014-2015 Martin Ueding <dev@martin-ueding.de>
 
WSGIScriptAlias /shoppinglist /usr/share/pyshared/shoppinglistsite/wsgi.py
WSGIPythonPath /usr/share/pyshared/

<Directory /usr/share/pyshared/shoppinglistsite/>
        <Files wsgi.py>
        Allow from all
        </Files>
</Directory>
