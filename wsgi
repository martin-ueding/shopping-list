# Copyright © 2014-2015 Martin Ueding <dev@martin-ueding.de>
 
WSGIScriptAlias /shoppinglist /use/lib/python2.7/dist-packages/shoppinglistsite/wsgi.py
WSGIPythonPath /use/lib/python2.7/dist-packages/

<Directory /use/lib/python2.7/dist-packages/shoppinglistsite/>
        <Files wsgi.py>
        Allow from all
        </Files>
</Directory>
