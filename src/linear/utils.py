import os.path

#extracts the number from a string
def extract_number(term):
    # Remove 'x1' or 'x2' from the term
    term = term.replace('x1', '').replace('x2', '')

    # If the term is empty, assume coefficient is 1
    if term == '':
        return 1

    # If the term is just '-', assume coefficient is -1
    if term == '-':
        return -1

    # Otherwise, parse the coefficient
    return int(term)

def handle_bounds(constraint):
    constraint = constraint.split(" ")
    tmp_x = constraint[0]

    #if there is comma -> both x and y have the same bounds
    if tmp_x != "x1":
        upper_bound = None
        lower_bound = None
        for i in range(1, len(constraint)):
            if constraint[i] == ">=":
                lower_bound = int(constraint[i+1])
            elif constraint[i] == "<=":
                upper_bound = int(constraint[i+1])

        return [lower_bound, upper_bound]



def handle_min_max(constraint):
    constraint = constraint.split(" ")
    if constraint[0] != "min" and constraint[0] != "max":
        raise ValueError("Invalid constraint type. Must be either 'min' or 'max'")

    #if the constraint is a maximization problem, we need to invert the final result
    invert = constraint[0] == "max"

    #extract the coefficients of the objective function
    x = extract_number(constraint[1])
    y = extract_number(constraint[2])

    if invert:
        x = -x
        y = -y
    return [x,y], invert


def numberize_constraint(constraint, invert=False):
    #split in a list of strings
    constraint = constraint.split(" ")

    #remove \n from the last element
    constraint[3] = constraint[3].rstrip("\n")

    #remove the ">=" or "<=" from the constraint
    constraint.pop(2)

    #convert the strings to integers and invert the constraint if needed
    for i in range(3):
        constraint[i] = extract_number(constraint[i])
        constraint[i] = int(constraint[i]) if not invert else -int(constraint[i])


    return constraint


#reads from the file,inverts if needed and returns a list of constraints
def read_data():
    if not os.path.exists('constraints.txt'):
        raise FileNotFoundError("File constraints.txt not found")

    with open('constraints.txt', 'r') as file:
        data = file.readlines()

    #handle the first line(c is the objective function coefficients, invert is a boolean that tells we need to invert the final result)
    c, invert = handle_min_max(data[0])
    data.pop(0)

    #x,y bounds
    bounds = handle_bounds(data[len(data)-1])
    data.pop(len(data)-1)

    #convert the constraints to a list of lists
    constraints = []
    #numbers on the right side of the constraints
    numbers = []
    for constraint in data:

        #boolean to check if we need to invert the constraint
        needs_invert = ">= " in constraint
        constraint = numberize_constraint(constraint, needs_invert)

        #pop the number from the end of the constraint
        number = constraint.pop(2)
        numbers.append(number)
        constraints.append(constraint)

    return c, constraints, numbers, bounds, invert