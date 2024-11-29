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

-Local Directories: Simple and fast, using local file systems for storage.
-LVM (Logical Volume Manager) / LVM Thin: Advanced volume management with thin provisioning, allowing for flexible storage allocation.
-NFS (Network File System): Network-based storage that enables sharing files over a network.
-iSCSI (Internet Small Computer System Interface): Network protocol that allows data storage over IP networks, often used for SANs (Storage Area Networks).
-GlusterFS: Scalable network file system suitable for large-scale data storage and handling.
-Ceph RADOS Block Devices (RBD): Highly scalable and distributed block storage, perfect for cloud environments.
-ZFS (Zettabyte File System): High-performance file system with integrated volume management, known for data integrity and advanced features.




### 1.3.1. Draw.io Server Infrastructure

The Draw.io Integration extension for Visual Studio Code brings the full functionality of Draw.io diagramming directly into your code editor. Ideal for creating flowcharts, network diagrams, or UML models, this extension lets you diagram without switching between applications. You can save diagrams as .drawio.png or .drawio.svg, preserving editable data within the image's metadata for easy sharing and future editing. With offline support, Git repository integration, and seamless Markdown embedding, this extension enhances team collaboration and workflow visualization, making it a powerful addition to any developer's toolkit.

<img src="https://github.com/simonrenauld/ServerSetup/blob/main/01_Infrastructure_hardware/screenshots/proxmox_architecture.png" alt="Hetzner Server" width="400" />



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


### 2.4.2. set up Dynamic DNS (DDNS) and port forwarding for your Nextcloud server


Choose a DDNS provider (such as No-IP or Dynu) and follow these instructions to set up DDNS.

Sign Up for a DDNS Provider:

Create an account on a DDNS provider like No-IP or Dynu.
Choose a free or paid plan as needed.
Create a Hostname:

Once you’re logged in, create a hostname (e.g., yourdomain.ddns.net) that will point to your server's IP address.
Install DDNS Client on Hetzner Server:

Install the DDNS client (e.g., ddclient) on your Hetzner server to keep the hostname updated with your server’s IP address.
  ```

sudo apt update
sudo apt install ddclient
Configure the DDNS Client:
  ```
During installation, you’ll be prompted to enter your DDNS provider details.
If prompted, choose to configure it automatically. If not, configure it manually by editing the /etc/ddclient.conf file:
  ```
sudo nano /etc/ddclient.conf
Add your DDNS credentials and hostname (adjust these details based on your DDNS provider):
plaintext
Copy code
protocol=dyndns2
use=web, web=dynamicdns.park-your-domain.com/getip
server=dyndns.your-provider.com
login=your-ddns-username
password=your-ddns-password
yourdomain.ddns.net

  ```
Save and close the file, then restart the ddclient service:
  ```
sudo systemctl restart ddclient
sudo systemctl enable ddclient
  ```


### 2.4.3. Install Xrdp Server for Windows Remote Desktop feature

For Ubuntu: 
Source: https://www.digitalocean.com/community/tutorials/how-to-enable-remote-desktop-protocol-using-xrdp-on-ubuntu-22-04
```
For Fedora:
dnf -y install xrdp tigervnc-server
systemctl enable --now xrdp



sudo apt update
sudo apt install xfce4 xfce4-goodies -y
sudo apt install xrdp -y

verify Status
sudo systemctl status xrdp
if not running
sudo systemctl start xrdp


Configuring xrdp and Updating Your Firewall
sudo nano /etc/xrdp/xrdp.ini



Here’s the reviewed and corrected Markdown, with some refinements for clarity, accuracy, and compatibility across systems:



# Let's set up llama.cpp on your Fedora VM

## 3. Install required dependencies

### 3.1. First, install required dependencies:



```
sudo dnf groupinstall "Development Tools"
sudo dnf install cmake wget git
```

3.2. Clone and build llama.cpp:
```
git clone https://github.com/ggerganov/llama.cpp.git
cd llama.cpp
mkdir build
cd build
cmake .. -DLLAMA_BLAS=ON -DLLAMA_BLAS_VENDOR=OpenBLAS
make -j4
```

3.3. Download a compatible Llama model
```
# Create models directory
mkdir -p models
cd models

# Download TinyLlama
wget https://huggingface.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF/resolve/main/tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf
```

3.4. Run the model:
```
cd ..
./main -m models/tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf -n 1024 --interactive

