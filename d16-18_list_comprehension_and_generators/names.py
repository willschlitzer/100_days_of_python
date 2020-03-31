NAMES = [
    "arnold schwarzenegger",
    "alec baldwin",
    "bob belderbos",
    "julian sequeira",
    "sandra bullock",
    "keanu reeves",
    "julbob pybites",
    "bob belderbos",
    "julian sequeira",
    "al pacino",
    "brad pitt",
    "matt damon",
    "brad pitt",
]


def dedup_and_title_case_names(names):
    """Should return a list of title cased names,
       each name appears only once"""
    title_names = []
    for name in names:
        if name.title() not in title_names:
            title_names.append(name.title())
    return title_names


def sort_by_surname_desc(names):
    """Returns names list sorted desc by surname"""
    names = dedup_and_title_case_names(names)
    surnames = []
    alpha_names = []
    for name in names:
        surname = name.split()[1]
        surnames.append(surname)
    surnames.sort(reverse=True)
    for surname in surnames:
        for name in names:
            if name.split()[1] == surname:
                alpha_names.append(name)
    return alpha_names


def shortest_first_name(names):
    """Returns the shortest first name (str).
       You can assume there is only one shortest name.
    """
    names = dedup_and_title_case_names(names)
    name_len = 0
    for name in names:
        first_name = name.split()[0]
        if (len(first_name) < name_len) or name_len == 0:
            name_len = len(first_name)
            short_name = first_name
    return short_name


if __name__ == "__main__":
    # dedup_and_title_case_names(names=NAMES)
    # sort_by_surname_desc(names=NAMES)
    shortest_first_name(names=NAMES)
