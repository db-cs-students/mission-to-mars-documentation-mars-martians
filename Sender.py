radio.set_group(127)
def on_forever():
    radio.send_value("x", input.acceleration(Dimension.X))
basic.forever(on_forever)
