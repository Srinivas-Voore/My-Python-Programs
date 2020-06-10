from string import Template


s1="jithu";
s2="sai";

print(s1+s2);

print("".join([s1,s2]))

print("%s^%s"%(s1,s2));

print("{}{}".format(s1,s2));



print(f"{s1}{s2}");



z=Template("$n3 and $n4");
print(z.substitute(n3=s1,n4=s2));


