import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('ls -la /home/user/paper01.pdf /home/user/ans.docx\n'), shell=True, check=True)
import time; time.sleep(0.05)