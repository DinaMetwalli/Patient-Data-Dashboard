const { app, BrowserWindow } = require('electron');
const node_path = require('node:path');
const path = require('path');

function createWindow() {
    const win = new BrowserWindow({
        width: 1200,
        height: 900,
        webPreferences: {
            nodeIntegration: true,
            preload: node_path.join(__dirname, 'preload.js'),
            webSecurity: false
        }
    });

    win.setMenuBarVisibility(false);

    win.loadFile(path.join(__dirname, 'index.html'));

    win.on('closed', function() {
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