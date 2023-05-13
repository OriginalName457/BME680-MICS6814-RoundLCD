import time
from pimoroni_i2c import PimoroniI2C
from breakout_mics6814 import BreakoutMICS6814
from breakout_bme68x import BreakoutBME68X
from picographics import PicoGraphics, DISPLAY_ROUND_LCD_240X240

PINS_BREAKOUT_GARDEN = {"sda": 4, "scl": 5}
PINS_PICO_EXPLORER = {"sda": 20, "scl": 21}

DISPLAY_UPDATE_INTERVAL = 15

i2c = PimoroniI2C(**PINS_BREAKOUT_GARDEN)
gas = BreakoutMICS6814(i2c)
bme = BreakoutBME68X(i2c)

display = PicoGraphics(display=DISPLAY_ROUND_LCD_240X240)
display.set_backlight(1.0)

BLACK = display.create_pen(0, 0, 0)
WHITE = display.create_pen(255, 255, 255)
RED = display.create_pen(255, 0, 0)
BLUE = display.create_pen(0, 0, 255)
GREEN = display.create_pen(0, 255, 0)

def draw_mics_data():
    for _ in range(DISPLAY_UPDATE_INTERVAL):
        display.set_pen(BLACK)
        display.clear()

        oxd = gas.read_oxidising()
        red = gas.read_reducing()
        nh3 = gas.read_nh3()

        max_val = max(oxd, red, nh3)

        display.set_pen(WHITE)
        display.text("MICS6814 Readings", 20, 20, 220)
        display.text("OX: {:.2f}".format(oxd), 20, 60, 220)
        display.text("Red: {:.2f}".format(red), 20, 100, 220)
        display.text("NH3: {:.2f}".format(nh3), 20, 140, 220)

        display.set_pen(RED)
        display.rectangle(20, 80, int(180 * oxd / max_val), 15)
        display.set_pen(BLUE)
        display.rectangle(20, 120, int(180 * red / max_val), 15)
        display.set_pen(GREEN)
        display.rectangle(20, 160, int(180 * nh3 / max_val), 15)

        display.update()
        time.sleep(1)

def draw_bme_data():
    for _ in range(DISPLAY_UPDATE_INTERVAL):
        display.set_pen(BLACK)
        display.clear()

        temperature, pressure, humidity, gas, status, _, _ = bme.read()
        heater = "Stable" if status & 0x80 else "Unstable"

        display.set_pen(WHITE)
        display.text("BME68X Readings", 30, 30, 220)
        display.text("Temp: {:.2f} C".format(temperature), 30, 55, 220)
        display.text("Pressure: {:.2f} Pa".format(pressure), 30, 80, 220)
        display.text("Humidity: {:.2f} %".format(humidity), 30, 105, 220)
        display.text("Gas: {:.2f} Ohms".format(gas), 30, 130, 220)
        display.text("Heater: {}".format(heater), 30, 155, 220)

        display.update()
        time.sleep(1)


def main():
    while True:
        draw_mics_data()
        draw_bme_data()


if __name__ == "__main__":
    main()

