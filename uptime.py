import ctypes
import struct


def uptime_seconds():
    libc = ctypes.CDLL('libc.so.6')
    buf = ctypes.create_string_buffer(4096)  # generous buffer to hold
    # struct sysinfo
    if libc.sysinfo(buf) != 0:
        print('failed')
        return -1

    uptime = struct.unpack_from('@l', buf.raw)[0]
    return uptime


up_sec = uptime_seconds()
print(f'{up_sec // 60 // 60} hours {up_sec // 60 % 60} minutes')
