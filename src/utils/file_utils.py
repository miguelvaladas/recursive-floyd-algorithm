from datetime import datetime


def write_to_file(file, message):
    print(f"[{datetime.now()}] - {message}", file=file)
