import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('cp attached_file_extracted/word/media/image1.png ~'), shell=True, check=True)
import time; time.sleep(0.05)
import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('/Pictures/wallpaper.png\n'), shell=True, check=True)
import time; time.sleep(0.05)