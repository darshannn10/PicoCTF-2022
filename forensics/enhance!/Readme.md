# picoCTF 2022

> Darshan Patel

## Overview

| Tables | Description |
| ------ | ----------- |
| Category | Forensics |
| Challenge Name | Enhance! |
| Points | 100 |

## Description

Download this image file and find the flag.

## Approach

An Image behind have some XML. So, Open the file from browser and Hit the `CTRL+U` to view source code.
![2022-12-04_15-30](https://user-images.githubusercontent.com/87711310/205484703-ecafeb20-d571-43dd-bb6c-ed53ecd7fc04.png)

`script` to get the flag: 
```bash
#!/bin/bash

cat drawing.flag.svg | grep "</tspan" | cut -d ">" -f2 | cut -d "<" -f1 | tr -d "\n" | tr -d " "

```


## Flag

```
picoCTF{3nh4nc3d_aab729dd}
```
