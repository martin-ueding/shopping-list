.. Copyright © 2015 Martin Ueding <dev@martin-ueding.de>

#############
shopping-list
#############

Installation
============

Installation on Debian 7
------------------------

There is a Debian 7 package here:

One-off installation
    You can just download the latest package and install it using::

        dpkg -i shopping-list_1.0.6-django1.4-2_all.deb

    It will then probably complain about missing dependencies, then you have to
    install those with ``apt-get`` or ``aptitude`` yourself. You will not get
    automatic updates of the package.

Add repository
    You can add this as a repository to your system by adding the following
    line to ``/etc/apt/sources.list``::

        deb http://debian.martin-ueding.de/ /

Database installation
~~~~~~~~~~~~~~~~~~~~~

On any system, you will need a database set up for this project. I have used
MySQL so far.

In ``/etc/shopping-list/`` there is the file ``databases.js.sample`` which
contains the databases snippet for the Django configuration. You can use the
database you want. For MySQL, you need to set up a new user (although you can
also just use ``root`` if you are lazy) and a database for the program. Then
enter all this into a copy of the file at ``databases.js`` in the same folder.
The program will look for it there.

.. code-block:: javascript

    {
        "default": {
            "ENGINE": "django.db.backends.mysql",
            "NAME": "django",
            "USER": "django",
            "PASSWORD": "PASSWORD",
            "HOST": "localhost"
        }
    }

To set up a new MySQL user and database, do the following. Start the MySQL
client:

.. code-block:: console

    $ mysql -u root -p
    Enter password:

Then create a new database called ``django`` (or something else):

.. code-block:: sql

    CREATE DATABASE django;

Then create a new user called ``django`` (or something else) and grant that new
user all priviliges on the ``django`` database:

.. code-block:: sql

    CREATE USER 'django'@'localhost' IDENTIFIED BY 'password';
    GRANT ALL PRIVILEGES ON django . * TO 'django'@'localhost';
    FLUSH PRIVILEGES;

Then restart Apache httpd with::

    service apache2 restart

You should be able to access the thing now at::

    http://hostname/shoppinglist/

There is an admin interface at::

    http://hostname/shoppinglist/admin/
