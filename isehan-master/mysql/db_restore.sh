source .env
cat <<EOF > ./mysql/data/access.cnf
[client]
user = root
password = $MYSQL_ROOT_PASSWORD
EOF
FILE_NAME=`ls -t ./mysql/backup | head -n 1`
docker cp ./mysql/backup/$FILE_NAME `docker-compose ps -q db`:/tmp/
docker-compose exec db /bin/bash -c "mysql --defaults-extra-file=/var/lib/mysql/access.cnf $MYSQL_DATABASE < /tmp/$FILE_NAME"
docker-compose exec db rm "/tmp/$FILE_NAME"
