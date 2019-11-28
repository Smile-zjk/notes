#!/bin/bash
##
#
#
while true 
do
find /var/www/html/ -name "*.php" -mmin -10 | xargs -i mv {} /tmp/php
done
