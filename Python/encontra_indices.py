def encontra_indices(v,s):
    indices=[]
    for i, item in enumerate (s):
        if item == v:
            indices.append(i)
    
    return indices


s = [0,4,5,6,0,9,7,4,2,1,0]
v = 0

print(encontra_indices(v,s))