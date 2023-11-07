class my_calculator:

    # same name method with different parameter = method overloading for different language
    # but for python is not supported directly, so follow below
    # unknown number of arguments
    def product(self, *nums):
        sum = 1
        for x in nums:
            sum = sum * x
        print(sum)


# =======================================================================================
c1 = my_calculator()
c1.product(4)
c1.product(4, 5)
c1.product(4, 5, 6)
c1.product(4, 5, 6, 7)
