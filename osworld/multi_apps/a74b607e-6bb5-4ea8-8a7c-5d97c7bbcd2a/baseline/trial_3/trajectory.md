# Task a74b607e-6bb5-4ea8-8a7c-5d97c7bbcd2a

**Instruction:** I have developed a new Chrome extension myself, so it needs to be installed manually. Please help me install the extension located in the Desktop directory into the Chrome browser.

**Score:** 1.0

**Wall clock:** 2m 0s

**Steps:** 13

**Cost:** $0.31

---

## Step 1

![Step 1](step_0001/screenshot.png)

**Response:**
```
I need to first check what extension files are on the Desktop, then install the extension in Chrome. Let me start by checking the Desktop directory.
```

**Actions:** `pyautogui.click(1887, 139)`

---

## Step 2

![Step 2](step_0002/screenshot.png)

**Response:**
```
Let me first check what's on the Desktop directory by opening a terminal.
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
The extension directory contains `hello_extensions.png`, `hello.html`, `manifest.json`, and `popup.js` - this is a valid Chrome extension. Now I need to load it in Chrome. Let me navigate to Chrome's extensions page.
```

**Actions:** `pyautogui.click(166, 46)`

---

## Step 6

![Step 6](step_0006/screenshot.png)

**Response:**
```
Now I'll navigate to the Chrome extensions page.
```

**Actions:** `import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('chrome://extensions\n'), shell=True, check=True)
import time; time.sleep(0.05)`

---

## Step 7

![Step 7](step_0007/screenshot.png)

**Response:**
```
I'm on the Extensions page. I need to enable Developer mode first to be able to load an unpacked extension. Let me click the Developer mode toggle.
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
A file dialog has opened. I need to navigate to the Desktop folder and select the `helloExtension` directory. Let me click on "Desktop" in the left sidebar.
```

**Actions:** `pyautogui.click(637, 535)`

---

## Step 10

![Step 10](step_0010/screenshot.png)

**Response:**
```
I can see the Desktop contents with `helloExtension` and `__MACOSX` folders. I need to select the `helloExtension` folder and click "Select".
```

**Actions:** `pyautogui.click(820, 525)`

---

## Step 11

![Step 11](step_0011/screenshot.png)

**Response:**
```
I see the `helloExtension` folder is highlighted. Let me double-click on it to open it, and then click "Select" to select it as the extension directory.
```

**Actions:** `pyautogui.doubleClick(820, 525)`

---

## Step 12

![Step 12](step_0012/screenshot.png)

**Response:**
```
I'm now inside the `helloExtension` directory and can see the extension files (hello.html, hello_extensions.png, manifest.json, popup.js). This is the correct directory. Now I need to click "Select" to load this directory as an unpacked extension.
```

**Actions:** `pyautogui.click(1371, 412)`

---

## Step 13

![Step 13](step_0013/screenshot.png)

**Response:**
```
The extension has been successfully installed! I can see:

- **Hello Extensions 1.0** - "Base Level Extension" is now loaded and enabled in Chrome
- The toggle is turned on (blue)
- A confirmation message "Extension loaded" appears at the bottom of the page

The Chrome extension from the Desktop directory has been successfully installed as an unpacked extension in Chrome.

DONE
```

**Actions:** `DONE`

---
