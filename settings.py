####################################
# LED NUMERATION | SEVEN SEGMENT
####################################
#
#     0000
#    5    1   00
#    5    1   00
#     6666 
#    4    2   11
#    4    2   11
#     3333 
#
##################

##################
# LED NUMERATION 
##################
digit_leds = {} 

digit_leds[3] = [ 1, 0, 5, 4, 3, 2, 6]
digit_leds[2] = [ 8, 7,12,11,10, 9,13]
digit_leds[1] = [19,18,23,22,21,20,24]
digit_leds[0] = [26,25,30,29,28,27,31]

separator_leds = [14,15,16,17]

led_count = 32

#spidev_file = "/tmp/spidev0.0"
spidev_file = "/dev/spidev0.0"