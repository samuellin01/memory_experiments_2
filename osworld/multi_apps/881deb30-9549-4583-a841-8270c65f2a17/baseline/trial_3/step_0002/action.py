import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('cd ~/Documents/Fundings/ecs/ && pdftotext ecs15.pd'), shell=True, check=True)
import time; time.sleep(0.05)
import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('f - | head -100\n'), shell=True, check=True)
import time; time.sleep(0.05)