#!/bin/bash

# Download Python installer
echo "Downloading Python installer..."
curl -O https://www.python.org/ftp/python/3.11.8/python-3.11.8-macos11.pkg

# Install Python
echo "Installing Python..."
sudo installer -pkg python-3.11.8-macos11.pkg -target /

# Clean up
echo "Cleaning up..."
rm python-3.11.8-macos11.pkg

# Verify installation
echo "Verifying Python installation..."
python3 --version
pip3 --version

# Install requirements
echo "Installing project requirements..."
pip3 install -r requirements.txt

echo "Installation complete!" 