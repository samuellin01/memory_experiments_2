import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('ls -la /home/user/essay_submission.zip && unzip -l'), shell=True, check=True)
import time; time.sleep(0.05)
import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote(' /home/user/essay_submission.zip\n'), shell=True, check=True)
import time; time.sleep(0.05)