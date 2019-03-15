import os

LOG_FILE = 'log'


def add_log(message):
    if len(message) == 0:
        return "No message"
    with open(LOG_FILE, 'a') as log_file:
        log_file.write(message + '\n')
        return "Message added"


def read_log():
    lines = []
    try:
        with open(LOG_FILE, 'r') as log_file:
            for line in log_file:
                lines.append(line)
            return lines
    except FileNotFoundError:
        return lines


def clean_log():
    try:
        os.remove(LOG_FILE)
        return "Logs cleaned"
    except FileNotFoundError:
        return "Logs already empty"
