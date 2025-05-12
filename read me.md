# CS440 Project 2 — SQL Query Frontend (Extra Credit Submission)

Team Members
- **Jeff Cho** (`jc2848`)  
- **Daniel Chung** (`dbc70`)  

1. **Working Frontend (1 pt)**
- Built using **React** and connected to a **Flask backend**
- Users can input SQL queries (or adapted natural language inputs)
- A **submit button** triggers the backend request via fetch()
- App displays results below the input, with a responsive UI

2. **Modern, Interactive Interface with Output Table (1 pt)**
- Styled using Tailwind-compatible classes (or CSS fallback)
- Result table is formatted using clean HTML with headers and rows
- Output clearly separated into:
  - Original user input
  - Generated SQL (currently mirrors input)
  - Query result

3. **Full Result Breakdown with Separated Boxes (1 pt)**
- Input and output are displayed in separate labeled panels:
  - `"Original Input"`: the user’s typed query
  - `"Generated SQL"`: the raw SQL sent to the backend
  - `"Query Result"`: rendered as an HTML table or message
- Errors (like syntax or SSH issues) are shown cleanly as warnings

Backend Functionality
- Uses **Flask** to handle POST requests from React
- SSH connection is managed via **paramiko**
- Executes a remote script on iLab to run the SQL query
- Supports login via NetID and password (entered once per session)
- Captures both stdout and stderr for full result reporting