

for x in range(1, 1000):
    for y in range(1, 1000):
        for z in range(1, 1000):
            if ((x ** 2) + (y ** 2) == (z ** 2)):
                print('%d * %d * %d = %d' % (x, y, z, x * y * z))

print("Done")
