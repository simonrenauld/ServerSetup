import os
import subprocess

def run_command(command):
    """Run a shell command and print the output."""
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
        print(result.stdout)
        if result.stderr:
            print(result.stderr)
    except subprocess.CalledProcessError as e:
        print(f"Command '{command}' failed with exit status {e.returncode}")
        print(e.output)
        if e.stderr:
            print(e.stderr)

def install_dependencies():
    """Install all necessary dependencies."""
    # Install Graphviz software
    print("Installing Graphviz software...")
    run_command("choco install graphviz -y")  # Using Chocolatey for Windows

    # Set environment variables for Graphviz
    graphviz_bin = "C:/Program Files/Graphviz/bin"
    graphviz_include = "C:/Program Files/Graphviz/include"
    graphviz_lib = "C:/Program Files/Graphviz/lib"
    
    os.environ["PATH"] += os.pathsep + graphviz_bin
    os.environ["INCLUDE"] = graphviz_include
    os.environ["LIB"] = graphviz_lib

    # Install Python packages from requirements.txt
    print("Installing Python packages from requirements.txt...")
    requirements_file = "C:/Users/renau/OneDrive/00.gtihost/ServerSetup/01_Infrastructure_hardware/requirements.txt"
    if os.path.isfile(requirements_file):
        run_command(f"pip install -r {requirements_file}")
    else:
        print("ERROR: requirements.txt file not found.")

if __name__ == "__main__":
    install_dependencies()