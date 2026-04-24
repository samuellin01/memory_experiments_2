import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('rm ~/Desktop/section1.png ~/Desktop/section2.png ~'), shell=True, check=True)
import time; time.sleep(0.05)
import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('/Desktop/section3.png\n'), shell=True, check=True)
import time; time.sleep(0.05)