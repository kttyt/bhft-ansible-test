# bhft-ansible-test

This repository contains Ansible roles and playbooks to prepare a server for operation as per the specified requirements. It includes tasks such as disk and partition encryption, configuring kernel parameters, renaming network interfaces, and displaying CPU information.

## Repository Structure

- **files:** Contains files used by Ansible roles or playbooks.
- **inventories:** Contains inventory files defining target servers.
- **library:** Custom Ansible modules go here.
- **roles:** Custom Ansible roles are stored in this directory.
- **site.yaml:** The main playbook file orchestrating roles and tasks.
- **requirements.yaml:** Lists external Ansible collections required by the playbook.

## Preparation and Usage

### Prerequisites

Make sure you have the following prerequisites installed on your system:

- **Ansible:** Install Ansible using your system package manager or Python pip.
- **Python:** Ensure Python is installed on your system.

### Installation of Required Collections

Install the necessary Ansible collections using the following command:

```bash
ansible-galaxy collection install -r requirements.yaml
```

### Steps to Prepare and Run the Playbook

1. **Generate Encryption Key:**
   Generate the encryption key that LUKS will use for disk encryption.
   ```bash
   dd bs=512 count=4 if=/dev/random of=files/luks.key iflag=fullblock
   ```

2. **Update Inventory:**
   Edit the `inventories/test.yml` file to specify your target servers and their configurations.

3. **Run the Playbook:**
   Execute the following command to run the playbook.
   ```bash
   ansible-playbook -b -D site.yaml -i inventories
   ```

## Playbook Actions

1. **Disk Encryption (First Disk):**
   - Encrypts the specified disk.
   - Mounts the encrypted disk to the specified mount point.
   - Uses the encryption key from `files/luks.key`.

2. **Partition Encryption (Next to Root Partition):**
   - Finds the partition next to the root partition.
   - Determines the encryption type based on partition size.
   - Encrypts the partition.
   - Mounts the encrypted partition to the specified mount point.
   - Uses the encryption key from `files/luks.key`.

3. **Kernel Parameters and Network Configuration:**
   - Configures kernel parameters to optimize system performance.
   - Configures network interfaces using netplan.

4. **System Information Display:**
   - Gathers CPU information from `/proc/cpuinfo`.
   - Displays CPU model, number of cores, and Hyper-Threading status.

## Custom Module Usage

This repository utilizes a custom Ansible module named `find_volume_after_root`. This module is used to find the partition immediately following the root partition on a Linux system. Refer to `library/find_volume_after_root.py` for module details and usage examples.

## Notes

- Customize the playbook and roles according to your system requirements.
- Keep the encryption key (`luks.key`) secure and do not share it publicly.
- Ensure proper backup and recovery procedures before performing disk and partition encryption.
