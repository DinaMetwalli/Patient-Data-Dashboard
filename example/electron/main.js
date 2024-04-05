const { app, BrowserWindow, ipcMain } = require('electron');
const path = require('path');

function createWindow() {
    const mainWindow = new BrowserWindow({
        width: 800,
        height: 600,
        webPreferences: {
            nodeIntegration: true
        }
    });

    // removes the default electron top menu bar:
    mainWindow.setMenuBarVisibility(false);

    mainWindow.loadFile(path.join(__dirname, 'index.html'));

    mainWindow.on('closed', function () {
        app.quit();
    });

    // Define IPC handler for endpoint
    ipcMain.handle('calculate-data', async (event, { num1, num2 }) => {
        // Handle the calculation and return the result
        const result = num1 + num2;
        return { result };
    });
}

app.on('ready', createWindow);

app.on('window-all-closed', function () {
    if (process.platform !== 'darwin') {
        app.quit();
    }
});

// when you create the desktop run.bat application thing that opens the dashboard, you also have to make sure
// that on first time you open it, it runs the flask server and then waits for flask to start and then opens,
// then you have 1 of two options. 1: when you close it it also closes the flask server. 2: when you close it
// and go to open it again, it checks if the flask server is already running or not, and if it is, it doesn't
// start it, but instead instantly starts the electron app. 