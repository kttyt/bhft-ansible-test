Role Name: network_configure
=========

A role to configure network settings on Ubuntu 20.04 systems using netplan.

Requirements
------------

This role is specifically designed for Ubuntu 20.04. Please ensure that your target system meets this requirement.

Role Variables
--------------

- `skip_interface_check`: (Default: `false`) A boolean variable used to control the check for more than one active interface on the system. If set to `false`, the role will verify that there is only one active interface (excluding 'lo') and fail the playbook if more than one is found. This check is important because the active interface can change, and using the wrong interface for SSH connection might cause loss of connectivity. To skip this check and proceed regardless of the number of interfaces, set this variable to `true`.
- `netplan_templates`: A list of netplan configuration templates to be applied. The role will loop through these templates and apply them to the system.

Dependencies
------------

None.

Example Playbook
----------------

```yaml
- hosts: servers
  roles:
     - role: network_configure
       vars:
         skip_interface_check: false
         netplan_templates:
           - 01-netcfg.yaml
```
In this example, the skip_interface_check variable is set to false to enforce the check for more than one interface. The role will apply the 01-netcfg.yaml template.
