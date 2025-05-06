# CS440 Project 2 — SQL Query over SSH

## Team Members

- **Jeff Cho** (`jc2848`)  
- **Daniel Chung** (`dbc70`)

## Contributions

- **Jeff Cho**:
  - Created the initial PostgreSQL table (`loans`) and inserted test data.
  - Wrote and tested the remote Python script (`ilab_script.py`) on iLab.
  - Handled SSH connection setup and error debugging in `database_llm.py`.
  - Verified SQL output from both local and remote executions.

- **Daniel Chung**:
  - Designed and tested SQL queries for `query_script.sql`.
  - Helped resolve pandas and psycopg2-related issues on iLab.
  - Assisted in organizing project files and writing the README.
  - Participated in troubleshooting buffer/output errors over SSH.

## What We Found Challenging

- Getting the `pandas.read_sql_query()` function to work remotely without triggering errors.
- Dealing with Python SSH buffering (`stdout.channel.recv_exit_status()`) — output wasn’t printing until that was added.
- Installing and testing packages like `tabulate` and `psycopg2-binary` on iLab without sudo access.
- Avoiding issues caused by quote escaping and string parsing in the query arguments passed over SSH.

## What We Found Interesting

- Watching a SQL query execute remotely and return a live-formatted table directly in our local terminal was cool.
- Using `paramiko` to send and run full Python scripts over SSH showed us how real-world remote automation works.
- We realized how many layers (PostgreSQL → Python → SSH → terminal) need to work seamlessly for even one query.

## Did We Do the Extra Credit?
- Yes