import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('cd ~ && find . -name "character.png" 2>/dev/null\n'), shell=True, check=True)
import time; time.sleep(0.05)