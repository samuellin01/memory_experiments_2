import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('python3 -c "import docx; print(\'available\')" 2>&1\n'), shell=True, check=True)
import time; time.sleep(0.05)