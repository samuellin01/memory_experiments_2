import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('rm /home/user/Desktop/pic.png\necho "Cleanup done"\n'), shell=True, check=True)
import time; time.sleep(0.05)