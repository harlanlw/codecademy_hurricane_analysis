# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 1
# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}

def damages_floats():
  for i in damages:
    ind = damages.index(i)
    if i == 'Damages not recorded':
      continue
    else:
      if "M" in i:
        i = i.replace("M", "")
        i = float(i) * conversion["M"]
        damages[ind] = i
      elif "B" in i:
        i = i.replace("B", "")
        i = float(i) * conversion["B"]
        damages[ind] = i
        
# test function by updating damages
damages_floats()

# 2 
# Create a Table
atlantic_hurricanes = {}
def dictionary_hurricane():
  index = 0
  for key in names:
    atlantic_hurricanes.update({key: {"Name": names[index],
                                      "Month": months[index],
                                      "Year": years[index],
                                      "Max Sustaind Wind": max_sustained_winds[index],
                                      "Areas Affected": areas_affected[index],
                                      "Damage": damages[index],
                                      "Deaths": deaths[index]}})
    index += 1
  

# Create and view the hurricanes dictionary
dictionary_hurricane()
#print(atlantic_hurricanes) 

# 3
# Organizing by Year
atlantic_years = {}
def year_hurricane():
  index = 0
  for year in atlantic_hurricanes.values():
    atlantic_years.update({years[index]: year})
    index += 1

# create a new dictionary of hurricanes with year and key
year_hurricane()
#print(atlantic_years)

# 4
# Counting Damaged Areas
areas = []
single_areas = []
affected_areas_count = {}

def count_areas():
  for area in areas_affected:
    for i in area:
      areas.append(i)
    for unique_i in areas:
      if unique_i not in single_areas:
        single_areas.append(unique_i)
  for i in single_areas:
    count = areas.count(i)
    affected_areas_count.update({i:count})

# create dictionary of areas to store the number of hurricanes involved in
count_areas()
#print(areas)
#print(single_areas)
#print(affected_areas_count)

# 5 
# Calculating Maximum Hurricane Count

def worst_hit():
  new_value = max(affected_areas_count, key= affected_areas_count.get)
  print("The worst hit area is: " + new_value)

  other_value = max(affected_areas_count.values())
  print("It was hit " + str(other_value) + " times.")
  


# find most frequently affected area and the number of hurricanes involved in

worst_hit()

# 6
# Calculating the Deadliest Hurricane
dead = dict(zip(names, deaths))
def deadliest_hurricane():
  max_dead = max(zip(dead.values(), dead.keys()))
  print("The worst hurricane was " + max_dead[1] + " with a death count of " + str(max_dead[0]) + ".")
  return dead
  

# find highest mortality hurricane and the number of deaths
deadliest_hurricane()

# 7
# Rating Hurricanes by Mortality

hurricane_morality = {0:[],1:[],2:[],3:[],4:[]}

def morality_scale():
   for key, value in dead.items():
     if value >= 0 and value <=99:
       hurricane_morality[0].append({key:value})
     if value >= 100 and value <=499:
       hurricane_morality[1].append({key:value})
     if value >= 500 and value <=999:
       hurricane_morality[2].append({key:value})
     if value >= 1000 and value <= 9999:
       hurricane_morality[3].append({key:value})
     if value >= 10000 and value <= 99999:
       hurricane_morality[4].append({key:value})

# categorize hurricanes in new dictionary with mortality severity as key
morality_scale()
print(hurricane_morality)

# 8 Calculating Hurricane Maximum Damage

most_damage = {}
most_damage.update(dict(zip(names, damages)))
def greatest_damage():
  for key, value in list(most_damage.items()):
    if value == 'Damages not recorded':
      #print(key, value)
      del most_damage[key]  
  new_value = max(zip(most_damage.values(), most_damage.keys()))
  print("The most damaging hurricane was " + new_value[1] + " and it damaged " + str(new_value[0]) + " dollars." )

# find highest damage inducing hurricane and its total cost
greatest_damage()

# 9
# Rating Hurricanes by Damage
damage_scale = {0: [],
                1: [],
                2: [],
                3: [],
                4: []}

def damage_scale_function():
   for key, value in most_damage.items():
     if value >= 0 and value <=9999999:
       damage_scale[0].append({key:value})
     if value >= 1000000000 and value <=999999999:
       damage_scale[1].append({key:value})
     if value >= 10000000000 and value <=9999999999:
       damage_scale[2].append({key:value})
     if value >= 50000000000 and value <= 99999999999:
       damage_scale[3].append({key:value})
     if value >= 500000000000 and value <= 999999999999:
       damage_scale[4].append({key:value})
  
# categorize hurricanes in new dictionary with damage severity as key
damage_scale_function()
print(damage_scale)
