"""A program to help me estimate the costs for my tea party."""

__author__: str = "730775257"


def main_planner(guests: int) -> None:
    """Entrypoint of the program."""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print("Cost: $" + str(cost(tea_bags(people=guests), treats(people=guests))))


def tea_bags(people: int) -> int:
    """Return the total number of tea bags based on the number of guests."""
    return people * 2


def treats(people: int) -> int:
    """Return the total number of treats."""
    return int(1.5 * tea_bags(people=people))


def cost(tea_count: int, treat_count: int) -> float:
    """Return the cost of tea bags and treats combined."""
    return treat_count * 0.75 + tea_count * 0.5


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
