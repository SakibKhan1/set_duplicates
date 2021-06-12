def find_intersection(a,b):
        duplicates = set()
        for number in a:
            if number in b:
                duplicates.add(number)
        return duplicates

l1 = [0,1,2,3,4]
l2 = [0,1,2,3,4,5,6,7,8]

res = find_intersection(l1,l2)
print('result: ' + str(res))

