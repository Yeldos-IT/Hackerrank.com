def person_lister(format_name):
    def inner(people):
        for person in sorted(people, key=lambda x: int(x[2])):
            yield format_name(person)
    return inner