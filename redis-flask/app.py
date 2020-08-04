# compose_flask/app.py
import redis
from rq import Queue
from flask import Flask, request, jsonify
from task import task_in_background

app = Flask(__name__)

r = redis.Redis(host='redis', port=6379)
que = Queue(connection=r)

@app.route('/')
def index():
    return 'Index'

@app.route("/task")  
def add_task():  
    if request.args.get("t"):  
        job = que.enqueue(task_in_background, request.args.get("t"))  
        q_len = len(que)  
                              
        return f"""The task {job.id} is added into the task queue at {job.enqueued_at}. 
            {q_len} task in the queue"""



if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
