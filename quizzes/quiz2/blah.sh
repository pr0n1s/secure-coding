#!/usr/bin/env bash

curl -g "http://localhost:5000/profile{{config.items()}}" > blah.html

x-www-browser blah.html
