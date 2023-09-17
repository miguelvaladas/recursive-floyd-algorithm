from datetime import datetime


def write_to_file(file, message):
    file.write(f"[{datetime.now()}] - {message}\n")
