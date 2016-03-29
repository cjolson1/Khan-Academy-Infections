from infections import *
a = User('User 1')
b = User('User 2')
c = User('User 3')
coach(a, b)
coach(a, c)
total_infection([a,b,c],a,1)
visualize([a,b,c], 1)