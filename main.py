r=0
f="forward"
b="backward"
c="actions available: "
t=" tunnel."
d="You are in the depths of the"+t
p=print
a=1
l="You are standing at the entrance to a long"+t
x="look"
n=","+x+"\n> "
h='',f", {b}"
q=[f,x],[f,b,x]
w=["p(d);r=1","p(l)"],["r=2;p('You have escaped the'+t,'You win!')","p(l);r=0","p(d)"]
while r != 2:exec(w[r][q[r].index(input(c+f+h[r]+n))])
