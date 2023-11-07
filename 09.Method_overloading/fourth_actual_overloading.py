# to work like another language method overloading(ex: same name multiple method)
from multipledispatch import dispatch


class my_calculator:
    @dispatch(int, int)
    def product(self, a, b):
        print(a * b)

    @dispatch(int, int, int)
    def product(self, a, b, c):
        print(a * b * c)

    @dispatch(str, str)
    def product(self, a, b):
        print(int(a) * int(b))

    @dispatch(float, float, float)
    def product(self, a, b, c):
        print(a * b * c)

    @dispatch(float, int, str)
    def product(self, a, b, c):
        print(a * b * int(c))


# =======================================================================================
c1 = my_calculator()
c1.product(4, 5)
c1.product(4, 5, 6)
c1.product("8", "2")

# to write method overloading in python like other languages then must need a decorator pakage "multipledispatch"
