# no pastrami

sandwich_orders = [ "blt",
                  "grilled cheese",
                  "pastrami sandwhich",
                  "club sandwich",
                  "pastrami sandwhich",
                  "reuben",
                  "banana sandwich",
                  "pastrami sandwhich",
                ]

finished_sandwhiches = []


print("\n")
while sandwich_orders:
    
    for item in sandwich_orders:
        if item == "pastrami sandwhich":
            sandwich_orders.remove("pastrami sandwhich")
            print("We are out of pastrami")
    
    current_sandwhich = sandwich_orders.pop()
    print(f"Making {current_sandwhich.title()}.")
    finished_sandwhiches.append(current_sandwhich)
            

    


print(f"\n Sandwhich orders: {sandwich_orders},\n") 
print(f"Finished sandwhiches: {finished_sandwhiches}\n")