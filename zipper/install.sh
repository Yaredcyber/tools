#!/bin/bash


echo "Requirement installation"
sudo apt update
sudo apt install -y python3-pip
pip3 install pyzipper
pip install platform
pip install zipfile

cd tools
mv zipper ../
cd ..
rm -rf tools
echo "Installation complete"

