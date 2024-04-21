import subprocess
import time

def call_script(script_name):
    try:
        subprocess.run(["python", script_name], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing {script_name}: {e}")
    except FileNotFoundError:
        print(f"Error: {script_name} not found.")

def main():
    # Call script1
    print("Calling script1...")
    call_script("script1.py")

    # Wait for 60 seconds
    print("Waiting for 60 seconds...")
    time.sleep(60)

    # Call script2
    print("Calling script2...")
    call_script("script2.py")

    print("Script execution completed.")

if __name__ == "__main__":
    main()
