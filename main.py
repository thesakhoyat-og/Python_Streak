import requests

# secret channel.
# unguessable — this name is basically password.
TOPIC = "py-streak-sensei-9f3kx72q"

def send_reminder():
    response = requests.post(
        f"https://ntfy.sh/{TOPIC}",
        data="Don't break the streak, Sensei. Feed the Python flame.".encode("utf-8"),
        headers={
            "Title": "Python Streak",
            "Tags": "fire",
            "Priority": "high",
        },
    )
    return response

if __name__ == "__main__":
    result = send_reminder()
    if result.status_code == 200:
        print("Reminder sent to your phone")
    else:
        print(f"Something went wrong: {result.status_code}")
        
    
    

print(__name__)