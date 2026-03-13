import os


def find_app(app_name):

    app_name = app_name.lower()

    paths = [
        "/Applications",
        "/System/Applications"
    ]

    for path in paths:

        if not os.path.exists(path):
            continue

        for app in os.listdir(path):

            if app.lower().startswith(app_name) and app.endswith(".app"):
                return app.replace(".app", "")

    return None