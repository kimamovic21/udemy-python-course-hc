class OutOfIngredientsError(Exception):
    pass


def make_chai(milk, sugar):
    if milk == 0 or sugar == 0:
        raise OutOfIngredientsError("Missing milk or sugar")
    print("chai is ready...")


# make_chai(0, 0)
# make_chai(1, 1)
make_chai(1, 0)
