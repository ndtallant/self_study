import atexit
import time

# v2.x version - see https://stackoverflow.com/a/38501429/135978
# for the 3.x version
from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return jsonify({'success': True})

def job_function():
    print("Sleeping")
    time.sleep(3)
    print("Done")


# Shutdown your cron thread if the web process is stopped
# Explicitly kick off the background thread
cron = BackgroundScheduler()
cron.add_job(func=job_function, trigger="interval", seconds=5)
cron.start()

atexit.register(lambda: cron.shutdown(wait=False))

if __name__ == '__main__':
    app.run()
