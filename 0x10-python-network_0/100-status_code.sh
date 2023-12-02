#!/bin/bash
# Script to return only the status code
curl -so /dev/null -w "%{http_code}" "$1"
