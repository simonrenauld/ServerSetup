# Cloud Server Setup

### Why Creating Server from Rescue

- Cost cheap and flexibility
- Activated, currently booted in the Rescue System

### Notes

- **Outgoing Traffic Blocked:** Ports 25 and 465 are blocked by default; you can request unblocking for a valid use case.
- **Downloads:** Tools, packages, and OS images are available at [Hetzner Downloads](https://download.hetzner.com) (Username: hetzner, Password: download).
- **Quick Start Guide:** Available at [Hetzner Docs](https://docs.hetzner.com).

## 1. Accessing the Server

### SH into Your Server:

1. **Open a Terminal:**
   On your local machine, open a terminal or command prompt.

2. **Use the SSH Command:**
   Enter the following command, replacing `2a01:4f8:171:1e1c::2` with your actual server's IP address or hostname:

   ```bash
   ssh root@2a01:4f8:171:1e1c::2

2. **Choose and Install an Operating System**
   * **List Available Boot Images:**
     * The directory `bootimages/` likely contains pre-configured images you can use to boot the server into a new operating system.
   * **Select an OS from the Hetzner Mirror:**
     * Depending on your preference, you can choose an OS from the available directories, such as `ubuntu/`, `debian/`, `centos/`, `rockylinux/`, etc.
   * **Install the OS:**
     * To install an OS, you can typically use a rescue system or direct installation method provided by Hetzner.
     * If you're in the rescue system, you might use a command like:

       ```bash
       wget https://download.hetzner.com/path/to/your/chosen/os.iso
       ```
     * Follow the installation instructions specific to that OS.

3. **Configure Your Server**
   * **Network Configuration:**
     * Ensure that your server's network settings are correctly configured, including IPv6 if necessary.
   * **Update and Upgrade the System:**
     * Once the OS is installed, log in and update your system:

       ```bash
       sudo apt update && sudo apt upgrade -y # For Debian/Ubuntu
       sudo yum update -y # For CentOS/RockyLinux
       ```
   * **Install Necessary Packages:**
     * Install essential packages for managing your server, such as `htop`, `curl`, `vim`, etc.

4. **Security Setup**
   * **Change the Root Password:**
     * For security, change the root password:

       ```bash
       passwd
       ```
   * **Set Up a Firewall:**
     * Consider setting up a firewall (e.g., `ufw` for Ubuntu/Debian):

       ```bash
       sudo ufw allow OpenSSH
       sudo ufw enable 
       ```
   * **SSH Key Authentication:**
     * Set up SSH key-based authentication for more secure access.

5. **Installing Additional Software**
   * **Web Server, Database, etc.:**
     * Depending on your use case, install software like Apache/Nginx, MySQL/PostgreSQL, etc.
   * **Download Additional Tools:**
     * Use the `tools/` directory on Hetzner's mirror to download any additional utilities you might need.

6. **Documentation and Logging**
   * **Set Up Logs:**
     * Configure logging to monitor system performance and issues.
