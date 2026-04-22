import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('python3 -c "import PyPDF2; print(\'PyPDF2 available'), shell=True, check=True)
import time; time.sleep(0.05)
import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('\')" 2>/dev/null || echo "no PyPDF2"\n'), shell=True, check=True)
import time; time.sleep(0.05)