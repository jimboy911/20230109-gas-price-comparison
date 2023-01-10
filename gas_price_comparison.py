#gas_price_comparison.py

#ask user for price at sheetz - premium gasonline
sheetz_price = float(input("How much is gas at Sheetz? "))
#ask user for price at costco
costco_price = float(input("How much is gas at Costco? "))
#set constant for distance to sheetz roundtrip
irs_cost = 0.655
sheetz_distance = 5
#convert distance for sheetz to money
sheetz_mileage = irs_cost * sheetz_distance
#set constant for distance to costco roundtrip
costco_distance = 19.4
#convert distance for costco to money
costco_mileage = irs_cost * costco_distance
#add price to drive and price for full tank (15 gallons)
fuel_tank = 15
sheetz_cost = fuel_tank * sheetz_price
costco_cost = fuel_tank * costco_price
sheetz_total = sheetz_cost + sheetz_mileage
costco_total = costco_cost + costco_mileage
#subtract sheetz from costco
theDifference = sheetz_total - costco_total
theDifference_dollars = round(theDifference, 2)
#reply if sheetz or costco is cheaper
if (sheetz_total < costco_total):
	print("Whoa, Sheetz is cheaper!")
else:
	print("Costco is gonna be chaper for you.")
#and by how much
print("By: $" + str(abs(theDifference_dollars)))
