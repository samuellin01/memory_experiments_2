import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('which tesseract || sudo apt-get install -y tessera'), shell=True, check=True)
import time; time.sleep(0.05)
import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('ct-ocr 2>/dev/null\n'), shell=True, check=True)
import time; time.sleep(0.05)