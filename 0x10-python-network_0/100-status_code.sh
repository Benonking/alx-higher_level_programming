#!/bin/bash
# send request to a URL passed as an argument 
curl -sI -w '%{response_code}' "$1" -o /dev/null
