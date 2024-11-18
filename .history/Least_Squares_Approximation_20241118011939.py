def least_squares_approximation(times: list[float], temps: list[float]):
    """
    Compute the least squares approximation for a linear relationship
    between times and temps using the (X^T X)^-1 X^T Y method.

    Args:
        times (list[float]): List of time values (independent variable).
        temps (list[float]): List of temperature values (dependent variable).

    Returns:
        tuple: Coefficients (slope, intercept) of the least squares line.
    """
    times_np = np.array(times)
    temps_np = np.array(temps)
    
    if len(times_np) != len(temps_np) or len(times_np) < 2:
        raise ValueError("Input lists must have the same length and contain at least two points.")
    
    # Construct the design matrix X
    X = np.vstack([times_np, np.ones(len(times_np))]).T
    
    # Compute the least squares solution
    coefficients = np.linalg.inv(X.T @ X) @ X.T @ temps_np
    
    return coefficients[0], coefficients[1]  # slope, intercept