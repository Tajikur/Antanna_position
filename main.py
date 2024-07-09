import math
def calculate_elevation_azimuth(S, N, L):
    # Convert degrees to radians for trigonometric functions
    S_rad = math.radians(S)
    N_rad = math.radians(N)
    L_rad = math.radians(L)
    
    # Calculate G in radians
    G = S_rad - N_rad
    
    # Calculate elevation angle (E)
    numerator = math.cos(G) * math.cos(L_rad) - 0.1512
    denominator = math.sqrt(1 - (math.cos(G) * math.cos(L_rad))**2)
    E = math.atan(numerator / denominator)
    
    # Convert elevation angle to degrees
    E_deg = math.degrees(E)
    
    # Calculate azimuth angle (A)
    tan_G = math.tan(G)
    sin_L = math.sin(L_rad)
    A = math.atan(tan_G / sin_L)
    
    # Convert azimuth angle to degrees
    A_deg = math.degrees(A)
    
    return E_deg, A_deg

# Example values
satellite_longitude = 100  # S
site_longitude = 80       # N
site_latitude = 45        # L

elevation, azimuth = calculate_elevation_azimuth(satellite_longitude, site_longitude, site_latitude)

print(f"Elevation angle: {elevation:.2f} degrees")
print(f"Azimuth angle: {azimuth:.2f} degrees")
