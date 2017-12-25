#!/usr/bin/python

import json
from ansible.module_utils.basic import AnsibleModule
import docker


def main():

    module = AnsibleModule(
        argument_spec=dict(
            repository=dict(required=True, type='str'),
            tag=dict(required=True, type='str'),
            task_var=dict(default={}, type='dict')
        )
    )
    repository = module.params['repository']
    client = docker.from_env()
    client.images.push(repository)

    print (json.dumps({
        "Message": "Image is available in your docker cloud repository!"
    }))

    module.exit_json(changed=True, keyword=value)
    module.exit_json(changed=False, msg='error message', keyword=value)


if __name__ == '__main__':
    main()
