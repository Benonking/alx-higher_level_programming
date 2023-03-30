#!/bin/bash
# sends a request to URL and dsplays the size of the body response
curl -sI "$1" | grep content-length
