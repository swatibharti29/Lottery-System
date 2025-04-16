import time
import threading
import random
import re
import sys
import signal
from datetime import datetime
from tabulate import tabulate

LOG_FILE = "lottery_log.txt"
registered_users = {}
lock = threading.Lock()
registration_duration = 15  # Duration in sec
min_users_required = 3
shutdown_flag = threading.Event()

def signal_handler(sig, frame):
    print("\n[!] Interrupted. Saving progress...")
    save_log()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

def is_valid_username(username):
    return re.match(r"^[A-Za-z0-9_]{3,15}$", username)

def save_log():
    with lock, open(LOG_FILE, "w") as f:
        f.write("Lottery Log\n")
        f.write(f"Start Time: {datetime.fromtimestamp(start_time)}\n")
        for user, ts in registered_users.items():
            f.write(f"{user} - Registered at {datetime.fromtimestamp(ts)}\n")
        if registered_users:
            winner = select_winner()
            f.write(f"\nWinner: {winner}\n")
            f.write(f"Total Participants: {len(registered_users)}\n")

def user_input_listener(duration):
    end_time = time.time() + duration
    print(f"\nRegistration is open for {duration} seconds...\n")
    while time.time() < end_time and not shutdown_flag.is_set():
        try:
            username = input("Enter a unique username: ").strip()
        except EOFError:
            break
        if not username:
            print("Username cannot be empty.")
        elif not is_valid_username(username):
            print("Invalid username. Use 3-15 alphanumeric/underscores.")
        elif username in registered_users:
            print("Username already registered.")
        else:
            with lock:
                registered_users[username] = time.time()
                print(f"'{username}' registered.")
    print("\n Registration time ended.")

def select_winner():
    return random.choice(list(registered_users.keys())) if registered_users else None

def display_results():
    print("\n Winner Announcement\n")
    table_data = [
        [user, datetime.fromtimestamp(ts).strftime("%Y-%m-%d %H:%M:%S")]
        for user, ts in registered_users.items()
    ]
    print(tabulate(table_data, headers=["Username", "Registration Time"], tablefmt="fancy_grid"))
    winner = select_winner()
    print(f"\n Winner: {winner}")
    print(f"Total Participants: {len(registered_users)}")
    print("\nThank you for participating!\n")

def run_lottery():
    global start_time
    start_time = time.time()
    
    user_input_listener(registration_duration)

    if len(registered_users) < min_users_required:
        print(f"\n Not enough users registered (min {min_users_required} needed). Lottery canceled.")
        save_log()
        return

    save_log()
    display_results()

if __name__ == "__main__":
    run_lottery()