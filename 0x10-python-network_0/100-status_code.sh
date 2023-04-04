#!/bin/bash
# send request to a URL passed as an argument 
#	and display status code of the response
curl -sI -w '%{http_code}' "$1" -o /dev/null
