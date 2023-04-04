#!/bin/bash
# send request to a URL passed as an argument 
#	and display status code of the response
curl -s -o /dev/null -w '%{http_code}' "$1"
