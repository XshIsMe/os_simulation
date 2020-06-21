#!/usr/bin/env python
# -*- encoding: utf-8 -*-


def run(pcb, slice_length):
    now_slice = 0
    pcb.status = '运行'
    while (now_slice < slice_length) and ('完成' != pcb.status):
        pcb.run()
        now_slice += 1
    return now_slice
