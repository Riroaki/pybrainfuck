# Calculate multiplication
a(0) = input1
a(1) = input2
index = 0
,.>,.<

while a(0) is positive:
    copy step:
        move a(1) to a(3)
        move a(3) to a(1) and a(2)
    index = 0
    a(0) sub 1
[>[>>+<<-]>>[<+<+>>-]<<<-]

print result a(2)
>>.
