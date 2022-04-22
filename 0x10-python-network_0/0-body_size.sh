#!/bin/bash
# -s silent -I head
curl -so "$1" -w '%{size_download}\n'
