# System Information Playbook

This Ansible playbook, `information.yaml`, is designed to gather and display detailed information about the system's central processing units (CPUs), including the model, number of cores, and Hyper-Threading status.

## Tasks

### 1. Gather CPUs Information

This task reads the CPU information from the `/proc/cpuinfo` file on the target servers and stores it for processing.

### 2. CPU and Hyper-Threading Information

This task processes the CPU information and displays the following details:

- **CPU Model**: Displays the model name of the CPU.
- **CPU Cores**: Displays the number of CPU cores.
- **Hyper-Threading**: Displays whether Hyper-Threading is enabled or disabled based on the number of threads per core.

## Usage Instructions

1. **Inventory Configuration**:
   - Ensure the inventory file (`inventory.yaml`) includes the target servers from which you want to gather CPU information.

2. **Running the Playbook**:
   - Execute the playbook using the following command:
     ```shell
     ansible-playbook information.yaml -i inventories
     ```

3. **Viewing Results**:
   - Check the playbook output for detailed CPU information, including the model, number of cores, and Hyper-Threading status.

## Notes

- The playbook relies on reading information from the `/proc/cpuinfo` file, which provides detailed CPU information on Linux systems. Ensure that the playbook runs on supported Linux distributions.
