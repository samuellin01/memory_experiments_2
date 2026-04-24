import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote("grep 'rId8\\|rId9\\|rId10\\|rId11' attached_file_extr"), shell=True, check=True)
import time; time.sleep(0.05)
import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('acted/word/_rels/document.xml.rels\n'), shell=True, check=True)
import time; time.sleep(0.05)