import os


def save_token_to_file(token):
    appdata_path = os.getenv('APPDATA') + '\\telegraph-uploader'

    if not os.path.exists(appdata_path):
        os.makedirs(appdata_path)

    with open(appdata_path + '\\app.dat', 'w') as f:
        f.write(token)
