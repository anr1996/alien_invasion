from functions import Restuarant 

wangs = Restuarant("wangs uptown chinese", 'chinese')
chyras = Restuarant("chyras", 'russian steakhouse')
sushi_chop = Restuarant("sushi chop", 'sushi')





divider = "-" * 60
print(f"\n{divider}")

wangs.describe_restuarant()
print("\n")

wangs.open_restuarant()
print(divider)

chyras.describe_restuarant()
print("\n")

chyras.open_restuarant()
print(divider)

sushi_chop.describe_restuarant()
print("\n")

sushi_chop.open_restuarant()
print(divider)



