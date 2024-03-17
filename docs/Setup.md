# Setup
Follow this guide to setup programming environment.
Make sure to complete all steps in the correct order.

## Setup Git
git config --global user.name "Your Name"
git config --global user.email "Your Email"
git config --global core.editor "vscode --wait"

## Clone Repository
git clone https://github.com/DinaMetwalli/feeding-dashboard.git
git pull

## Create Virtual Environment
py -m venv .venv
### Activate Venv:
WINDOWS: .\.venv\Scripts\activate.bat
LINUX: source .venv/bin/activate
### Install Requirements:
py -m pip install -r requirements.txt

## Install Node.js
Install Node.js for electron if you haven't already. Make sure to install the LTS version.