# Or use the chat completion interface
./main -m models/tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf --interactive-first -n 1024 -c 4096 --temp 0.7
```

3.5. Performance Tips:
```
# Set the number of threads to match your CPU
export OMP_NUM_THREADS=8  # i7-6700 has 4 cores/8 threads

# Use smaller context sizes for better performance
# Add these flags when running:
--ctx_size 2048  # Smaller context window
--batch_size 512  # Adjust based on performance
```
3.6. Model Recommendations for your hardware:
TinyLlama (1.1B) - Fast, light on resources
```
Llama-2-7B-Chat-GGUF (Q4 quantized) - Good balance

Mistral-7B-v0.1-GGUF (Q4 quantized) - Good performance
```
3.7. Handling Errors:
```

# Go back to build directory and compile
cd ~/llama.cpp/build
cmake .. -DLLAMA_BLAS=ON -DLLAMA_BLAS_VENDOR=OpenBLAS
make -j4

# Verify the executable was created
ls -l main

# Now try running with the model (using full path to be sure)
./main -m ./models/tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf -n 1024 --interactive
```
3.8. If you're still getting errors, let's install OpenBLAS first for better CPU performance:
```
# Install OpenBLAS
sudo dnf install openblas-devel

# Clean and rebuild
cd ~/llama.cpp/build
rm -rf *
cmake .. -DLLAMA_BLAS=ON -DLLAMA_BLAS_VENDOR=OpenBLAS
make -j4

# Now try running again
./main -m ./models/tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf -n 1024 --interactive
```


3.9. Checking Permissions:
```
# Check permissions
chmod +x ~/llama.cpp/build/bin/main

# Run the model
./main -m ../models/tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf --interactive-first
```

3.10. Running llama-cli:
```
simonadmin@fedora:~/llama.cpp$ ./llama-cli -m ./models/tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf --interactive-first

Example Output:
Create me a simple data model to optimize retail operations:
```
I have a customer database that contains:

Product name

Product description

Price

Sku (a unique identifier for each product)

Stock level

I need to create a database schema that optimizes the following:

Implementing a search function to retrieve products quickly

Implementing a way to track inventory levels so we can quickly adjust stock levels if necessary

A way to easily update prices of products, making sure prices are accurate and up-to-date

The schema should also be optimized for readability, allowing for easy maintenance and updates in the future. Please provide the necessary SQL queries, and also consider any limitations or considerations for implementing this in a production database.

<|user|> Could you add some information on how to optimize the search function for quick retrieval of products? Also, can you suggest some best practices for implem

```
```

4.1 Connecting to Proxmox Server with `virt-manager`

Absolutely, here’s the revised README without the sensitive information:

```markdown
# Connecting to Proxmox Server with `virt-manager`

This guide provides step-by-step instructions to connect to a Proxmox server using `virt-manager` on a Fedora system, including setting up SSH key-based authentication and configuring the SSH config file.

## Prerequisites

- A Proxmox server with `libvirtd` service running.
- `virt-manager` installed on your Fedora system.
- SSH access to the Proxmox server.

## Steps

### 1. Install Required Packages

Ensure `libvirt` packages are installed on your Proxmox server.

```sh
sudo apt-get update
sudo apt-get install libvirt-daemon-system libvirt-clients
```

### 4.2 Start and Enable `libvirtd` Service

```sh
sudo systemctl start libvirtd
sudo systemctl enable libvirtd
sudo systemctl status libvirtd
```

### 4.3. Set Up SSH Key-Based Authentication

 **Generate SSH Key Pair**:

    ```sh
    ssh-keygen -t rsa -b 2048
    ```

**Copy Public Key to Proxmox Server**:

    ```sh
    ssh-copy-id -i ~/.ssh/id_rsa.pub -p [PORT] [USER]@[PROXMOX_SERVER]
    ```

**Verify Connection**:

    ```sh
    ssh -p [PORT] [USER]@[PROXMOX_SERVER]
    ```

### 4.4 Configure SSH Config File

Edit the SSH config file on your Fedora system to include the Proxmox server details.

```sh
nano ~/.ssh/config
```

Add the following configuration:

```plaintext
Host proxmox
    HostName [PROXMOX_SERVER]
    Port [PORT]
    User [USER]
    IdentityFile ~/.ssh/id_rsa
```



