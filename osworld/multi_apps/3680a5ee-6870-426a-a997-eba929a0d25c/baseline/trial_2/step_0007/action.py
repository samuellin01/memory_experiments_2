import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('head -3 /tmp/file1.csv && echo "---" && head -3 /t'), shell=True, check=True)
import time; time.sleep(0.05)
import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('mp/file2.csv\n'), shell=True, check=True)
import time; time.sleep(0.05)