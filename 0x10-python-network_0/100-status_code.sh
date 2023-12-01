#!/bin/bash
# Script to return only the status code
curl -sI "$1" | grep "HTTP/1.1" | cut -d " " -f 2 