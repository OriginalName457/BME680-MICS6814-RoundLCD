Raspberry Pi Pico Environmental Monitor
This project is designed to provide real-time environmental monitoring using a Raspberry Pi Pico with Breakout MICS6814 Gas sensor and Breakout BME68X environmental sensor. The sensor readings are displayed on a round LCD screen.


Installation
Ensure you have MicroPython installed on your Raspberry Pi Pico. If you haven't, follow the guide here.


Install the necessary Python libraries for the breakout sensors and LCD display. For MicroPython, you can download them from the official Pimoroni repository here.


Clone or download this repository to your local system.


Upload the Python script and the necessary libraries onto your Raspberry Pi Pico. You can use a tool such as rshell or Thonny Python IDE for this.


Usage
Connect the Raspberry Pi Pico to a power source.


The script will run automatically, displaying environmental sensor readings on the LCD screen. The display will switch between sensor readings every 15 seconds.


Sensors
Breakout MICS6814 Gas sensor: Measures Oxidising gases, Reducing gases, and Ammonia (NH3).


Breakout BME68X environmental sensor: Measures temperature, pressure, humidity, and gas resistance.


Display
The Round LCD display will show readings from each sensor with the following format:


MICS6814 Readings: Oxidising, Reducing, and NH3 levels are shown with corresponding values and visual histogram.


BME68X Readings: Temperature, Pressure, Humidity, Gas resistance, and Heater status are displayed.