# eCommerce_project
Project for Biznes Elektroniczny - eCommerce shop

## Authors
Paweł Leśniewski  
Łukasz Skołd  
Łukasz Zdziarski  
Laura Zembrzuska  

## Deployment with Docker

To deploy application you will need to follow these steps:
1. Open two terminals
2. In terminal #1 run `docker build -t ubrokeit .` when in root of this repository
3. While build is running in terminal #1 go to terminal #2 and run following set of commands:
```bash
docker network create prestashop-net
docker run --name biznes-db --network prestashop-net -e MYSQL_ROOT_PASSWORD=admin -d mysql:5.7

docker cp ./sql/dump.sql biznes-db:/tmp/dump.sql
mysql -u root -padmin

# here prompt should change from # to mysql>
CREATE DATABASE prestashop;
exit;

# here prompt should change once again back to #
mysql -u root -padmin prestashop < /tmp/dump.sql
mysql -u root -padmin
# prompt changes to mysql>
USE prestashop;
UPDATE `ps_configuration` SET `value` = NULL WHERE `ps_configuration`.`id_configuration` = 9;
UPDATE `ps_shop_url` SET `domain` = 'localhost:8080', `domain_ssl` = 'localhost:8443' WHERE `ps_shop_url`.`id_shop_url` = 1;
UPDATE ps_configuration SET value = 'localhost:8080' WHERE ps_configuration.`id_configuration` = 229;
UPDATE ps_configuration SET value = 'localhost:8443' WHERE ps_configuration.`id_configuration` = 230;
```
4. When build in terminal #1 finishes run:
```bash
docker run --name ubrokeit --network prestashop-net -p 8080:80 -p 8443:443 ubrokeit
```
5. ubrokeit shop should be reachable at: https://localhost:8443
