#calculates how many levels of a soda can piramid can you stack with
#given money and price per can, each level requires level**2 number of cans
def canPiramid(money, price):
    cans = 0
    level = 1
    while cans < money // price:
        cans += level**2
        if cans == money // price or cans + (level+1)**2 > money // price:
            return level
        else:
            level += 1
    return 0

canPiramid(5000, 10)
