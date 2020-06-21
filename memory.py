#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from config import INITIAL_SIZE, SIZE


class Memory:

    def __init__(self, address, size):
        self.address = address
        self.size = size


def init_memory_list():
    memoryList = []
    memory = Memory(0, INITIAL_SIZE)
    memoryList.append(memory)
    return memoryList


class MemoryList:
    memory_list = init_memory_list()


def firstFit(jcb):
    for i in range(len(MemoryList.memory_list)):
        now_memory = MemoryList.memory_list[i]
        if now_memory.size > jcb.request_size:
            if now_memory.size - jcb.request_size <= SIZE:
                jcb.memory['address'] = now_memory.address
                jcb.memory['size'] = now_memory.size
                MemoryList.memory_list.pop(i)
            else:
                jcb.memory['address'] = now_memory.address
                jcb.memory['size'] = jcb.request_size
                now_memory.address += jcb.request_size
                now_memory.size -= jcb.request_size
            return True
    return False


def reclaim_memory(jcb):
    jcb_address = jcb.memory['address']
    jcb_size = jcb.memory['size']
    for i in range(len(MemoryList.memory_list)):
        last_memory = MemoryList.memory_list[i-1] if 0 != i else None
        next_memory = MemoryList.memory_list[i]
        if next_memory.address > jcb_address:
            if(
                # 与前一个临接
                None != last_memory and
                jcb_address == last_memory.address + last_memory.size and
                # 且与后一个临接
                jcb_address + jcb_size == next_memory.address
            ):
                MemoryList.memory_list[i-1].size = next_memory.address + \
                    next_memory.size - last_memory.address
                MemoryList.memory_list.pop(i)
            elif(
                # 与前一个临接
                None != last_memory and
                jcb_address == last_memory.address + last_memory.size
            ):
                MemoryList.memory_list[i-1].size += jcb_size
            elif(
                # 与后一个临接
                jcb_address + jcb_size == next_memory.address
            ):
                MemoryList.memory_list[i].address = jcb_address
                MemoryList.memory_list[i].size += jcb_size
            else:
                memory = Memory(jcb_address, jcb_size)
                MemoryList.memory_list.insert(i, memory)
            jcb.memory['address'] = -2
            jcb.memory['size'] = -2
            break


def allocated_memory(jcb):
    if True == firstFit(jcb):
        jcb.memory['status'] = '已分配{size}K'.format(
            size=str(jcb.memory['size'])
        )
        return True
    else:
        jcb.memory['status'] = '内存不足，未分配'
        return False


def free_memory(jcb):
    reclaim_memory(jcb)
    jcb.memory['status'] = '已释放'
