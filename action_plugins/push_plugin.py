from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

from ansible.plugins.action import ActionBase
import socket


class ActionModule(ActionBase):

    def run(self, tmp=None, task_vars=None):
        if task_vars is None:
            task_vars = dict()

        result = super(ActionModule, self).run(tmp, task_vars)
        repository = self._task.args.get('repository', None)
        tag = self._task.args.get('tag', None)

        new_module_args = dict()
        new_module_args.update(
            dict(
                repository=repository,
                tag=tag,
            ),
        )

        result.update(
            self._execute_module(
                module_name='box_push',
                module_args=new_module_args,
            )
        )

        return result