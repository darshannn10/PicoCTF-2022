# picoCTF 2022

> Darshan Patel

## Overview

| Tables | Description |
| ------ | ----------- |
| Category | Forensics |
| Challenge Name | Torrent Analyze |
| Points | 400 |

## Description
SOS, someone is torrenting on our network.
One of your colleagues has been using torrent to download some files on the company’s network. Can you identify the file(s) that were downloaded? The file name will be the flag, like picoCTF{filename}

## Approach
We're given a torrent.pcap() file. As this is a torrent challenge, I went to Wireshark and enabled the BitTorrent DHT Protocol (BT-DHT) by going to `Analyze -> Enabled Protocol`.


<img width="980" alt="bt" src="https://user-images.githubusercontent.com/87711310/205495334-25cfb4a4-39f3-477c-a843-db1d759b02b3.png"> 


The overall packet capture looks like the following,


<img width="1228" alt="pcap" src="https://user-images.githubusercontent.com/87711310/205495368-80effc7a-ba3c-4f4c-bd9f-5d3cf6598872.png">


I applied the `bt-dht` filter, and looked through the packets, and saw that some contained `info_hash`. 


<img width="1228" alt="hash" src="https://user-images.githubusercontent.com/87711310/205495382-8aed505b-1784-4f1f-be42-97af241b6a25.png">


The challenge only wants us to find the file name, and not reconstruct the file, so I knew that this `info_hash` information will be very important because it tells us the hash of the file. As `hash` is `68 61 73 68` in hex, I inputted this hex value into the Wireshark search to look for all packets that contained this hash information.

<img width="843" alt="hex" src="https://user-images.githubusercontent.com/87711310/205495388-030590fe-8017-400f-880f-ba596c5c121b.png">

The first packet that contained `info_hash` was packet 79 with a hash value of `17d62de1495d4404f6fb385bdfd7ead5c897ea22`

<img width="967" alt="79" src="https://user-images.githubusercontent.com/87711310/205495410-03c8604f-cf93-4b43-8eba-e20c98c6f842.png">

So I looked up `17d62de1495d4404f6fb385bdfd7ead5c897ea22` on Google, and saw that it corresponded to `Awakened.2013.1080p.BluRay.X264-iNVANDRAREN`.

<img width="816" alt="79file" src="https://user-images.githubusercontent.com/87711310/205495417-80398da1-c7ff-4da1-8a80-96e669299274.png">

The first packet that contained `info_hash` was packet 332 with a hash value of `17c1e42e811a83f12c697c21bed9c72b5cb3000d`

<img width="839" alt="332" src="https://user-images.githubusercontent.com/87711310/205495435-58d610e8-cb4c-47b4-9520-c6fa854adffe.png"> 

This file corresponded to `name: Zoo (2017) 720p WEB-DL x264 ESubs - MkvHub.Com`.

<img width="773" alt="332file" src="https://user-images.githubusercontent.com/87711310/205495440-a726dce2-25dc-493e-9b91-00de49cb3059.png">


I looked through a few more, and I was at packet 51080 which had a hash value of `e2467cbf021192c241367b892230dc1e05c0580e`. 

<img width="842" alt="isopacket" src="https://user-images.githubusercontent.com/87711310/205495472-81b2d7ec-9336-4829-8d2d-8b0f68262cfe.png">


I Googled this, and saw that it corresponded to `ubuntu-19.10-desktop-amd64.iso` from [LinuxTracker.org](https://linuxtracker.org/index.php?page=torrent-details&id=e2467cbf021192c241367b892230dc1e05c0580e).

<img width="719" alt="google" src="https://user-images.githubusercontent.com/87711310/205495488-6814b9c5-e032-42d7-9057-86ea86c242ff.png">

<img width="776" alt="flag" src="https://user-images.githubusercontent.com/87711310/205495491-464df5ba-01e9-4d17-8c19-b0159939b435.png">


Therefore, the flag is,

`picoCTF{ubuntu-19.10-desktop-amd64.iso}`

