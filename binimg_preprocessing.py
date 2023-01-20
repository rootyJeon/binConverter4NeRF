#########################
#                       #
# Made by Byungwoo Jeon #
#   Date : 01/20/2023   #
#                       #
#########################

import struct
from functools import partial

filename = "..."

struct_fmt = 'B'
# 'B' is for 1byte(8bit) unsigned integer which is same as uint8 in C++
struct_len = struct.calcsize(struct_fmt)
struct_unpack = struct.Struct(struct_fmt).unpack_from

# Loading
with open(filename, "rb") as file:
    datas = [struct_unpack(byte) for byte in iter(partial(file.read, struct_len), b'')]

# Show up
for i, pixel_val in enumerate(datas):
    if i % (512 * 512) == 0:
        print("\n\n=========================================\n\n")
    print(pixel_val, end="")
