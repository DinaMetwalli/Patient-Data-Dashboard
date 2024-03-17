# Setup
Follow this guide to setup programming environment.
Make sure to complete all steps in the correct order.

## Setup Git
```bash
git config --global user.name "Your Name"
git config --global user.email "Your Email"
git config --global core.editor "vscode --wait"
```

## Clone Repository
```bash
git clone https://github.com/DinaMetwalli/feeding-dashboard.git
git pull
```

## Virtual Environment
### Create venv
```bash
py -m venv .venv
```
### Activate Venv:
```bash
WINDOWS: .\.venv\Scripts\activate.bat
LINUX: source .venv/bin/activate
```
Note: if the bottom right corner of vscode does not show the interpeter as ('venv':venv) then simply close vscode and go to the directory where the project is located, then right click > open in code. Now it should work as expected!
### Install Requirements:
```bash
pip install -r requirements.txt
```

## Install Node.js
Install Node.js for electron if you haven't already. Make sure to install the LTS version.