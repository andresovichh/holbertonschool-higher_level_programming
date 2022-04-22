#!/bin/bash
# -s silent -I head
curl -sI "$1" -w '%{size_download}\n'