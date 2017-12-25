#!/usr/bin/python

import json
from ansible.module_utils.basic import AnsibleModule
import docker


def main():

    module = AnsibleModule(
        argument_spec=dict(
            path=dict(required=True, type='str'),
            dockerfile=dict(required=True, type='str'),
            name=dict(required=True, type='str'),
            task_var=dict(default={}, type='dict')
        )
    )

    path = module.params['path']
    dockerfile = module.params['dockerfile']
    name = module.params['name']

    client = docker.from_env()
    client.images.build(path=path, dockerfile=dockerfile, tag=name)


    print (json.dumps({
        "Message": "Image was successfully created"
    }))

    module.exit_json(changed=True, keyword=value)
    module.exit_json(changed=False, msg='error message', keyword=value)


if __name__ == '__main__':
    main()
