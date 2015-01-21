#!/bin/sh

/usr/bin/couchdb -b

sleep 5

curl -X PUT http://127.0.0.1:5984/puzzle
curl -X PUT http://127.0.0.1:5984/puzzle/3/piece -H 'Content-type: image/png' --data-binary @/tmp/piece3.png

sleep 20

rm -f /tmp/piece3.png
rm -f /tmp/couchdb_bootstrap.sh

/usr/bin/couchdb -d
