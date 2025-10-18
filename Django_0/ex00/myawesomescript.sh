#!/bin/bash

if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

if [[ $1 != https://bit.ly/* ]]; then
    echo "the URL must start with https://bit.ly/"
    exit 1
fi

curled_html=$(curl -s -I $1 | grep location | cut -d" " -f2)


printf "%s\n" "$curled_html"