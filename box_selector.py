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


def show_boxes():
    print("Boxes in inventory: ")
    for box in boxes:
        print("{}in x {}in x {}in".format(box.width, box.length, box.height))
    return master_loop()


# Add a function to calculate dimensional weight. Round up to nearest inch then use (length x width x height / 139)
def dim_weight():
    dw_w = math.ceil(float(input("Enter box width: ")))
    dw_l = math.ceil(float(input("Enter box length: ")))
    dw_h = math.ceil(float(input("Enter box height: ")))
    dw_convert = math.ceil((dw_w * dw_l * dw_h) / 139)
    print("Dimensional weight is: {} lbs".format(dw_convert))
    return master_loop()


# Take inch input, convert to millimeters and output result
def in_to_mm():
    in_c = float(input('Enter size in inches to convert to millimeters: '))
    in_convert = in_c * 25.4
    print("{} millimeters".format(in_convert))
    return con_loop()


# Take millimeter input, convert to inches and output result
def mm_to_in():
    mm_c = float(input('Enter size in millimeters to convert to inches: '))
    mm_convert = mm_c / 25.4
    print("{} inches".format(mm_convert))
    return con_loop()

# Take gram input, convert to ounces and output results
def g_to_oz():
    g_c = float(input('Enter weight in grams to convert to ounces: '))
    g_convert = g_c / 28.35
    print("{} oz".format(g_convert))
    return con_loop()

# Take ounce input, convert to grams and output results
def oz_to_g():
    oz_c = float(input('Enter weight in ounces to convert to grams: '))
    oz_convert = oz_c * 28.35
    print("{} grams".format(oz_convert))
    return con_loop()

# Take gram input, convert to pounds and output results
def g_to_lb():
    lb_c = float(input('Enter weight in grams to convert to pounds: '))
    lb_convert = lb_c / 453.59
    print("{} lbs".format(lb_convert))
    return con_loop()


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


def con_loop():
    while True:
        print("Conversion Tools")
        print("(1) For Millimeter to Inch Converter")
        print("(2) For Inch to Millimeter Converter")
        print("(3) For Gram to Ounce Converter")
        print("(4) For Ounce to Gram Converter")
        print("(5) For Gram to Pound Converter")
        dim_nav = input("Type the number of your selection, (B) to go back or (Q) to Quit: ").lower()
        if dim_nav == '1':
            return mm_to_in()
        elif dim_nav == '2':
            return in_to_mm()
        elif dim_nav == '3':
            return g_to_oz()
        elif dim_nav == '4':
            return oz_to_g()
        elif dim_nav == '5':
            return g_to_lb()
        elif dim_nav == 'b':
            return master_loop()
        elif dim_nav == 'q':
            break
        else:
            print('Not a valid option')


# Master loop to direct to all implemented functions
def master_loop():
    while True:
        print("Welcome to Boxtopia!")
        print("(1) For Box Selection")
        print("(2) For Conversion Tools")
        print("(3) For Dimensional Weight Calculator")
        print("(4) For Box Inventory")
        nav = input("Type the number of your selection or (Q) to Quit: ").lower()
        if nav == '1':
            return take_dim('self')
        elif nav == '2':
            return con_loop()
        elif nav == '3':
            return dim_weight()
        elif nav == '4':
            return show_boxes()
        elif nav == 'q':
            break
        else:
            print('Not a valid option')

master_loop()
