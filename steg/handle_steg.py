import subprocess
import re

def get_texte(sub_proc):
    command = ["strings", sub_proc]
    lsProcess = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    output, error = lsProcess.communicate()
    return output

pattern = r"-----BEGIN PGP PUBLIC KEY BLOCK-----[\s\S]*?-----END PGP PUBLIC KEY BLOCK-----"

def reg(sub_proc):
    texte = get_texte(sub_proc)
    match = re.search(pattern, texte)

    if match:
        print(match.group())
    else:
        print("Aucune clé PGP trouvée.")
