#!/bin/bash

# Deployment script to commit changes and push to GitHub

# Check for changes
if [[ `git status --porcelain` ]]; then
  # Add changes to git
  git add .

  # Commit changes
  git commit -m "Deployment commit on 2026-02-08 12:58:36"

  # Push to GitHub
  git push origin main
else
  echo "No changes to commit"
fi
