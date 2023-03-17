def simpleGenerator():
    for idx in range(5):
        yield idx
        
for val in simpleGenerator():
    print(val)