#!/usr/bin/env python3


state = ('0', 'A', 'p')

i = ({
    '0': '0',
    '1': '1',
    '2': '2',
    '3': '3',
    '4': '4',
},
{
    'A': 'A',
    'B': 'B',
    'C': 'C',
    'D': 'D',
},
{
    'p': 'p',
    'q': 'q',
    'r': 'r',
    's': 's',
},
)

ff = ({
    '0': '1',
    '1': '2',
    '2': '2',
    '3': '0',
},
{
    'A': 'A',
    'B': 'B',
    'C': 'D',
    'D': 'B',
},
{
    'p': 'p',
    'q': 'q',
    'r': 'r',
    's': 's',
},
)

gg = ({
    '0': '3',
    '1': '2',
    '2': '2',
    '3': '0',
},
{
    'A': 'C',
    'B': 'B',
    'C': 'D',
    'D': 'B',
},
{
    'p': 'p',
    'q': 'q',
    'r': 'r',
    's': 's',
},
)

f = ({
    '0': '1',
    '1': '2',
    '2': '3',
    '3': '4',
    '4': '0',
},
{
    'A': 'B',
    'B': 'C',
    'C': 'D',
    'D': 'E',
    'E': 'A',
},
{
    'p': 'p',
    'q': 'q',
    'r': 'r',
    's': 's',
},
)

g = ({
    '0': '4',
    '1': '2',
    '2': '3',
    '3': '0',
    '4': '1',
},
{
    'A': 'C',
    'B': 'E',
    'C': 'D',
    'D': 'B',
    'E': 'A',
},
{
    'p': 'p',
    'q': 'q',
    'r': 'r',
    's': 's',
},
)

ingredients = [i, f, g]
reset = 0
r = reset
def names(x):
   if x == f:
       return 'f'
   elif x == g:
       return 'g'
   elif x == r:
       return 'r'

def apply(ingredient):
    global state
    if (ingredient == reset):
        state = ('0', 'A', 'p')
    else:
        state = (ingredient[0][state[0]], ingredient[1][state[1]], ingredient[2][state[2]])
    print(names(ingredient) + ': ' + str(state))

def go(*ingredients):
    apply(reset)
    for i in ingredients:
        apply(i)

print("Create 3BP using go(....[f|g])")
