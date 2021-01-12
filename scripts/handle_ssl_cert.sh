openssl req -newkey rsa:2048 -new -nodes -x509 \
	-keyout /etc/ssl/private/ubrokeit.key \
	-out /etc/ssl/certs/ubrokeit.crt \
	-subj "/C=PL/ST=Pomorskie/L=Gdansk/O=uBrokeIt/OU=IT/CN=."