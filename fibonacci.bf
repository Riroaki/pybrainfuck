# Print first 10 items in fibonacci array
>++[<+++++>-]       iteration count a(0) = 10 = 2 * 5; index = 0

>+.>+.              a(1) = a(2) = 1 and print them
<<--                index = 0

[                   while a(0) is positive:
    >>[>>+<<-]          move a(2) to a(4)
    >[>>+<<-]           move a(3) to a(5)
    >>[<+<<+>>>-]       move a(5) to a(2) and a(4)
    <[<+>-]             move a(4) to a(3)
    <.                  print a(3)
    <<<-                a(0) sub 1
]
