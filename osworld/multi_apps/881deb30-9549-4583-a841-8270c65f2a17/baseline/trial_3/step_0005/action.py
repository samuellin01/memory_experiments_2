import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('pdftotext -layout ecs15.pdf /tmp/ecs15_layout.txt '), shell=True, check=True)
import time; time.sleep(0.05)
import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('&& cat /tmp/ecs15_layout.txt\n'), shell=True, check=True)
import time; time.sleep(0.05)