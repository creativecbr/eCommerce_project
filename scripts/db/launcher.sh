#!/bin/bash

kubectl --namespace="biznes-elektroniczny" cp ~/studenci/11/db/db_11.sql biznes-db-7d46b58f4d-rm2v9:/tmp/db_11.sql
kubectl --namespace="biznes-elektroniczny" cp ~/studenci/11/db/creator.sh biznes-db-7d46b58f4d-rm2v9:/tmp/creator.sh
kubectl --namespace="biznes-elektroniczny" exec --stdin --tty biznes-db-7d46b58f4d-rm2v9 -- chmod +x /tmp/creator.sh
kubectl --namespace="biznes-elektroniczny" exec --stdin --tty biznes-db-7d46b58f4d-rm2v9 -- /tmp/creator.sh
kubectl --namespace="biznes-elektroniczny" exec --stdin --tty biznes-db-7d46b58f4d-rm2v9 -- rm /tmp/creator.sh
kubectl --namespace="biznes-elektroniczny" exec --stdin --tty biznes-db-7d46b58f4d-rm2v9 -- rm /tmp/db_11.sql
