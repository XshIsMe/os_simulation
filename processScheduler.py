#!/usr/bin/env python
# -*- encoding: utf-8 -*-


def all_pcb_finish(pcb_list):
    for pcb in pcb_list:
        if '完成' != pcb.status:
            return False
    return True


def schedul(pcb_list, now_pcb_index):
    # 如果所有进程执行完成，不调度
    if all_pcb_finish(pcb_list):
        return -1
    # 将所有未完成进程的状态设置为就绪
    for pcb in pcb_list:
        if '完成' != pcb.status:
            pcb.status = '就绪'
    # 获取下一个要执行的进程下标
    new_pcb_index = (now_pcb_index + 1) % len(pcb_list)
    while '完成' == pcb_list[new_pcb_index].status:
        new_pcb_index = (new_pcb_index + 1) % len(pcb_list)
    return new_pcb_index
