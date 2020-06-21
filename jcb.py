#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import random
import pcb


class JCB:

    def __init__(self, name):
        self.name = name
        self.request_size = random.randint(3, 100)
        self.arrival_time = random.randint(3, 100)
        self.pcb_list = []
        self.memory = {
            'address': -1,
            'size': -1,
            'status': '未分配',
        }

    def is_finish(self):
        for pcb in self.pcb_list:
            if '完成' != pcb.status:
                return False
        return True


def create_jcb_list(num):
    jcb_list = []
    for i in range(num):
        tmp_jcb = JCB('JCB ' + str(i))
        tmp_jcb.pcb_list = pcb.create_pcb_list(
            random.randint(1, 3), tmp_jcb.name.replace('J', 'P')
        )
        jcb_list.append(tmp_jcb)
    jcb_list[0].arrival_time = 0
    return jcb_list
