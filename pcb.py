#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import random


class PCB:

    def __init__(self, name):
        self.name = name
        self.need_time = random.randint(3, 100)
        self.run_time = 0
        self.status = '未到达'

    def run(self):
        self.run_time += 1
        if self.run_time >= self.need_time:
            self.status = '完成'


def create_pcb_list(num, jcb_name):
    pcb_list = []
    for i in range(num):
        tmp_pcb = PCB(jcb_name + '.' + str(i))
        pcb_list.append(tmp_pcb)
    return pcb_list
