blink-led
=========

Simple script for outputting a blinking LED from a Raspberry Pi GPIO pin. Inpsired by Scott Mangold's article 'Lighting Up An Led Using Your Raspberry Pi and Python' (http://www.thirdeyevis.com/pi-page-2.php)

Dependancies
------------
raspberry-gpio-python
```bash
$ sudo apt-get update
$ sudo apt-get dist-upgrade
$ sudo apt-get install python-rpi.gpio python3-rpi.gpio
```

Usage
-----
Must be executed by root or user with permission to output to GPIO pins.
When blink.py is either imported or executed within the python/ipython shell, the 'blink()' function is available:
>blink(count, period, pin_number=11)
>outputs a loop of blinks to an LED via GPIO pin number defined by the function 'pin_num'
>count = number of LED blinks
>period = number of seconds for each LED blink

Example:
```python
import blink as b
b.blink(5,1) # will make the LED blink 5 times, holding for 1 second per blink.
```
