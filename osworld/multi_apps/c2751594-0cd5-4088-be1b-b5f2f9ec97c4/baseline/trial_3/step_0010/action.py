import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('grep -o \'r:embed="[^"]*"\' attached_file_extracted/'), shell=True, check=True)
import time; time.sleep(0.05)
import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('word/document.xml | head -5\n'), shell=True, check=True)
import time; time.sleep(0.05)