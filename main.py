r=0
f="forward"
b="backward"
c="actions available: "
t=" tunnel."
d="You are in the depths of the"+t
p=print
l="You are standing at the entrance to a long"+t
x="look"
n=f", {x}\n> "
h='',", "+b
q=f,x,b
w=["p(d);r=1","p(l)"],["r=2;p('You have escaped the'+t,'You win!')","p(d)","p(l);r=0"]
while r-2:exec(w[r][q.index(input(c+f+h[r]+n))])
