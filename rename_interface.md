# Network Interface Configuration Playbook

This Ansible playbook, `rename_interface.yaml`, is designed for Ubuntu 20.04 systems. It ensures proper network configuration by renaming the active network interface to "net0." The playbook first verifies the system compatibility and checks the number of active interfaces. It then creates a Netplan configuration file to rename the interface, deletes the Cloud Init network config to prevent conflicts, and waits for a stable network connection. Finally, it gathers facts about the renamed interface and displays them. The playbook includes handlers to generate and apply Netplan configuration changes.

## Usage Instructions

1. **Inventory Configuration**:
   - Ensure the inventory file (`inventory.yaml`) includes the target Ubuntu 20.04 servers.

2. **Variable Configuration**:
   - Optionally, set `skip_interface_check` to true if you want to skip the interface count check.

3. **Running the Playbook**:
   - Execute the playbook using the following command:
     ```shell
     ansible-playbook rename_interface.yaml -i inventories
     ```

4. **Viewing Results**:
   - Check the playbook output for task execution status and ensure there are no errors during the playbook run.

## Notes
   - Ensure that you have appropriate backup and recovery mechanisms in place before making network configuration changes.
