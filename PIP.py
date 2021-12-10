# A program that helps the user identify plants given certain features of the plant and its locations, the Plant Identification Program (PIP)
# PIP.py
from PIL import ImageTk, Image
from colorama import init, Fore, Back, Style

# Main program that takes in user inputs, decides plant identity, and asks user if the answer is correct 
def main():
    # Lay out the rules
    init()
    print(Fore.YELLOW + "\nWelcome to PIP - the Plant Identification Program. Use this program to help identify common poisonous plant species found within the United States of America and \nlearn what to do in case you come into contact with them.")
    print(Fore.WHITE + "\nThis program will ask you a series of questions to help deduce which species you are looking for. Unless otherwise specified in the question, \nplease answer either", Fore.BLUE + "Yes", Fore.WHITE + "or", Fore.RED + "No", Fore.WHITE + "for each question. Happy searching!")
    
    # Ask user what time of year it is and what state they are in. Add these inputs to dictionary of user's responses called USER
    USER = {}
    USER['State'] = input("\nWhat state are you in or are looking to identify a plant in? ")
    season = input("What season is it? (Spring, Summer, Fall, or Winter) ")

    # Decision structure to handle which leaf color should be compared given the season (since there are four possible color options)
    if season == 'Spring':
        seasonIndex = 'Leaf color spring'
    elif season == 'Summer':
        seasonIndex = 'Leaf color summer'
    elif season == 'Fall':
        seasonIndex = 'Leaf color fall'
    else:
        seasonIndex = 'Leaf color winter'
    
    # Ask user about leaf features of plant and add each response to a dictionary of user's responses called USER
    leafPresent = input(Fore.GREEN + "Does the plant have leaves? ")
    if leafPresent == "Yes":
        USER[seasonIndex] = input(Fore.GREEN + "What color are the leaves? (Green, Yellow, Orange, Red, Bronze, or Green with reddish tint) ")
        USER['Leaf count'] = input(Fore.GREEN + "How many leaves are connected to a single point on the stem? (please enter a number such as 1, 5, 13, etc.) ")
        USER['Leaf shape'] = input(Fore.GREEN + "Is the leaf Oblong, Egg-shaped, or Elliptical in shape? ")            
        USER['Leaf edges'] = input(Fore.GREEN + "Does the leaf have Toothed, Smooth, or Lobed edges? ")
        USER['Leaf position'] = input(Fore.GREEN + "Are the leaf groupings Alternating on the stem or Paired? ")

    # Ask user about flowers
    flowerPresent = input(Fore.MAGENTA + "Does the plant have flowers? ")
    if flowerPresent == "Yes":
         USER['Flower color'] = input(Fore.MAGENTA + "What color are the flowers? (Greenish, Green-yellow, or White) ")
         USER['Petal count'] = input(Fore.MAGENTA + "What is the maximum number of petals a single flower has? (please enter a number such as 2, 5, 7, etc.) ")
    
    # Ask user about berry features of plant
    berryPresent = input(Fore.LIGHTBLUE_EX + "Does the plant have berries? ")
    if berryPresent == "Yes":
        USER['Berry grouping'] = input(Fore.LIGHTBLUE_EX + "Are the berries grouped as Single, Druped/Paired, or Clustered? ")
        USER['Berry color'] = input(Fore.LIGHTBLUE_EX + "What color are the berries? (White, Greenish-white, Orange, or Purple-black) ")
    
    print(Fore.WHITE + "\nThank you for your input! Let's identify that plant...")

    # Deduce plant identity
    # Dictionary of plant info
    PLANTS = {'Poison Ivy': {'Scientific name': 'Toxicodendron radicans', 'State': 'Alabama, Arizona, Arkansas, Colorado, Connecticut, Delaware, Florida, Georgia, Idaho, Illinois, Indiana, Iowa, Kansas, Kentucky, Louisiana, Maine, Maryland, Massachusetts, Michigan, Minnesota, Mississippi, Missouri, Montana, Nebraska, Nevada, New Hampshire, New Jersey, New Mexico, New York, North Carolina, North Dakota, Ohio, Oklahoma, Oregon, Pennsylvania Rhode Island, South Carolina, South Dakota, Tennessee, Texas, Utah, Vermont, Virginia, Washington, West Virginia, Wisconsin, Wyoming',
              'Leaf color spring': 'Green', 'Leaf color summer': 'Green', 'Leaf color fall': 'Red', 'Leaf color winter': 'None', 'Leaf count': '3', 
              'Leaf shape': 'Elliptic or egg-shaped', 'Leaf edges': 'Smooth or toothed', 'Leaf position': 'Alternating on stem', 
              'Flowers': 'Yes, in spring to summer', 'Flower color': 'Green-yellow', 'Petal count': '5', 'Berries': 'Yes', 'Berry time': 'Fall', 
              'Berry grouping': 'Single', 'Berry color': 'White'},
              'Poison Oak': {'Scientific name': 'Toxicodendron diversilobum', 'State': 'Illinois, Missouri, Kansas, Oklahoma, Texas, Louisiana, Alabama, Arkansas, Mississippi, Georgia, Florida, North Carolina, South Carolina, Tennessee, Virginia, West Virginia, New Jersey, Washington, Oregon, California, Nevada',
              'Leaf color spring': 'Green', 'Leaf color summer': 'Green', 'Leaf color fall': 'Red or Orange', 'Leaf color winter': 'Bronze', 'Leaf count': '3', 
              'Leaf shape': 'Elliptic', 'Leaf edges': 'Lobed', 'Leaf position': 'Alternating on stem, but loses leaves in winter', 
              'Flowers': 'Yes, in spring to summer', 'Flower color': 'White', 'Petal count': '5', 'Berries': 'Yes', 'Berry time': 'Spring', 
              'Berry grouping': 'Drupe/Paired', 'Berry color': 'Greenish-white'},
              'Poison Sumac': {'Scientific name': 'Toxicodendron vernix', 'State': 'Texas, Minnesota, Wisconson, Illinois, Louisiana, Alabama, Arkansas, Mississippi, Georgia, Florida, Tennessee, South Carolina, North Carolina, Indiana, Ohio, Kentucky, Michigan, Virginia, West Virginia, Pennsylvania, New York, Maine, Vermont, New Hampshire, New Jersey, Massachusetts, Rhode Island',
              'Leaf color spring': 'Green with reddish tint', 'Leaf color summer': 'Green with reddish tint', 'Leaf color fall': 'Red', 'Leaf color winter': 'None', 'Leaf count': '7 to 13', 
              'Leaf shape': 'Oval to oblong', 'Leaf edges': 'Smooth', 'Leaf position': 'Paired on stem', 
              'Flowers': 'Yes', 'Flower color': 'Greenish', 'Petal count': '5', 'Berries': 'Yes', 'Berry time': 'Spring', 
              'Berry grouping': 'Cluster', 'Berry color': 'White'},
              'Giant Hogweed': {'Scientific name': 'Heracleum mantegazzium', 'State': 'New York, Pennsylvania, Ohio, Maryland, Oregon, Washington, Michigan, Virginia, Vermont, New Hampshire, Maine', 
              'Leaf color spring': 'Green', 'Leaf color summer': 'Green', 'Leaf color fall': 'None', 'Leaf color winter': 'None', 'Leaf count': '1',
              'Leaf shape': 'Lobed', 'Leaf edges': 'Toothed', 'Leaf position': 'Paired', 
              'Flowers': 'Yes', 'Flower color': 'White', 'Petal count': '5', 'Berries': 'Yes', 'Berry time': 'Summer',
              'Berry grouping': 'Single', 'Berry color': 'Orange'},
              'Pokeweed': {'Scientific name': 'Phytoloacca americana', 'State': 'Oregon, Washington, California, Arizona, New Mexico, Texas, Nebraska, Oklahoma, Kansas, Minnesota, Iowa, Missouri, Louisiana, Arkansas, Wisconsin, Illinois, Tennessee, Mississippi, Michigan, Ohio, Indiana, Kentucky, Alabama, Pennsylvania, West Virginia, North Carolina, South Carolina, Georgia, Florida, New York, New Jersey, Vermont, Rhode Island, Maine, Massachusetts, Maryland', 
              'Leaf color spring': 'Green', 'Leaf color summer': 'Green', 'Leaf color fall': 'Red', 'Leaf color winter': 'None', 'Leaf count': '1',
              'Leaf shape': 'Elliptical', 'Leaf edges': 'Smooth', 'Leaf position': 'Alternating on stem', 
              'Flowers': 'Yes', 'Flower color': 'Greenish-white', 'Petal count': '5', 'Berries': 'Yes', 'Berry time': 'Summer',
              'Berry grouping': 'Cluser', 'Berry color': 'Purple-black'}}
    
    # Establish lists that hold how many traits match between PLANTS and USER
    poisonIvyTrue = []
    poisonOakTrue = []
    poisonSumacTrue = []
    giantHogweedTrue = []
    pokeweedTrue = []
    # Check if traits for each plant match traits inputted by the user
    for plant in PLANTS:
        for trait in USER:
            if USER[trait].lower() in PLANTS[plant][trait].lower() and plant == 'Poison Ivy':
                poisonIvyTrue.append(trait)
            elif USER[trait].lower() in PLANTS[plant][trait].lower() and plant == 'Poison Oak':
                poisonOakTrue.append(trait)
            elif USER[trait].lower() in PLANTS[plant][trait].lower() and plant == 'Poison Sumac':
                poisonSumacTrue.append(trait)
            elif USER[trait].lower() in PLANTS[plant][trait].lower() and plant == 'Giant Hogweed':
                giantHogweedTrue.append(trait)
            elif USER[trait].lower() in PLANTS[plant][trait].lower() and plant == 'Pokeweed':
                pokeweedTrue.append(trait)

    # Find longest list. In other words, which plant has the most traits that match what the user inputted
    if len(poisonIvyTrue) > len(poisonOakTrue) and len(poisonIvyTrue) > len(poisonSumacTrue) and len(poisonIvyTrue) > len(giantHogweedTrue) and len(poisonIvyTrue) > len(pokeweedTrue):
        plantIdentity = "Poison Ivy"
    elif len(poisonOakTrue) > len(poisonSumacTrue) and len(poisonOakTrue) > len(giantHogweedTrue) and len(poisonOakTrue) > len(pokeweedTrue):
        plantIdentity = "Poison Oak"
    elif len(poisonSumacTrue) > len(giantHogweedTrue) and len(poisonSumacTrue) > len(pokeweedTrue):
        plantIdentity = "Poison Sumac"
    elif len(giantHogweedTrue) > len(pokeweedTrue):
        plantIdentity = "Giant Hogweed"
    else:
        plantIdentity = "Pokeweed"
    print("\nBased on the information you provided, your plant is most likely", Fore.LIGHTGREEN_EX + plantIdentity+".")

    # Show user a picture of what the plant could be. Ask user if this is correct
    if plantIdentity == "Poison Ivy":
        poisonivyImage1 = Image.open('poisonivy1.png')
        poisonivyImage2 = Image.open('poisonivy2.png')
        poisonivyImage3 = Image.open('poisonivy3.png')
        poisonivyImage4 = Image.open('poisonivy4.png')
        poisonivyImage1.show()
        poisonivyImage2.show()
        poisonivyImage3.show()
        poisonivyImage4.show()
    elif plantIdentity == "Poison Oak":
        poisonoakImage1 = Image.open('poisonoak1.png')
        poisonoakImage2 = Image.open('poisonoak2.png')
        poisonoakImage3 = Image.open('poisonoak3.png')
        poisonoakImage4 = Image.open('poisonoak4.png')
        poisonoakImage1.show()
        poisonoakImage2.show()
        poisonoakImage3.show()
        poisonoakImage4.show()
    elif plantIdentity == "Poison Sumac":
        poisonsumacImage1 = Image.open('poisonsumac1.png')
        poisonsumacImage2 = Image.open('poisonsumac2.png')
        poisonsumacImage3 = Image.open('poisonsumac3.png')
        poisonsumacImage4 = Image.open('poisonsumac4.png')
        poisonsumacImage1.show()
        poisonsumacImage2.show()
        poisonsumacImage3.show()
        poisonsumacImage4.show()
    elif plantIdentity == "Giant Hogweed":
        gianthogweedImage1 = Image.open('gianthogweed1.png')
        gianthogweedImage2 = Image.open('gianthogweed2.png')
        gianthogweedImage3 = Image.open('gianthogweed3.png')
        gianthogweedImage4 = Image.open('gianthogweed4.png')
        gianthogweedImage1.show()
        gianthogweedImage2.show()
        gianthogweedImage3.show()
        gianthogweedImage4.show()
    elif plantIdentity == "Pokeweed":
        pokeweedImage1 = Image.open('pokeweed1.png')
        pokeweedImage2 = Image.open('pokeweed2.png')
        pokeweedImage3 = Image.open('pokeweed3.png')
        pokeweedImage4 = Image.open('pokeweed4.png')
        pokeweedImage1.show()
        pokeweedImage2.show()
        pokeweedImage3.show()
        pokeweedImage4.show()
    checkPlant = input(Fore.YELLOW + "Is this the plant you are looking for? (Please enter 'Yes' or 'No') ")

    # If user confirms that the picture is the plant they are looking for, Print scientific name, states, reactivity and safety info from plants.txt
    # Read plants.txt
    infile = open('plants.txt', 'r')
    line0 = infile.readline()
    line1 = infile.readline()
    line2 = infile.readline()
    line3 = infile.readline()
    line4 = infile.readline()
    line5 = infile.readline()
    line6 = infile.readline()
    line7 = infile.readline()
    line8 = infile.readline()
    line9 = infile.readline()
    line10 = infile.readline()
    line11 = infile.readline()
    line12 = infile.readline()
    line13 = infile.readline()
    line14 = infile.readline()
    line15 = infile.readline()
    line16 = infile.readline()
    line17 = infile.readline()
    line18 = infile.readline()
    line19 = infile.readline()
    line20 = infile.readline()
    line21 = infile.readline()
    line22 = infile.readline()
    line23 = infile.readline()
    line24 = infile.readline()
    line25 = infile.readline()
    line26 = infile.readline()
    line27 = infile.readline()
    line28 = infile.readline()
    line29 = infile.readline()
    line30 = infile.readline()
    line31 = infile.readline()
    line32 = infile.readline()
    line33 = infile.readline()
    line34 = infile.readline()
    line35 = infile.readline()
    line36 = infile.readline()
    line37 = infile.readline()
    line38 = infile.readline()
    line39 = infile.readline()
    line40 = infile.readline()
    line41 = infile.readline()
    line42 = infile.readline()
    line43 = infile.readline()
    line45 = infile.readline()
    line46 = infile.readline()
    line47 = infile.readline()
    line48 = infile.readline()
    line49 = infile.readline()
    line50 = infile.readline()
    line51 = infile.readline()
    line52 = infile.readline()
    line53 = infile.readline()
    line54 = infile.readline()
    infile.close()

    # Print appropriate information specific to what the plant is 
    if checkPlant == "Yes" and plantIdentity == "Poison Ivy":
        print(Fore.WHITE + "\nFantastic! Now that you know what it looks like, here are some tips for handling", Fore.LIGHTGREEN_EX + plantIdentity+"...")
        print('\n', line0, '\n', line1, '\n', line2, '\n', line3, '\n', line4, '\n', line5, '\n', line6, '\n', line7, '\n', line8, '\n', line9, '\n', line10, sep="")
    if checkPlant == "Yes" and plantIdentity == "Poison Oak":
        print("\nFantastic! Now that you know what it looks like, here are some tips for handling", Fore.LIGHTGREEN_EX + plantIdentity+"...")
        print('\n', line11, '\n', line12, '\n', line13, '\n', line14, '\n', line15, '\n', line16, '\n', line17, '\n', line18, '\n', line19, '\n', line20, '\n', line21, '\n', sep="")
    if checkPlant == "Yes" and plantIdentity == "Poison Sumac":
        print("\nFantastic! Now that you know what it looks like, here are some tips for handling", Fore.LIGHTGREEN_EX + plantIdentity+"...")
        print('\n', Fore.WHITE + line22, '\n', line23, '\n', line24, '\n', line25, '\n', line26, '\n', line27, '\n', line28, '\n', line29, '\n', line30, '\n', line31, '\n', line32, '\n', line33, sep="")
    if checkPlant == "Yes" and plantIdentity == "Giant Hogweed":
        print("\nFantastic! Now that you know what it looks like, here are some tips for handling", Fore.LIGHTGREEN_EX + plantIdentity+"...")
        print('\n', Fore.WHITE + line34, '\n', line35, '\n', line36, '\n', line37, '\n', line38, '\n', line39, '\n', line40, '\n', line41, '\n', line42, '\n', line43, sep="")
    if checkPlant == "Yes" and plantIdentity == "Pokeweed":
        print("\nFantastic! Now that you know what it looks like, here are some tips for handling", Fore.LIGHTGREEN_EX + plantIdentity+"...")
        print('\n', Fore.WHITE + line45, '\n', line46, '\n', line47, '\n', line48, '\n', line49, '\n', line50, '\n', line51, '\n', line52, '\n', line53, '\n', line54, sep="")

    # If user rejects the proposed plant identity, Print an apology and ask user if they want to try the process again or quit
    if checkPlant == "No":
        print(Fore.RED + "\nSorry about that! If this isn't the plant you're looking for, there may be inconsistent information that makes it difficult to identify. ")
    # If user wants to try again, restart the program. If user quits, offer a website with plant information
        tryAgain = input(Fore.YELLOW + "Would you like to try again? ")
        if tryAgain == "Yes":
            return main()
        if tryAgain == "No":
            print("\nThank you for using PIP! Here are some other resources that may help you on your plant identification journey...")
            print("https://www.greenbelly.co/pages/poisonous-plants-identification-guide")
            print("https://www.webpages.uidaho.edu/range/toxicplants_horses/Toxic%20Plant%20Database.html")
            print("https://www.cdc.gov/niosh/topics/plants/geographic.html")
            print("https://www.worldatlas.com/articles/10-poisonous-plants-found-in-the-united-states.html")


if __name__ == "__main__":
    main()