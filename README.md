# Cloud Server Setup Guide

## 1. Buying a Server from Hetzner

[Hetzner Robot Portal](https://robot.hetzner.com/)

Simple as it is: For very little per month, you can own/rent your own dedicated server to meet any requirements and needs.

[Understanding components of a server](https://www.spiceworks.com/tech/tech-general/articles/what-is-a-server/)

[![Hetzner Server]<a href="https://github.com/simonrenauld/ServerSetup/blob/main/01_Infrastructure_hardware/HetzerServer.jpg">
  <img src="https://github.com/simonrenauld/ServerSetup/blob/main/01_Infrastructure_hardware/HetzerServer.jpg" alt="Hetzner Server" width="600" />
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

### 1.2. QEMU command with VNC setup (This command is starting a QEMU virtual machine to install Proxmox from the ISO, with the ability to control it over VNC (Virtual Network Computing)
```

printf "change vnc password\n%s\n" "abcd_123456": This sets a VNC password (abcd_123456). It's printing a command that will later be passed into QEMU's monitor interface to set the VNC password.
```


```
### QEMU Command Breakdown

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





















Up Next!!! 

## 1.1. Infrastructure Summary


## 1.2. IP and Firewall Settings









## 1.3. 




























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

### 1.2. Virtualization Platform

Proxmox VE is a free, open-source virtualization platform for Linux. It uses KVM, a powerful hypervisor, and offers a web-based management interface. You can create VMs and containers, manage storage, and ensure high availability.

- KVM-based virtualization: Leveraging the efficient and high-performance KVM hypervisor, Proxmox VE allows you to create and run virtual machines (VMs) directly on your physical hardware.
- Web-based management: The user-friendly web interface provides a centralized dashboard for managing all your virtualized environments, including VMs, containers, and storage.
- Container support: In addition to VMs, Proxmox VE supports LXC (Linux Containers) for running lightweight, isolated applications within a single operating system kernel.
- Storage management: The platform offers tools for managing various storage types, including local disks, iSCSI, NFS, and Ceph, ensuring efficient data storage and retrieval.
- High availability: Proxmox VE includes features like clustering and HA (High Availability) to ensure continuous operation and minimize downtime.
- API integration: The platform provides a RESTful API, allowing for automation and integration with other systems.

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
