import subprocess

def open_file(path):

    try:

        subprocess.Popen(["open", path])

        print(f"Abriendo: {path}")

    except Exception as e:

        print("Error:", e)