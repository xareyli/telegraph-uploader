import os


def save_token_to_file(token):
    appdata_path = os.getenv('APPDATA') + '\\telegraph-uploader'

    if not os.path.exists(appdata_path):
        os.makedirs(appdata_path)

    with open(appdata_path + '\\app.dat', 'w') as f:
        f.write(token)


def export_token_from_file():
    appdata_path = os.getenv('APPDATA') + '\\telegraph-uploader\\app.dat'

    if not os.path.exists(appdata_path):
        return False

    with open(appdata_path, 'r') as f:
        return f.read()
