source .env
cat <<EOF > ./mysql/data/access.cnf
[client]
user = root
password = $MYSQL_ROOT_PASSWORD
EOF
docker-compose exec db mysqldump --defaults-extra-file=/var/lib/mysql/access.cnf --all-databases > ./mysql/backup/db-`date "+%Y%m%d_%H%M%S"`.dump