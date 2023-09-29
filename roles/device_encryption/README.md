# Device Encryption Role
=========

Role for encrypting block devices using a key file and then mounting them.

## Requirements
- Host machine must have `cryptsetup` package installed.

## Role Variables

- `encrypted_volume_name`: The name of the resulting encrypted device.
- `encrypted_volume_fstype`: Filesystem type, default is ext4.
- `luks_type`: Type of encryption (luks1, luks2); luks2 is more modern but requires more disk space (16MB vs 2MB in luks1).
- `encrypt_device`: Path to the block device to be encrypted, can be either a disk or a partition.
- `keyfile_path`: Path in the system to the encryption key.
- `keyfile_content`: Encryption key, example usage `lookup('file', 'key_filename')`.
- `mount_point`: Mount point for the encrypted device.

## Dependencies

- Name: community.crypto
  Source: https://galaxy.ansible.com
  Version: 2.15.1

## Example Playbook

```yaml
- hosts: database
  gather_facts: false
  roles:
    - role: device_encryption
      vars:
        encrypted_volume_name: db_vol
        mount_point: /mounts/db
        encrypt_device: /dev/sdb
        keyfile_content: "{{ lookup('file', 'db_disk.key') }}"
```
