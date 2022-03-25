budget = float(input())
flour_price_per_kg = float(input())
cost = 0
loaf_of_bread_price = 0
loaf_pieces = 0
eggs = 0
eggs_pack_price = flour_price_per_kg * 0.75
milk_price_per_litre = flour_price_per_kg + (flour_price_per_kg* 0.25)


loaf_of_bread_price = flour_price_per_kg + eggs_pack_price + (milk_price_per_litre / 4)

# loaf_pieces = budget // loaf_of_bread_price

while budget >= loaf_of_bread_price:
    loaf_pieces += 1
    budget -= loaf_of_bread_price
    eggs += 3
    if loaf_pieces % 3 == 0:
        eggs -= (loaf_pieces - 2)
    # if budget <= loaf_of_bread_price:
    #     break

print (f"You made {loaf_pieces} loaves of Easter bread! Now you have {eggs} eggs and {budget:.2f}BGN left.")
