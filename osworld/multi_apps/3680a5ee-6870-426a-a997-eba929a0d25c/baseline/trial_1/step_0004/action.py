import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('cat file1.csv && echo "---" && cat file2.csv\n'), shell=True, check=True)
import time; time.sleep(0.05)