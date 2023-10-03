Role Name: kernel_parameters
=========

A role to configure kernel parameters for improved system performance and energy efficiency.

Requirements
------------

This role is designed for Linux systems using the GRUB bootloader. Ensure that your target system meets this requirement.

Role Variables
--------------

- `cmdline_filename`: (Default: `"90-cmdlinux.cfg"`) The name of the GRUB configuration file where the custom kernel parameters will be stored.
- `cmdline_parameters`: (Default: `["processor.max_cstate=1", "intel_idle.max_cstate=0"]`) A list of kernel parameters that improve system performance by disabling certain power-saving features. These parameters are set by default to enhance system responsiveness.

Dependencies
------------

None.

Example Playbook
----------------

```yaml
- hosts: servers
  roles:
     - role: kernel_parameters
       vars:
         cmdline_filename: "90-custom.cfg"
         cmdline_parameters:
           - "processor.max_cstate=1"
           - "intel_idle.max_cstate=0"
```
In this example, the role will create a GRUB configuration file named "90-custom.cfg" with the specified kernel parameters. 

Note: The default parameters provided in cmdline_parameters are specifically chosen to improve system performance by disabling certain power-saving features. Modify these parameters carefully according to your system requirements.

