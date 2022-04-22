#!/bin/bash
# -s silent -I head
curl -so /dev/null "$1" -w '%{size_download}\n'
