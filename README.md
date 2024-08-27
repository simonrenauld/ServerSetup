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
