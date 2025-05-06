import getpass
import paramiko

# Path to the remote Python script on iLab
REMOTE_SCRIPT = "/common/home/jc2848/Downloads/ilab_script.py"
ILAB_HOST = "ilab.cs.rutgers.edu"

def run_remote_query(sql_query):
    netid = input("Enter your NetID: ")
    password = getpass.getpass("Enter your password: ")

    try:
        # Set up SSH connection
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ILAB_HOST, username=netid, password=password)
        print("[+] Connected to ILAB.")

        # Escape quotes in SQL query
        escaped_query = sql_query.replace('"', '\\"')
        cmd = f'python3.10 {REMOTE_SCRIPT} "{escaped_query}"'

        # Execute the remote script
        stdin, stdout, stderr = ssh.exec_command(cmd)

        # Wait for command to finish
        stdout.channel.recv_exit_status()

        output = stdout.read().decode()
        errors = stderr.read().decode()

        # Print output if it exists
        if output.strip():
            print("[✔] Query Result:\n")
            print(output)
        elif errors.strip():
            print("[!] Warning (possibly harmless):\n", errors)
        else:
            print("[!] No output returned.")

        ssh.close()

    except Exception as e:
        print("[!] SSH Failed:", e)

def main():
    print("Welcome to the iLab SQL query tool.\n")

    # Prompt user until a non-empty SQL query is entered
    while True:
        query = input("Enter your SQL query (e.g., SELECT * FROM loans;)\n> ").strip()
        if query:
            break
        print("[!] Query cannot be empty. Please try again.\n")

    run_remote_query(query)

if __name__ == "__main__":
    main()
