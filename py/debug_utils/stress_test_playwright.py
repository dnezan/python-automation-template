
import subprocess

# Define the Python file to run
file_to_run = "..\1_main.py"

# Initialize a variable to count exceptions
exception_count = 0

# Number of times to run the file
total_runs = 100

for _ in range(total_runs):
    try:
        # Run the Python file using subprocess
        subprocess.run(["python", file_to_run], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except subprocess.CalledProcessError as e:
        # Handle exceptions here (if needed)
        print(f"Exception occurred: {e}")
        exception_count += 1

# Print the total number of exceptions
print(f"Total exceptions: {exception_count}")
