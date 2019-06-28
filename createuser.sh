#!/bin/bash

# Creates a user record for the current Cloud9 user
# Author: Matt Rudge

echo "Creating the ${C9_USER} user in MySQL"

sudo mysql -e "CREATE USER '${C9_USER}'@'%' IDENTIFIED BY '';"

echo "Granting privileges"

sudo mysql -e "GRANT ALL PRIVILEGES ON *.* TO '${C9_USER}'@'%' WITH GRANT OPTION;"

echo "Done"