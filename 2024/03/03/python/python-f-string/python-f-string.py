#%%
# python-f-string

integer = 123
number_ = 9876.6789
percent = 0.98765

xxx = [
    {"integer": 'd'},
    {"integer": 'b'}, 
    {"integer": '8b'},
    {"integer": '_b'},
    {"integer": '09_b'},
    {"integer": 'o'},
    {"integer": '#o'},
    {"integer": 'x'},       
    {"integer": '#x'},
    {"integer": '08x'},
    {"integer": 'c'},
    {"number_": 'f'},
    {"number_": '.2f'},
    {"number_": '09.2f'},
    {"number_": '09.5f'},
    {"number_": '.2f'},
    {"percent": '%'},
    {"percent": '9.5%'},
    {"percent": '09.4%'},
    {"percent": '09.5%'},
    {"number_": '.2e'},
    {"number_": '09.2e'}
]

cmd = '\n'.join([f'print(f"{{{k}}}|{v}|{{{k}:{v}}}")' for xx in xxx for k, v in xx.items() ])
print(cmd)

ccc = ''
for xx in xxx:
    for k, v in xx.items():
        ccc += f'print(f"{k} | {{{k}}} | {v} | f\'{{{{{k}:{v}}}}}\' | {{{k}:{v}}}") \n'

print(ccc)


#%%
print(f"integer | {integer} | d | f'{{integer:d}}' | {integer:d}") 
print(f"integer | {integer} | b | f'{{integer:b}}' | {integer:b}") 
print(f"integer | {integer} | 8b | f'{{integer:8b}}' | {integer:8b}") 
print(f"integer | {integer} | _b | f'{{integer:_b}}' | {integer:_b}") 
print(f"integer | {integer} | 09_b | f'{{integer:09_b}}' | {integer:09_b}") 
print(f"integer | {integer} | o | f'{{integer:o}}' | {integer:o}") 
print(f"integer | {integer} | #o | f'{{integer:#o}}' | {integer:#o}") 
print(f"integer | {integer} | x | f'{{integer:x}}' | {integer:x}") 
print(f"integer | {integer} | #x | f'{{integer:#x}}' | {integer:#x}") 
print(f"integer | {integer} | 08x | f'{{integer:08x}}' | {integer:08x}") 
print(f"integer | {integer} | c | f'{{integer:c}}' | {integer:c}") 
print(f"number_ | {number_} | f | f'{{number_:f}}' | {number_:f}") 
print(f"number_ | {number_} | .2f | f'{{number_:.2f}}' | {number_:.2f}") 
print(f"number_ | {number_} | 09.2f | f'{{number_:09.2f}}' | {number_:09.2f}") 
print(f"number_ | {number_} | 09.5f | f'{{number_:09.5f}}' | {number_:09.5f}") 
print(f"number_ | {number_} | .2f | f'{{number_:.2f}}' | {number_:.2f}") 
print(f"percent | {percent} | % | f'{{percent:%}}' | {percent:%}") 
print(f"percent | {percent} | 9.5% | f'{{percent:9.5%}}' | {percent:9.5%}") 
print(f"percent | {percent} | 09.4% | f'{{percent:09.4%}}' | {percent:09.4%}") 
print(f"percent | {percent} | 09.5% | f'{{percent:09.5%}}' | {percent:09.5%}") 
print(f"number_ | {number_} | .2e | f'{{number_:.2e}}' | {number_:.2e}") 
print(f"number_ | {number_} | 09.2e | f'{{number_:09.2e}}' | {number_:09.2e}") 

#%%

string = "Python"

xxx = [{"string": '20'},
       {"string": '>20'},
       {"string": '<20'}, 
       {"string": '^20'},
       {"string": '>>20'},
       {"string": '<<20'},
       {"string": '^^20'},
       {"string": '=^20'},
]

cmd = '\n'.join([f'print(f"{{{k}}}|{v}|{{{k}:{v}}}")' for xx in xxx for k, v in xx.items() ])
print(cmd)

ccc = ''
for xx in xxx:
    for k, v in xx.items():
        ccc += f'print(f"{k} | {{{k}}} | {v} | f\'{{{{{k}:{v}}}}}\' | {{{k}:{v}}}") \n'

print(ccc)

#%%
print(f"string | {string} | 20 | f'{{string:20}}' | {string:20}") 
print(f"string | {string} | >20 | f'{{string:>20}}' | {string:>20}") 
print(f"string | {string} | <20 | f'{{string:<20}}' | {string:<20}") 
print(f"string | {string} | ^20 | f'{{string:^20}}' | {string:^20}") 
print(f"string | {string} | >>20 | f'{{string:>>20}}' | {string:>>20}") 
print(f"string | {string} | <<20 | f'{{string:<<20}}' | {string:<<20}") 
print(f"string | {string} | ^^20 | f'{{string:^^20}}' | {string:^^20}") 
print(f"string | {string} | =^20 | f'{{string:=^20}}' | {string:=^20}")
# %%
