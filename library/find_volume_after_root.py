#!/usr/bin/python
# -*- coding: utf-8 -*-

from ansible.module_utils.basic import AnsibleModule

DOCUMENTATION = '''
---
module: find_volume_after_root
short_description: "Finds the next partition after the root partition on a system."
description:
    - This Ansible module searches for the partition immediately following the root partition ("/") on a Linux system using the provided ansible_facts. It returns the name and size of the next partition, if found.
options:
  ansible_facts:
    description:
      - A dictionary containing ansible facts about the system, including mounts and devices information.
    required: true
    type: dict
    default: None
    aliases:
      - facts
author:
  - Vlad Cherkasov
version_added: "1.0.0"
requirements: []
notes:
  - This module requires access to ansible_facts, which should be gathered prior to using this module.
  - The module will fail if the root mount ("/") is not found in ansible_facts or if no next partition is found.
'''

EXAMPLES = '''
- name: Find volume using ansible_facts
  hosts: localhost
  gather_facts: yes
  tasks:
    - name: Find the next partition after the root partition
      find_volume_after_root:
          ansible_facts: "{{ ansible_facts }}"
          register: result
    - name: Print the result
      debug:
          var: result
'''


def find_next_element(search_string, xs):
    if search_string in xs:
        index = xs.index(search_string)
        if index < len(xs) - 1:
            return xs[index + 1]
        else:
            return None
    else:
        return None

def main():
    module = AnsibleModule(
        argument_spec={
            'ansible_facts': {'type': 'dict', 'required': True},
        },
        supports_check_mode=True
    )
    ansible_facts = module.params.get('ansible_facts', {})

    # Throw error if ansible_facts is empty
    if not ansible_facts:
        module.fail_json(msg='ansible_facts is empty')

    root_mount = next((x for x in ansible_facts['mounts'] if x['mount'] == '/'), None)
    if root_mount:
        # Get the UUID of the mount '/'
        root_uuid = root_mount['uuid']
        # Find partitions with the corresponding UUID in devices
        for device in ansible_facts['devices'].values():
            for partition, details in device['partitions'].items():
                if details['uuid'] == root_uuid:
                    # Find the next partition after the partition with root_uuid
                    partitions = sorted(device['partitions'].keys())
                    next_partition = find_next_element(partition, partitions)
                    size = device['partitions'][next_partition]['size']
                    if next_partition is None:
                        module.fail_json(msg='Next partition not found')
                    break
    else:
        module.fail_json(msg='Root mount not found in ansible_facts')


    result = {
        'volume_name': next_partition,
        'size': size,
    }

    module.exit_json(changed=False, **result)


if __name__ == '__main__':
    main()
