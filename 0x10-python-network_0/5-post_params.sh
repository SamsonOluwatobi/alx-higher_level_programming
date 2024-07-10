#!/bin/bash
# Bash script to send a HTTP POST request with two parameters to a certain server
curl -s "$1" -X POST -d "email=test@gmail.com&subject=I will always be here for PLD"
