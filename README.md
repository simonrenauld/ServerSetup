# Cloud Server Setup Guide

## 1. Infrastructure Summary

[View Infrastructure Diagram](01_Infrastructure_hardware/infrastructure_diagram.html)

### 1.1 Operating Systems

- Linux (Ubuntu, CentOS, Rocky Linux)
- Windows Server

### 1.2 Software and Services

- Web Servers: Nginx, Apache
- Databases: MySQL, PostgreSQL, MongoDB
- Containers: Docker, Kubernetes

### 1.3 Data Science and Engineering Tools

- Data Science: Jupyter Notebook, RStudio, Anaconda
- Data Engineering: Apache Hadoop, Apache Spark, Kafka

### 1.4 AI/ML Frameworks

- TensorFlow, PyTorch, Hugging Face (LLaMA)
- Continuous Learning Pipeline
- Document Generation: Automated proposal and roadmap creation tools

### 1.5 Monitoring and Management Tools

- Monitoring: Prometheus, Grafana, Zabbix
- Configuration Management: Ansible, Terraform
- Backup: Rsync, Bacula, Veeam

### 1.6 Data Governance

- Data Governance Framework
- Data Cataloging: Apache Atlas, Collibra
- Data Quality Management: Talend, Informatica, Great Expectations
- Data Security and Compliance: Encryption, Apache Ranger, AWS IAM
- Data Lineage: Apache Atlas, Alation
- Master Data Management (MDM): Informatica MDM, TIBCO
- Data Governance Platform: Collibra, Informatica
- Monitoring and Reporting: Grafana, Tableau

### 1.7 Media Server

- Jellyfin: For storing and streaming movies
- FFmpeg, HandBrake (optional)
- Wi-Fi configuration for projector connectivity

### 1.8 Backup System for Phone Photos and Videos

- Nextcloud: For file storage and syncing from mobile devices
- ZFS/Btrfs: For storage management
- NAS (optional): For additional storage capacity

### 1.9 AI-Powered Messaging and Calendar Management

- LLaMA AI Model: For natural language processing
- Custom Chatbot: Integrated with the LLaMA model
- Google Calendar API/Nextcloud Calendar: For calendar management
- Nextcloud Tasks: For task management
- GPU (optional): For AI processing acceleration

### 1.10 AI for Business and Technical Management

- Data Lakes and Warehousing: For storing and analyzing client data
- Document Generation: Automated proposals and roadmaps
- CRM Integration: Track client interactions and projects
- Project Management Integration: AI-powered task and project tracking
- AI Dashboard: Centralized control and monitoring interface
- Enhanced Compute Power: Additional CPUs, RAM, and GPUs

## 2. Server Setup

### 2.1 Why Create Server from Rescue

- Cost-effective and flexible
- Activated, currently booted in the Rescue System

### 2.2 Getting Started

- **Outgoing Traffic:** Ports 25 and 465 are blocked by default; unblocking available upon request
- **Downloads:** Tools, packages, and OS images available at [Hetzner Downloads](https://download.hetzner.com)
- **Quick Start Guide:** Available at [Hetzner Docs](https://docs.hetzner.com)

### 2.3 Accessing the Server

Proxmox 



1. Open a terminal on your local machine
2. SSH into your server:
   ssh root@136.243.155.166
   ssh simonadmin@136.243.155.166
   ```
   Replace the IP address with your server's actual address

3. Accept the server's fingerprint when prompted

### 2.4 Initial Server Configuration

1. Create SSH directory and set permissions:
   ```bash
   sudo mkdir -p /root/.ssh
   sudo chmod 700 /root/.ssh
   ```

2. Add your public key:

   ```bash
   echo "your-public-key" | sudo tee -a /root/.ssh/authorized_keys
   sudo chmod 600 /root/.ssh/authorized_keys
   ```

3. Configure SSH:
   ```bash
   sudo nano /etc/ssh/sshd_config
   ```
   Add or modify these lines:  
   ```
   PermitRootLogin yes
   PasswordAuthentication yes
   PubkeyAuthentication yes
   ```

4. Set root password:
   ```bash
   sudo passwd root
   ```

5. Restart SSH service:
   ```bash
   sudo systemctl restart sshd
   ```

### 2.5 Server Information

Check server configurations:
```bash
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
```

### 2.6 SSH Host Keys

1. Backup existing host keys:
   ```bash
   sudo mkdir -p /etc/ssh/backup
   sudo cp /etc/ssh/ssh_host_* /etc/ssh/backup/
   ```

2. Generate new host keys:
   ```bash
   sudo ssh-keygen -t rsa -b 3072 -f /etc/ssh/ssh_host_rsa_key -N ""
   sudo ssh-keygen -t ecdsa -b 256 -f /etc/ssh/ssh_host_ecdsa_key -N ""
   sudo ssh-keygen -t ed25519 -f /etc/ssh/ssh_host_ed25519_key -N ""
   ```

3. If you receive a host key change warning, remove the old key:
   ```bash
   ssh-keygen -f "/home/user/.ssh/known_hosts" -R "server_ip"
   ```

## 3. Operating System Installation

### 3.1 Choose and Install an Operating System

1. List available boot images in the `bootimages/` directory
2. Select an OS from the Hetzner mirror
3. Install the OS using the rescue system or direct installation method

### 3.2 Post-Installation Configuration

1. Update and upgrade the system:
   ```bash
   # For Debian/Ubuntu
   sudo apt update && sudo apt upgrade -y

   # For CentOS/RockyLinux
   sudo yum update -y
   ```

2. Install essential packages:
   ```bash
   sudo apt install htop curl vim
   ```

### 3.3 Security Setup

1. Set up a firewall (e.g., ufw for Ubuntu/Debian):
   ```bash
   sudo ufw allow OpenSSH
   sudo ufw enable
   ```
Create a non-root user:
adduser admin
usermod -aG sudo admin 

2. Installing raid system

Difference Between Unraid and RAID:
Unraid: Unraid is a flexible operating system designed for NAS (Network Attached Storage) servers. It allows you to mix and match drives of different sizes and uses a parity drive for redundancy. It's designed for home users or small businesses who need a simple, flexible storage solution.

RAID: RAID is a technology that uses multiple hard drives to increase redundancy and performance. There are different RAID levels (RAID 0, RAID 1, RAID 5, RAID 6, etc.), each offering a different balance of redundancy, performance, and storage capacity. RAID is often used in enterprise environments for critical data protection and high availability.

https://download.hetzner.com/
Username:	hetzner
Password:	download

https://docs.hetzner.com/robot/dedicated-server/raid/3ware-raid-controller

1. https://docs.hetzner.com/robot/dedicated-server/raid/linux-software-raid






2. Configure SSH key authentication for more secure access

### 3.4 Additional Software Installation

Install necessary software based on your use case (e.g., web server, database)

## 4. Documentation and Logging

Set up logging to monitor system performance and issues