# 9.	In the TV class, add the channel_no attribute indicating the number of the TV 
# channel displayed by the TV set. Initially, the TV is set to channel 1. 
# Modify the show_status() method so that it also displays the TV channel number, 
# but only if the TV is turned on:
#TV is on, channel 1
#Then try using the TV set.


class TV():
    def __init__(self):
        self.is_on = False
        self.channel_no = 1

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def show_status(self):
        if self.is_on == True:
            print("TV is on, Channel " + str(self.channel_no))
        else:
            print("TV is off")

tv= TV()

tv.show_status()
tv.turn_on()
tv.show_status()
tv.turn_off()
tv.show_status()
