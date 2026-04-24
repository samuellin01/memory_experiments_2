# Task a74b607e-6bb5-4ea8-8a7c-5d97c7bbcd2a

**Instruction:** I have developed a new Chrome extension myself, so it needs to be installed manually. Please help me install the extension located in the Desktop directory into the Chrome browser.

**Score:** 1.0

**Wall clock:** 2m 12s

**Steps:** 15

**Cost:** $0.36

---

## Step 1

![Step 1](step_0001/screenshot.png)

**Response:**
```
I need to first check what's in the Desktop directory, then install the Chrome extension. Let me start by checking the Desktop directory contents.
```

**Actions:** `pyautogui.click(1887, 139)`

---

## Step 2

![Step 2](step_0002/screenshot.png)

**Response:**
```
Let me first check what extension files are on the Desktop by opening a terminal.
```

**Actions:** `pyautogui.click(33, 673)`

---

## Step 3

![Step 3](step_0003/screenshot.png)

**Response:**
```
Good, the terminal is open. Let me check what's in the Desktop directory.
```

**Actions:** `import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('ls ~/Desktop/\n'), shell=True, check=True)
import time; time.sleep(0.05)`

---

## Step 4

![Step 4](step_0004/screenshot.png)

**Response:**
```
I can see there's a `helloExtension` directory and a `__MACOSX` directory on the Desktop. Let me check the contents of the `helloExtension` directory to confirm it's a Chrome extension.
```

**Actions:** `import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('ls ~/Desktop/helloExtension/\n'), shell=True, check=True)
import time; time.sleep(0.05)`

---

## Step 5

![Step 5](step_0005/screenshot.png)

**Response:**
```
I can see the `helloExtension` directory contains a Chrome extension with `manifest.json`, `hello.html`, `hello_extensions.png`, and `popup.js`. Now I need to load this as an unpacked extension in Chrome. Let me navigate to the Chrome extensions page.
```

**Actions:** `pyautogui.click(169, 46)`

---

## Step 6

![Step 6](step_0006/screenshot.png)

**Response:**
```
Now I'll navigate to the Chrome extensions page. Let me type the URL in the address bar.
```

**Actions:** `import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('chrome://extensions/\n'), shell=True, check=True)
import time; time.sleep(0.05)`

---

## Step 7

![Step 7](step_0007/screenshot.png)

**Response:**
```
I'm on the Chrome Extensions page. I need to enable "Developer mode" first to be able to load an unpacked extension. Let me click the Developer mode toggle.
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
I can see the Desktop directory contents with `helloExtension` and `__MACOSX` folders. I need to select the `helloExtension` folder and click "Select". Let me click on `helloExtension`.
```

**Actions:** `pyautogui.click(820, 525)`

---

## Step 11

![Step 11](step_0011/screenshot.png)

**Response:**
```
The `helloExtension` folder is selected (highlighted). Now I need to click the "Select" button to load it as an unpacked extension.
```

**Actions:** `pyautogui.click(1371, 412)`

---

## Step 12

![Step 12](step_0012/screenshot.png)

**Response:**
```
The extension has been successfully loaded! I can see the "Extension loaded" notification at the bottom of the page. The Chrome extension from the Desktop directory (`helloExtension`) has been installed into the Chrome browser. Let me scroll down to verify the extension appears in the list.
```

**Actions:** `pyautogui.scroll(-3, 960, 600)`

---

## Step 13

![Step 13](step_0013/screenshot.png)

**Response:**
```
It seems the extension might not be visible in the current view. The "Extension loaded" message appeared earlier, which confirms it was loaded. Let me scroll back up to check if the extension appears at the top of the page, or refresh the page.
```

**Actions:** `pyautogui.scroll(3, 960, 600)`

---

## Step 14

![Step 14](step_0014/screenshot.png)

**Response:**
```
The extension was loaded (we saw the "Extension loaded" notification), but it doesn't seem to be showing in the list. Let me refresh the page to see if it appears.
```

**Actions:** `pyautogui.keyDown('f5')
pyautogui.keyUp('f5')`

---

## Step 15

![Step 15](step_0015/screenshot.png)

**Response:**
```
The Chrome extension has been successfully installed! I can see "Hello Extensions 1.0" (described as "Base Level Extension") is now showing in the Chrome extensions page. It's enabled (the toggle is blue/on) and has options to view "Details" or "Remove" it.

DONE
```

**Actions:** `DONE`

---
