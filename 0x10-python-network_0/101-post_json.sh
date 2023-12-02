#!/bin/bash
# Script that sends a post request to a URL and returns response body
curl -s "$1" -d "@$2" -X POST -H "Content-Type: application/json"
