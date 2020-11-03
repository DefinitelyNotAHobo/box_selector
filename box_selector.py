import pdb
import math
# Database list of all boxes we keep in stock.
# In this test case, It's the boxes used for Pro-M kit + a few additional for more accurate testing
# Eventually would like to capture box weight, but I can't add the functionality without adding box weight to every instance.

from dataclasses import dataclass
@dataclass(frozen=True)
class BoxDimensions:
    width: float
    length: float
    height: float

if __name__ == "__main__":
    BOX_6_6_24 = BoxDimensions(width=6, length=6, height=24)
    # print(BOX_6_6_24)
    # print(BOX_6_6_24.width)
    # print(BOX_6_6_24.length)
    # print(BOX_6_6_24.height)

    BOX_22_22_4 = BoxDimensions(width=22, length=22, height=4)

    BOX_12_10_8 = BoxDimensions(width=12, length=10, height=8)

    BOX_8_8_36 = BoxDimensions(width=8, length=8, height=36)

    BOX_40_6_1 = BoxDimensions(width=40, length=6, height=1)

    BOX_54_24_1 = BoxDimensions(width=54, length=24, height=1)

    BOX_60_8_1 = BoxDimensions(width=60, length=8, height=1)

    # Not part of this auto program. Added for testing phase
    BOX_36_18_18 = BoxDimensions(width=36, length=18, height=18)

    # Not part of this auto program. Added for testing phase
    BOX_10_10_56 = BoxDimensions(width=10, length=10, height=56)

    # Not part of this auto program. Added for testing phase
    BOX_6_6_48 = BoxDimensions(width=6, length=6, height=48)
    
    # Not part of this auto program. Added for testing phase
    BOX_4_4_9 = BoxDimensions(width=4.3, length=4.3, height=9.6)

boxes = (BOX_6_6_24, 
         BOX_22_22_4,
         BOX_12_10_8,
         BOX_8_8_36,
         BOX_40_6_1,
         BOX_54_24_1,
         BOX_60_8_1,
         BOX_36_18_18,
         BOX_10_10_56,
         BOX_6_6_48,
         BOX_4_4_9)

# Add a function to calculate dimensional weight. Round up to nearest inch then use (length x width x height / 139)
def dim_weight():
    dw_w = math.ceil(float(input("Enter box width: ")))
    dw_l = math.ceil(float(input("Enter box length: ")))
    dw_h = math.ceil(float(input("Enter box height: ")))
    dw_convert = math.ceil((dw_w * dw_l * dw_h) / 139)
    print("Dimensional weight is: {} lbs".format(dw_convert))
    return master_loop()

# Take millimeter input, convert to inches and output result
def mm_to_in():
    mm_c = float(input('Enter size in millimeters to convert to inches: '))
    mm_convert = mm_c / 25.4
    print("{} inches".format(mm_convert))
    return master_loop()


# Take dimensional input from user and store into variables
def take_dim(self):
    y_dim = float(input('Enter part width in inches: '))
    x_dim = float(input('Enter part length in inches: '))
    z_dim = float(input('Enter part height in inches: '))
    return box_filter(self, y_dim, x_dim, z_dim)

# Iterate user input through boxes in inventory to find all boxes that fit.
def box_filter(self, y_dim, x_dim, z_dim):
    fit_1 = []
    fit_2 = []
    fit_3 = []
    fit_4 = []

    # Logic to check possible box orientations
    for box in boxes:
        if box.width > y_dim and box.length > x_dim and box.height > z_dim:
            fit_1.append(box)
    
    for box in boxes:
        if box.length > y_dim and box.width > x_dim and box.height > z_dim:
            fit_2.append(box)

    for box in boxes:
        if box.height > y_dim and box.width > x_dim and box.length > z_dim:
            fit_3.append(box)

    for box in boxes:
        if box.length > y_dim and box.height > x_dim and box.width > z_dim:
            fit_4.append(box)

    # Convert results to sets that can be checked for intersections
    first_set = set(fit_1) 
    second_set = set(fit_2)
    third_set = set(fit_3)
    fourth_set = set(fit_4)

    # Check for results that are present in all 'fit' lists
    set1 = first_set.intersection(second_set)
    set2 = third_set.intersection(fourth_set)
    result_set = set1.intersection(set2)
    final_list = list(result_set)

    print(final_list)
    return master_loop()

# Master loop to direct to all implemented functions
def master_loop():
    while True:
        nav = input("Type (B) for Box selection, (C) for millimeter to inch Converter, (D) for Dimensional Weight Calculator, (Q)' to Quit: ").lower()
        if nav == 'b':
            return take_dim('self')
        elif nav == 'c':
            return mm_to_in()
        elif nav == 'd':
            return dim_weight()
        elif nav == 'q':
            break
        else:
            print('Not a valid option')

master_loop()
