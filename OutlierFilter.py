class OutlierFilter:
    def __init__(self):
        self.lastAngle = 0.0
        self.muteCounter = 0

    def run(self, pilot_angle):
        tmp_angle = float(pilot_angle)
        self.muteCounter += 1
        if self.muteCounter >= 2:
            if abs(tmp_angle - self.lastAngle) >= 0.5:
                pilot_angle = self.lastAngle
                self.muteCounter = 0
            else:
                self.lastAngle = tmp_angle
        else:
            self.lastAngle = tmp_angle
        return pilot_angle

filter = OutlierFilter()
while True:
    angle = input("Enter pilot angle: ")
    print(filter.run(angle))
