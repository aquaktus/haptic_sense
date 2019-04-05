from haptic_driver import hapticDriver

hptc = hapticDriver(4,0.3,True)

message = "hello world"
hptc.write_message(message)