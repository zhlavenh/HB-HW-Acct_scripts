"""Print out all the melons in our inventory."""
#Importing information
from melons import melons, melon_names

#Requesting user input
more_melons = input("Would you like to add for melons Y/N: ")

if more_melons =="Y" or more_melons == "y":

    new_melon = input("insert the info as name, price, seedless(True/False), flesh_color, rind_color, avg_weight: ")
    new_melon = new_melon.lstrip().split(",")

    melon_names[len(melon_names)+1] = new_melon[0]

    melons[new_melon[0]] = {
        "prices": new_melon[1],
        "seedless": new_melon[2],
        "flesh_color": new_melon[3],
        "rind_color": new_melon[4],
        "avg_weight": new_melon[5]}


print(melons)

#print report for all melons
# for i in melon_names:
#     name = melon_names[i]
#     melon_info = melons[name]
#     print(f'{name}\nprice: {melon_info["price"]}\nseedless: {melon_info["seedless"]}\nflesh_color: {melon_info["flesh_color"]}\nrind color: {melon_info["rind_color"]}\naverage_weight: {melon_info["avg_weight"]}\n\n')
