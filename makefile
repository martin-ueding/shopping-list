# Copyright © 2015 Martin Ueding <dev@martin-ueding.de>

all:

install:
	python setup.py install --root $(DESTDIR) --install-layout deb
	mkdir -p $(DESTDIR)/var/www/
	cp -r static $(DESTDIR)/var/www/
	mkdir -p $(DESTDIR)/etc/apache2/conf.d/
	cp wsgi $(DESTDIR)/etc/apache2/conf.d/shopping-list

.PHONY: clean
clean:
	$(RM) *.class *.jar
	$(RM) *.o *.out
	$(RM) *.orig
	$(RM) *.pyc *.pyo
	$(RM) -r _build *.egg-info
	$(RM) -r build
	$(RM) -r dist
