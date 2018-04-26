def union(A, B):
    return [x for x in [ y for y in B if y not in A] + A]
    '''
    list1 = [x for x in A]
    list2 = [y for y in B if y not in list1]
    return list1 + list2
    '''

def intersection(A, B):
    return [x for x in A if x in [y for y in B]]

def set_diff(A, B):
    return [x for x in A if x not in [y for y in B]]

def symmetric_diff(A, B):
    return union(set_diff(A, B),set_diff(B, A))

def cartesian_product(A, B):
    return [ [x, y] for x in A for y in B]

A = [1,2,3]
B = [2,3,4]

print "A = [1,2,3]"
print "B = [2,3,4]\n"
print "union(A, B) = "
print union(A, B)#[1,2,3,4]
print ""

#print "union(B, A) = "
#print "\n"
#print union(B, A)#[2,3,4,1]

print "intersection(A, B) = " 
print intersection(A, B)#[2,3]
print ""

print "set_diff(A, B) = "
print set_diff(A, B)#[1]
print ""

print "symmetric_diff(A, B) = "
print symmetric_diff(A, B)#[1]
print ""

C = [1,2]
D = ["red", "white"]

print "C = [1,2]"
print "D = [\"red\", \"white\"]\n"

print "cartesian_product(C, D) = "
print cartesian_product(C, D)
print ""

