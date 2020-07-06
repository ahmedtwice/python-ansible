#!/bin/bash
# Script to publish changes to GitHub

git pull
git add . 
git commit -m "$*"
git push
