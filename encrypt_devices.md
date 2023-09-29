# Encrypt Devices Playbook

This Ansible playbook is designed to automate the process of encrypting disk partitions on servers. It includes tasks to encrypt both the second disk in the system and a specific partition on the first disk.

## Tasks

### 1. Encrypting the Second Disk in the System

This task encrypts the specified second disk in the system.

- **Role**: `device_encryption`
- **Tags**: `first_device_encryption`

### 2. Encrypting Partition on the First Disk in the System

This task encrypts a specific partition on the first disk in the system. It also includes additional parameters for file system type and LUKS type.

- **Role**: `device_encryption`
- **Tags**: `second_device_encryption`, `never` (This tag indicates that the task should never run due to specific conditions.)

- **Note**: The second task is tagged as never because the specified partition is marked with the grub_boot flag, indicating that it contains crucial bootloader information. Encrypting this partition would render the system unable to boot after a restart.

## Usage Instructions

1. **Inventory Configuration**:
   - Ensure the inventory file (`inventory.yaml`) includes the target servers where encryption needs to be applied.

2. **Variable Configuration**:
   - Modify the variables in the playbook according to the specific disk and partition details. Ensure keyfiles are correctly specified and present in the specified paths.

3. **Running the Playbook**:
   - Execute the playbook using the following command:
     ```shell
     ansible-playbook encrypt_devices.yaml -b -i inventories
     ```

4. **Viewing Results**:
   - Check the playbook output for task execution status and any error messages.

## Note

- The task with the tag `never` will not execute due to specific conditions. Please ensure the appropriate conditions are met before attempting to run this task.
