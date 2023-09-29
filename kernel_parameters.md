# Kernel Parameters Playbook

This Ansible playbook, `kernel_parameters.yaml`, is designed to optimize kernel parameters for better system performance. It configures specific settings related to CPU states and idle states.

## Tasks

### 1. Setup Kernel Parameters for Better Performance

This task sets up kernel parameters to enhance system performance. It creates a custom configuration file and updates the GRUB configuration with the specified parameters.

- **Task**: Create a custom GRUB configuration file (`90-cmdlinux.cfg`) with the following parameters:
  - `GRUB_CMDLINE_LINUX="processor.max_cstate=1 intel_idle.max_cstate=0"`
  - The parameters `processor.max_cstate=1` and `intel_idle.max_cstate=0` disable power-saving mode and optimize CPU idle states for better performance.

### Handlers

#### 1. Update GRUB Configuration

This handler triggers the update of the GRUB configuration file (`/boot/grub/grub.cfg`) after the custom configuration file is created or modified.

- **Handler**: Update GRUB configuration file using the command:
  ```shell
  grub-mkconfig -o /boot/grub/grub.cfg
  ```
#### 2. Reboot System
This handler initiates a system reboot after updating the GRUB configuration to apply the kernel parameter changes.

- **Handler**: Reboot the system with a specified reboot timeout of 300 seconds.
Reboot Message: "Reboot initiated by Ansible for kernel parameter change"

### Usage Instructions
1. **Inventory Configuration**:
  - Ensure the inventory file (`inventory.yaml`) includes the target servers where you want to apply the kernel parameter changes.
2. **Variable Configuration**:
   - Modify the variables in the playbook according to the specific disk and partition details. Ensure keyfiles are correctly specified and present in the specified paths.

3. **Running the Playbook**:
   - Execute the playbook using the following command:
     ```shell
     ansible-playbook kernel_parameters.yaml -b -i inventories
     ```

4. **Viewing Results**:
  - Check the playbook output for task execution status and ensure there are no errors during the playbook run.
## Notes
- **Caution**: Modifying kernel parameters can impact system behavior. Ensure that the specified parameters are appropriate for your system and have been tested in a non-production environment before applying them to production servers.

- **Reboot**: The playbook will automatically initiate a system reboot to apply the kernel parameter changes. Ensure that you have planned for system downtime accordingly.
