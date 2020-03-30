import random

NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']

#print([name.title() for name in NAMES])
#print(random.choices(NAMES, k=2))

def gen_pairs(names=NAMES):
    while True:
        first_names = [name.split()[0].title() for name in names]
        choices = random.choices(first_names, k=2)
        my_string = "{} teams up with {}".format(choices[0].title(), choices[1].title())
        yield my_string

def reverse_names(name):
    first, last = name.split()
    return f'{last.title()}, {first.title()}'

print([reverse_names(name) for name in NAMES])

#pairs = gen_pairs()
#for _ in range(10):
#    print(next(pairs))

