FROM prestashop/prestashop

# Override prestshop/base variables' values
ENV PSS_CONFIGURATION_FILE=/var/www/html/app/config/parameters.php \
DBS_SERVER=biznes-db \
DBS_NAME=prestashop \
DBS_PORT='' \
DBS_PREFIX=ps_ \
DBS_USER=root \
DBS_PASSWD=admin \
PSS_DOMAIN=localhost

RUN rm -rf /var/www/html/install/

# Copy files of prestashop
COPY ./html /var/www/html
RUN chown -R www-data:www-data /var/www/html && \
	chmod -R 755 /var/www/html

# Update parameters
RUN sed -i "s|'biznes-db'|'${DBS_SERVER}'|g" ${PSS_CONFIGURATION_FILE}
RUN sed -i "s|''|'${DBS_PORT}'|g" ${PSS_CONFIGURATION_FILE}
RUN sed -i "s|'database_user' => 'root'|'database_user' => '${DBS_USER}'|g" ${PSS_CONFIGURATION_FILE}
RUN sed -i "s|'database_password' => 'admin'|'database_password' => '${DBS_PASSWD}'|g" ${PSS_CONFIGURATION_FILE}
RUN sed -i "s|'prestashop'|'${DBS_NAME}'|g" ${PSS_CONFIGURATION_FILE}
RUN sed -i "s|'ps_'|'${DBS_PREFIX}'|g" ${PSS_CONFIGURATION_FILE}

# Create SSL cert and copy apache2 configuration
RUN mkdir /scripts
COPY ./scripts/handle_ssl_cert.sh /scripts/handle_ssl_cert.sh
RUN /scripts/handle_ssl_cert.sh
COPY ./server_conf/000-default.conf /etc/apache2/sites-available/000-default.conf

# Enable apache2 modules
RUN a2enmod ssl headers

# Set default directory
WORKDIR /var/www/html

# Expose ports
EXPOSE 80 443
