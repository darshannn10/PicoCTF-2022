# picoCTF 2022

> Darshan Patel

## Overview

| Tables | Description |
| ------ | ----------- |
| Category | Forensics |
| Challenge Name | Eavesdrop |
| Points | 300 |

## Description

Download this packet capture and find the flag.

#### Hint

- All we know is that this packet capture includes a chat conversation and a file transfer.

## Approach

Open the pcap file on Wireshark and Follow the TCP Stream.

![eavesdrop1](https://user-images.githubusercontent.com/87711310/205489250-5eb68060-24ec-4602-bffb-f177ea90a113.png)

In the conversation, They've shared DES Encrypted file.txt over the port 9002. Let's export the packet and decode the file.txt

![eavesdrop2](https://user-images.githubusercontent.com/87711310/205489252-5cf0a988-c313-4eba-b0dd-d313c3c00781.png)

```bash
openssl des3 -d -salt -in file.dat -out file.txt -k supersecretpassword123
```

## Flag

```
picoCTF{nc_73115_411_0ee7267a}
```
