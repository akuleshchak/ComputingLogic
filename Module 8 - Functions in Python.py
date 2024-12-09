def greaterThan(x, y):
    if x > y: return True
    else: return False

a = 10
b = 6
result = str(greaterThan(a, b)).lower()
print("The statement", str(a), "is greater than", str(b), "is", result)
