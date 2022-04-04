import os
import pickle
from hiq import read_file

here = os.path.dirname(os.path.realpath(__file__))


def f1():
    itree_tpl = read_file(f"{here}/tau.tpl", by_line=False)
    pickle.dump(itree_tpl, open(f"{here}/tau.pk", "wb"))


def f2():
    res = pickle.load(open(f"{here}/tau.pk", "rb"))
    assert isinstance(res, str), "res should be string instance"
    print(res)


if __name__ == "__main__":
    f1()
    # f2()
