#!/bin/bash
# sends delete request to the url as the first argument and displays the body respnse
curl -sX DELETE $1
