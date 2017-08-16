class Celsius:
    def __init__(self, temperature=0):
        self._temperature = temperature

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, temperature):
        if temperature < -273.15:
            raise ValueError('Temperature cannot be lower than -273.15⁰ celsius.')

        self._temperature = temperature


c = Celsius(5)
c.temperature = -273.15
print(c.temperature)
