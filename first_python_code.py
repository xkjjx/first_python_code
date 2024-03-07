print ("enter the quadratic value")
quadterm = int(input())
print("enter the linear value")
linterm = int(input())
print("enter the constant value")
constterm = int(input())
numlist=[]
def quadformula( a,b,c,root = True ):
    
    if root:
      x = ((b*-1)+(d**0.5))/(2*a)
    else:
      x = ((b*-1)-(d**0.5))/(2*a)
    return x;
def findpolyval(root):
    for x in numlist:
        y = root*x
        if y == round(y):
            return y
for x in range(1,50000001):
    numlist.append(x)
overallfactor=1
for x in numlist:
    tempquad = quadterm/x
    templin = linterm/x
    tempcon=constterm/x
    if tempquad==round(tempquad) and templin==round(templin) and tempcon==round(tempcon):
        overallfactor=x*overallfactor
        quadterm=tempquad
        linterm=templin
        constterm=tempcon

print(quadterm)
print(linterm)
print(constterm)
print(overallfactor)
d=(linterm**2)-4*quadterm*constterm
if d == 0:
    root = quadformula(quadterm,linterm,constterm)
    print("the answer is "+str(root))
    secondTerm = findpolyval(root)
    firstTerm = secondTerm/root
    print(str(overallfactor)+"("+str(firstTerm)+"x"+" + "+str(secondTerm)+")^2")
elif d == round(d) and d > 0:
    root1 = quadformula(quadterm,linterm,constterm)
    root2 = quadformula(quadterm,linterm,constterm,False)
    print("the answeres are "+str(root1))
    print("and "+str(root2))
    secondTerm = findpolyval(root1)
    firstTerm = secondTerm/root1
    fourthTerm = findpolyval(root2)
    thirdTerm = fourthTerm/root2
    print(str(overallfactor)+"("+str(firstTerm)+"x"+" + "+str(secondTerm)+")("+str(thirdTerm)+"x"+" + "+str(fourthTerm)+")")
