# 10.	Add the set_channel(new_channel_no) method in the TV class to set the TV channel number. 
# Then try using the TV set.
#a.	Create a TV set
#b.	Show TV status
#c.	Turn TV on
#d.	Show TV status
#e.	Change TV channel to 5
#f.	Show TV status
#g.	Turn TV off
#h.	Show TV status 


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
    def set_channel(self, new_channel_no):
        self.channel_no = new_channel_no

# a. 
tv= TV()

tv.show_status()
tv.turn_on()
tv.show_status()
tv.set_channel("5")
tv.show_status()
tv.turn_off()
tv.show_status()
