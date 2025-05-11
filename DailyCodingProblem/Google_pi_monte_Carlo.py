"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.

Hint: The basic equation of a circle is x2 + y2 = r2.
"""

"""
The Algorithm 
1. Initialize circle_points, square_points and interval to 0. 
2. Generate random point x. 
3. Generate random point y. 
4. Calculate d = x*x + y*y. 
5. If d <= 1, increment circle_points. 
6. Increment square_points. 
7. Increment interval. 
8. If increment < NO_OF_ITERATIONS, repeat from 2. 
9. Calculate pi = 4*(circle_points/square_points). 
10. Terminate.
"""

def estimate_pi(num_samples: int) -> float:
    import random

    circle_points = 0
    square_points = 0

    for _ in range(num_samples):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        d = x * x + y * y

        if d <= 1:
            circle_points += 1
        square_points += 1

    pi_estimate = 4 * (circle_points / square_points)
    return round(pi_estimate, 3)

if __name__ == "__main__":
    num_samples = 1000000  # You can adjust the number of samples for more accuracy
    pi_value = estimate_pi(num_samples)
    print(f"Estimated value of π: {pi_value}")