import sys
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import os
import subprocess

class FileChangeHandler(FileSystemEventHandler):
    def __init__(self, script):
        self.script = script
        self.process = None
        self.start_script()

    def start_script(self):
        if self.process:
            self.process.kill()
        self.process = subprocess.Popen([sys.executable, self.script])

    def on_modified(self, event):
        if event.src_path.endswith(".py"):
            print(f"{event.src_path} has been modified, restarting script...")
            self.start_script()

if __name__ == "__main__":
    script_to_watch = "main.py"  # 这里指定你想要监视的主脚本
    event_handler = FileChangeHandler(script_to_watch)
    observer = Observer()
    observer.schedule(event_handler, path='.', recursive=True)
    observer.start()
    print(f"Watching for changes in {script_to_watch}...")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()