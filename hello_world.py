from haptic_driver import hapticDriver

hptc = hapticDriver(4,0.7,True)

message = "hello world from carlos and eric in their living room"
alphabet = "a b c d e f g  h i j k  lmnop  q r s  t u v  w x  y  z"
hptc.write_message(message)
