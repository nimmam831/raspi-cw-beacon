import RPi.GPIO as GPIO
import time
# Use VOX at a low setting, just enough for the morse code to trigger it but not too much
# YOU NEED A LICENSE TO TRANSMIT ON THE HAM BANDS. YOU ARE RESPONSIBLE IF YOU DO NOT HAVE A LICENSE
# TODO
# change the duration to a variable
# make the duration a duty cycle, for easier RF exposure calculation
# set the mode
# How to use
# Plug the mic in of a radio to Pin 21 on GPIO
# (on Pi 4, this is physical pin 40 (top right when ethernet is on right)
# You can use any radio that has VOX support
GPIO.setmode(GPIO.BCM)
# set GPIO pin 21 (audio) as output
GPIO.setup(21, GPIO.OUT)
# set up PWM wave
pwm = GPIO.PWM(21, 1000/0.885)
# change this, with callsign and other stuff to send
morse_code = "-.- --.- ....- --. --- -... / -... . .- -.-. --- -. / ..- ... .. -. --. / -... .- --- ..-. . -. --. / -... ..-. -....- ..-. ---.. .... .--. -..-. .-. .- ... / .--. .."
# define timing parameters (adjust to change speed)
dit_duration = 0.125  # duration of a single dit (seconds)
dah_duration = dit_duration * 3  # multiplier is in dits
gap_duration = dit_duration * 0.8  # change the duration between each dit or dah
word_duration = dit_duration * 5 # adjust as needed
def play_morse_code():
    while True: # infinite loop
        for char in morse_code: # every character/symbol
            if char == ".": # dit, dot
                pwm.start(50) # start PWM, making a tone
                time.sleep(dit_duration) # wait for duration specified
            elif char == "-": # dah, dash
                pwm.start(50) 
                time.sleep(dah_duration)
            elif char == "/":
                pwm.stop() # word spacing
                time.sleep(word_duration)
            else:
                pwm.stop()  # gap between words
                time.sleep(gap_duration)
            pwm.stop()  # make it stop after the time
            time.sleep(gap_duration)
        time.sleep(9.5) # delay between loops
        
try: 
    play_morse_code() # starts
except KeyboardInterrupt: # this is needed to clean all the stuff
	pass
finally:
	GPIO.cleanup() # end of the script

print("Morse code beacon program by KQ4GOB closed.") # last line
