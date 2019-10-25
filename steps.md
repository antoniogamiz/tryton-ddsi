1. Inicitial setup

~~~
sudo apt-get install python3-env
python3 -m venv .venv --prompt "tryton-demo"
. .venv/bin/activate # virtual **environment**
pip3 install cookiecutter # templates engine
sudo apt install mercurial # como git
cookiecutter hg+https://hg.tryton.org/cookiecutter
~~~

2. Module creation

~~~
cd tryton-demo
mkdir party_custom
touch __init.py
touch party_custom/__init__.py
touch party_custom/party.py
touch party_custom/tryton.cfg
touch party_custom/party.xml
mkdir view
touch view/party_custom_party_form.xml
python setup.py develop
~~~

~~~
<-- Construimos la imagen de nuestro contenedor -->
docker build --rm -f "Dockerfile" -t tryton-ddsi:latest .
<-- Arrancamos la base de datos -->
docker-compose up -d postgres
<-- Configuramos el usuario admin de tryton (solo 1 vez) -->
docker-compose run --no-deps --rm tryton trytond-admin -d demot --all -vv
<-- Arrancamos todos los servicios -->
docker-compose up -d (hacer esto tambien para actualizar)
~~~

/tryton-demo
    /tryton.cfg
    __init__.py
    /party_custom
        /__init__.py
        /party.py
        /party.xml
    /view
        /party_custom_party_form.xml