#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import memory


def all_jcb_finish(jcb_list):
    for jcb in jcb_list:
        if not jcb.is_finish():
            return False
    return True


def add_jcb_to_pcb(jcb_list, pcb_list):
    for jcb in jcb_list:
        for pcb in jcb.pcb_list:
            if pcb not in pcb_list:
                pcb_list.append(pcb)
    return pcb_list


def update_jcb_status(jcb_list):
    for jcb in jcb_list:
        if jcb.is_finish():
            jcb.status = '完成'
            # 释放内存
            if '已释放' != jcb.memory['status']:
                memory.free_memory(jcb)


def schedul(jcb_list, now_time):
    jcb_to_memory = []
    jcb_list.sort(key=lambda x: x.arrival_time)
    # 申请内存
    for jcb in jcb_list:
        if '未分配' in jcb.memory['status']:
            if now_time >= jcb.arrival_time:
                if True == memory.allocated_memory(jcb):
                    jcb_to_memory.append(jcb)
    return jcb_to_memory
