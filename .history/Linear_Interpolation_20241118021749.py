def compute_line_interpolation(times: list[float], temps: list[float]):
    """
    Compute piecewise linear interpolation between consecutive points.
    
    Args:
        times (list[float]): List of time values.
        temps (list[float]): List of temperature values.
    
    Returns:
        tuple: List of slopes and intercepts for each segment.
    """
    times_np = np.array(times)
    temps_np = np.array(temps)
    
    slopes = []
    intercepts = []

    if len(times_np) == len(temps_np) and len(times_np) > 1:
        # Calculate the differences in temps and times
        delta_t = times_np[1:] - times_np[:-1]
        delta_y = temps_np[1:] - temps_np[:-1]

        # Calculate slopes (m = Δy / Δx)
        slopes = delta_y / delta_t

        # Calculate y-intercepts (y_intercept = y - mx)
        intercepts = temps_np[:-1] - slopes * times_np[:-1]

    return slopes, intercepts
