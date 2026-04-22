import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('cp /home/user/Desktop/pic.png /home/user/Desktop/p'), shell=True, check=True)
import time; time.sleep(0.05)
import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('ic.jpg\necho "Done"\n'), shell=True, check=True)
import time; time.sleep(0.05)