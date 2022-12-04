# picoCTF 2022

> Darshan Patel

## Overview

| Tables | Description |
| ------ | ----------- |
| Category | Reverse Engineering |
| Challenge Name | Lookey here |
| Points | 100 |

## Description

Attackers have hidden information in a very large mass of data in the past, maybe they are still doing it.

#### Hint

- Download the file and search for the flag based on the known prefix.

## Approach
#### Approach-1
```bash
#!/bin/bash
egrep ^*{*}$ anthem.flag.txt
```
#### Approach-2
```bash
#!/bin/bash
cat anthem.flag.txt | grep -oE "picoCTF{.*?}" --color=none
```

## Flag

```
picoCTF{gr3p_15_@w3s0m3_4c479940}
```
