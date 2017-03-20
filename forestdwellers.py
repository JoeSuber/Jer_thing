
a = [-1, 150, 110, -1, -1, 160, 180, 120, -1, 110]


def march(everything=a):
    people = sorted([n for n in everything if n > 0], reverse=True)
    for i, thing in enumerate(everything):
        if thing > 0:
            everything[i] = people.pop()
    return everything

print march()

