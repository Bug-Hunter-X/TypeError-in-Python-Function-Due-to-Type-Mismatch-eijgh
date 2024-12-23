def function(a, b):
    try:
        return int(a) + int(b)
    except ValueError:
        return "Error: Inputs must be integers."

result = function(5, '10')
print(result)

result2 = function(5, 10)
print(result2)

result3 = function('5', '10')
print(result3)