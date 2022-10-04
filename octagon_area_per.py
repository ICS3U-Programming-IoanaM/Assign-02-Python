#!/usr/bin/env python3
# Copyright (c) 2022 Ioana Marinescu All rights reserved.
# Created By: Ioana Marinescu
#
# Date: Oct. 3, 2022
# calculates area and perimeter of an octagon


def main():
    # variables
    units = input("Enter units (cm, inches, mm, etc.): ")
    side_length = float(input("Enter side length: "))

    # calculations
    area = 2 * (1 + 2) * side_length**2
    perimeter = 8 * side_length

    # display results
    print(f"Area: {area:.2f}{units}^2")
    print(f"Perimeter: {perimeter:.2f}{units}")


if __name__ == "__main__":
    main()
