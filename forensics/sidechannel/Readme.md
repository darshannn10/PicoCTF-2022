# picoCTF 2022

> Darshan Patel

## Overview

| Tables | Description |
| ------ | ----------- |
| Category | Forensics |
| Challenge Name | Side Channel |
| Points | 400 |

## Description

There's something fishy about this PIN-code checker, can you figure out the PIN and get the flag? Download the PIN checker program here [pin_checker](https://artifacts.picoctf.net/c/143/pin_checker). Once you've figured out the PIN (and gotten the checker program to accept it), connect to the master server using `nc saturn.picoctf.net 55824` and provide it the PIN to get your flag.

## Approach

The following shows the example execution, where `Incorrect Length` is outputted when a PIN that's not 8-digits is entered, `Checking PIN...` is outputted if a 8-digit PIN is entered, and `Access denied.` is outputted if the 8-digit PIN is incorrect.

![first-step](https://user-images.githubusercontent.com/87711310/205494180-1181056e-f4fb-4ecd-94fb-0038ebb75f27.png)


There is a noticable time delay during the `Checking PIN...` and `Access denied.`, so we can use a time-based side channel attack here. 



From the program behavior, I saw that the length is first checked, and if the length is 8, the program proceeds to check the digits of the 8-digit PIN code (otherwise, it immediately returns `Incorrect length`).


I made the following Python script [side.py](./files/side.py) to measure the time before `Access denied.` is outputted

```
from pwn import *
import time
import sys

io = process(['./pin_checker'])

context.arch = 'amd64'
gs = '''
continue
'''

#allow pin number to be inputted as argument, eg: python3 side.py 12345678
pin = str(sys.argv[1])

#send the pin as the input to the pin_checker
io.sendline(pin)
#skip first output, which is 'Please enter your 8-digit PIN code:'
io.recvline()
#skip second output, which is PIN length
io.recvline()
#skip third output, which is 'Checking PIN...'
io.recvline()
#start the timer
start = time.time()
#fourth output is 'Access denied.', we are measuring time until this is outputted
recevied4 = io.recvline()
#stop the timer
stop = time.time()
#calculate time difference
time_taken = stop - start

log.info(f"Time taken: {time_taken}")
log.info(f"Received4: {recevied4}")
log.info(f"Guess: {pin}")


sys.exit()

```

I made the script so that the PIN could be inputted like the following,

`$ python3 side.py 12345678`

The following shows the example execution, where the `Time taken` is outputted in seconds.

![2nd-step](https://user-images.githubusercontent.com/87711310/205494182-3025f602-3c62-491f-94bd-d8fc3f553adb.png) 


I assumed that the PIN is checked from left to right, where  `Access denied.` is outputted as soon as the leftmost digit does not match. Therefore, the PIN with the correct leftmost digit should take the longest time because it will move onto the next digit comparison. For the first test batch, I decided to use `00000000`, `10000000`, `20000000`, `30000000`, `40000000`, `50000000`, `60000000`, `70000000`, `80000000`, `90000000` for the PINs. To automate this process, I made the following shell script [auto.sh](./files/auto.sh),

```
#!/bin/bash

python3 side.py 00000000
python3 side.py 10000000
python3 side.py 20000000
python3 side.py 30000000
python3 side.py 40000000
python3 side.py 50000000
python3 side.py 60000000
python3 side.py 70000000
python3 side.py 80000000
python3 side.py 90000000
```

Before I executed this script, I closed all programs that I wasn't using to reduce variations in time due to background processes. I then executed this script,

![3rd-step](https://user-images.githubusercontent.com/87711310/205494183-5519ff3c-d037-4392-a909-6e20465d7805.png) 

Here, I saw that the pin `40000000` took the longest, with a significant time difference from the other PINs.

Therefore, `40000000` is what I will be using for the second test batch, thus I used the following shell script.


```
#!/bin/bash

python3 side.py 40000000
python3 side.py 41000000
python3 side.py 42000000
python3 side.py 43000000
python3 side.py 44000000
python3 side.py 45000000
python3 side.py 46000000
python3 side.py 47000000
python3 side.py 48000000
python3 side.py 49000000
```

I executed the script,

![4th](https://user-images.githubusercontent.com/87711310/205494188-c1dc3c32-938f-49c6-a9ca-73c8ba51a1ae.png)
 
This shows that `48000000` takes the longest, therefore you can go on by modifying the script to find the pin-number at different position one by one.

At the end, you end finding out the pin. `48390513`is the correct pin.
Logging in to the master server using the same pin, we can obtain the flag

![final-step](https://user-images.githubusercontent.com/87711310/205494178-8cb050e5-6b94-475f-ac5c-fab3196c43b9.png)

## Flag
```
picoCTF{t1m1ng_4tt4ck_914c5ec3}
```
