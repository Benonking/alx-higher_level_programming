#!/bin/bash
# sends a request to URL and dsplays the size of the body response
curl -s "$1" | wc -c
