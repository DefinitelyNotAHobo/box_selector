# Database list of all boxes we keep in stock.
# In this test case, It's the boxes used for Pro-M kit + a few additional for more accurate testing

from dataclasses import dataclass
@dataclass
class BoxDimensions:
    width: float
    length: float
    height: float

if __name__ == "__main__":
    BOX_6_6_24 = BoxDimensions(width=6, length=6, height=24)
    print(BOX_6_6_24)
    print(BOX_6_6_24.width)
    print(BOX_6_6_24.length)
    print(BOX_6_6_24.height)

    BOX_22_22_4 = BoxDimensions(width=22, length=22, height=4)
    print(BOX_22_22_4)
    print(BOX_22_22_4.width)
    print(BOX_22_22_4.length)
    print(BOX_22_22_4.height)

    BOX_12_10_8 = BoxDimensions(width=12, length=10, height=8)
    print(BOX_12_10_8)
    print(BOX_12_10_8.width)
    print(BOX_12_10_8.length)
    print(BOX_12_10_8.height)

    BOX_8_8_36 = BoxDimensions(width=8, length=8, height=36)
    print(BOX_8_8_36)
    print(BOX_8_8_36.width)
    print(BOX_8_8_36.length)
    print(BOX_8_8_36.height)

    BOX_40_6_1 = BoxDimensions(width=40, length=6, height=1)
    print(BOX_40_6_1)
    print(BOX_40_6_1.width)
    print(BOX_40_6_1.length)
    print(BOX_40_6_1.height)

    BOX_54_24_1 = BoxDimensions(width=54, length=24, height=1)
    print(BOX_54_24_1)
    print(BOX_54_24_1.width)
    print(BOX_54_24_1.length)
    print(BOX_54_24_1.height)

    BOX_60_8_1 = BoxDimensions(width=60, length=8, height=1)
    print(BOX_60_8_1)
    print(BOX_60_8_1.width)
    print(BOX_60_8_1.length)
    print(BOX_60_8_1.height)

    # Not part of this auto program. Added for testing phase
    BOX_36_18_18 = BoxDimensions(width=36, length=18, height=18)
    print(BOX_36_18_18)
    print(BOX_36_18_18.width)
    print(BOX_36_18_18.length)
    print(BOX_36_18_18.height)

    # Not part of this auto program. Added for testing phase
    BOX_10_10_56 = BoxDimensions(width=10, length=10, height=56)
    print(BOX_10_10_56)
    print(BOX_10_10_56.width)
    print(BOX_10_10_56.length)
    print(BOX_10_10_56.height)

    # Not part of this auto program. Added for testing phase
    BOX_6_6_48 = BoxDimensions(width=6, length=6, height=48)
    print(BOX_6_6_48)
    print(BOX_6_6_48.width)
    print(BOX_6_6_48.length)
    print(BOX_6_6_48.height)
    
    # Not part of this auto program. Added for testing phase
    BOX_4_4_9 = BoxDimensions(width=4.3, length=4.3, height=9.6)
    print(BOX_4_4_9)
    print(BOX_4_4_9.width)
    print(BOX_4_4_9.length)
    print(BOX_4_4_9.height)



# Ideally we can take a size input and loop through boxes in inventory to find and output the best box size.
# To further break it down, I'm going to do this step by step:
# 1. Iterate through the box variables and return all of them that have a width greater than input width
# 2. Iterate through the box variables and return all of them that have a length greater than input length
# 3. Iterate through the box variables and return all of them that have a height greater than input height

def box_filter(self):
    x = input('Enter part width: ')
    y = input('Enter part length: ')
    z = input('Enter part height: ')
    
# 4. Nest those results within scope variables and return only the variables that matched all three.