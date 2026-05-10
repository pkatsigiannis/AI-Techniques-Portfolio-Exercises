# Install library: 
# pip install python-constraint

from constraint import Problem, AllDifferentConstraint


def office_next_to(a, b):
    return abs(a - b) == 1


def solve():
    problem = Problem()

    modules = ["CS", "Mathematics", "Philosophy", "History", "M5"]
    research = ["AI", "ClimateChange", "QuantumPhysics", "Neuroscience", "MedievalLiterature"]
    cars = ["Tesla", "BMW", "Mercedes", "Audi", "Volvo"]
    universities = ["Oxford", "Cambridge", "Harvard", "MIT", "Stanford"]
    decor = ["Blue", "Green", "Red", "Yellow", "White"]
    drinks = ["Espresso", "HerbalTea", "GreenTea", "BlackCoffee", "D5"]

    variables = modules + research + cars + universities + decor + drinks

    problem.addVariables(variables, [1, 2, 3, 4, 5])

    problem.addConstraint(AllDifferentConstraint(), modules)
    problem.addConstraint(AllDifferentConstraint(), research)
    problem.addConstraint(AllDifferentConstraint(), cars)
    problem.addConstraint(AllDifferentConstraint(), universities)
    problem.addConstraint(AllDifferentConstraint(), decor)
    problem.addConstraint(AllDifferentConstraint(), drinks)

    problem.addConstraint(lambda cs, blue: cs == blue, ["CS", "Blue"])
    problem.addConstraint(lambda oxford, tesla: oxford == tesla, ["Oxford", "Tesla"])
    problem.addConstraint(lambda ai, espresso: ai == espresso, ["AI", "Espresso"])
    problem.addConstraint(lambda cambridge: cambridge == 1, ["Cambridge"])
    problem.addConstraint(office_next_to, ["BMW", "Green"])
    problem.addConstraint(lambda cc, tea: cc == tea, ["ClimateChange", "HerbalTea"])
    problem.addConstraint(lambda math, red: math == red, ["Mathematics", "Red"])
    problem.addConstraint(lambda mercedes, qp: mercedes == qp, ["Mercedes", "QuantumPhysics"])
    problem.addConstraint(lambda green_tea: green_tea == 3, ["GreenTea"])
    problem.addConstraint(office_next_to, ["Cambridge", "Yellow"])
    problem.addConstraint(lambda volvo, philosophy: volvo == philosophy, ["Volvo", "Philosophy"])
    problem.addConstraint(office_next_to, ["Neuroscience", "Audi"])
    problem.addConstraint(lambda history, coffee: history == coffee, ["History", "BlackCoffee"])
    problem.addConstraint(lambda white, mit: white == mit, ["White", "MIT"])
    problem.addConstraint(lambda stanford, harvard: stanford > harvard, ["Stanford", "Harvard"])

    solutions = problem.getSolutions()

    possible_professors = set()

    for solution in solutions:
        medieval_office = solution["MedievalLiterature"]

        for module in modules:
            if solution[module] == medieval_office:
                possible_professors.add(module)

    print("Number of valid solutions:", len(solutions))
    print("Possible professors researching Medieval Literature:")

    for professor in sorted(possible_professors):
        print("-", professor)


if __name__ == "__main__":
    solve()
