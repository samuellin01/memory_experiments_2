import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('cd ~/Downloads && unzip -o attached_file.docx -d a'), shell=True, check=True)
import time; time.sleep(0.05)
import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('ttached_file_extracted\n'), shell=True, check=True)
import time; time.sleep(0.05)