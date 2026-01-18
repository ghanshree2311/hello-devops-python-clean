from flask import Flask
import os
import time
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def hello():
    return f"""
    <h1>Hello DevOps! 🚀</h1>
    <p>Version: 2.0 Enhanced</p>
    <p>Server Time: {datetime.now()}</p>
    <p>Environment: {os.environ.get('ENV', 'development')}</p>
    <p>Pod Name: {os.environ.get('POD_NAME', 'local')}</p>
    <hr>
    <p><strong>Deployed by: Ghanshree Mahure</strong></p>
    """

@app.route('/health')
def health():
    return {"status": "healthy", "timestamp": time.time()}

@app.route('/version')
def version():
    return {"app_version": "2.0", "deployed": "Jan 2026"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)

