# Buidling 𝐚 𝗰𝘂𝘀𝘁𝗼𝗺 𝗰𝗹𝗼𝘂𝗱 𝐀.𝐈. 𝐃𝐚𝐭𝐚 𝗶𝗻𝗳𝗿𝗮𝘀𝘁𝗿𝘂𝗰𝘁𝘂𝗿𝗲

## 1. Buying a Server from Hetzner

[Hetzner Robot Portal](https://robot.hetzner.com/)

Simple as it is: For very little per month, you can own/rent your own dedicated server to meet any requirements and needs.

[Understanding components of a server](https://www.spiceworks.com/tech/tech-general/articles/what-is-a-server/)
[What is a server](https://www.spiceworks.com/tech/tech-general/articles/what-is-a-server/)


<a href="https://github.com/simonrenauld/ServerSetup/blob/main/01_Infrastructure_hardware/HetzerServer.jpg">
  <img src="https://github.com/simonrenauld/ServerSetup/blob/main/01_Infrastructure_hardware/HetzerServer.jpg" alt="Hetzner Server" width="400" />
</a>


### 1.1. Hetzner Rescue mode and Server Info:

```
root@rescue ~ # # run this command to get your interface name
(udevadm info -e | grep -m1 -A 20 ^P.*eth0 | grep ID_NET_NAME_PATH | cut -d'=' -f2)

root@rescue ~ # # run this command to get your main IP4 and Netmask
(ip address show "$(udevadm info -e | grep -m1 -A 20 ^P.*eth0 | grep ID_NET_NAME_PATH | cut -d'=' -f2)" | grep global | grep "inet "| xargs | cut -d" " -f2)

root@rescue ~ # (ip route | grep default | xargs | cut -d" " -f3)

root@rescue ~ # # run this command to get your MAC address
(ifconfig eth0 | grep -o -E '([[:xdigit:]]{1,2}:){5}[[:xdigit:]]{1,2}')

root@rescue ~ # # run this command to get your IPv6 CIDR
(ip address show "$(udevadm info -e | grep -m1 -A 20 ^P.*eth0 | grep ID_NET_NAME_PATH | cut -d'=' -f2)" | grep global | grep "inet6 "| xargs | cut -d" " -f2)
```
### 1.2. Server Virtualization Oveview

Many businesses start by managing data in Excel files, and as they grow, they transition to servers and cloud services with company maturity. However, the core principles often get lost along the way. While successful projects are remembered, failed projects carry valuable lessons that shouldn't be overlooked.

There's also a tendency for different departments to focus only on the most successful aspects of the company, creating a bias in how growth is perceived. This is where virtualization and tools like Proxmox come into play, enabling us to build a perfect testing lab that preserves both success and failure, allowing for deeper insights and innovation.





### 1.3. Virtualization and Proxmox VE

Even though it's stored somewhere globally, you'll need to virtualize access to your physical drives. At the core of this process is the **hypervisor**—a key software, hardware, or firmware layer that manages and creates virtual machines (VMs). 
A **bare metal hypervisor** bridges physical hardware and VMs, allowing seamless migration while maintaining functionality. VMs don't interact with hardware directly; they interface with the hypervisor, ensuring a consistent virtual environment across different hardware setups.

#### Proxmox Virtual Environment (VE)
Proxmox VE is a powerful, adaptable virtualization solution offering **enterprise-grade features** without high costs. It's ideal for managing data centers, educational institutions, or even home labs. 
Proxmox is notable for its **versatility** and **affordability**, letting you build a fully operational virtual infrastructure for free, with paid options offering extra support and updates.

#### Key Features

- **Free & Open Source**: Community edition is free; paid versions offer additional features for production environments.
- **Built-in Firewall**: Highly configurable, offering **per-VM firewall controls**, perfect for multi-tenant environments.
- **Open vSwitch Support**: Reduces network management overhead and enables **complex virtual network setups**.
- **GUI**: **User-friendly interface** for managing clusters, VMs, storage, and networking.
- **KVM Support**: Full **OS virtualization** for running multiple operating systems like Linux and Windows.
- **LXC Support**: Lightweight **Linux container-based virtualization** for efficient resource use.

#### Storage Options
Proxmox VE supports various storage types:

- Local directories
- **LVM / LVM Thin**
- **NFS**
- **iSCSI**
- **GlusterFS**
- **Ceph RADOS Block Devices (RBD)**
- **ZFS**

This wide range of storage options provides flexibility in managing data within your virtual environment.



### 1.3.1. Draw.io Server Infrastructure

The Draw.io Integration extension for Visual Studio Code brings the full functionality of Draw.io diagramming directly into your code editor. Ideal for creating flowcharts, network diagrams, or UML models, this extension lets you diagram without switching between applications. You can save diagrams as .drawio.png or .drawio.svg, preserving editable data within the image's metadata for easy sharing and future editing. With offline support, Git repository integration, and seamless Markdown embedding, this extension enhances team collaboration and workflow visualization, making it a powerful addition to any developer's toolkit.

![Proxmox Architecture] <img src="https://github.com/simonrenauld/ServerSetup/blob/main/01_Infrastructure_hardware/screenshots/proxmox_architecture.png" alt="Hetzner Server" width="400" />






### 2. Installing Proxmox

You will find many documentation around the web. IS NOT that straight forward.I will not give more details explainations step by step. Because its constantly updating and 
there is different ways to set-up your proxmox. Do you own research and find the best approach. 

#### Resources:
https://www.amazon.com/Mastering-Proxmox-virtualized-environments-hypervisor/dp/1788397606
https://github.com/ariadata/proxmox-hetzner?tab=readme-ov-file
https://www.youtube.com/watch?v=cf3OljqAxEU&t=728s
https://www.virtualizationhowto.com/2024/03/proxmox-ebook-free-download-for-home-labs/
https://github.com/ariadata/proxmox-hetzner?tab=readme-ov-file



### 2.1. QEMU commands

QEMU is a type-2 hypervisor that uses dynamic translation to emulate CPU instructions on a foreign architecture. It’s helpful for many tasks, such as testing and development, cloud computing, and system administration. 
In conjunction with other virtualization technologies like KVM or Xen, it allows the guest to run directly on the host CPU at near-native speed.

[QEMU Documentation](https://qemu-project.gitlab.io/qemu/system/monitor.html)
[QEMU from terminal](https://www.baeldung.com/linux/qemu-from-terminal)


with VNC setup (This command is starting a QEMU virtual machine to install Proxmox from the ISO, with the ability to control it over VNC (Virtual Network Computing)
```
printf "change vnc password\n%s\n" "abcd_123456": This sets a VNC password (abcd_123456). It's printing a command that will later be passed into QEMU's monitor interface to set the VNC password.
```



#### QEMU Command Breakdown

- **qemu-system-x86_64**: This is the command to start a QEMU virtual machine for 64-bit x86 architectures.
- **-enable-kvm**: Enables hardware virtualization support (KVM), which improves performance if supported by your system.
- **-cpu host**: This tells QEMU to emulate the host's CPU type for the VM, meaning the VM will use the same type of CPU as the physical machine.
- **-smp 4**: Specifies the number of CPU cores (4) allocated to the virtual machine.
- **-m 4096**: Allocates 4096 MB (4 GB) of RAM to the virtual machine.
- **-boot d**: Tells the VM to boot from the CDROM (the Proxmox ISO in this case).
- **-cdrom ./pve.iso**: This specifies the Proxmox ISO file (`pve.iso`) as the bootable CD image.
- **-drive file=/dev/nvme0n1,format=raw,media=disk,if=virtio**: Sets the first disk drive for the VM. It's pointing to `/dev/nvme0n1` (a physical NVMe disk) and using the `virtio` driver for better disk performance in the VM.
- **-drive file=/dev/nvme1n1,format=raw,media=disk,if=virtio**: Sets the second disk drive for the VM, also using the `virtio` driver.
- **-vnc :0,password=on**: Enables a VNC server on display `:0` (port 5900), and the option `password=on` ensures that the VNC connection is password-protected.
- **-monitor stdio**: Opens the QEMU monitor in the terminal, allowing you to interact with the VM via commands, including changing the VNC password.
- **-no-reboot**: Prevents the VM from automatically rebooting after shutting down, which is useful during installations where you might want to control the reboot manually.




BOOT BACK INTO THE DRIVES
The changes made:
1.	Removed -bios /usr/share/ovmf/OVMF.fd: This option was specifying the UEFI firmware. For legacy BIOS boot, we don't need to specify a BIOS file as QEMU will use its default BIOS.
2. add port 2222
```
qemu-system-x86_64 -enable-kvm -cpu host -k en-us -device virtio-net,netdev=net0 -netdev user,id=net0,hostfwd=tcp:127.0.0.1:2222-:22 -smp 4 -m 4096 -drive file=/dev/nvme0n1,format=raw,media=disk,if=virtio -drive file=/dev/nvme1n1,format=raw,media=disk,if=virtio -vnc :0
```


Difference Between Unraid and RAID:
Unraid: Unraid is a flexible operating system designed for NAS (Network Attached Storage) servers. It allows you to mix and match drives of different sizes and uses a parity drive for redundancy. It's designed for home users or small businesses who need a simple, flexible storage solution.

RAID: RAID is a technology that uses multiple hard drives to increase redundancy and performance. There are different RAID levels (RAID 0, RAID 1, RAID 5, RAID 6, etc.), each offering a different balance of redundancy, performance, and storage capacity. RAID is often used in enterprise environments for critical data protection and high availability.

https://136.243.155.166:8006/


### 2.2. Getting started with Proxmox GUI 
to access: https://your.ip.1111.166:8006/ 


<a href="https://github.com/simonrenauld/ServerSetup/blob/main/01_Infrastructure_hardware/HetzerServer.jpg](https://github.com/simonrenauld/ServerSetup/blob/main/proxmoxinfra.PNG">
  <img src="https://github.com/simonrenauld/ServerSetup/blob/main/01_Infrastructure_hardware/HetzerServer.jpg" alt="Hetzner Server" width="400" />
</a>




## 2.3. Kernel based Virtual Machine (KVM)

KVM is a virtualization technology that enables the Linux kernel to act as a hypervisor, allowing the creation of fully isolated virtual machines (VMs). These VMs operate independently of the host operating system and kernel by emulating various hardware components like CPU, RAM, and network cards. To create KVM VMs, the host CPU must support hardware virtualization extensions.

KVM differs from container-based virtualization (like OpenVZ and LXC) by providing full system virtualization rather than kernel-level virtualization. This means KVM can run a wider range of operating systems (e.g., Linux, BSD, Windows, macOS) but typically allows for fewer VMs per host compared to containers. KVM is essential for running non-Linux operating systems and specialized Linux-based OSs.

WHY KVM? 

- KVM-based virtualization: Leveraging the efficient and high-performance KVM hypervisor, Proxmox VE allows you to create and run virtual machines (VMs) directly on your physical hardware.
- Web-based management: The user-friendly web interface provides a centralized dashboard for managing all your virtualized environments, including VMs, containers, and storage.
- Container support: In addition to VMs, Proxmox VE supports LXC (Linux Containers) for running lightweight, isolated applications within a single operating system kernel.
- Storage management: The platform offers tools for managing various storage types, including local disks, iSCSI, NFS, and Ceph, ensuring efficient data storage and retrieval.
- High availability: Proxmox VE includes features like clustering and HA (High Availability) to ensure continuous operation and minimize downtime.
- API integration: The platform provides a RESTful API, allowing for automation and integration with other systems.


Creating a KVM in Proxmox:

From scratch using an ISO image
From a template
Using network PXE boot



### 2.3.1. Installing Fedora or Ubuntu VM on Proxmox and Set networking connections

<img src="https://github.com/simonrenauld/ServerSetup/blob/main/01_Infrastructure_hardware/screenshots/proxmoxgui.jpg" alt="Hetzner Server" width="800" />


```

source /etc/network/interfaces.d/*

auto lo
iface lo inet loopback

iface lo inet6 loopback

iface enp0.... inet manual
iface enp0....inet manual

auto vmbr0
iface vmbr0 inet static
        address youripaddress/26
        gateway yourgateway
        bridge-ports enp0....
        bridge-stp off
        bridge-fd 1
        bridge-vlan-aware yes
        bridge-vids 2-4094
        hwaddress xxxxxxxxxxx
        pointopoint xxxxxxxxxxxxxx
        up sysctl -p

iface vmbr0 inet6 static
        address xxxxxxxxx/64
        gateway xxxx::1

auto vmbr1
iface vmbr1 inet manual
        bridge-ports none
        bridge-stp off
        bridge-fd 0
        bridge-vlan-aware yes
        bridge-vids 2-4094

```

 nano /etc/dhcp/dhcpd.conf
```
add your subnet to connect VM to internet: 

#  update with your own network informatiosn
# This is a very basic subnet declaration.
subnet 192.222.222.0 netmask 111.111.111.0 {
    range 111.111.111.50 111.111.111.200;
    option routers 111.111.111.5;
    option subnet-mask 111.111.11.0;
    option domain-name-servers 8.8.8.8, 8.8.4.4, 1.1.1.1;
}


```


<img src="https://github.com/simonrenauld/ServerSetup/blob/main/01_Infrastructure_hardware/screenshots/Ubuntu and Fedora 40 VM.jpg" alt="gui" width="400" />



### 2.4. Installing nextcloud: 

Advantages of Nextcloud

- Comprehensive Platform: Offers a suite of mobile and desktop applications for various operating systems, including Linux, Windows, Mac, Android, iOS, F-Droid, and even Windows Mobile.
- Scalable Storage: Supports unlimited free storage space, depending on your hardware setup.
- Self-Hosting: Provides the freedom to host your own cloud storage and file-sharing solution, ensuring data privacy and security.
- Open-Source: Built on open-source principles, allowing for customization and community-driven development.
- Rich Feature Set: Offers a wide range of features beyond basic file storage, including:Calendar and Contacts, Real-time Collaboration, Secure Communication, Task Management, Photo and Video Sharing
- Integration Capabilities: Seamlessly integrates with other popular tools and services.

### Install 
```
sudo snap install nextcloud

snap changes nextcloud

snap info nextcloud
```

### Connections
```
snap connections nextcloud

Output
Interface        Plug                       Slot           Notes
network          nextcloud:network          :network       -
network-bind     nextcloud:network-bind     :network-bind  -
removable-media  nextcloud:removable-media  -              -
```
```
## Snap services
cat /snap/nextcloud/current/meta/snap.yaml 

### admin Account

sudo nextcloud.manual-install adminname password

### adjust trusted domains
sudo nextcloud.occ config:system:set trusted_domains 1 --value=example.com


## Securing Nextcloud
Option 1: Setting Up SSL with Let’s Encrypt
sudo nextcloud.enable-https self-signed

Or

sudo nextcloud.enable-https self-signed
Self-Signed Certificate
sudo ufw allow 80,443/tcp
```
 <img src="https://github.com/simonrenauld/ServerSetup/blob/main/01_Infrastructure_hardware/screenshots/nextcloudProxmoxUbuntu.jpg" alt="gui" width="400" />



### 2.4.1 SSH into Proxmox and connect to your Fedora virtual machine via command line.

**Why: SSH and why Fedora**

SSH is a secure method for connecting to remote servers and managing them via the command line. Fedora is a popular Linux distribution known for its stability and up-to-date software, making it a solid choice for server environments.

### Connect to Proxmox Server

1. **Connect to your Proxmox server via SSH as root or admin user**:
   ```
   ssh -p 5555 root@yourproxmoxip

List your virtual machines to ensure VM 104 is running:
root@proxmox-example:~# qm list
      VMID NAME                 STATUS     MEM(MB)    BOOTDISK(GB) PID
       100 ubuntu-vm            stopped    4048              32.00 0
       101 ubuntu-vm-22         stopped    10000            100.00 0
       102 ubuntu-Desktop-24    stopped    8192              40.00 0
       103 fedora               stopped    2048              32.00 0
       104 fedora40             running    8192              32.00 606015


Find the IP Address
Once VM 104 is running, you can find its IP address using the following command:
   ```
qm monitor 104
   ```

You can find the IP address of VM 104 by using the following methods instead:
   ```
Using Proxmox Shell:
ip a show tap104i0

inside proxmox connect to the ip of any virtual machine via command lines
root@proxmox-example:~# ssh simonadmin@ipvirtualmachine


Install and Configure OpenSSH on Fedora

sudo apt update && sudo apt install openssh-server -y
sudo dnf update -y
sudo dnf install -y openssh-server
sudo systemctl start sshd
sudo systemctl enable sshd
sudo firewall-cmd --permanent --add-service=ssh
sudo firewall-cmd --reload

sudo nano /etc/ssh/sshd_config

   ```


Install and Configure OpenSSH on Fedora
   ```
sudo apt update && sudo apt install openssh-server -y

sudo dnf update -y
sudo dnf install -y openssh-server
sudo systemctl start sshd
sudo systemctl enable sshd
sudo firewall-cmd --permanent --add-service=ssh
sudo firewall-cmd --reload
Edit SSH configuration:
sudo nano /etc/ssh/sshd_config
Enable temporary PasswordAuthentication yes or use key
   ```
Nextcloud on Fedora
There are many different ways to host and install Nextcloud. Below is one method using the LAMP stack.

Update the System and Install LAMP Stack Components
Nextcloud requires a web server, PHP, and a database. We’ll use Apache, MariaDB, and PHP.
   ```
sudo dnf update -y
sudo dnf install -y httpd mariadb-server php php-mysqlnd php-fpm php-json php-gd php-zip php-curl php-intl php-mbstring php-xml php-ldap php-opcache php-apcu

Start and Enable Apache and MariaDB

sudo systemctl start httpd
sudo systemctl enable httpd
sudo systemctl start mariadb
sudo systemctl enable mariadb
   ```
Troubleshooting Apache
If you encounter errors, such as:

   ```
simonadmin@fedora:~$ sudo systemctl status httpd.service
× httpd.service - The Apache HTTP Server
     Loaded: loaded (/usr/lib/systemd/system/httpd.service; enabled; preset: disabled)
    Drop-In: /usr/lib/systemd/system/service.d
             └─10-timeout-abort.conf
             /etc/systemd/system/httpd.service.d
             └─php-fpm.conf
     Active: failed (Result: exit-code) since Tue 2024-11-12 12:16:18 EST; 27s ago
       Docs: man:httpd.service(8)
   Main PID: 360294 (code=exited, status=1/FAILURE)
     Status: "Reading configuration..."
        CPU: 94ms

Nov 12 12:16:18 fedora systemd[1]: Starting httpd.service - The Apache HTTP Server...
Nov 12 12:16:18 fedora (httpd)[360294]: httpd.service: Referenced but unset environment variable eva>
Nov 12 12:16:18 fedora httpd[360294]: AH00558: httpd: Could not reliably determine the server's full>
Nov 12 12:16:18 fedora httpd[360294]: (98)Address already in use: AH00072: make_sock: could not bind>
Nov 12 12:16:18 fedora httpd[360294]: (98)Address already in use: AH00072: make_sock: could not bind>
Nov 12 12:16:18 fedora httpd[360294]: no listening sockets available, shutting down
Nov 12 12:16:18 fedora httpd[360294]: AH00015: Unable to open logs
Nov 12 12:16:18 fedora systemd[1]: httpd.service: Main process exited, code=exited, status=1/FAILURE
Nov 12 12:16:18 fedora systemd[1]: httpd.service: Failed with result 'exit-code'.
Nov 12 12:16:18 fedora systemd[1]: Failed to start httpd.service - The Apache HTTP Server.

MariaDB Server

sudo mysql_secure_installation
sudo mysql -u root -p CREATE DATABASE nextcloud; CREATE USER 'simonadmin'@'localhost' IDENTIFIED BY 'password'; GRANT ALL PRIVILEGES ON nextcloud.* TO 'simonadmin'@'localhost'; FLUSH PRIVILEGES; EXIT;



Download the Latest Nextcloud Release
cd /var/www
sudo wget https://download.nextcloud.com/server/releases/nextcloud-26.0.2.zip
sudo dnf install -y unzip
sudo unzip nextcloud-26.0.2.zip

sudo chown -R apache:apache /var/www/nextcloud
sudo chmod -R 755 /var/www/nextcloud
   ```


Configure Apache for Nextcloud
Create a new Apache configuration file for Nextcloud:
   ```
sudo nano /etc/httpd/conf.d/nextcloud.conf
   ```
Copy this configuration file inside:


Alias /nextcloud "/var/www/nextcloud/"
   ```
<Directory /var/www/nextcloud/>
    Options +FollowSymlinks
    AllowOverride All
    
    <IfModule mod_dav.c>
        Dav off
    </IfModule>

    SetEnv HOME /var/www/nextcloud
    SetEnv HTTP_HOME /var/www/nextcloud

    Require all granted
</Directory>

   ```
 
sudo systemctl restart

http://yourip/nextcloud
  ```


If you encounter the error "compatible with PHP>=8.3. You are currently running 8.3.13", downgrade to PHP 8.1:

  ```
sudo dnf remove php*
sudo dnf module reset php
sudo dnf module enable php:8.1 -y
sudo dnf install php php-cli php-fpm php-common php-mysqlnd php-gd php-xml php-mbstring php-curl -y
sudo systemctl restart httpd
php -v
If the PHP 8.1 packages are not available in the default Fedora repositories, consider using the Remi repository:

sh
sudo dnf remove php php-cli php-fpm php-gd php-json php-mbstring php-mysqlnd php-opcache php-xml php-pecl-zip
sudo dnf module reset php
sudo dnf module enable
  ```


'''


### 2.4. Install Xrdp Server for Windows Remote Desktop feature

For Ubuntu: 
Source: https://www.digitalocean.com/community/tutorials/how-to-enable-remote-desktop-protocol-using-xrdp-on-ubuntu-22-04

For Fedora:
dnf -y install xrdp tigervnc-server
systemctl enable --now xrdp



```
sudo apt update
sudo apt install xfce4 xfce4-goodies -y
sudo apt install xrdp -y

# verify Status
sudo systemctl status xrdp
if not running
sudo systemctl start xrdp


Configuring xrdp and Updating Your Firewall
sudo nano /etc/xrdp/xrdp.ini

```











































































```





RDP Connect to Linux/Ubuntu Proxmox VM 

Sources: https://www.digitalocean.com/community/tutorials/how-to-enable-remote-desktop-protocol-using-xrdp-on-ubuntu-22-04


```
sudo apt update


sudo apt install xfce4 xfce4-goodies -y

###  Installing xrdp on Ubuntu








```


### INSTALLLING UBUNTU VIRTUAL MACHINE ON PROXMOX



<img src="https://github.com/simonrenauld/ServerSetup/blob/main/01_Infrastructure_hardware/screenshots/vm-cores.jpg" alt="gui" width="400" />








<img src="https://github.com/simonrenauld/ServerSetup/blob/main/01_Infrastructure_hardware/screenshots/vm-memory.jpg" alt="gui" width="400" />






<img src="https://github.com/simonrenauld/ServerSetup/blob/main/01_Infrastructure_hardware/screenshots/start-vm.jpg" alt="gui" width="400" />
Installling nextcloud : 

Advantages
All the mobile and desktop applications you would expect - Linux (packaged in Fedora,) Windows, Mac, Android, iOS and even F-Droid and Windows Mobile.
Unlimited free storage space (depends on your hardware)





Install Next Cloud Container:

























### 1.1 Operating Systems

- Linux: Highly customizable and versatile, suitable for a wide range of applications and hardware.
- Windows Server: Offers a familiar interface and strong integration with Microsoft products, making it a popular choice for businesses.
- macOS: Apple's proprietary operating system for its computers, known for its user-friendly interface and integration with Apple devices.
- Android: A mobile operating system based on Linux, used by most smartphones and tablets.
- iOS: Apple's mobile operating system, used by iPhones and iPads.
-- Chrome OS: A lightweight operating system developed by Google, primarily designed for web-based applications.
- FreeBSD: A Unix-like operating system known for its stability and performance.
- OpenBSD: A BSD-based operating system with a strong focus on security.
- Solaris: A proprietary operating system developed by Oracle, primarily used for servers and high-performance computing.
- AIX: A proprietary operating system developed by IBM for its Power Systems hardware.
- HP-UX: A proprietary operating system developed by HP for its Itanium-based servers.



#### 1.2.1 Software and Services

=======
### Virtual Machines

The choice of virtualization technology depends on your specific needs and environment. Here are some considerations for each option:

Proxmox VE:

Pros:
- Open-source and free.
- Supports both KVM and LXC containers.
- Web-based management interface.
- Good for enterprise environments.

Cons:
- Requires a dedicated server.
- Might be overkill for small-scale or personal projects.

VirtualBox:

Pros:
- Free and open-source.
- Easy to set up and use.
- Good for desktop virtualization.

Cons:
- Not as performant as bare-metal hypervisors.
- Limited scalability for enterprise use.

VMware ESXi:

Pros:
- High performance and reliability.
- Widely used in enterprise environments.
- Extensive support and documentation.

Cons:
- Requires a license for advanced features.
- Can be complex to set up and manage.

KVM (Kernel-based Virtual Machine):

Pros:
- Integrated into the Linux kernel.
- High performance and scalability.
- Suitable for both personal and enterprise use.

Cons:
- Requires more manual setup and management.
- No native GUI management interface (though tools like Virt-Manager can be used).

Recommendations:
- For Personal Use or Small Projects: VirtualBox is a good choice due to its ease of use and setup.
- For Enterprise or Large-Scale Deployments: Proxmox VE or VMware ESXi are better suited due to their advanced features and scalability.
- For Linux Enthusiasts or Custom Solutions: KVM offers flexibility and performance but requires more hands-on management.

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

- Jellyfin: A great choice for a personal media server. It's open-source, supports various formats, and offers a user-friendly interface
- FFmpeg, HandBrake: These tools can be used to transcode media files to compatible formats for streaming. While optional, they can be helpful for ensuring smooth playback on different devices.
- Wi-Fi configuration for projector connectivity

### 1.8 Backup System for Phone Photos and Videos

- Nextcloud: A versatile solution for both file storage and syncing. It's easy to set up and offers a mobile app for convenient backups.
- ZFS/Btrfs: These are powerful file systems known for their reliability and features like snapshotting and data integrity. They're excellent choices for long-term storage.
- NAS: A Network Attached Storage device can provide additional storage capacity and can be integrated with Nextcloud for increased redundancy.

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
