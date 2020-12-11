radio.set_group(127)
def on_forever():
    radio.send_number(input.acceleration(Dimension.X))
basic.forever(on_forever)
