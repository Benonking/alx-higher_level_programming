#!/bin/bash
#send GET request to URL and display the body of the response message
curl -sX GET $1 -H "X-school-User-Id: 98"
