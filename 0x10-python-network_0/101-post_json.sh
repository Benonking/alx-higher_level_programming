#!/bin/bash
#make a post request with the cotents oa a file passed with filename as argument
curl -s -X POST "$1" -H "Content-Type: application/json" -d @"$2"
