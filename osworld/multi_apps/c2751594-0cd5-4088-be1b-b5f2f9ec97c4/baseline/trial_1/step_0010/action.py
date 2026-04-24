import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('cat docx_extracted/word/_rels/document.xml.rels | '), shell=True, check=True)
import time; time.sleep(0.05)
import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote("tr ' ' '\\n' | grep -A2 'rId8'\n"), shell=True, check=True)
import time; time.sleep(0.05)