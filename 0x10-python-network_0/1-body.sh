#!/bin/bash
# Script that sends a get request to a URL and returns the body
if [[ $(curl -sI "$1" | grep "HTTP/1.1" | cut -d " " -f 2) == 200 ]]; then curl -s "$1"; fi 
