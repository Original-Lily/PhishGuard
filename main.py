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

def run_usr_input_script(script_name, usr_input):
    try:
        subprocess.check_call([sys.executable, script_name, usr_input])
    except subprocess.CalledProcessError as e:
        print(f"Error running {script_name}: {e}")
        sys.exit(1)

def run_other_scripts(scripts_to_run):
    for script in scripts_to_run:
        print(script)
        try:
            subprocess.check_call([sys.executable, script])
        except subprocess.CalledProcessError as e:
            print(f"Error running {script}: {e}")
            sys.exit(1)

def main():
    # Install requirements
    install_requirements()

    # Get user input from command line
    if len(sys.argv) != 2:
        print("Usage: main.py <UserInput>")
        sys.exit(1)

    usr_input = sys.argv[1]
    print(usr_input)

    # Run usrInput.py script
    run_usr_input_script("usrInput.py", usr_input)

    # Run other Python scripts in order
    other_scripts_to_run = ["preProcess.py", "TFIDF.py", "model.py"]
    run_other_scripts(other_scripts_to_run)

if __name__ == "__main__":
    main()
