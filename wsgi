# Copyright © 2014-2015 Martin Ueding <dev@martin-ueding.de>
 
WSGIScriptAlias /shoppinglist /usr/lib/pyshared/shoppinglistsite/wsgi.py
WSGIPythonPath /usr/lib/pyshared/

<Directory /usr/lib/pyshared/shoppinglistsite/>
    <Files wsgi.py>
        Allow from all
    </Files>
</Directory>

Alias /static/ /usr/share/shopping-list/

<Directory /usr/share/shopping-list/>
    Order deny,allow
    Allow from all
</Directory>

# vim: ft=apache
