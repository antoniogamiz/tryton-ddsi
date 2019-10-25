1. Inicitial setup

~~~
sudo apt-get install python3-env
python3 -m venv .venv --prompt "tryton-demo"
. .venv/bin/activate # virtual environment
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
docker build --rm -f "Dockerfile" -t tryton-ddsi:latest .
docker-compose up -d postgres
docker-compose run --no-deps --rm tryton trytond-admin -d demot --all -vv
docker-compose up -d (hacer esto tambien para actualizar)
~~~

