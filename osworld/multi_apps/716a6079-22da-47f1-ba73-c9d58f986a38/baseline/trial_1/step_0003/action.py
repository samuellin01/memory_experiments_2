import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('echo -n "/home/user/Data3/List3/secret.docx" | xcl'), shell=True, check=True)
import time; time.sleep(0.05)
import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('ip -selection clipboard\n'), shell=True, check=True)
import time; time.sleep(0.05)