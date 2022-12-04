# picoCTF 2022

> Darshan Patel
## Overview

| Tables | Description |
| ------ | ----------- |
| Category | Forensics |
| Challenge Name | File types |
| Points | 100 |

## Description

This file was found among some files marked confidential but my pdf reader cannot read it, maybe yours can.

#### Hint

Remember that some file types can contain and nest other files

## Approach

```bash
┌─[darshan@kali]─[~/Workspace/picoctf/picoctf2022/forensics/file-types]
└──╼ $file Flag.pdf 
Flag.pdf: shell archive text

┌─[darshan@kali]─[~/Workspace/picoctf/picoctf2022/forensics/file-types]
└──╼ $mv Flag.pdf Flag.sh

┌─[darshan@kali]─[~/Workspace/picoctf/picoctf2022/forensics/file-types]
└──╼ $chmod +x Flag.sh

┌─[darshan@kali]─[~/Workspace/picoctf/picoctf2022/forensics/file-types]
└──╼ $./Flag.sh 
x - created lock directory _sh00046.
x - extracting flag (text)
x - removed lock directory _sh00046.

┌─[darshan@kali]─[~/Workspace/picoctf/picoctf2022/forensics/file-types]
└──╼ $file flag 
flag: current ar archive

┌─[darshan@kali]─[~/Workspace/picoctf/picoctf2022/forensics/file-types]
└──╼ $ar x flag

┌─[darshan@kali]─[~/Workspace/picoctf/picoctf2022/forensics/file-types]
└──╼ $file flag 
flag: cpio archive

┌─[darshan@kali]─[~/Workspace/picoctf/picoctf2022/forensics/file-types]
└──╼ $mv flag Flag

┌─[darshan@kali]─[~/Workspace/picoctf/picoctf2022/forensics/file-types]
└──╼ $cpio -i < Flag
2 blocks

┌─[darshan@kali]─[~/Workspace/picoctf/picoctf2022/forensics/file-types]
└──╼ $file flag 
flag: bzip2 compressed data, block size = 900k

┌─[darshan@kali]─[~/Workspace/picoctf/picoctf2022/forensics/file-types]
└──╼ $mv flag flag.bz2

┌─[darshan@kali]─[~/Workspace/picoctf/picoctf2022/forensics/file-types]
└──╼ $bzip2 -dv flag.bz2 
  flag.bz2: done

┌─[darshan@kali]─[~/Workspace/picoctf/picoctf2022/forensics/file-types]
└──╼ $file flag 
flag: gzip compressed data, was "flag", last modified: Tue Mar 15 06:50:36 2022, from Unix, original size modulo 2^32 329

┌─[darshan@kali]─[~/Workspace/picoctf/picoctf2022/forensics/file-types]
└──╼ $mv flag flag.gz

┌─[darshan@kali]─[~/Workspace/picoctf/picoctf2022/forensics/file-types]
└──╼ $gunzip flag.gz

┌─[darshan@kali]─[~/Workspace/picoctf/picoctf2022/forensics/file-types]
└──╼ $file flag 
flag: lzip compressed data, version: 1

┌─[darshan@kali]─[~/Workspace/picoctf/picoctf2022/forensics/file-types]
└──╼ $mv flag flag.lz

┌─[darshan@kali]─[~/Workspace/picoctf/picoctf2022/forensics/file-types]
└──╼ $lzip -d flag.lz

┌─[darshan@kali]─[~/Workspace/picoctf/picoctf2022/forensics/file-types]
└──╼ $file flag
flag.lz4: LZ4 compressed data (v1.4+)

┌─[darshan@kali]─[~/Workspace/picoctf/picoctf2022/forensics/file-types]
└──╼ $mv flag flag.lz4

┌─[darshan@kali]─[~/Workspace/picoctf/picoctf2022/forensics/file-types]
└──╼ $lz4 -dv flag.lz4 
*** LZ4 command line interface 64-bits v1.9.3, by Yann Collet ***
Decoding file flag 
flag.lz4             : decoded 283 bytes

┌─[darshan@kali]─[~/Workspace/picoctf/picoctf2022/forensics/file-types]
└──╼ $file flag
flag.lz4: LZ4 compressed data (v1.4+)

┌─[darshan@kali]─[~/Workspace/picoctf/picoctf2022/forensics/file-types]
└──╼ $mv flag flag.lz4

┌─[darshan@kali]─[~/Workspace/picoctf/picoctf2022/forensics/file-types]
└──╼ $lz4 -dv flag.lz4 
*** LZ4 command line interface 64-bits v1.9.3, by Yann Collet ***
Decoding file flag 
flag.lz4             : decoded 266 bytes

┌─[darshan@kali]─[~/Workspace/picoctf/picoctf2022/forensics/file-types]
└──╼ $file flag
flag: LZMA compressed data, non-streamed, size 255

┌─[darshan@kali]─[~/Workspace/picoctf/picoctf2022/forensics/file-types]
└──╼ $mv flag flag.lzma

┌─[darshan@kali]─[~/Workspace/picoctf/picoctf2022/forensics/file-types]
└──╼ $lzma -d flag.lzma

┌─[darshan@kali]─[~/Workspace/picoctf/picoctf2022/forensics/file-types]
└──╼ $file flag 
flag: lzop compressed data - version 1.040, LZO1X-1, os: Unix

┌─[darshan@kali]─[~/Workspace/picoctf/picoctf2022/forensics/file-types]
└──╼ $mv flag flag.lzo

┌─[darshan@kali]─[~/Workspace/picoctf/picoctf2022/forensics/file-types]
└──╼ $lzop -d flag.lzo

┌─[darshan@kali]─[~/Workspace/picoctf/picoctf2022/forensics/file-types]
└──╼ $file flag
flag: lzip compressed data, version: 1

┌─[darshan@kali]─[~/Workspace/picoctf/picoctf2022/forensics/file-types]
└──╼ $mv flag flag.lzip

┌─[darshan@kali]─[~/Workspace/picoctf/picoctf2022/forensics/file-types]
└──╼ $lzip -d flag.lzip

┌─[darshan@kali]─[~/Workspace/picoctf/picoctf2022/forensics/file-types]
└──╼ $file flag.lzip.out

┌─[darshan@kali]─[~/Workspace/picoctf/picoctf2022/forensics/file-types]
└──╼ $mv flag.lzip.out flag.xz

┌─[darshan@kali]─[~/Workspace/picoctf/picoctf2022/forensics/file-types]
└──╼ $xz -d flag.xz

┌─[darshan@kali]─[~/Workspace/picoctf/picoctf2022/forensics/file-types]
└──╼ $file flag 
flag: ASCII text

┌─[✗]─[darshan@kali]─[~/Workspace/picoctf/picoctf2022/forensics/file-types]
└──╼ $cat flag | xxd -r -p

```

## Flag

```
picoCTF{f1len@m3_m@n1pul@t10n_f0r_0b2cur17y_347eae65}
```
