# Task a74b607e-6bb5-4ea8-8a7c-5d97c7bbcd2a

**Instruction:** I have developed a new Chrome extension myself, so it needs to be installed manually. Please help me install the extension located in the Desktop directory into the Chrome browser.

**Score:** 1.0

**Wall clock:** 1m 54s

**Steps:** 13

**Cost:** $0.31

---

## Step 1

![Step 1](step_0001/screenshot.png)

**Response:**
```
I need to first check what extension files are on the Desktop, then install them in Chrome. Let me start by checking the Desktop directory.
```

**Actions:** `pyautogui.click(1888, 139)`

---

## Step 2

![Step 2](step_0002/screenshot.png)

**Response:**
```
Let me first check what's on the Desktop by opening a terminal.
```

**Actions:** `pyautogui.click(33, 673)`

---

## Step 3

![Step 3](step_0003/screenshot.png)

**Response:**
```
Good, the terminal is open. Let me check what's on the Desktop.
```

**Actions:** `import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('ls ~/Desktop/\n'), shell=True, check=True)
import time; time.sleep(0.05)`

---

## Step 4

![Step 4](step_0004/screenshot.png)

**Response:**
```
I can see there's a `helloExtension` directory and a `__MACOSX` directory on the Desktop. Let me check the contents of the extension directory to confirm it has a manifest.json file.
```

**Actions:** `import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('ls ~/Desktop/helloExtension/\n'), shell=True, check=True)
import time; time.sleep(0.05)`

---

## Step 5

![Step 5](step_0005/screenshot.png)

**Response:**
```
The extension directory contains `hello_extensions.png`, `hello.html`, `manifest.json`, and `popup.js` - this is a valid Chrome extension. Now I need to load it in Chrome as an unpacked extension. Let me navigate to `chrome://extensions` in Chrome.
```

**Actions:** `pyautogui.click(990, 88)`

---

## Step 6

![Step 6](step_0006/screenshot.png)

**Actions:** `import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('chrome://extensions\n'), shell=True, check=True)
import time; time.sleep(0.05)`

---

## Step 7

![Step 7](step_0007/screenshot.png)

**Response:**
```
I'm on the Chrome extensions page. I need to enable Developer mode first to be able to load an unpacked extension. Let me toggle the Developer mode switch.
```

**Actions:** `pyautogui.click(1884, 141)`

---

## Step 8

![Step 8](step_0008/screenshot.png)

**Response:**
```
Developer mode is now enabled and I can see the "Load unpacked" button. Let me click on it to load the extension.
```

**Actions:** `pyautogui.click(151, 196)`

---

## Step 9

![Step 9](step_0009/screenshot.png)

**Response:**
```
A file dialog has opened. I need to navigate to the Desktop directory and select the `helloExtension` folder. Let me click on "Desktop" in the left sidebar.
```

**Actions:** `pyautogui.click(637, 535)`

---

## Step 10

![Step 10](step_0010/screenshot.png)

**Response:**
```
I can see the Desktop directory contents with `helloExtension` and `__MACOSX` folders. I need to select the `helloExtension` folder and click "Select".
```

**Actions:** `pyautogui.click(820, 525)`

---

## Step 11

![Step 11](step_0011/screenshot.png)

**Response:**
```
I see the `helloExtension` folder is highlighted. Now I need to select it properly - let me click on it to select it and then click "Select" button. It seems like I need to either double-click to enter the folder or select it and click "Select". Since the dialog says "Select the extension directory", I should select the `helloExtension` folder and click "Select".
```

**Actions:** `pyautogui.click(820, 525)`

---

## Step 12

![Step 12](step_0012/screenshot.png)

**Response:**
```
The `helloExtension` folder appears to be selected (highlighted). Now I need to click the "Select" button to confirm the selection.
```

**Actions:** `pyautogui.click(1371, 412)`

---

## Step 13

![Step 13](step_0013/screenshot.png)

**Response:**
```
The extension has been successfully installed! I can see:

- **Hello Extensions 1.0** - "Base Level Extension" is now loaded and enabled in Chrome
- The status bar at the bottom shows "Extension loaded"
- The extension is enabled (toggle is blue/on)
- It has an ID: `mocnjhgdiggfoillfodlefncpjkahbp`

The Chrome extension from the Desktop directory has been successfully installed as an unpacked extension.

DONE
```

**Actions:** `DONE`

---
