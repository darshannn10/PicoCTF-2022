# picoCTF 2022

> Darshan Patel

## Overview

| Tables | Description |
| ------ | ----------- |
| Category | Cryptography |
| Challenge Name | Credstuff |
| Points | 100 |

## Description

We found a leak of a blackmarket website's login credentials. Can you find the password of the user cultiris and successfully decrypt it?
The first user in usernames.txt corresponds to the first password in passwords.txt. The second user corresponds to the second password, and so on.

#### Hint

- Maybe other passwords will have hints about the leak?

## Approach

Firstly, open the `usernames.txt` file in notepad and note down the line on which the username cultiris is on. Then, open up the `passwords.txt` file and visit the exact same line number, the username `cultiris` was on and you will find an encrypted flagAfter find flag from corresponded username of `cultiris`. The flag covered with ROT13 cipher. We can able to decode by using terminal and also Online tools like [CyberChef](https://gchq.github.io/CyberChef/) as well.

```bash
echo -n cvpbPGS{P7e1S_54I35_71Z3}| tr "A-Za-z" "N-ZA-Mn-za-m"
```

## Flag

```
picoCTF{C7r1F_54V35_71M3}
```
