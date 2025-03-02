class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_instances = {}

    for person in people:
        person_instances[person["name"]] = Person(person["name"],
                                                  person["age"])

    for person in people:
        person_instance = person_instances[person["name"]]
        if "wife" in person and person["wife"]:
            person_instance.wife = person_instances[person["wife"]]
        if "husband" in person and person["husband"]:
            person_instance.husband = person_instances[person["husband"]]
    return list(person_instances.values())
