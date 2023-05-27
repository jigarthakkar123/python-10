str1="Tops Technologies"
rev_upper = lambda string: string.upper()[::-1]
print(rev_upper(str1))


def rev_upper1(str2):
    return str2.upper()[::-1]

print(rev_upper1(str1))

lambda_cube = lambda y: y*y*y
print(lambda_cube(5))
