"""
Script to calculate short circuit faults
"""
import math
import cmath


class FaultsCalculator():
    """
    Main class
    """
    def __init__(self):
        """
        Initialization
        """
        self.nominal_voltage = 20e3
        self.ea1 = self.nominal_voltage/math.sqrt(3)
        self.z_1 = 17 + 1j
        self.z_2 = 17 + 1j
        self.z_0 = 17 + 1j
        self.z_f = 0 + 0j
        self.alpha = cmath.rect(1, math.radians(120))

    def single_phase_fault_solid(self):
        """
        Method to calculate single phase short circuit current
        """
        print("Single Phase Fault Solid")
        try:
            fault_current = \
                3*self.ea1 / (self.z_0 + self.z_1 + self.z_2)
            fault_current, angle = cmath.polar(fault_current)
        except ZeroDivisionError:
            print("Error calculating current")

        print(f"Current: {fault_current} A at {math.degrees(angle)} degrees\n")

    def single_phase_fault(self):
        """
        Method to calculate single phase short circuit current
        """
        print("Single Phase Fault")
        try:
            fault_current = \
                (3*self.ea1) / \
                (self.z_0 + self.z_1 + self.z_2 + 3*self.z_f)
            fault_current, angle = cmath.polar(fault_current)
        except ZeroDivisionError:
            print("Error calculating current")
        print(f"Current: {fault_current} A at {math.degrees(angle)} degrees\n")

    def three_phase_fault_solid(self):
        """
        Method to calculate single phase short circuit current
        """
        print("Three Phase Fault Solid")
        try:
            fault_current_a = \
                self.ea1 / \
                (self.z_1)
            fault_current_b = pow(self.alpha, 2) * fault_current_a
            fault_current_c = self.alpha * fault_current_a
            fault_current_a, angle_a = cmath.polar(fault_current_a)
            fault_current_b, angle_b = cmath.polar(fault_current_b)
            fault_current_c, angle_c = cmath.polar(fault_current_c)
        except ZeroDivisionError:
            print("Error calculating current")
        print(f"I: {fault_current_a} A at {math.degrees(angle_a)} degrees")
        print(f"I: {fault_current_b} A at {math.degrees(angle_b)} degrees")
        print(f"I: {fault_current_c} A at {math.degrees(angle_c)} degrees\n")

    def three_phase_fault(self):
        """
        Method to calculate single phase short circuit current
        """
        print("Three Phase Fault")
        try:
            fault_current_a = \
                self.ea1 / \
                (self.z_1 + self.z_f)
            fault_current_b = pow(self.alpha, 2) * fault_current_a
            fault_current_c = self.alpha * fault_current_a
            fault_current_a, angle_a = cmath.polar(fault_current_a)
            fault_current_b, angle_b = cmath.polar(fault_current_b)
            fault_current_c, angle_c = cmath.polar(fault_current_c)
        except ZeroDivisionError:
            print("Error calculating current")
        print(f"I: {fault_current_a} A at {math.degrees(angle_a)} degrees")
        print(f"I: {fault_current_b} A at {math.degrees(angle_b)} degrees")
        print(f"I: {fault_current_c} A at {math.degrees(angle_c)} degrees\n")

    def two_phase_fault_solid(self):
        """
        Method to calculate single phase short circuit current
        """
        print("Two Phase Fault Solid")
        try:
            fault_current_b = \
                ((-1j)*self.ea1*math.sqrt(3)) / (self.z_1 + self.z_2)
            fault_current_c = \
                ((1j)*self.ea1*math.sqrt(3)) / (self.z_1 + self.z_2)
            fault_current_b, angle_b = cmath.polar(fault_current_b)
            fault_current_c, angle_c = cmath.polar(fault_current_c)
        except ZeroDivisionError:
            print("Error calculating current")

        print(f"I: {fault_current_b} A at {math.degrees(angle_b)} degrees")
        print(f"I: {fault_current_c} A at {math.degrees(angle_c)} degrees\n")

    def two_phase_fault(self):
        """
        Method to calculate single phase short circuit current
        """
        print("Two Phase Fault")
        try:
            fault_current_b = \
                ((-1j)*self.ea1*math.sqrt(3)) / (self.z_1 + self.z_2 + self.z_f)
            fault_current_c = \
                ((1j)*self.ea1*math.sqrt(3)) / (self.z_1 + self.z_2 + self.z_f)
            fault_current_b, angle_b = cmath.polar(fault_current_b)
            fault_current_c, angle_c = cmath.polar(fault_current_c)
        except ZeroDivisionError:
            print("Error calculating current")

        print(f"I: {fault_current_b} A at {math.degrees(angle_b)} degrees")
        print(f"I: {fault_current_c} A at {math.degrees(angle_c)} degrees\n")

    def two_phase_grounding_fault(self):
        """
        Method to calculate single phase short circuit current
        """
        print("Two Phase Grounding Fault")
        try:
            fault_current_b = \
                ((-1j)*self.ea1*math.sqrt(3)*(self.z_0 + (3*self.z_f) - (self.alpha*self.z_2))) / ((self.z_1*self.z_2)+((self.z_1+self.z_2)*(self.z_0+(3*self.z_f))))
            fault_current_c = \
                ((1j)*self.ea1*math.sqrt(3)*(self.z_0 + (3*self.z_f) - (self.alpha*self.z_2))) / ((self.z_1*self.z_2)+((self.z_1+self.z_2)*(self.z_0+(3*self.z_f))))
            fault_current_b, angle_b = cmath.polar(fault_current_b)
            fault_current_c, angle_c = cmath.polar(fault_current_c)
        except ZeroDivisionError:
            print("Error calculating current")

        print(f"I: {fault_current_b} A at {math.degrees(angle_b)} degrees")
        print(f"I: {fault_current_c} A at {math.degrees(angle_c)} degrees\n")

    def two_phase_grounding_fault_solid(self):
        """
        Method to calculate single phase short circuit current
        """
        print("Two Phase Grounding Fault Solid")
        try:
            fault_current_b = \
                ((-1j)*self.ea1*math.sqrt(3)*(self.z_0 - (self.alpha*self.z_2))) / ((self.z_1*self.z_2)+((self.z_1+self.z_2)*(self.z_0)))
            fault_current_c = \
                ((1j)*self.ea1*math.sqrt(3)*(self.z_0  - (self.alpha*self.z_2))) / ((self.z_1*self.z_2)+((self.z_1+self.z_2)*(self.z_0)))
            fault_current_b, angle_b = cmath.polar(fault_current_b)
            fault_current_c, angle_c = cmath.polar(fault_current_c)
        except ZeroDivisionError:
            print("Error calculating current")

        print(f"I: {fault_current_b} A at {math.degrees(angle_b)} degrees")
        print(f"I: {fault_current_c} A at {math.degrees(angle_c)} degrees\n")

    def calculate_all(self):
        """
        Method to return all the faults
        """
        self.single_phase_fault()
        self.single_phase_fault_solid()
        self.three_phase_fault()
        self.three_phase_fault_solid()
        self.two_phase_fault()
        self.two_phase_fault_solid()
        self.two_phase_grounding_fault()
        self.two_phase_grounding_fault_solid()

    def calculate_solid(self):
        """
        Method to return only solid faults
        """
        self.single_phase_fault_solid()
        self.three_phase_fault_solid()
        self.two_phase_fault_solid()
        self.two_phase_grounding_fault_solid()


if __name__ == "__main__":
    print("Faults Calculator")
    FaultsCalculator().calculate_solid()
