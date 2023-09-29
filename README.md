# Ansible Playbook Suite

This Ansible playbook suite (`site.yaml`) automates essential server configuration tasks. Before running the playbook suite, ensure you have installed the necessary dependencies listed in the `requirements.yaml` file. The suite includes the following playbooks:

1. **`encrypt_devices.yaml`**: Encrypts specified disk partitions for enhanced security.
2. **`kernel_parameters.yaml`**: Optimizes kernel parameters for improved system performance.
3. **`rename_interface.yaml`**: Configures network interfaces, renaming the active interface to "net0."
4. **`information.yaml`**: Gathers detailed system information, including CPU details and Hyper-Threading status.

## Usage Instructions

1. **Dependency Installation**:
   - Install the required dependencies by running `ansible-galaxy install -r requirements.yaml`.

2. **Inventory Configuration**:
   - Ensure your inventory file (`inventory.yaml`) includes the target servers.

3. **Running the Playbook**:
   - Execute the playbook suite using the command `ansible-playbook site.yaml -b -i inventories`.

4. **Monitoring Execution**:
   - Monitor the output for task execution status and ensure there are no errors.

5. **Refer to Individual Playbooks**:
   - For specific details about each configuration task, refer to the respective playbook README files.
