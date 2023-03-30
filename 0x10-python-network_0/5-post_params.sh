#!/bin/bash
# sends POST request variable email=test@gmail.com,subject= I will always be here for PLD
curl -s "$1" -X POST -d "email=test@gmail.com&subject=I will always be here for PLD"
