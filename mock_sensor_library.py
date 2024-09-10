import random

class MockTemperatureSensor:
    def __init__(self):
        # Initialize with a list of predefined temperature values
        self.temperatures = [20.5, 22.0, 24.1, 19.8, 23.3]
        self.index = 0

    def read_temperature(self):
        # Return a temperature value from the list, cycling through them
        temperature = self.temperatures[self.index]
        self.index = (self.index + 1) % len(self.temperatures)
        return temperature

class MockFlowSensor:
    def __init__(self):
        # Initialize with a range of flow rates
        self.flow_rates = [1.0, 3.5, 5.0, 7.2, 9.8]
        self.index = 0

    def read_flow_rate(self):
        # Return a flow rate value from the list, cycling through them
        flow_rate = self.flow_rates[self.index]
        self.index = (self.index + 1) % len(self.flow_rates)
        return flow_rate

class MockColorSensor:
    def __init__(self):
        # Initialize with a list of predefined colors
        self.colors = ["Red", "Green", "Blue", "Yellow", "White", "Black"]
        self.index = 0

    def read_color(self):
        # Return a color from the list, cycling through them
        color = self.colors[self.index]
        self.index = (self.index + 1) % len(self.colors)
        return color