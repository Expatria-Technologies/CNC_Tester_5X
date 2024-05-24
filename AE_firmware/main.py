from machine import Timer
import time
import _thread

tick_timer_period = 20 # Hz
systick = 0

from modbus_registers import client
from event_handler import process_event
from nuts_bolts import current_state, program_flow

#import program_steppers

# Set up the action timer.
tim = Timer()



# Main Timer ISR
def tick(timer):                # we will receive the timer object when being called
    global systick
        
    systick = systick + 1
        
tim.init(freq=tick_timer_period, mode=Timer.PERIODIC, callback=tick)  # 50ms timer period

# Main Loop
while True:
    
    result = client.process()
    process_event()

        