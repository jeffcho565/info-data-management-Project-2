from flask import Flask, request, jsonify
from flask_cors import CORS
import getpass
import paramiko

app = Flask(__name__)
CORS(app)  # Allow requests from React (localhost:3000)

# SSH & script config
REMOTE_SCRIPT = "/common/home/jc2848/Downloads/ilab_script.py"
ILAB_HOST = "ilab.cs.rutgers.edu"
USERNAME = "jc2848"
PASSWORD = ""  # Will be prompted once on first use

def run_remote_query(sql_query):
    global PASSWORD
    if not PASSWORD:
        PASSWORD = getpass.getpass(f"Enter password for {USERNAME}@{ILAB_HOST}: ")

    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ILAB_HOST, username=USERNAME, password=PASSWORD)
        print("[✔] Connected to iLab")

        # Escape quotes and prepare command
        escaped_query = sql_query.replace('"', '\\"')
        cmd = f'python3.10 {REMOTE_SCRIPT} "{escaped_query}"'

        print("[▶] Running command:", cmd)
        stdin, stdout, stderr = ssh.exec_command(cmd)
        stdout.channel.recv_exit_status()

        output = stdout.read().decode()
        errors = stderr.read().decode()

        ssh.close()
        print("[✔] SSH session closed")

        if output.strip():
            return output
        elif errors.strip():
            return f"[stderr] {errors}"
        else:
            return "[!] No output received."

    except Exception as e:
        print("[SSH ERROR]", e)
        return str(e)

@app.route("/query", methods=["POST"])
def query():
    print("\n=== [POST /query] Received ===")

    try:
        data = request.get_json()
        print("[DEBUG] Request data:", data)

        user_input = data.get("query", "").strip()
        if not user_input:
            print("[ERROR] No query provided.")
            return jsonify({"error": "Missing query"}), 400

        print("[DEBUG] Executing SQL:", user_input)
        result = run_remote_query(user_input)
        print("[DEBUG] Output:\n", result)

        return jsonify({
            "input": user_input,
            "sql": user_input,
            "result": [{"output": line} for line in result.splitlines()]
        })

    except Exception as e:
        print("[EXCEPTION]", str(e))
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(port=5000)