### 5. Accessing Fedora VM on Proxmox from Windows Using Virt-Viewer

This guide provides a step-by-step procedure to set up and access your Fedora VM on Proxmox from a local Windows machine using Virt-Viewer.

## Prerequisites

- Proxmox installed with Fedora VM
- Local Windows machine


## Steps

### 1. Install Required Packages on Fedora VM

Ensure your Fedora VM has the necessary packages installed.

```
sudo dnf update
sudo dnf install qemu-kvm spice-vdagent spice-webdavd
```

### 5.2. Start and Enable SPICE Service
```
sudo systemctl start spice-webdavd
sudo systemctl enable spice-webdavd
```


### 5.3. Configure Firewall on Fedora VM
```
sudo firewall-cmd --permanent --add-service=ssh
sudo firewall-cmd --permanent --add-port=5900/tcp
sudo firewall-cmd --permanent --add-port=1234/tcp
sudo firewall-cmd --reload

```

### 5.4. Verify Service and Ports
Check the status of the SPICE service and ensure the necessary ports are open.
sudo systemctl status spice-webdavd
sudo firewall-cmd --list-ports


### 5.5. Install Virt-Viewer on Windows
Download and install Virt-Viewer from Virt-Manager's Download Page.
https://virt-manager.org/

Choose the Win x64 MSI (gpg) version if you are using a 64-bit Windows system.

Choose the Win x86 MSI (gpg) version if you are using a 32-bit Windows system.

6. Connect to Fedora VM Using Virt-Viewer
Launch Virt-Viewer on your Windows machine.

Enter the IP address of your Fedora VM (100.168.192.100) and the SPICE port (5900).

Click Connect to access your Fedora VM.

7. Troubleshooting
Firewall Issues: Ensure the firewall on Fedora VM allows incoming connections on the required ports.
on proxmox check the display in hardware spice should be selected and in options make the SPICE WebDav daemon is installed in the VM and folder and video sharing is selectected
Service Issues: Ensure SPICE service is running correctly.


Sure! Here are the commands and steps to optimize your Fedora VM and analyze its performance, formatted to match your example:

### 5.6. Optimize Virtual Machine Performance

Install `spice-vdagent` and `qemu-guest-agent`:
```bash
sudo dnf install spice-vdagent qemu-guest-agent
sudo systemctl enable spice-vdagent --now
sudo systemctl enable qemu-guest-agent --now
```

Configure Video Memory:
```bash
sudo nano /etc/pve/qemu-server/104.conf
```
Add or modify the following lines:
```conf
vga: qxl,mem=128
spice: enable=1
```

Restart the VM:
```bash
sudo systemctl reboot
```

Network Performance Test:
Install and Run `iperf3`:
On the host (server):
```bash
sudo dnf install iperf3
iperf3 -s
```
On the VM (client):
```bash
sudo dnf install iperf3
iperf3 -c <host-ip-address>
```

Update and Install Necessary Packages:
Update System:
```bash
sudo dnf update
sudo dnf install kernel-modules-extra
sudo reboot
```

Optimize Windows Machine for SPICE:
Install Latest Spice Guest Tools:
Download and install from [Spice Space website](https://www.spice-space.org/download.html).

Adjust Remote Viewer Settings:
- Open Remote Viewer.
- Go to **Edit** > **Preferences**.
- Adjust image quality and enable compression/video streaming.

Optimize Network Settings on Windows:
- Ensure a wired connection.
- Configure network adapter settings for optimal performance.

Performance Analysis:
Run Benchmarks:
```bash
phoronix-test-suite benchmark pts/compress-7zip
phoronix-test-suite benchmark pts/compilebench
phoronix-test-suite benchmark pts/ramspeed
phoronix-test-suite benchmark pts/iperf
```

View Results:
```bash
phoronix-test-suite result-file <result-name>
phoronix-test-suite result-view <result-name>
```

Generate Detailed Reports:
```bash
phoronix-test-suite result-view <result-name>
```

Troubleshooting and Monitoring:
Monitor System Performance:
```bash
top
htop
iotop
```

Disable Unnecessary Services:
```bash
sudo systemctl disable <service-name>
```

Switch Display Server:
- Log out and select "GNOME on Xorg" at the login screen.

By following these commands and steps, you can optimize the performance of your Fedora VM and analyze its performance effectively. Let me know if you need any further assistance!

