import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('ls ~/Desktop/*.docx ~/Documents/*.docx ~/*.docx 2>'), shell=True, check=True)
import time; time.sleep(0.05)
import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('/dev/null\n'), shell=True, check=True)
import time; time.sleep(0.05)