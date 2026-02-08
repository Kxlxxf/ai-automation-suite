#!/bin/bash

# Update package lists
sudo apt-get update

# Install Python and Node.js dependencies
sudo apt-get install -y python3 python3-pip
sudo apt-get install -y nodejs npm

# Create necessary directories
mkdir -p ~/projects/ai-automation-suite/logs
mkdir -p ~/projects/ai-automation-suite/data

echo "Installation complete!"