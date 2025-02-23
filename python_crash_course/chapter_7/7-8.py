# deli

sandwich_orders = [ "blt",
                  "grilled cheese",
                  "club sandwich",
                  "reuben",
                  "banana sandwich",
                ]

finished_sandwhiches = []

print("\n")
while sandwich_orders:
    current_sandwhich = sandwich_orders.pop()
    print(f"Making {current_sandwhich.title()}.")
    finished_sandwhiches.append(current_sandwhich)
    

print(f"\n Sandwhich orders: {sandwich_orders},\n Finished sandwhiches: {finished_sandwhiches}\n")
