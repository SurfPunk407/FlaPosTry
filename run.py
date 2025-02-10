import sys
import os

# Use os.path.dirname to get the directory containing the current file.
project_root = os.path.dirname(os.path.abspath(__file__))

# Insert the project root at the BEGINNING of sys.path.
sys.path.insert(0, project_root)

print(sys.path)  # Print the Python search path (CRUCIAL FOR DEBUGGING)

from app import create_app  # Correct import

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
    