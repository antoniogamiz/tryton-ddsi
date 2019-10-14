sudo apt install docker.io
sudo groupadd docker
sudo gpasswd -a $USER docker
newgrp docker

docker pull tryton/tryton
docker run --name tryton-postgres -e POSTGRES_PASSWORD=mysecretpassword -e POSTGRES_DB=tryton -d postgres
docker run --link tryton-postgres:postgres -it tryton/tryton trytond-admin -d tryton --all
docker run --name tryton -p 8000:8000 --link tryton-postgres:postgres -d tryton/tryton
docker run --name tryton-cron --link tryton-postgres:postgres -d tryton/tryton trytond-cron -d tryton
