#!/bin/bash
# takes URL as argumen, sends a GET reuest to the URL and displays the body of the response
curl -sH "X-HolbertonSchool-User-Id:98" "$1"
