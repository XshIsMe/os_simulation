#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import time
import os
import cpu
import jcb
import processScheduler
import jobScheduler
import memory
from config import REFRESH_TIME, SILICE_LENGTH, JCB_NUM


def output(jcb_list, now_time):
    # 刷新屏幕
    time.sleep(REFRESH_TIME)
    os.system('cls')
    # 打印时间
    print('当前时间:', now_time)
    # 打印内存列表
    print('\n内存列表:')
    print('{address:<20} {size:<20}'.format(
        address='Address',
        size='Size'
    ))
    for m in memory.MemoryList.memory_list:
        print('{address:<20} {size:<20}'.format(
            address=m.address,
            size=m.size
        ))
    # 打印JCB列表
    print('\nJCB列表:')
    print('{name:<20} {request_size:<20} {arrival_time:<20} {memory_address:<20} {memory_size:<20} {memory_status:<20}'.format(
        name='Name',
        request_size='RequestSize',
        arrival_time='ArrivalTime',
        memory_address='MemoryAddress',
        memory_size='MemorySize',
        memory_status='MemoryStatus'
    ))
    for jcb in jcb_list:
        print('{name:<20} {request_size:<20} {arrival_time:<20} {memory_address:<20} {memory_size:<20} {memory_status:<20}'.format(
            name=jcb.name,
            request_size=jcb.request_size,
            arrival_time=jcb.arrival_time,
            memory_address=jcb.memory['address'],
            memory_size=jcb.memory['size'],
            memory_status=jcb.memory['status']
        ))
    # 打印PCB列表
    print('\nPCB列表:')
    print('{name:<20} {need_time:<20} {run_time:<20} {status:<20}'.format(
        name='Name',
        need_time='NeedTime',
        run_time='RunTime',
        status='Status'
    ))
    for jcb in jcb_list:
        for pcb in jcb.pcb_list:
            print('{name:<20} {need_time:<20} {run_time:<20} {status:<20}'.format(
                name=pcb.name,
                need_time=pcb.need_time,
                run_time=pcb.run_time,
                status=pcb.status
            ))


def main():
    # 初始化
    jcb_list = jcb.create_jcb_list(JCB_NUM)
    pcb_list = []
    now_pcb_index = -1
    now_time = 0

    # 运行直到完成所有作业
    while not jobScheduler.all_jcb_finish(jcb_list):
        # 打印结果
        output(jcb_list, now_time)

        # 作业调度
        jcb_to_memory = jobScheduler.schedul(jcb_list, now_time)
        pcb_list = jobScheduler.add_jcb_to_pcb(jcb_to_memory, pcb_list)

        # 进程调度
        now_pcb_index = processScheduler.schedul(pcb_list, now_pcb_index)

        # 运行
        if -1 != now_pcb_index:
            now_pcb = pcb_list[now_pcb_index]
            used_time = cpu.run(now_pcb, SILICE_LENGTH)

        # 更新作业状态
        jobScheduler.update_jcb_status(jcb_list)

        # 更新时间
        now_time += used_time

    # 打印最后一次结果
    output(jcb_list, now_time)


if __name__ == "__main__":
    main()
