#!/bin/bash
# takes in a URL, sends POST request, to URL, displays the body of response
# variable email=test@gmail.com, subject= I will always be here for PLD
curl -sd "email=test@gmail.com&subject=I will always be here for PLD" -X POST $1
