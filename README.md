# eCommerce_project
Project for Biznes Elektroniczny - eCommerce shop

## Authors
Paweł Leśniewski  
Łukasz Skołd  
Łukasz Zdziarski  
Laura Zembrzuska  

## Deployment with Docker

To deploy full application (database and prestashop containers), simply use provided docker-compose file:
```bash
docker-compose up
```
You will have to manually upload sql dump to biznes-db container and change two field there:
```bash
# On host machine command line, when in root of this repository
docker cp ./sql/dump.sql biznes-db:/tmp/dump.sql
```

```bash
# On docker container
mysql -u root -padmin

# MySQL starts (you should see mysql> as prompt instead of #)
create database prestashop;
exit;

# Exit from MySQL
mysql -u root -padmin prestashop < /tmp/dump.sql

# Enter MySQL once again
mysql -u root -padmin
UPDATE `ps_configuration` SET `value` = NULL WHERE `ps_configuration`.`id_configuration` = 9;
UPDATE `ps_shop_url` SET `domain` = '${DOMAIN}', `domain_ssl` = '${DOMAIN_SSL}' WHERE `ps_shop_url`.`id_shop_url` = 1;
exit;
```

