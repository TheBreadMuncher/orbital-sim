from math import pi, sqrt, sin, cos, radians

# Constants
G = 6.67430e-11       # Universal gravitational constant (m^3 kg^-1 s^-2)
M_EARTH = 5.972e24    # Mass of Earth (kg)
R_EQUATOR = 6378137   # Equatorial radius in meters
R_POLAR = 6356752     # Polar radius in meters

def earth_radius_at_latitude(latitude_deg):
    """
    Calculate local Earth radius at a given latitude using the WGS-84 ellipsoid formula.
    
    Parameters:
        latitude_deg (float): Latitude in degrees (-90 to 90)
    
    Returns:
        float: Local Earth radius in meters
    """
    lat_rad = radians(latitude_deg)
    # Ellipsoid approximation formula for radius at latitude
    a = R_EQUATOR
    b = R_POLAR
    numerator = (a**2 * cos(lat_rad))**2 + (b**2 * sin(lat_rad))**2
    denominator = (a * cos(lat_rad))**2 + (b * sin(lat_rad))**2
    radius = sqrt(numerator / denominator)
    return radius

def calculate_orbit(altitude_km, latitude_deg):
    """
    Calculate orbital radius and period using Kepler's Third Law.
    
    Parameters:
        altitude_km (float): Altitude above sea level in km
        latitude_deg (float): Latitude of location in degrees
    
    Returns:
        tuple: (orbital_radius_m, orbital_period_sec)
    """
    # Convert altitude to meters
    altitude_m = altitude_km * 1000
    
    # Local Earth radius at given latitude
    local_radius = earth_radius_at_latitude(latitude_deg)
    
    # Orbital radius = local radius + altitude
    orbital_radius = local_radius + altitude_m
    
    # Orbital period using Kepler's Third Law
    orbital_period_sec = 2 * pi * sqrt(orbital_radius**3 / (G * M_EARTH))
    
    return orbital_radius, orbital_period_sec

if __name__ == "__main__":
    # Example: ISS at 400 km altitude near equator (~0° latitude)
    altitude = 400       # km
    latitude = 0         # degrees
    radius, period_sec = calculate_orbit(altitude, latitude)
    period_hr = period_sec / 3600

    print(f"Altitude: {altitude} km")
    print(f"Latitude: {latitude}°")
    print(f"Orbital Radius: {radius/1000:.2f} km")
    print(f"Orbital Period: {period_hr:.2f} hours")
