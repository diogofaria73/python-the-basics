cars = {'Fiat Uno', 'Golf GTI', 'Honda Civic'}
items_fiat_uno = {'Airbag', 'ABS', 'Air Conditioner'}
items_golf_gti = {'Airbag', 'ABS', 'Air Conditioner', 'Leather Seats'}
items_honda_civic = {'Airbag', 'ABS',
                     'Air Conditioner', 'Leather Seats', 'GPS'}

# Disjunction in python is the union of two sets. For example:
# Is Disjoint if the intersection of two sets is empty.
isDisjoint = set.isdisjoint(items_fiat_uno, items_golf_gti)

print(isDisjoint)

# Intersection in python is the intersection of two sets. For example:
# Is Intersection if the intersection of two sets is not empty.
result = set.intersection(items_fiat_uno, items_golf_gti, items_honda_civic)
print(result)
