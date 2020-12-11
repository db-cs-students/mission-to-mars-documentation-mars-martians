radio.set_group(127)
def on_forever():
    led.toggle(4, 4)
    radio.send_value("x", input.acceleration(Dimension.X))
    radio.send_value("y", input.acceleration(Dimension.Y))
    radio.send_value("z", input.acceleration(Dimension.Z))
basic.forever(on_forever)
