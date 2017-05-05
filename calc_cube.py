
if __name__ == "__main__":
    snow_density = 0.9
    cube_dimension = 6.5
    east = 1.25
    west = 1.25
    north = 1.25
    south = 1.25
    top = 1.25
    snow_volume = (cube_dimension**3) - (cube_dimension-east-west) * \
        (cube_dimension-north-south)*(cube_dimension-top)
    lb_per_cubic_foot = 62.43
    print snow_volume * lb_per_cubic_foot*snow_density

