# testing.py
# A file to test all the parts of my project code
# Test the dictionary
'''import pdb

season = input()

if season == "spring":
    seasonIndex = 'Leaf color spring'
elif season == 'summer':
    seasonIndex = 'Leaf color summer'
elif season == 'fall':
    seasonIndex = 'Leaf color fall'
else:
    seasonIndex = 'Leaf color winter'

dictUser = {}
dictUser['State'] = input('Enter the state:')
dictUser[seasonIndex] = input('Enter leaft color:')
dictUser['Leaf count'] = input('Enter the leaf count') 


PLANTS = {  'Poison Ivy': {'State': 'Alabama, Arizona, Arkansas, Colorado, Connecticut, Delaware, Florida, Georgia, Idaho, Illinois, Indiana, Iowa, Kansas, Kentucky, Louisiana, Maine, Maryland, Massachusetts, Michigan, Minnesota,, Mississippi, Missouri, Montana, Nebraska, Nevada, New Hampshire, New Jersey, New Mexico, New York, North Carolina, North Dakota, Ohio, Oklahoma, Oregon, Pennsylvania Rhode Island, South Carolina, South Dakota, Tennessee, Texas, Utah, Vermont, Virginia, Washington, West Virginia, Wisconsin, Wyoming',
            'Leaf color spring': 'Green', 'Leaf color summer': 'Green', 'Leaf color fall': 'Red', 'Leaf color winter': 'None', 'Leaf count': '3', 'Leaf shape': 'Elliptic or egg-shaped', 'Leaf edges': 'Smooth or toothed', 'Leaf position': 'Alternating on stem', 'Flowers': 'Yes, in spring to summer', 'Flower color': 'Green-yellow', 'Petal count': '5', 'Berries': 'Yes', 'Berry time': 'Fall', 'Berry grouping': 'Single', 'Berry color': 'White'},
            'Poison Oak': {'State': 'Illinois, Missouri, Kansas, Oklahoma, Texas, Louisiana, Alabama, Arkansas, Mississippi, Georgia, Florida, North Carolina, South Carolina, Tennessee, Virginia, West Virginia, New Jersey, Washington, Oregon, California, Nevada',
            'Leaf color spring': 'Green', 'Leaf color summer': 'Green', 'Leaf color fall': 'Red or Orange', 'Leaf color winter': 'Bronze', 'Leaf count': '3', 'Leaf shape': 'Elliptic', 'Leaf edges': 'Lobed', 'Leaf position': 'Alternating on stem, but loses leaves in winter', 'Flowers': 'Yes, in spring to summer', 'Flower color': 'White', 'Petal count': '5', 'Berries': 'Yes', 'Berry time': 'Spring', 'Berry grouping': 'Drupe/Paired', 'Berry color': 'Greenish-white'},
            'Poison Sumac': {'State': 'Texas, Minnesota, Wisconson, Illinois, Louisiana, Alabama, Arkansas, Mississippi, Georgia, Florida, Tennessee, South Carolina, North Carolina, Indiana, Ohio, Kentucky, Michigan, Virginia, West Virginia, Pennsylvania, New York, Maine, Vermont, New Hampshire, New Jersey, Massachusetts, Rhode Island',
            'Leaf color spring': 'Green with reddish tint', 'Leaf color summer': 'Green with reddish tint', 'Leaf color fall': 'Red', 'Leaf color winter': 'None', 'Leaf count': '7 to 13', 'Leaf shape': 'Oval to oblong', 'Leaf edges': 'Smooth', 'Leaf position': 'Paired on stem', 'Flowers': 'Yes', 'Flower color': 'Greenish', 'Petal count': '5', 'Berries': 'Yes', 'Berry time': 'Spring', 'Berry grouping': 'Cluster', 'Berry color': 'White'}}

traits = []   #list(PLANTS['Poison Ivy'].keys())

for key in PLANTS.keys():
    #print("==== {} ====".format(key))
    for trait in PLANTS[key].keys():
        print("{} = {}".format(trait, PLANTS[key][trait]))

for plant in PLANTS: 
    for trait in UserPlant:
        if UserPlant[trait] == PLANTS[plant][trait]:  

# These two lines extract a singe trait if you give the plant name and trait type
inner_dict = PLANTS['Poison Ivy'][0]
print(inner_dict['Scientific name']) # Gives Toxicodendron radicans

# Could be used for all the traits up to the 18th trait
scientific_name = PLANTS['Poison Ivy'][0]
state = PLANTS['Poison Ivy'][1]
leaf_color_spring = PLANTS['Poison Ivy'][2]
...
berry_color = PLANTS['Poison Ivy'][18]

# But what if I try to loop through the dictionary for a single plant?
for traits in PLANTS['Poison Ivy']:
    pass

# Functions to show images of possible plants 
def showPoisonivy(plantIdentity):
    poisonivyImage1 = Image.open('poisonivy1.png')
    poisonivyImage2 = Image.open('poisonivy2.png')
    poisonivyImage3 = Image.open('poisonivy3.png')
    poisonivyImage4 = Image.open('poisonivy4.png')
showPoisonivy()

def showPoisonoak(plantIdentity):
    poisonoakImage1 = Image.open('poisonoak1.png')
    poisonoakImage2 = Image.open('poisonoak2.png')
    poisonoakImage3 = Image.open('poisonoak3.png')
    poisonoakImage4 = Image.open('poisonoak4.png')
showPoisonoak()

def showPoisonsumac(plantIdentity):
    poisonsumacImage1 = Image.open('poisonsumac1.png')
    poisonsumacImage2 = Image.open('poisonsumac2.png')
    poisonsumacImage3 = Image.open('poisonsumac3.png')
    poisonsumacImage4 = Image.open('poisonsumac4.png')
showPoisonsumac()
'''
def main():
#if checkPlant == "Yes" and plantIdentity == "Poison Ivy":
#print("\nFantastic! Now that you know what it looks like, here are some tips for handling", plantIdentity+"...")
    infile = open('plants.txt', 'r')
    line0 = infile.readline()
    line1 = infile.readline()
    line2 = infile.readline()
    print(line0, '\n', line1, '\n', line2, sep="")

    
main()