name1 = input("Enter first name").lower()
name2 = input("Enter second name").lower()

t = name1.count("t")
r = name1.count("r")
u = name1.count("u")
e = name1.count("e")
l = name1.count("l")
o = name1.count("o")
v = name1.count("v")

t_2 = name2.count("t")
r_2 = name2.count("r")
u_2 = name2.count("u")
e_2 = name2.count("e")
l_2 = name2.count("l")
o_2 = name2.count("o")
v_2 = name2.count("v")

name1_count = t + r + u + e + l + o + v
name2_count = t_2 + r_2 + u_2 + e_2 + l_2 + o_2 + v_2
print("Love score : " + name1_count.__str__() + name2_count.__str__())
