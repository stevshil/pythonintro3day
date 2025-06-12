ee = "Mobile company"

def city():
    """
    Demonstrate functions
    """
    global localbus
    localbus = 92
    print(f"Local bus number: {localbus}")
    print(f"Global variable ee: {ee}")
    print(f"Possible global variable o2: {o2}")
    # print(f"Maybe global shard {shard}") # Not defined before definition or call

o2="O2 company"
city()
print(f"Localbus number: {localbus}")
print(f"Global variable ee: {ee}")
print(f"Possible global variable o2: {o2}")
shard = "Big building"
localbus = 100 
print(f"Localbus number: {localbus}")
city()
print(f"Localbus number: {localbus}")
print(f"Maybe global shard: {shard}")
