import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('pdftotext ~/Desktop/"GLUE: A MULTI-TASK BENCHMARK '), shell=True, check=True)
import time; time.sleep(0.05)
import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('AND ANALYSIS.pdf" - 2>/dev/null | head -20\n'), shell=True, check=True)
import time; time.sleep(0.05)