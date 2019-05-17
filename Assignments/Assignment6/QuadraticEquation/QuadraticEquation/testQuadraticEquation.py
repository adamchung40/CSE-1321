from QuadraticEquation import quadraticEquation

def main():
#Sample 1
	e1 = quadraticEquation(3,8,4)
	print("a =", e1.getA())
	print("b =", e1.getB())
	print("c =", e1.getC())
	e1.getRoot1()
	e1.getRoot2()
	print()
#Sample 2
	e2 = quadraticEquation(3,4,8)
	print("a =", e2.getA())
	print("b =", e2.getB())
	print("c =", e2.getC())
	e2.getRoot1()
	e2.getRoot2()
	print()
#Sample 3
	e1 = quadraticEquation(2,8,2)
	print("a =", e1.getA())
	print("b =", e1.getB())
	print("c =", e1.getC())
	e1.getRoot1()
	e1.getRoot2()
main()
