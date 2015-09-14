#/bin/sh

RESOURCE_GROUP=$1
#azure group create $RESOURCE_GROUP "East Asia"
#azure group deployment create -f ./vnet.json -p "{\"region\": {\"value\": \"East Asia\"}}" $RESOURCE_GROUP t0

azure group deployment create -f ./opsCenter.json -p "{\"username\": {\"value\": \"datastax\"}, \"password\": {\"value\": \"foo123!\"}, \"region\": {\"value\": \"East Asia\"}}" $RESOURCE_GROUP t0

#azure group deployment create -f ./mainTemplate.json $RESOURCE_GROUP t0
#azure group deployment create -f ./opsCenterNode.json $RESOURCE_GROUP t0
