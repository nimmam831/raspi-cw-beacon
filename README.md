# raspi-cw-beacon

This is a CW beacon made for the Raspberry Pi. It works on a Raspberry Pi, and all other 40-pin Raspberry Pi computers, like the 2B and Zero W. 

# How to use: 

Plug pin 21 (BCM pin) into the microphone input jack on your radio, and plug ground on the Raspberry Pi to your radio. <br>
(WARNING): YOU NEED A LICENSE TO TRANSMIT ON THE HAM BANDS. I AM NOT RESPONSIBLE FOR ANY CHARGES FOR NOT BEING LICENSED AND TRANSMITTING. <br>
You need VOX turned on, at a low level that is still high enough for it to not be always transmitting. I was trying it with PTT, but that induced a <br>
lot of noise and made the signal level lower. I found out that not using PTT removed the extra noise, and made it much louder. <br>
I have tested it on a Baofeng BF-F8HP, and it works just fine. (Only connect ring on the TRS cable to pin 21, and ground to - on the Pi.)
This can also be useful for testing antennas and seeing their null. Normal HT antennas have a null when facing right at the transmitter antenna, <br>
and might also have a null in the other angle. I found that the Wouxun stock antennas have a null that I measured around 25 dB. You <br>
could even set it up as a radio fox for foxhunting events, as long as it is not easily visible.
