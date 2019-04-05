from haptic_driver import hapticDriver

hptc = hapticDriver(char_frequency=4, char_vibration_time=0.3, debug=True)

message = "hello world"
hptc.write_message(message)