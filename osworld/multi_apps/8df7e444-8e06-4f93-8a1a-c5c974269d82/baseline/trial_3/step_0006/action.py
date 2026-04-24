import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('unzip -l /home/user/essay_submission.zip\n'), shell=True, check=True)
import time; time.sleep(0.05)