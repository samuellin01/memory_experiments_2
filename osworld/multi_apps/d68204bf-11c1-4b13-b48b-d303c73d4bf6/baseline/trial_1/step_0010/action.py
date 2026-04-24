import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('convert section1.png section2.png section3.png +ap'), shell=True, check=True)
import time; time.sleep(0.05)
import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('pend ~/Desktop/rearranged.png\n'), shell=True, check=True)
import time; time.sleep(0.05)