# Lottery System

A fun and interactive terminal-based Lottery Registration System built using Python. Participants can register within a time limit, and a winner is selected randomly. The results are displayed in a clean table format using the `tabulate` library.

---

## Features

- Timed registration window
- Username validation (3–15 characters, alphanumeric or underscores)
- Unique registration check
- Minimum participants requirement
- Tabulated results with `tabulate`
- Log file (`lottery_log.txt`) for record-keeping
- Graceful exit on `Ctrl+C` (SIGINT)

---

## Requirements

- Python 3.x
- `tabulate` library

Install dependencies:

`
pip install tabulate
```


## How to Run
python lottery.py
```

Follow the on-screen instructions to enter unique usernames during the registration period.

---

## Username Rules

- Length: 3 to 15 characters
- Allowed: Alphanumeric characters and underscores
- Must be unique

---

## Log File

After execution, a `lottery_log.txt` file is generated with:
- Registration start time
- Usernames and their registration times
- Winner info
- Total participant count

---

## Customization

- Change registration time or minimum participants:
```python
registration_duration = 15  # seconds
min_users_required = 3
```

- Modify username rules in `is_valid_username()` function.


