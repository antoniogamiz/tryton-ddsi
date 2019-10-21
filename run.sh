docker run --name tryton-postgres -e POSTGRES_PASSWORD=mysecretpassword -e POSTGRES_DB=tryton -d postgres
sleep 5
docker run --link tryton-postgres:postgres -it tryton/tryton trytond-admin -d tryton --all
docker run --name tryton -p 8000:8000 --link tryton-postgres:postgres -d tryton/tryton

