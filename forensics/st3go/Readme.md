# picoCTF 2022

> Darshan Patel

## Overview

| Tables | Description |
| ------ | ----------- |
| Category | Forensics |
| Challenge Name | St3g0 |
| Points | 300 |

## Description

Download this image and find the flag.

#### Hint

- We know the end sequence of the message will be $t3g0.

## Approach

A `zsteg` is stegnography tool which can able to find the hidden data in BMP and PNG type images.

TO install `zsteg`
```bash
sudo apt-get install -y ruby-dev &&
sudo gem install rake &&
sudo gem install zsteg
```

![2022-12-04_18-15](https://user-images.githubusercontent.com/87711310/205491235-ae36e844-f4b4-42e6-905d-9d7cde89e9ce.png)

## Flag

```
picoCTF{7h3r3_15_n0_5p00n_a9a181eb}
```
