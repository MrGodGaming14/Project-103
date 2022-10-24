import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "D:/Coding/Python/Project 103"

class FileEventHandler(FileSystemEventHandler):

    def on_created(self, event):
        print(f"Hey, {event.src_path} has been created!")
    def on_deleted(self, event):
        print(f"Oops, someone deleted {event.src_path}!")
    def on_modified(self, event):
        print(f"Someone has modified {event.src_path}!")
    def on_moved(self, event):
        print(f"{event.src_path} has been moved!")

#Intialize Event Handler Class
event_handler = FileEventHandler()

#Initialize Observer
obs = Observer()

#Schedule Observer
obs.schedule(event_handler,from_dir,recursive=True)

#Start Observer
obs.start()

try:
    while True:
        time.sleep(1)
        print("Running.....")
except KeyboardInterrupt:
    print("Stopped")
    obs.stop()