import subprocess


def open_app(name):

    try:

        subprocess.Popen(["open", "-a", name])

        print(f"Abriendo {name}")

    except Exception as e:

        print("Error al abrir app:", e)