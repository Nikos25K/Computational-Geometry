from scipy.optimize import linprog
from utils import read_data


if __name__ == "__main__":
    c, constraints, numbers, bounds, invert = read_data()

    res = linprog(c, A_ub=constraints, b_ub=numbers, bounds=bounds, method='highs', options={"disp": True})

    # Print the result
    if res.success:
        print("Optimal solution:", res.x)
        res_fun = res.fun if not invert else -res.fun

        # Since we negated the coefficients for maximization, we need to negate the result again
        print("Optimal value:", res_fun)
    else:
        print("No solution found.")