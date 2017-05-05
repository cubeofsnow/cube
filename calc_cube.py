
if __name__ == "__main__":
    # density of snow compared to water
    snow_density = 0.9
    # how many feet is cube
    cube_dimension = 6.5
    # the number of feet on each side of cube
    east = 1.25
    west = 1.25
    north = 1.25
    south = 1.25
    # the number of feet on top of cube
    top = 1.25
    snow_volume = (cube_dimension**3) - (cube_dimension-east-west) * \
        (cube_dimension-north-south)*(cube_dimension-top)
    lb_per_cubic_foot = 62.43
    print snow_volume * lb_per_cubic_foot*snow_density

