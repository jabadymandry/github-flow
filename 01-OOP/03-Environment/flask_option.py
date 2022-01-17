# pylint: disable=missing-docstring

import os

def start():
    env = os.getenv('FLASK_ENV')
    if env == "development":
        data = "Starting in development mode..."
    else:
        data = "Starting in production mode..."
    return data

if __name__ == "__main__":
    print(start())
