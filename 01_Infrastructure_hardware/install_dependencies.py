import subprocess

def run_command(command):
    """Run a shell command and print the output."""
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    print(result.stdout)
    if result.stderr:
        print(result.stderr)

def install_dependencies():
    """Install all necessary dependencies."""
    # Install Graphviz software
    print("Installing Graphviz software...")
    run_command("choco install graphviz -y")  # Using Chocolatey for Windows

    # Install Python packages from requirements.txt
    print("Installing Python packages from requirements.txt...")
    run_command("pip install -r requirements.txt")

if __name__ == "__main__":
    install_dependencies()