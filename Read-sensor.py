from SX127x.LoRa import *
from SX127x.board_config import BOARD
#then set up the board GPIOs

BOARD.setup()
#The LoRa object is instantiated and put into the standby mode

lora = LoRa()
lora.set_mode(MODE.STDBY)
#Registers are queried like so:

print lora.get_version()        # this prints the sx127x chip version
print lora.get_freq()       # this prints the frequency setting 
#and setting registers is easy, too

lora.set_freq(433.0)       # Set the frequency to 433 MHz 
#In applications the LoRa class should be subclassed while overriding one or more of the callback functions that are invoked on successful RX or TX operations, for example.

class MyLoRa(LoRa):

  def __init__(self, verbose=False):
    super(MyLoRa, self).__init__(verbose)
    # setup registers etc.

  def on_rx_done(self):
    payload = self.read_payload(nocheck=True) 
    # etc.
#In the end the resources should be freed properly

BOARD.teardown()
#More details
#Most functions of SX127x.Lora are setter and getter functions. For example, the setter and getter for the coding rate are demonstrated here

print lora.get_coding_rate()                # print the current coding rate
lora.set_coding_rate(CODING_RATE.CR4_6)     # set it to CR4_6
