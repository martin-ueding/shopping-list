.. Copyright © 2015 Martin Ueding <dev@martin-ueding.de>

#############
shopping-list
#############

Installation
============

Installation on Debian 7
------------------------

Installation of package
~~~~~~~~~~~~~~~~~~~~~~~

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

    Then you can install it with::

        aptitude update
        aptitude install shopping-list

Database installation
~~~~~~~~~~~~~~~~~~~~~

On any system, you will need a database set up for this project. I have used
MySQL so far and will describe how this works in detail.

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
    exit

In ``/etc/shopping-list/`` there is the file ``databases.js.sample`` which
contains the databases snippet for the Django configuration. Create a copy a
copy of the file at ``databases.js`` in the same folder. The program will look
for it there. The copy has to be done that APT will not overwrite your changed
configuration when a new version comes out.

The file looks likes this:

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

Insert the database name (``NAME``), the user (``USER``) and the password
(``PASSWORD``) you have just configured. The host can be left to be localhost.

Fill database, admin interface
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Now you have to let Django fill up the database. Run ``manage-shopping-list
syncdb`` to fill the database. It will also let you set up a password for the
admin interface. It looks like this:

.. code-block:: console

    # manage-shopping-list syncdb
    Creating tables ...
    Creating table django_admin_log
    Creating table auth_permission
    Creating table auth_group_permissions
    Creating table auth_group
    Creating table auth_user_user_permissions
    Creating table auth_user_groups
    Creating table auth_user
    Creating table django_content_type
    Creating table django_session
    Creating table shoppinglist_shelf
    Creating table shoppinglist_product

    You just installed Django's auth system, which means you don't have any superusers defined.
    Would you like to create one now? (yes/no): yes
    Username (leave blank to use 'root'):
    E-mail address:
    Error: That e-mail address is invalid.
    E-mail address:
    Password:
    Password (again):
    Superuser created successfully.
    Installing custom SQL ...
    Installing indexes ...
    Installed 0 object(s) from 0 fixture(s)

Then restart Apache httpd with::

    service apache2 restart

You should be able to access the thing now at::

    http://HOSTNAME/shoppinglist/

There is an admin interface at::

    http://HOSTNAME/shoppinglist/admin/
