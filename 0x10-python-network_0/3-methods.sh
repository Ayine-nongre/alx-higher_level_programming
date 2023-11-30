#!/bin/bash
# Script to check what methods are available in a URL
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
