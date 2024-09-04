# Cloud Server Setup


 Infrastructure Summary with AI Business Functionality
Operating Systems

Linux (Ubuntu, CentOS, Rocky Linux)
Windows Server
Software and Services

Web Servers: Nginx, Apache
Databases: MySQL, PostgreSQL, MongoDB
Containers: Docker, Kubernetes
Data Science and Engineering Tools

Data Science: Jupyter Notebook, RStudio, Anaconda
Data Engineering: Apache Hadoop, Apache Spark, Kafka
AI/ML Frameworks

TensorFlow, PyTorch, Hugging Face (LLaMA)
Continuous Learning Pipeline: For ongoing model training
Document Generation: Automated proposal and roadmap creation tools
Monitoring and Management Tools

Monitoring: Prometheus, Grafana, Zabbix
Configuration Management: Ansible, Terraform
Backup: Rsync, Bacula, Veeam

Data Governance

Data Governance Framework: Policies, Procedures, Data Stewardship
Data Cataloging: Apache Atlas, Collibra
Data Quality Management: Talend, Informatica, Great Expectations
Data Security and Compliance: Encryption, Apache Ranger, AWS IAM
Data Lineage: Apache Atlas, Alation
Master Data Management (MDM): Informatica MDM, TIBCO
Data Governance Platform: Collibra, Informatica
Monitoring and Reporting: Grafana, Tableau
Documentation and Training
Media Server

Jellyfin: For storing and streaming movies
FFmpeg, HandBrake (optional)
Wi-Fi configuration for projector connectivity
Backup System for Phone Photos and Videos

Nextcloud: For file storage and syncing from mobile devices
ZFS/Btrfs: For storage management
NAS (optional): For additional storage capacity
AI-Powered Messaging and Calendar Management

LLaMA AI Model: For natural language processing
Custom Chatbot: Integrated with the LLaMA model
Google Calendar API/Nextcloud Calendar: For calendar management
Nextcloud Tasks: For task management
GPU (optional): For AI processing acceleration
AI for Business and Technical Management

Data Lakes and Warehousing: For storing and analyzing client data
Document Generation: Automated proposals and roadmaps
CRM Integration: Track client interactions and projects
Project Management Integration: AI-powered task and project tracking
AI Dashboard: Centralized control and monitoring interface
Enhanced Compute Power: Additional CPUs, RAM, and GPUs





01_Infrastructure and Hardware Setup
02_

### Why Creating Server from Rescue

- Cost cheap and flexibility
- Activated, currently booted in the Rescue System
 
python install_dependencies.py
01_Infrastructure_hardware\requirements.txt


### Getting strated 

- **Outgoing Traffic Blocked:** Ports 25 and 465 are blocked by default; you can request unblocking for a valid use case.
- **Downloads:** Tools, packages, and OS images are available at [Hetzner Downloads](https://download.hetzner.com) (Username: hetzner, Password: download).
- **Quick Start Guide:** Available at [Hetzner Docs](https://docs.hetzner.com).




## 1. Accessing the Server


### SH into Your Server:

1. **Open a Terminal:**
   On your local machine, open a terminal or command prompt.


   

2. **Use the SSH Command:**

https://ipv6-test.com/ Hetzner comes with IPV6 support, you will probably want to go to add IPV4 support


   Enter the following command, replacing `2a01:4f8:171:1e1c::2` with your actual server's IP address or hostname:

The first time you connect to a server, a message prompts you to examine the "fingerprint" of the server and to confirm it. The fingerprint is a condensed version of the server's public key.

The authenticity of host 'example.com (10.0.0.1)' can't be established.
RSA key fingerprint is SHA256:DlxqI4BctJqAgyCfyExywbm9a7qdL7nqfMKgoQuGp5w..
Are you sure you want to continue connecting (yes/no)?

Depending on which key you use for the connection, the output will look different. In addition to RSA, the key types DSA, ECDSA and ED25519 are all common ones. But you should no longer use DSA; by default, it is no longer the default option as of OpenSSH 7.

sudo mkdir -p /root/.ssh
sudo chmod 700 /root/.ssh

Add Your Public Key: If you have a public key, add it to the authorized_keys file. Replace your-public-key with your actual public key content.
echo "your-public-key" | sudo tee -a /root/.ssh/authorized_keys
sudo chmod 600 /root/.ssh/authorized_keys


sudo nano /etc/ssh/sshd_config

PermitRootLogin yes
PasswordAuthentication yes
PubkeyAuthentication yes

Set Root Password: Ensure that the root password is correctly set.

Restart SSH Service: Apply the changes by restarting the SSH service.

2. You should now be able to Yes, you are successfully connected to your server. 
ssh root@136.243.155.166


Lets see our server configurations

# Operating System and Kernel Version
uname -a
lsb_release -a

# CPU Information
lscpu

# Memory Information
free -h

# Disk Usage
df -h

# Mounted Filesystems
mount | column -t

# Network Configuration
ip a

# Active Network Connections
netstat -tuln

# Running Processes
ps aux


#  Set new password
(you Generate a Strong Password: Use a password generator to create a strong password. You can use tools like pwgen, openssl, or online password generators.
Example using openssl:) openssl rand -base64 16


# Htop Configuration
htop

OR
sudo passwd root

Steps to Generate New SSH Host Keys
Backup Existing Host Keys: Backup the existing host keys before generating new ones.


Backup Existing Host Keys: Backup the existing host keys before generating new ones.

sudo mkdir -p /etc/ssh/backup
sudo cp /etc/ssh/ssh_host_* /etc/ssh/backup/

Generate New Host Keys: Generate new SSH host keys for RSA, ECDSA, and ED25519.

sudo ssh-keygen -t rsa -b 3072 -f /etc/ssh/ssh_host_rsa_key -N ""
sudo ssh-keygen -t ecdsa -b 256 -f /etc/ssh/ssh_host_ecdsa_key -N ""
sudo ssh-keygen -t ed25519 -f /etc/ssh/ssh_host_ed25519_key -N ""


@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@    WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!     @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
IT IS POSSIBLE THAT SOMEONE IS DOING SOMETHING NASTY!

Steps to Resolve the Host Key Change Warning
Remove the Old Host Key: Use the ssh-keygen command to remove the old host key from your known_hosts file.

 ssh-keygen -f "/home/simon/.ssh/known_hosts" -R "136.243.1111.1"
 Connect to the Server Again:
ssh root@136.243.....


How do I create a new SSH host key?
A ll host keys are automatically regenerated with an automatic installation via Robot or via the Installimage Script in the Rescue System. To replace a key in an installed system, use ssh-keygen. You can find a list of all available Keys (ssh_host*) under /etc/ssh/

ls -l /etc/ssh


Renew the ED25519 key using ssh-keygen -t ed25519 -f /etc/ssh/ssh_host_ed25519_key -N "".
Renew the RSA key using ssh-keygen -t rsa -b 3072 -f /etc/ssh/ssh_host_rsa_key -N "".
Renew the ECDSA key using ssh-keygen -t ecdsa -b 256 -f /etc/ssh/ssh_host_ecdsa_key -N "".



3.** Partition alignments



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
    
   * ![image](https://github.com/user-attachments/assets/a89d9cb1-9541-4645-91c5-6f39ecc98782)
  
   * ![image](https://github.com/user-attachments/assets/7917d65d-0181-4158-b057-a55818a36115)


![image](https://github.com/user-attachments/assets/0024177d-576b-464b-9a4d-ca9773cae42b)


