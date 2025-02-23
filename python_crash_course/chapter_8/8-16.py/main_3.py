from functions import make_car as fn

divider = "-" * 70
print(divider)

fn('toyota', 'corolla', color = 'red', transmission = 'automatic')
fn('tesla', 'roadster', color = 'black', transmission = 'manual', 
                   fuel = 'electric' )
fn('subaru', 'outback', color = 'blue', tow_package = True)
