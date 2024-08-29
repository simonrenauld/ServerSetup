import os
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
    # import os
    
    def install_dependencies():
        """Install all necessary dependencies."""
        # Install Graphviz software
        print("Installing Graphviz software...")
        run_command("choco install graphviz -y")  # Using Chocolatey for Windows
    
        # Install Python packages from requirements.txt
        print("Installing Python packages from requirements.txt...")
        requirements_file = "C:/Users/renau/OneDrive/00.gtihost/ServerSetup/01_Infrastructure_hardware/requirements.txt"
        if os.path.isfile(requirements_file):
            run_command(f"pip install -r {requirements_file}")
        else:
            print("ERROR: requirements.txt file not found.")
    
    if __name__ == "__main__":
        install_dependencies()

if __name__ == "__main__":
    install_dependencies()