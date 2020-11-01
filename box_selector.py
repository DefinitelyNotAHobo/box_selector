# Database list of all boxes we keep in stock.
# In this test case, It's the boxes used for Pro-M kit + a few additional for more accurate testing

# Add a function to calculate dimensional weight. Round to nearest inch then use (length x width x height / 139)

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


# Ideally we can take a size input and loop through boxes in inventory to find and output the best box size.
# To further break it down, I'm going to do this step by step:
# 1. Iterate through the box variables and return all of them that have a width greater than input width
# 2. Iterate through the box variables and return all of them that have a length greater than input length
# 3. Iterate through the box variables and return all of them that have a height greater than input height
# 4. Nest those results within scope variables and return only the variables that matched all three.

def box_filter():
    fit_w = []
    fit_l = []
    fit_h = []

    y_dim = float(input('Enter part width in inches: '))
    for box in boxes:
        if box.width > y_dim:
            fit_w.append(box)

    x_dim = float(input('Enter part length in inches: '))
    for box in boxes:
        if box.length > x_dim:
            fit_l.append(box)

    z_dim = float(input('Enter part height in inches: '))
    for box in boxes:
        if box.height > z_dim:
            fit_h.append(box)

    y_set = set(fit_w) 
    x_set = set(fit_l)
    z_set = set(fit_h)

    set1 = y_set.intersection(x_set)
    result_set = set1.intersection(z_set)
    final_list = list(result_set)

    print(final_list)

# This is an attempt at the previous function but checking if ANY dimension of each box will fit the input dimensions
# Unsurprisingly it returns many more results that aren't narrowed down in any way and also that wouldn't actually
# fit the part since there's no logic to disqualify a result if one dimension doesn't fit
def box_filter2():
    fit_w = []
    fit_l = []
    fit_h = []

    y_dim = float(input('Enter part width in inches: '))
    for box in boxes:
        if box.height > y_dim:
            fit_w.append(box)
        elif box.width > y_dim:
            fit_w.append(box)
        elif box.length > y_dim:
            fit_w.append(box)

    x_dim = float(input('Enter part length in inches: '))
    for box in boxes:
        if box.height > x_dim:
            fit_l.append(box)
        elif box.width > x_dim:
            fit_l.append(box)
        elif box.length > x_dim:
            fit_l.append(box)

    z_dim = float(input('Enter part height in inches: '))
    for box in boxes:
        if box.height > z_dim:
            fit_h.append(box)
        elif box.width > z_dim:
            fit_h.append(box)
        elif box.length > z_dim:
            fit_h.append(box)

    y_set = set(fit_w) 
    x_set = set(fit_l)
    z_set = set(fit_h)

    set1 = y_set.intersection(x_set)
    result_set = set1.intersection(z_set)
    final_list = list(result_set)

    print(final_list)

box_filter()

box_filter2()