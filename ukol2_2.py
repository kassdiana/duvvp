def gcd(a, b):
    # Euklidův algoritmus pro výpočet největšího společného dělitele (NSD) dvou čísel
    u = a
    w = b
    while w != 0:
        r = u % w
        u = w
        w = r
    return u


a = 2 * 2 * 3 * 5 * 7 * 11 * 13
b = 2 * 3 * 3 * 7 * 17

print(a)
print(b)

gcd(a, b)