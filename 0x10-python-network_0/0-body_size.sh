#!/bin/bash

# Check if URL was provided as argument
if [ $# -eq 0 ]; then
  echo "Usage: $0 [URL]"
  exit 1
fi

# Send request to URL and store response in variable
response=$(curl -s -w "\n%{size_download}\n" -o /dev/null "$1")

# Extract size from response
size=$(echo "$response" | tail -n 1)

# Display size in bytes
echo "Size of $1 is ${size} bytes"
