import design_compare_class

c1 = design_compare_class.Cat("White", "Jumping")
c2 = design_compare_class.Cat("Brown", "Sitting")

c1.view()
c2.view()

# pass by reference
c1.compare(c2)

# update
c2 = design_compare_class.Cat("Brown", "Jumping")
c2.view()
# compair again
c1.compare(c2)
