import subprocess


def open_file(*args):
    subprocess.call(['open', *args])


def create_video_capture():
    pass
