def egged(year, span):
    total = 0
    eggs_per_chicken = 300
    for i in range(min(span,year)):
        total += 3 * eggs_per_chicken
        eggs_per_chicken = int(eggs_per_chicken * 0.8)

    return total or "No chickens yet!"
def egged(year, span, chickens = 3):
    production = [300, 240, 192, 153, 122, 97, 77, 61, 48, 38, 30, 24, 19, 15, 12, 9, 7, 5, 4, 3, 2, 1]
    return 'No chickens yet!' if not year else sum(production[:min(year, span)]) * chickens



def greet(name): 
    capit = name.capitalize()
    return f"Hello {capit}!"


def generate_shape(n):
    result = ''
    for i in range(n):
        for i in range(n):
            result += '+'
        result += '\n'
    return result[0:-1]