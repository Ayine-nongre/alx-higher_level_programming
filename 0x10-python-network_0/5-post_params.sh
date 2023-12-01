#!/bin/bash
# Script that makes a post request to a url
curl -sd "email=test@gmail.com&subject=I will always be here for PLD" "$1"
