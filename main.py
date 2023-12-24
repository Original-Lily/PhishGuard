import subprocess
import sys

def install_requirements():
    user_input = input("Do you want to install dependencies? (y/n): ").lower()
    if user_input == 'y':
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        except subprocess.CalledProcessError as e:
            print(f"Error installing requirements: {e}")
            sys.exit(1)
    else:
        print("Skipping dependency installation.")

def run_python_script(script_name):
    try:
        subprocess.check_call([sys.executable, script_name])
    except subprocess.CalledProcessError as e:
        print(f"Error running {script_name}: {e}")
        sys.exit(1)

def main():
    # Install requirements
    install_requirements()

    # Run Python scripts in order
    scripts_to_run = ["usrInput.py", "preProcess.py", "TFIDF.py", "model.py"]
    for script in scripts_to_run:
        run_python_script(script)

if __name__ == "__main__":
    main()
