#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
#
# Wrap a device tree blob in the MTK LK header the bootloader expects in
# the vendor_boot dtb section, the way the stock image ships it: a 64-byte
# header (magic, big-endian sizes, the 0x20000000 load address) followed by
# the plain FDT.
#
# Usage: mtk_dtb_header.py <dtb>
import struct
import sys

path = sys.argv[1]
dtb = open(path, "rb").read()
size = len(dtb)

header = bytearray(64)
header[0:4] = bytes.fromhex("d7b7ab1e")      # magic
header[4:8] = struct.pack(">I", size + 64)   # total size
header[8:12] = bytes.fromhex("00000020")     # 0x20000000
header[12:16] = bytes.fromhex("00000020")
header[16:20] = bytes.fromhex("00000001")
header[20:24] = bytes.fromhex("00000020")
header[24:28] = bytes.fromhex("00000800")    # 0x80000
header[28:32] = b"\0" * 4
header[32:36] = struct.pack(">I", size)      # dtb size
header[36:40] = bytes.fromhex("00000040")    # header size

open(path, "wb").write(bytes(header) + dtb)
