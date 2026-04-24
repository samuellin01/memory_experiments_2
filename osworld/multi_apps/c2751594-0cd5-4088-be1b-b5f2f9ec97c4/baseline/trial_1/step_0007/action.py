import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('cd ~/Downloads && unzip -o attached_file.docx "wor'), shell=True, check=True)
import time; time.sleep(0.05)
import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('d/media/*" -d docx_extracted\n'), shell=True, check=True)
import time; time.sleep(0.05)