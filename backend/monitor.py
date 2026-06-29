from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from datetime import datetime
import time
copy_count = 0
delete_count = 0
from events import events
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_FILE = os.path.join(BASE_DIR, "logs", "threat.log")

def save_log(threat):
    print("save log called")
    with open(LOG_FILE, "a") as file:
        print("written")
        file.write(
            f"[{threat['time']}]"
            f"[{threat['severity']}]"
            f"{threat['type']}"
            f"{threat['path']}\n"
        )

class NXTHandler(FileSystemEventHandler):
    def on_created(self, event):
        global copy_count
        if not event.is_directory:
            print(f"[INFO] file created: {event.src_path}")
           
        threat = {
            "type" : "File Created",
            "path" : event.src_path,
            "severity" : "INFO",
            "time" : datetime.now().strftime("%H:%M:%S")
        }
        print(threat)
        events.append(threat)
        save_log(threat)
        copy_count += 1

       
        if copy_count >= 20:
            threat = {
                "type" : "Large Data Copy",
                "path" : event.src_path,
                "severity" : "HIGH",
                "time" : datetime.now().strftime("%H:%M:%S")

            }
            print(threat)
            events.append(threat)
            save_log(threat)
            copy_count = 0
        if event.src_path.endswith((".exe", ".sh", ".py", ".dll", ".so")):
            threat = {
                "type" : "Suspicious File",
                "path" : event.src_path,
                "severity" : "HIGH",
                "time" : datetime.now().strftime("%H:%M:%S")
            }
            events.append(threat)
            save_log(threat)
        
    
    
    def on_deleted(self, event):
        global delete_count

        if not event.is_directory:
            print("[Medium] file deleted", event.src_path)
            threat = {
                "type" : "File Deleted",
                "path" : event.src_path,
                "severity" : "MEDIUM",
                "time" : datetime.now().strftime("%H:%M:%S")
            }
            events.append(threat)
            save_log(threat)
            if delete_count >= 20:
                threat = {
                    "type" : "Ransomware Attack",
                    "path" : event.src_path,
                    "severity" : "CRITICAL",
                    "time" : datetime.now().strftime("%H:%M:%S")
                }
                print(threat)
                events.append(threat)
                save_log(threat)
                delete_count = 0
            
    def on_modified(self, event):
        if not event.is_directory:
            print("[LOW] file modified", event.src_path)
            threat = {
                "type" : "File Modified",
                "path" : event.src_path,
                "severity" : "LOW",
                "time" : datetime.now().strftime("%H:%M:%S")
            }
            events.append(threat)
            save_log(threat)
             
    def on_moved(self, event):
        if not event.is_directory:
            threat = {
                "type" : "File Renamed",
                "path" : f"{event.src_path} -> {event.dest_path}",
                "severity" : "HIGH",
                "time" : datetime.now().strftime("%H:%M:%S")
            }
            events.append(threat)
            save_log(threat)
            print(f"[HIGH] File Renamed")
            print(f"From: {event.src_path}")
            print(f"To: {event.dest_path}")
observer = Observer()
handler = NXTHandler()

observer.schedule(handler, "/home/crimson/testfolder", recursive=True)
def start_monitor():
    observer.start()
    print("NXT Monitoring Started")



