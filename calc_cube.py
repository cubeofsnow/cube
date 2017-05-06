
if __name__ == "__main__":
    lb_per_cubic_foot = 62.43
    ft_per_meter = 3.28084

    # density of snow compared to water
    snow_density = 0.8
    # how many feet is cube
    cube_dimension = 6.5
    # the number of feet on each side of cube
    east = 1.0
    west = 1.0
    north = 1.0
    south = 1.0
    # the number of feet on top of cube
    top = 1.5
    snow_volume_meters = (cube_dimension**3) - (cube_dimension-east-west) * \
        (cube_dimension-north-south)*(cube_dimension-top)
    snow_volume_feet = snow_volume_meters * (ft_per_meter)**3
    print snow_volume_meters, 'cubic meters of snow'
    print snow_volume_feet, 'cubic feet of snow'
    print snow_volume_meters * lb_per_cubic_foot*snow_density, 'pounds of snow'
