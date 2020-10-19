# Database list of all boxes we keep in stock.
# In this test case, It's the boxes used for Pro-M kit

from dataclasses import dataclass
@dataclass
class BoxDimensions:
    width: int
    height: int
    depth: int

if __name__ == "__main__":
    # BOX_6_6_24 = (6, 6, 24)
    BOX_6_6_24 = BoxDimensions(width=6, height=6, depth=24)
    print(BOX_6_6_24)
    print(BOX_6_6_24.width)
    print(BOX_6_6_24.height)
    print(BOX_6_6_24.depth)

    # BOX_22_22_4 = (22, 22, 4)
    BOX_22_22_4 = BoxDimensions(width=22, height=22, depth=4)
    print(BOX_22_22_4)
    print(BOX_22_22_4.width)
    print(BOX_22_22_4.height)
    print(BOX_22_22_4.depth)

    # BOX_12_10_8 = (12, 10, 8)
    BOX_12_10_8 = BoxDimensions(width=12, height=10, depth=8)
    print(BOX_12_10_8)
    print(BOX_12_10_8.width)
    print(BOX_12_10_8.height)
    print(BOX_12_10_8.depth)

    # BOX_8_8_36 = (8, 8, 36)
    BOX_8_8_36 = BoxDimensions(width=8, height=8, depth=36)
    print(BOX_8_8_36)
    print(BOX_8_8_36.width)
    print(BOX_8_8_36.height)
    print(BOX_8_8_36.depth)

    # BOX_40_6_1 = (40, 6, 1)
    BOX_40_6_1 = BoxDimensions(width=40, height=6, depth=1)
    print(BOX_40_6_1)
    print(BOX_40_6_1.width)
    print(BOX_40_6_1.height)
    print(BOX_40_6_1.depth)

    # BOX_54_24_1 = (54, 24, 1)
    BOX_54_24_1 = BoxDimensions(width=54, height=24, depth=1)
    print(BOX_54_24_1)
    print(BOX_54_24_1.width)
    print(BOX_54_24_1.height)
    print(BOX_54_24_1.depth)

    # BOX_60_8_1 = (60, 8, 1)
    BOX_60_8_1 = BoxDimensions(width=60, height=8, depth=1)
    print(BOX_60_8_1)
    print(BOX_60_8_1.width)
    print(BOX_60_8_1.height)
    print(BOX_60_8_1.depth)



# Ideally we can take a size input and loop through boxes in inventory to find and output the best box size.
