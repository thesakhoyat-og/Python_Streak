# Python Streak Reminder

Python Streak Reminder is a small Python automation project that sends a motivational notification to a phone using the [ntfy](https://ntfy.sh/) notification service.

The project also demonstrates how Python's `if __name__ == "__main__":` block works when a file is run directly versus imported into another Python file.

## Features

- Sends a notification using an HTTP POST request
- Uses the `requests` library
- Adds a notification title, tag, and priority
- Checks the HTTP response status
- Demonstrates the `__name__` variable
- Includes a second file to test module importing

## Technologies Used

- Python
- Requests
- ntfy
- Git and GitHub

## Project Structure

```text
python-streak-reminder/
├── main.py
├── testimport.py
├── requirements.txt
├── .gitignore
└── README.md
```

## How It Works

The `send_reminder()` function sends a POST request to an ntfy topic.

```python
response = requests.post(
    f"https://ntfy.sh/{TOPIC}",
    data="Don't break the streak, Sensei. Feed the Python flame.".encode("utf-8"),
    headers={
        "Title": "Python Streak",
        "Tags": "fire",
        "Priority": "high",
    },
)
```

When `main.py` is executed directly, Python sets:

```python
__name__ == "__main__"
```

Therefore, the code inside this block runs:

```python
if __name__ == "__main__":
    result = send_reminder()
```

When `main.py` is imported inside `testimport.py`, its `__name__` becomes `"main"`. The reminder block does not run automatically.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/python-streak-reminder.git
cd python-streak-reminder
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

Activate it on macOS or Linux:

```bash
source .venv/bin/activate
```

### 3. Install the dependency

```bash
pip install -r requirements.txt
```

Your `requirements.txt` file should contain:

```text
requests
```

## Setup

Choose a difficult-to-guess ntfy topic and place it in `main.py`:

```python
TOPIC = "your-private-random-topic"
```

Install the ntfy mobile app, subscribe to the same topic, and then run:

```bash
python main.py
```

A successful request should print:

```text
Reminder sent to your phone
```

## Testing `__name__`

Run the main file:

```bash
python main.py
```

Expected final value:

```text
__main__
```

Run the import test:

```bash
python testimport.py
```

Expected value:

```text
main
```

This shows that imported Python files receive their module name instead of `"__main__"`.

## Security Note

An ntfy topic is not a real password. Anyone who knows the topic name may be able to publish notifications to it, so avoid simple or public topic names.


## Future Improvements

- Store the topic in a `.env` file
- Schedule the reminder automatically
- Add timeout and exception handling
- Allow custom notification messages
- Log successful and failed requests
- Package the project as a command-line application

## Author

Md Sakhoyat Hossain Siam

## Licence

This project was created for educational and portfolio purposes.
