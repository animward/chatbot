import subprocess
import time

def run_command(command):
    process = subprocess.Popen(command, shell=True)
    process.communicate()
    if process.returncode != 0:
        print(f"Error running command: {command}")
        
run_command("python scripts/clean_text.py")   
     
run_command("python scripts/chatbot.py")