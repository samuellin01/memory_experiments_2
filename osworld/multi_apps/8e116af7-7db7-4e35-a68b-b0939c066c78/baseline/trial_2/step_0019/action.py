import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('sudo apt-get install -y tesseract-ocr 2>/dev/null '), shell=True, check=True)
import time; time.sleep(0.05)
import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('| tail -5\n'), shell=True, check=True)
import time; time.sleep(0.05)