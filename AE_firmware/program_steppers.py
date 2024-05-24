import machine
import time
import sys

###############################################################################
# Settings

# Initialize SPI
spi = machine.SPI(0,
                  baudrate=1000000,
                  polarity=1,
                  phase=1,
                  bits=8,
                  firstbit=machine.SPI.MSB,
                  sck=machine.Pin(18),
                  mosi=machine.Pin(19),
                  miso=machine.Pin(16))


# Define the SS (Slave Select) pins for each TMC2660 device
ss_pin1 = machine.Pin(17, machine.Pin.OUT)  # Example SS pin for device 1, using Pin 5
ss_pin2 = machine.Pin(20, machine.Pin.OUT)  # Example SS pin for device 2, using Pin 6
ss_pin3 = machine.Pin(21, machine.Pin.OUT)  # Example SS pin for device 3, using Pin 7
ss_pin4 = machine.Pin(22, machine.Pin.OUT)  # Example SS pin for device 3, using Pin 7
ss_pin5 = machine.Pin(23, machine.Pin.OUT)  # Example SS pin for device 3, using Pin 7

# Create a list of SS pins
ss_pins = [ss_pin1, ss_pin2, ss_pin3, ss_pin4, ss_pin5]

drvctrl = bytes([0x00, 0x00, 0x07])
chopconf = bytes([0x08, 0x05, 0x11])
smarten = bytes([0x0A, 0x60, 0x61])
sgsconf = bytes([0x0D, 0x3F, 0x1F])
drvconf = bytes([0x0E, 0xA3, 0x10])

registers = [drvctrl, chopconf, smarten, sgsconf, drvconf]

for ss_pin in ss_pins:
    # Configure SS pin as an output and set it to high
    ss_pin.value(1)
    
time.sleep_ms(1)

for ss_pin in ss_pins:
    # Enable SPI for the current device
    for reg in registers:
        ss_pin.value(0)
        time.sleep_ms(1)
        spi.write(reg)
        time.sleep_ms(1)
        ss_pin.value(1)
        time.sleep_ms(1)

spi.deinit()  # Deinitialize SPI after configuration
print('steppers initialized')