import sys
from haptic_driver import hapticDriver

hptc = hapticDriver(float(sys.argv[1]), float(sys.argv[2]))

while True:
    inp = input("write vibration message:")
    hptc.write_message(inp)
