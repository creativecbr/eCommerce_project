#!/bin/bash

function help {
	echo "Script creating user, database and uploading sql dump."
	echo "Options:"
	echo "--database-name			name of database to create, default is db_11"
	echo "--domain 				domain of prestashop, default value is localhost:8080"
	echo "--domain-ssl 			domain of prestashop with ssl, default value is localhost:8443"
	echo "--dump-path			path to sql dump, default is /tmp/db_11.sql"
	echo "--user				database user to create, default is user_11"
	echo "--user-password			user's password, default is root"
	echo "--password			root's password to database, default is dev"
	echo "--help 				shows this message"
}

DB="db_11"
USER="user_11"
USR_PASS="root"
PASS="dev"
DUMP_PATH="/tmp/db_11.sql"
DOMAIN="localhost:8080"
DOMAIN_SSL="localhost:8443"

while [ -n "$1" ]; do
	case "$1" in
		--database-name)
			DB="$2"
			shift
			shift
			;;
		--user)
			USER="$2"
			shift
			shift
			;;
		--user-password)
			USR_PASS="$2"
			shift
			shift
			;;
		--password)
			PASS="$2"
			shift
			shift
			;;
		--dump-path)
			DUMP_PATH="$2"
			shift
			shift
			;;
		--domain)
			DOMAIN="$2"
			shift
			shift
			;;
		--domain-ssl)
			DOMAIN_SSL="$2"
			shift
			shift
			;;
		--help)
			help
			exit 0
			;;
		*)
			echo "Option $1 not recognized"
			help
			exit 0
			;;
	esac
done

# Create database, database user and set its privileges
mysql -p$PASS -e "CREATE DATABASE IF NOT EXISTS ${DB};"
mysql -p$PASS -e "CREATE USER IF NOT EXISTS '${USER}'@'%' IDENTIFIED BY '${USR_PASS}';"
mysql -p$PASS -e "GRANT ALL PRIVILEGES ON ${DB}.* TO '${USER}'@'%';"
mysql -p$PASS -e "FLUSH PRIVILEGES;"

mysql -u $USER -p$USR_PASS $DB < $DUMP_PATH

# Modify field in dump.sql
mysql -u $USER -p$USR_PASS $DB -e "UPDATE `ps_configuration` SET `value` = NULL WHERE `ps_configuration`.`id_configuration` = 9;"
mysql -u $USER -p$USR_PASS $DB -e "UPDATE `ps_shop_url` SET `domain` = '${DOMAIN}', `domain_ssl` = '${DOMAIN_SSL}' WHERE `ps_shop_url`.`id_shop_url` = 1;"

