"""
Background Tasks Example

Description:
Shows how to run tasks in the background using FastAPI's BackgroundTasks.
"""

from fastapi import FastAPI, BackgroundTasks

app = FastAPI(title="Background Tasks Example")

def send_email(to: str, subject: str):
    print(f"Sending email to {to}: {subject}")

@app.post("/notify")
def notify(email: str, tasks: BackgroundTasks):
    tasks.add_task(send_email, email, "Thanks for signing up")
    return {"queued": True}
