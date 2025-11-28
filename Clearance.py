class Clearance:
    def __init__(self):
        self.hole_dia = float(input("Please enter the diameter of Hole "))
        self.ll_hole = float(input("Please enter the LowerLimit of Hole "))
        self.up_hole = float(input("Please enter the UpperLimit of Hole "))
        self.shaft_dia = float(input("Please enter the diameter of Shaft "))
        self.ll_shaft = float(input("Please enter the LowerLimit of Shaft "))
        self.up_shaft = float(input("Please enter the UpperLimit of Shaft "))
        choice = int(input("Enter 0 for Minimum Clearance, 1 for Maximum Clearance: "))

        if choice == 0:
            print("Minimum Clearance:", self.minimum_clearance())
        else:
            print("Maximum Clearance:", self.maximum_clearance())

    def minimum_clearance(self):
        return self.ll_hole - self.up_shaft

    def maximum_clearance(self):
        return self.up_hole - self.ll_shaft

Clearance()
