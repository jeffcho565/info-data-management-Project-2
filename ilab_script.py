import sys
import psycopg2
import pandas as pd

def run_query(query):
    conn = psycopg2.connect(
        host="postgres.cs.rutgers.edu",
        dbname="group8",  # Replace with your group DB if needed
        user="jc2848"
    )
    df = pd.read_sql_query(query, conn)
    conn.close()

    if df.empty:
        print("[!] Query returned no results.")
    else:
        print(df.to_markdown(index=False)) 
sys.stdout.flush()
def main():
    if len(sys.argv) > 1:
        query = sys.argv[1]
    else:
        query = sys.stdin.read().strip()

    if not query:
        print("[!] No query provided.")
        return

    run_query(query)

if __name__ == "__main__":
    main()
 