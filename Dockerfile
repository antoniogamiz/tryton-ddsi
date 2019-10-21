FROM tryton/tryton:5.2

# you can install the module with pip3 install git+/hg+ if in a accesible version control
# otherwise you can COPY the custom module in the site-package/tryton/module folder
# or you can COPY the module folder and install it
# with RUN cd modulename && python3 setup.py install

EXPOSE 8000
VOLUME ["/var/lib/trytond/db"]

RUN pip install -U pip

ENV TRYTOND_CONFIG=/etc/trytond.conf
USER trytond