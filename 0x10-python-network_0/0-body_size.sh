#!/bin/bash
# This is a script that sends a URL request and returns the size of the body response
cURL -sI "$1" | grep "Content-Length:" | cut -d " " -f 2