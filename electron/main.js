const { app, BrowserWindow } = require('electron');
const node_path = require('node:path');
const path = require('path');
const fs = require('fs');

function createWindow() {
    const win = new BrowserWindow({
        width: 800,
        height: 600,
        webPreferences: {
            nodeIntegration: true,
            contextIsolation: false,
            preload: node_path.join(__dirname, 'preload.js'),
            webSecurity: false
        }
    });

    win.setMenuBarVisibility(false);

    const rootDir = path.resolve(__dirname, '..');
    const configFilePath = path.join(rootDir, 'config.json');

    let configContent;
    try {
        configContent = fs.readFileSync(configFilePath, 'utf8');
    } catch (err) {
        console.error('Error reading config.json:', err);
    }

    // Check if config.json file is empty or not and redirect to correct page
    if (configContent === null || configContent === undefined || configContent.trim() === '') {
        win.loadFile(path.join(__dirname, 'setup.html'));
    } else {
        win.loadFile(path.join(__dirname, 'login.html'));
    }

    win.on('closed', function () {
        app.quit();
    });
}

app.whenReady().then(() => {
    createWindow()

    app.on('activate', () => {
        if (BrowserWindow.getAllWindows().length === 0) {
            createWindow()
        }
    })
})

app.on('window-all-closed', () => {
    if (process.platform !== 'darwin') {
        app.quit()
    }
})