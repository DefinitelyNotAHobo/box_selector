# Database list of all boxes we keep in stock.
# In this test case, It's the boxes used for Promaster

from dataclasses import dataclass
@dataclass
class BoxDimensions:
    width: int
    height: int
    depth: int

if __name__ == "__main__":
    BOX_6_6_24 = BoxDimensions(width=6, height=6, depth=24)
    print(BOX_6_6_24)
    print(BOX_6_6_24.width)
    print(BOX_6_6_24.height)
    print(BOX_6_6_24.depth)

# BOX_6_6_24 = (6, 6, 24)
# BOX_22_22_4 = (22, 22, 4)
# BOX_12_10_8 = (12, 10, 8)
# BOX_8_8_36 = (8, 8, 36)
# BOX_40_6_1 = (40, 6, 1)
# BOX_54_24_1 = (54, 24, 1)
# BOX_60_8_1 = (60, 8, 1)



# Ideally we can take a size input and loop through boxes in inventory to find and output the best box size.