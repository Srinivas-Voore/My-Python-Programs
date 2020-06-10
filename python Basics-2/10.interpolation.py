from string import Template


#f strings
n1=1
n2=2
print(f"{n1}and{n2}")


n=Template("$n6 with $n7")
print(n.substitute(n6=n1,n7=n2))
