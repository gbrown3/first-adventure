import random

# Declare global variables

condition = False
inventory = []
intercom = False
shieldAccess = False
engineAccess = False
mainShieldRoom = False
toothbrush = False
talkedToHerbert = False
firstTimeShieldRoom = True
herbertInShieldRoom = True
herbertHasPass = False
talkedJosh = False
talkedGeorge = False
talkedJosh2 = False
beenToDining = False
beenToBathroom = False
beenToSleeping = False
gaveToJosh = False
fixed = False



def main():
    """This is the function for the prologue. It returns once CONDITION is true."""
    global inventory  
    global condition  
    
    introtext = "\nWelcome to our swagadelic adventure game. You are the captain of a spaceship that\nis doing something, probably. You are in the cockpit. Your job is to get back home\nsafely. To view a list of possible actions, type 'help'. To start, go talk to\nyour co-captain.\n"
    print(introtext)
    
    while not condition:
        # Get user input while CONDITION is false (turns to true at end of game).
        command = input("Enter a command: ")
        if 'talk' in command:
            # Dialogue with the co-captain
            if 'co-captain' in command:
                print("\nCo-Captain: 'You know, I really don't like the way you're running\nthis ship. I'm going to take it over and stuff.'\n")
                print("The Co-Captain knocks you unconscious. You wake up in the living\nquarters with the rest of your crew. It appears as though the co-captain\nhas taken over the ship and locked everyone else in here. Find your way out\nand regain control of the ship!")
                # Once the co-captain knocks you out, run the LIVINGQUARTERS() function.
                livingQuarters()
            else:
                print("\nYou cannot do that. (type 'help' to see a list of commands)\n")
                
        elif command == 'help':
            # Print a list of possible actions.
            helpList()
            
        elif command == 'ship':
            # Display list of discovered/undiscovered rooms.
            ship()
            
        elif command == 'location':
            # Describe the user's surroundings.
            print(introtext)
        
        elif command == 'inventory':
            # Print the user's inventory.
            print("\n", inventory, "\n")
            
        else:
            print("\nYou cannot do that. (type 'help' to see a list of commands)\n")
            
    return
            
        
def livingQuarters():
    """This is the function for the living quarters."""
    global condition
    global inventory
    
    introtext = "\nYou are in the living quarters. There is a dining hall, a sleeping space, and a\nbathroom. Go to the dining hall to start.\n" 
    print(introtext)
    
    while not condition:
        # Get user input while CONDITION is false (turns to true at end of game).
        command = input("Enter a command: ")
        if command == 'help':
            # Print a list of possible actions.
            helpList()
            
        elif command == 'inventory':
            # Print the user's inventory.
            print("\n", inventory, "\n")
            
        elif command == 'location':
            # Describe the user's surroundings.
            print(introtext)
            
        elif command == 'ship':
            # Display a list of discovered/undiscovered rooms.
            ship()
            
        elif 'goto' or 'go to' in command:
            # Go to a specified room.
            goto(command)            
            
        else:
            print("\nYou cannot do that.\n")
            
    return
            
def diningHall():
    """This is the function for the dining hall."""
    global inventory
    global beenToDining
    global engineAccess
    global talkedJosh
    global talkedJosh2
    global gaveToJosh
    global condition
    
    introtext = "\nYou are in the dining hall where there is a long table with various objects\non top, a bunch of cupboards, and one of your crewmembers: Josh, the repairman.\n"
    print(introtext)
    
    beenToDining = True
    
    while not condition:
        # Get user input while CONDITION is false (turns true when game ends).
        command = input("Enter a command: ")
        if command == 'help':
            # Print a list of possible actions.
            helpList()
            
        elif command == 'ship':
            # Display a list of discovered/undiscovered rooms.
            ship()            
            
        elif command == 'location':
            # Describe the user's surroundings.
            print(introtext)
            
        elif 'investigate' in command:
            if 'table' in command:
                # Run the function for the table in the dining hall.
                longtable()
            elif 'cupboard' in command:  
                # Run the function for the cupboards in the dining hall.
                cupboards()
            else:
                print("\nYou cannot investigate that.\n")   
            
        elif 'talk' in command:
            if 'Josh' or 'josh' or 'repairman' in command:
                # Dialogue with Josh
                talkJosh()    
            else:
                print("\nYou cannot do that.\n")
                
        elif 'give' in command:
            if 'Josh' and 'teddy bear' in command and 'teddy bear' in inventory:
                # Give Josh the teddy bear and have him fix the intercom (moves to the engine room).
                print("\nJosh: 'You found my teddy bear! Thank you so much. I can look at\nthat intercom now.'")
                gaveToJosh = True
                inventory.remove("teddy bear")
                engineRoom()
            else:
                print("\nYou cannot do that.\n")
                
        elif command == 'inventory':
            # Display a list of the user's inventory.
            print("\n", inventory, "\n")
            
        elif 'goto' or 'go to' in command:
            # Go to a specified room.
            goto(command)             
            
        else:
            print("You cannot do that.\n")
            
    return

def longtable():
    """Function governing the table object in the dining room."""
    global inventory
    global beenToDining
    global engineAccess
    global talkedJosh
    global talkedJosh2    
    global gaveToJosh
    global condition
    
    # Describe the table depending on what the user has already taken.
    if 'pass' not in inventory and 'bowl' not in inventory and 'silverware' not in inventory:    
        print("\nThere is a bowl and silverware on the table, along with what\nappears to be an all-access meal pass. Interesting!\n")
        
    elif 'pass' not in inventory and 'bowl' not in inventory:
        print("\nThere is a bowl on the table along with what appears to be an\nall-access meal pass. Interesting!\n")
        
    elif 'pass' not in inventory and 'silverware' not in inventory:
        print("\nThere is silverware on the table along with what appears to be\nan all-access meal pass. Interesting!\n")
        
    elif 'bowl' not in inventory and 'silverware' not in inventory:
        print("\nThere is a bowl and silverware on the table.\n")
        
    elif 'bowl' not in inventory:
        print("\nThere is a bowl on the table.\n")
        
    elif 'silverware' not in inventory:
        print("\nThere is silverware on the table.\n")
        
    elif 'pass' not in inventory:
        print("\nThere is an all-access meal pass on the table. Interesting!\n")
        
    else:
        print("\nThe table is empty.\n")
        
    while not condition:
        # Get user input while CONDITION is false (turns to true at end of game).
        command = input("Enter a command: ")
        if command == 'help':
            # Print a list of possible actions.
            helpList()  
            
        elif 'take' in command:
            if 'pass' in command:
                # Add the meal pass to the inventory unless it is already there.
                if 'pass' in inventory:
                    print("\nThe meal pass is already in your inventory.\n")
                else:
                    inventory.append('pass')
                    print("\nThe meal pass has been added to your inventory.\n")  
            elif 'bowl' in command:
                # Add the bowl to the inventory unless it is already there.
                if 'bowl' in inventory:
                    print("\nThe bowl is already in your inventory.\n")
                else:
                    inventory.append('bowl')
                    print("\nThe bowl has been added to your inventory.\n")
            elif 'silverware' in command:
                # Add the silverware to the inventory unless it is already there.
                if 'silverware' in inventory:
                    print("\nThe silverware is already in your inventory.\n")
                else:
                    inventory.append('silverware')
                    print("\nThe silverware has been added to your inventory.\n")    
            else:
                print("\nYou cannot take that.\n")
                    
        elif 'investigate' in command:
            if 'cupboard' in command:
                # If the user wants to investigate the cupboard, run CUPBOARDS().
                cupboards()  
            elif 'table' in command:
                # If the user wants to investigate the table, run LONGTABLE().
                longtable()    
            else:
                print("\nYou cannot investigate that.\n")  
                
        elif 'talk' in command:
            if 'Josh' or 'josh' or 'repairman' in command:
                # Dialogue with Josh
                talkJosh()                     
            else:
                print("\nYou cannot do that.\n")
                                
        elif 'give' in command:
            if 'Josh' and 'teddy bear' in command and 'teddy bear' in inventory:
                # Give Josh the teddy bear and have him fix the intercom (moves to the engine room).
                print("\nJosh: 'You found my teddy bear! Thank you so much. I can look at\nthat intercom now.'")
                gaveToJosh = True
                inventory.remove("teddy bear")
                engineRoom()
            else:
                print("\nYou cannot do that.\n")
            
        elif command == 'inventory':
            # Print a list of the user's inventory.
            print("\n", inventory, "\n")
             
        elif command == 'location':
            # Describe the user's surroundings.
            print("\nYou are in the dining hall where there is a long table, a bunch of\ncupboards, and one of your crewmembers: Josh, the repairman.\n")
            
        elif command == 'ship':
            # Display a list of discovered/undiscovered rooms.
            ship()  
            
        elif 'goto' or 'go to' in command:
            # Go to a specified room.
            goto(command)    
            
        else:
            print("\nYou cannot do that.\n")
            
    return

def cupboards():
    """Function governing the cupboards in the dining room"""
    global inventory
    global beenToDining
    global engineAccess
    global talkedJosh
    global talkedJosh2 
    global gaveToJosh
    global condition
        
    print("\nYou can see various cooking supplies in some of the open cupboards-\nyou might not want to touch them or else George, the cook, would get mad. Most\nof the cupboards look boring except for one bright red cupboard.\n")
        
    while not condition:
        # Get user input while CONDITION is false (turns to true when game is over).
        command = input("Enter a command: ")
        if command == 'help':
            # Print a list of possible actions.
            helpList()      
            
        elif 'investigate' in command:
            if 'table' in command:
                # If the user wants to investigate the table, run LONGTABLE().
                longtable()
            elif 'red cupboard' in command:
                # Print text if the user investigates the red cupboard.
                print("\nYou open the cupboard to reveal a slew of questionable objects:\ncondoms, a Nickelback CD, black tar heroin, and peyote. This\nis really disconcerting...George listens to Nickelback?\n")             
            elif 'cupboard' in command:
                # Run CUPBOARDS() if the user wants to investigate the cupboards.
                cupboards()      
            else:
                print("\nYou cannot investigate that.\n")
            
        elif 'take' in command:
            if 'CD' in command or 'cd' in command:
                # Print text if the user tries to take the CD.
                print("\nHave some self respect.\n")
            elif 'condom' in command:
                # Print text if the user tries to take the condoms.
                print("\nLike you need those.\n")
            elif 'heroin' or 'peyote' in command:
                # Print text if the user tries to take the drugs.
                print("\nYou should probably leave that for George.\n")
            else:
                print("\nYou cannot take that.\n")
                
        elif 'talk' in command:
            if 'Josh' or 'josh' or 'repairman' in command:
                # Dialogue with Josh
                talkJosh()            
            else:
                print("\nYou cannot do that.\n")
                        
        elif 'give' in command:
            if 'Josh' and 'teddy bear' in command and 'teddy bear' in inventory:
                # Give Josh the teddy bear so he will fix the intercom (moves to engine room).
                print("\nJosh: 'You found my teddy bear! Thank you so much. I can look at\nthat intercom now.'")
                gaveToJosh = True
                engineRoom()
            else:
                print("\nYou cannot do that.\n")
            
        elif command == 'inventory':
            # Display a list of user's inventory.
            print("\n", inventory, "\n")
             
        elif command == 'location':
            # Describe the user's surroundings.
            print("\nYou are in the dining hall where there is a long table, a bunch of cupboards, and one of\nyour crewmembers: Josh, the repairman.\n")
            
        elif command == 'ship':
            # Display a list of discovered/undiscovered rooms.
            ship()
            
        elif 'goto' or 'go to' in command:
            # Go to a specified room.
            goto(command)
            
        else:
            print("You cannot do that.\n")
            
    return

            
def sleepingSpace():
    """This function is for the bedrooms in the ship."""
    global beenToSleeping
    global inventory
    global talkedGeorge
    global condition
    
    introtext = "\nYou are in the sleeping space where there are rows of beds and tables. George,\nthe cook, is lying on one of the beds. There is a large vent in the corner of the room.\nIt looks like you could fit through it.\n"
    print(introtext)
    
    beenToSleeping = True
    
    while not condition:
        # Get user input while CONDITION is false (turns to true at end of game).
        command = input("Enter a command: ")
        if command == 'help':
            # Print a list of possible commands.
            helpList()
            
        elif command == 'location':
            # Describe the user's surroundings.
            print(introtext)
            
        elif 'investigate' in command:
            if 'bed' in command:
                # Print text if the user investigates the bed.
                print("\nThis bed looks pretty comfy. George is lying down.\n")
            elif 'table' in command:
                # Print text if the user investigates the table.
                print("\nThis table looks nice and sturdy. Much like your ego.\n")
            elif 'vent' in command:
                # Run VENT() if the user investigates the vent.
                vent()
            else:
                print("\nYou cannot investigate that.\n")
                
        elif 'talk' in command:
            if 'George' or 'george' in command:
                # Dialogue with George
                if not talkedGeorge:
                    # Print this if the user hasn't talked to George yet.
                    print ("\nGeorge: 'Hey boss, how ya feeling?'\n")
                    talkedGeorge = True  
                else:
                    # Print this if the user has already talked to George.
                    print("\nGeorge: 'You managed to pry that traitorous turtle out of his shell\nyet, boss?'\n")
            else:
                print("\nYou cannot do that.\n")
          
        elif command == 'inventory':
            # Print a list of user's inventory.
            print("\n", inventory, "\n")  
            
        elif command == 'ship':
            # Display a list of discovered/undiscovered rooms.
            ship()
            
        elif 'goto' or 'go to' in command:
            # Go to a specified room.
            goto(command)
            
        else:
            print("\nYou cannot do that.\n")
            
    return
            
def vent():
    """This function is for the vent in the sleeping space."""
    global inventory
    global talkedGeorge
    global shieldAccess
    global condition
    
    # Describe the vent depending on whether or not it is open.
    if shieldAccess:
        print("\nThe vent is open.\n")
        decide = input("Go to the shield room? (say yes or no) ")
        if decide == 'yes':
            shieldRoom()
    else:
        print("\nThe vent is fairly large but will not budge. It looks as though you\nneed something special to open it.\n")
    
    while not condition:
        # Get user input while CONDITION is false (turns to true at end of game).
        command = input("Enter a command: ")  
        if command == 'help':
            # Print a list of possible actions.
            helpList()
            
        elif 'use' in command:
            if 'screwdriver' in command and 'screwdriver' in inventory:
                # If the user uses the screwdriver on the vent, open the vent and give them the option to go inside.
                # Going inside takes the user to the shield room.
                print("\nYou opened the vent!\n")
                decision = input("Go inside? (say yes or no) ")
                if decision == 'yes':
                    shieldAccess = True
                    # Run SHIELDROOM() if the user says 'yes'.
                    shieldRoom()
                elif decision == 'no':
                    sleepingSpace()
            else:
                print("\nYou cannot use that.\n")
    
        elif 'investigate' in command:
            if 'bed' in command:
                # Print text if the user investigates the bed.
                print("\nGeorge is asleep on the bed. It look like a pretty comfy bed.\n")
            elif 'table' in command:
                # Print text if the user investigates the table.
                print("\nThe table looks nice and sturdy. Much like your ego.\n")
            elif 'vent' in command:
                # Run VENT() if the user investigates the vent.
                vent()
            else:
                print("\nYou cannot investigate that.\n")   
                
        elif command == 'location':
            # Describe the user's surroundings.
            print("\nYou are in the sleeping space where there are rows of beds, tables, and maybe\nsome other things. George, the cook, is lying on one of the beds.\n")
            
        elif command == 'inventory':
            # Print the user's inventory.
            print("\n", inventory, "\n")             
            
        elif command == 'ship':
            # Display a list of discovered/undiscovered rooms.
            ship()
            
        elif 'talk' in command:
            if 'George' or 'george' in command:
                # Dialogue with George
                if not talkedGeorge:
                    # Print this if the user hasn't talked to George yet.
                    print ("\nGeorge: 'Hey boss, how ya feeling?'\n")
                    talkedGeorge = True  
                else:
                    # Print this if the user has already talked to George.
                    print ("\nGeorge: 'You managed to pry that traitorous turtle out of his shell\nyet, boss?'\n") 
            else:
                print("\nYou cannot do that.\n")   
            
        elif 'goto' or 'go to' in command:
            # Go to a specified room.
            goto(command)      
            
        else:
            print("\nYou cannot do that.\n")
            
    return

            
def bathrooms():
    """This is the function for the bathrooms."""
    global beenToBathroom
    global inventory 
    global condition
    
    introtext = "\nYou are in the bathrooms. There is a stall, a shower, and a sink. Go investigate!\n"
    print(introtext)
    
    beenToBathroom = True
    
    while not condition:
        # Get user input while CONDITION is false (turns true when game ends).
        command = input("Enter a command: ")
        if command == 'help':
            # Print a list of possible actions.
            helpList() 
            
        elif 'investigate' in command:
            if 'stall' in command:
                # If the user wants to investigate the stall, run STALL().
                stall()
            elif 'shower' in command:
                # If the user wants to investigate the shower, run SHOWER().
                shower()
            elif 'sink' in command:
                # If the user wants to investigate the sink, run SINK().
                sink()
            else:
                print("\nYou cannot investigate that.\n")
        
        elif command == 'inventory':
            # Print a list of the user's inventory.
            print("\n", inventory, "\n")
            
        elif command == 'location':
            # Describe the user's surroundings.
            print(introtext)
            
        elif command == 'ship':
            # Display a list of discovered/undiscovered rooms.
            ship()
            
        elif 'goto' or 'go to' in command:
            # Go to a specified room.
            goto(command)
            
        else:
            print("\nYou cannot do that.\n")
            
    return
                
def stall():
    """This is the function for the stall in the bathroom."""
    global inventory
    global condition
    
    # Describe the stall depending on what the user has already taken from the stall.
    if 'screwdriver' in inventory:
        print("\nIt looks like a normal stall.\n")
    else:
        print("\nIt looks like a normal stall. But wait...there's something in the toilet.\nIs that a sonic screwdriver?\n")
        
    while not condition:
        # Get user input while CONDITION is false (turns true when game ends).
        command = input("Enter a command: ")
        if command == 'help':
            # Print a list of possible commands.
            helpList()

        elif 'take' in command:
            if 'screwdriver' in command:
                # Add the screwdriver to the inventory unless it is already there.
                if 'screwdriver' in inventory:
                    print("\nThe screwdriver is already in your inventory.\n")
                else:
                    inventory.append('screwdriver') 
                    print("\nThe sonic screwdriver is now in your inventory.\n")
            else:
                print("\nYou cannot take that.\n")
                
        elif 'investigate' in command:
            if 'shower' in command:
                # If the user wants to investigate the shower, run SHOWER().
                shower()
            elif 'sink' in command:
                # If the user wants to investigate the sink, run SINK().
                sink()
            elif 'stall' in command:
                # If the user wants to investigate the stall, run STALL().
                stall()
            else:
                print("\nYou cannot investigate that.\n")
            
        elif command == 'inventory':
            # Print a list of the user's inventory.
            print("\n", inventory, "\n")
            
        elif command == 'location':
            # Describe the user's surroundings.
            print("\nYou are in a stall in the bathrooms.\n")
            
        elif command == 'ship':
            # Display a list of discovered/undiscovered rooms.
            ship()
            
        elif 'goto' or 'go to' in command:
            # Go to a specified room.
            goto(command)  
            
        else:
            print("\nYou cannot do that.\n")
            
    return

                
def shower():
    """This is the function for the shower in the bathroom."""
    global inventory
    global condition
    
    # Describe the shower depending on what the user has already taken from the shower.
    if 'shampoo' in inventory:
        print("\nIt's a normal shower (but it might be a good idea to stay away from the\ncurtain).\n")
    else:
        print("\nIt's a normal shower (but it might be a good idea to stay away from the\ncurtain). Someone appears to have left their shampoo behind.\n")
        
    while not condition:
        # Get user input while CONDITION is false (turns true at end of game).
        command = input("Enter a command: ")
        if command == 'help':
            # Print a list of possible actions.
            helpList()  
            
        elif 'take' in command:
            if 'shampoo' in command:
                # Add shampoo to the inventory if it is not already there.
                if 'shampoo' in inventory:
                    print("\nThe shampoo is already in your inventory.\n")
                else:
                    inventory.append('shampoo')
                    print("\nThe shampoo has been added to your inventory.\n")
            else:
                print("\nYou cannot take that.\n")
                    
        elif 'investigate' in command:
            if 'stall' in command:
                # If the user wants to investigate the stall, run STALL().
                stall()
            elif 'sink' in command:
                # If the user wants to investigate the sink, run SINK().
                sink()
            elif 'shower' in command:
                # If the user wants to investigate the shower, run SHOWER().
                shower()
            else:
                print("\nYou cannot investigate that.\n")
            
        elif command == 'inventory':
            # Print a list of the user's inventory.
            print("\n", inventory, "\n")
            
        elif command == 'location':
            # Describe the user's surroundings.
            print("\nYou are in a shower in the bathrooms.\n")
            
        elif command == 'ship':
            # Display a list of discovered/undiscovered rooms.
            ship()
            
        elif 'goto' or 'go to' in command:
            # Go to a specified room.
            goto(command)
                
        else:
            print("\nYou cannot do that.\n")
            
    return
            
def sink():
    """This is the function for the sink in the bathroom."""
    global inventory
    global condition
    
    # Describe the sink depending on what the user has already taken from the sink.
    if 'toothbrush' in inventory:
        print("\nSomeone left the water running in the sink. That's not very sustainable.\n")
    else:
        print("\nSomeone left the water running in the sink. That's not very sustainable.\nThere is also a mirror and a toothbrush.\n")
    
    while not condition:
        # Get user input while CONDITION is false (turns true at end of game).
        command = input("Enter a command: ")
        if command == 'help':
            # Print a list of possible actions.
            helpList()   
            
        elif 'take' in command:
            if 'toothbrush' in command:
                # Add the toothbrush to the inventory unless it is already there.
                if 'toothbrush' in inventory:
                    print("\nThe toothbrush is already in your inventory.\n")
                else:
                    inventory.append('toothbrush')  
                    print("\nThe toothbrush is now in your inventory.\n")
            else:
                print("\nYou cannot take that.\n")
                    
        elif 'investigate' in command:
            if 'stall' in command:
                # If the user wants to investigate the stall, run STALL().
                stall()
            elif 'shower' in command:
                # If the user wants to investigate the shower, run SHOWER().
                shower()
            elif 'sink' in command:
                # If the user wants to investigate the sink, run SINK().
                sink()
            else:
                print("\nYou cannot investigate that.\n")
            
        elif command == 'inventory':
            # Print a list of the user's inventory.
            print("\n", inventory, "\n")
            
        elif command == 'location':
            # Describe the user's surroundings.
            print("\nYou are standing at a sink in the bathrooms.\n")
            
        elif command == 'ship':
            # Display a list of discovered/undiscovered rooms.
            ship()
            
        elif 'goto' or 'go to' in command:
            # Go to a specified room.
            goto(command)        
        
        else:
            print("\nYou cannot do that.\n")
            
    return

def shieldRoom():
    """This is the function for the shield room."""
    global herbertHasPass
    global herbertInShieldRoom
    global firstTimeShieldRoom
    global inventory
    global engineAccess
    global gaveToJosh
    global condition
    
    # Describe the shields room depending on whether or not the user has been there before and whether or not Herbert is in there.
    if firstTimeShieldRoom == False:
        if herbertInShieldRoom == True:
            print("\nYou're back in the shields room. There are a bunch of levers and\nother complicated stuff that is hard to understand. There are cables\nsticking out of the shields control panel. There is also a green\nbutton on the shields control panel. At the moment, they're all out of reach,\nthough. You see Herbert and his trapdoor, but he might not let you near his room.\n")
        elif herbertInShieldRoom == False:
            print("\nYou're in the shield room. There are a bunch of levers and other\ncomplicated stuff that is hard to understand. There are cables\nsticking out of the shields control panel. There is also a green\nbutton on the shields control panel. At the moment, they're all out of reach,\nthough. Herbert's not here. His trapdoor is open and you see that he has obviously been hoarding lots of stuff.\n")
            
    elif firstTimeShieldRoom == True:
        print("\nYou made it to the shields room! There are a bunch of levers and other\ncomplicated stuff that is hard to understand. There are cables sticking\nout of the shields control panel. There is also a green button on the\nshields control panel. At the moment, they're all out of reach, though.\nYou hear a rustle under one of the floorboards. An old man pops out of a\ntrapdoor! It appears as if he has been secretly living here for many years.\nYou get a peek under the trapdoor and it appears as if he has been hoarding\nlots of stuff. You are accosted by the old man.")
        print("\nOld Man: 'Heyo! Look what the tides washed in. My name is\nHerbert. You know captain, your shield engineer is one dumb guy. He\ncomes in here every once in a while tryin to fix the shields. He\nusually makes them worse! HAH, you don't know it, but I've been the\none actually fixing the shields. I been down here so long, I know\nevery inch of this ship. But I'll say I get often hungry down\nhere. You don't suppose you could get me some food could you?'\n")
        firstTimeShieldRoom = False        
    
    while not condition:
        # Get user input while CONDITION is false (turns true at end of game).
        command = input("Enter a command: ")
        if command == 'help':
            # Print a list of possible commands.
            helpList()       
            
        elif "investigate" in command:
            if "trap" and "door" in command:
                # If the user wants to investigate the trap door, run TRAPDOOR().
                trapDoor()                
            elif "control panel" in command:
                # Print text if the user investigates the control panel.
                print("\nYou investigate the control panel and find out there is\nseemingly nothing wrong with it.\n")
            elif "button" in command:
                # Print text if the user investigates the button.
                print("\nThe button is very green. It might be best not to touch it, though.\n")
            elif "cable" in command:
                # Print text if the user investigates the cables.
                print("\nWow! those cables are really tangled!\n")
            elif "lever" in command:
                # Print text if the user investigates the lever.
                print("\nThese look really important, better not mess with them unless you want to die.\n")        
            else:
                print("\nYou cannot investigate that.\n")
                        
        elif 'talk' in command:
            # Print one of two different dialogues with Herbert depending on whether or not the user has given him the meal pass.
            if 'old man' or 'Herbert' or 'herbert' in command and herbertInShieldRoom:
                if herbertHasPass == False:
                    print("\nHerbert: 'Can you work on getting me that food?'\n")
                elif herbertHasPass == True:
                    print("\nHerbert: 'Get me my darn toothbrush and I'll show a secret passage into\nthe engine room.'\n")    
            else:
                print("\nYou cannot do that.\n")
                
        elif command == "inventory":
            # Print a list of the user's inventory.
            print("\n", inventory, "\n")
            
        elif command == 'ship':
            # Display a list of discovered/undiscovered rooms.
            ship()
            
        elif command == 'location':
            # Describe the user's surroundings.
            print("\nYou're back in the shields room. There are a bunch of levers and\nother complicated stuff that is hard to understand. There are cables\nsticking out of the shields control panel. There is also a green\nbutton on the shields control panel.\n")   
            
        elif "give" in command:
            if 'old man' or 'Herbert' or 'herbert' in command:
                # If the user gives Herbert the meal pass, change HERBERTHASPASS to equal "True", remove the meal pass from the inventory, and print text.
                if "pass" in command and "pass" in inventory:
                    herbertHasPass = True
                    inventory.remove("pass")
                    print("\nHerbert: 'Thank you for this meal pass! Now I can eat anything I\nwant, but... Well you see I haven't brushed my teeth in years. I could\nreally use a toothbrush.'\n\nYou: 'I can't play your games, I really need to find a way into the engine room!'\n\nHerbert: If you bring me a toothbrush I can take you through a secret tunnel into the engine room.'\n")
                elif "toothbrush" in command and "toothbrush" in inventory and herbertHasPass:
                    # If the user gives Herbert the toothbrush, remove the toothbrush from the inventory, print text, change ENGINEACCESS to equal "True", change HERBERTINSHIELDROOM to equal "False", and run ENGINEROOM().
                    inventory.remove("toothbrush")
                    print("\nHerbert takes the toothbrush and stashes it away in his secret\nroom. Afterward, as promised, he takes you through a secret tunnel\nto the engine room.")
                    engineAccess = True
                    herbertInShieldRoom = False
                    engineRoom()  
                else:
                    print("\nYou cannot do that.\n")
            else:
                print("\nYou cannot do that.\n") 
                
        elif "goto" or "go to" in command:
            # Go to a specified room.
            goto(command)          
                
        else:
            print("\nYou cannot do that.\n")
                  
    return
 
def trapDoor():
    """This function is for the trap door in the shields room."""
    global inventory
    global engineAccess
    global herbertInShieldRoom
    global herbertHasPass
    global gaveToJosh
    global condition
    
    print("\nUpon further investigation of the trapdoor you discover a\nspace under the floor that Herbert has been living in all these\nyears. You look around and see his bed with a blanket on\ntop. It is bulging a little. He has a shelf with lots of books\non it. You see a pile of junk in the corner including a\ntrinket, a hat, and an old piece of pizza.\n")
    
    while not condition:
        # Get user input while CONDITION is false (turns true at end of game).
        command = input("Enter a command: ")
        if command == 'help':
            # Print a list of possible actions.
            helpList()
            
        if 'investigate' in command:
            if 'blanket' in command:
                # Print text if the user investigates the blanket.
                print("\nIt looks like there's a teddy bear under the blanket.\nIs that Josh's?\n")
            elif 'shelf' in command:
                # Print text if the user investigates the shelf.
                print("\nThere are a lot of books- Herbert looks like a pretty studious guy.\nIt might be better to leave them be.\n")
            elif "trap" and "door" in command:
                # If the user investigates the trap door, run TRAPDOOR().
                trapDoor()                
            elif "control panel" in command:
                # Print text if the user investigates the control panel.
                print("\nYou investigate the control panel and find out there is\nseemingly nothing wrong with it.\n")
            elif "button" in command:
                # Print text if the user investigates the button.
                print("\nThe button is very green. It might be best not to touch it, though.\n")
            elif "cable" in command:
                # Print text if the user investigates the cables.
                print("\nWow! those cables are really tangled!\n")
            elif "lever" in command:
                # Print text if the user investigates the lever.
                print("\nThese look really important, better not mess with them unless you want to die.\n")                 
            else:
                print("\nYou cannot investigate that.\n")
                
        elif command == 'inventory':
            # Print a list of the user's inventory.
            print("\n", inventory, "\n")        
                
        elif command == 'ship':
            # Display a list of discovered/undiscovered rooms.
            ship()                
                
        elif "take" in command:
            if "trinket" in command:
                # Add the trinket to the inventory unless it is already there.
                if 'trinket' in inventory:
                    print("\nThe trinket is already in your inventory.\n")
                else:
                    inventory.append('trinket')
                    print("\nThe trinket is now in your inventory.\n")
            elif 'hat' in command:
                # Add the hat to the inventory unless it is already there.
                if 'hat' in inventory:
                    print("\nThe hat is already in your inventory.\n")
                else:
                    inventory.append('hat')
                    print("\nGreat, you took a poor old man's hat. The hat is in your inventory.\n")
            elif 'pizza' in command:
                # Print text if the user tries to take the pizza.
                print("\nGross. You should probably leave that for Herbert.\n")
            elif "teddy bear" in command:
                # Add the teddy bear to the inventory unless it is already there.
                if "teddy bear" in inventory:
                    print("\nThe teddy bear is already in your inventory.\n")
                else:
                    inventory.append('teddy bear')
                    print("\nThe teddy bear is now in your inventory.\n")             
            else:
                print("\nYou cannot take that.\n")
                
        elif 'talk' in command:
            # Print one of two possible dialogues with Herbert depending on whether or not he has the meal pass.
            if 'old man' or 'Herbert' or 'herbert' in command and herbertInShieldRoom: 
                if herbertHasPass == False:
                    print("\nHerbert: 'Can you work on getting me that food?'\n")
                elif herbertHasPass == True:
                    print("\nHerbert: 'Get me my darn toothbrush and I'll show a secret passage into\nthe engine room.'\n") 
            else:
                print("\nYou cannot do that.\n")
                      
        elif "give" in command:
            if 'old man' or 'Herbert' or 'herbert' in command:
                # Give Herbert the meal pass, change HERBERTHASPASS to equal "True", remove the meal pass from the inventory, and print text.
                if "pass" in command and "pass" in inventory:
                    herbertHasPass = True
                    inventory.remove("pass")
                    print("\nHerbert: 'Thank you for this meal pass! Now I can eat anything I\nwant, but... Well you see I haven't brushed my teeth in years. I could\nreally use a toothbrush.'\n\nYou: 'I can't play your games, I really need to find a way into the engine room!'\n\nHerbert: If you bring me a toothbrush I can take you through a secret tunnel into the engine room.'\n")
                elif "toothbrush" in command and "toothbrush" in inventory and herbertHasPass:
                    # Give Herbert the toothbrush, remove the toothbrush from the inventory, print text, change ENGINEACCESS to equal "True" and HERBERTINSHIELDROOM to equal "False" and then run ENGINEROOM().
                    inventory.remove("toothbrush")
                    print("\nHerbert takes the toothbrush and stashes it away in his secret\nroom. Afterward, as promised, he takes you through a secret tunnel\nto the engine room.")
                    engineAccess = True
                    herbertInShieldRoom = False
                    engineRoom()  
                else:
                    print("\nYou cannot do that.\n")
            else:
                print("\nYou cannot do that.\n") 
                
        elif command == 'ship':
            # Display a list of discovered/undiscovered rooms.
            ship()
            
        elif command == 'location':
            # Describe the user's surroundings.
            print("\nYou're back in the shields room. There are a bunch of levers and\nother complicated stuff that is hard to understand. There are cables\nsticking out of the shields control panel. There is also a green\nbutton on the shields control panel.\n")
            
        elif "goto" or "go to" in command:
            # Go to a specified room.
            goto(command) 
            
        else:
            print("\nYou cannot do that.\n")
            
    return
           

def engineRoom():
    """This is the function for the engine room."""
    global inventory
    global intercom
    global engineAccess
    global gaveToJosh
    global fixed
    global condition    
    
    # Give a description of the room depending on whether or not the intercom is fixed.
    introtext1 = "\nYou are in the engine room. Against the far wall you see a table\ncontaining a control panel that controls the engines, which are visible on\neither side of the panel. On the wall above your head is a broken intercom. Against another\nwall you see a maintenance hatch. That looks dangerous!\n"
    introtext2 = "\nYou are in the engine room. Against the far wall you see a table\ncontaining a control panel that controls the engines, which are visible on\neither side of the panel. On the wall above your head is the now functional intercom! Against\nanother wall you see a maintenance hatch. That looks dangerous!\n"
    if not fixed:
        print(introtext1)
        
    if fixed:
        print(introtext2)
    
    # Print further description depending on whether or not Josh has the teddy bear.
    if not gaveToJosh and not fixed:
        print("Suddenly, you get an idea! Maybe if you could figure out a way to fix the intercom,\nyou could call the co-captain in the cockpit and threaten to turn off the engines if he won't\nsurrender the ship to you.\n")
    
    if gaveToJosh and not fixed:
        intercom = True
        print("You show Josh the intercom.\nJosh: 'Yeah, I should be able to fix this. Hold on one second.'\nJosh fixes the intercom. You can now use it to call the co-captain in the cockpit! If you threatened\nto turn off the engines, that might convince him to turn over control of the ship.\n")  
        fixed = True
    
    while not condition:
        # Get user input while CONDITION is false (turns true at end of game).
        command = input("Enter a command: ")
        if command == 'help':
            # Print a list of possible actions.
            helpList()  
                
        elif 'investigate' in command:
            if 'intercom' in command and not intercom:
                # Print text if the intercom is broken and change BEENTOENGINEROOM to equal "True".
                print("\nThe intercom is broken. Maybe someone on the ship would be able to fix it.\n")
                beenToEngineRoom = True
            elif 'intercom' in command and intercom:
                # Print text if the intercom is fixed.
                print("\nThe intercom is fixed! You can call the co-captain now.\n")
            elif 'hatch' in command:
                
                #if the user has TRINKET in their inventory, text will be printed describing the near-death experience that the user's character just had.
                
                if "trinket" in inventory:
                    print("\nYou open the maintenance hatch and are instantly sucked out into the\nvacuum of space. Just as you realize that you have no hope, the\ntrinket in your pocket wiggles a bit and flies out of your pocket.\nUsing the last reserves of your willpower, you grab onto it in the\nhopes that it might take you back to the ship. The little trinket\nzooms straight towards the maintenance hatch and deposits you\nthere. As you watch the erratic little thing fly away, you notice a\npiece of paper on the engine room floor. You pick it up.\n\n'So long, and thanks for all the fish! - Sincerely, The Dolphins'\n")
                    
                # However, if the user does not have TRINKET in their inventory, the game ends instantly for the user when they investigate the hatch. It changes CONDITION to equal "True", prints text describing the user's blunder, and ends the game.
                elif "trinket" not in inventory:
                    condition = True
                    print("\nYou open the maintenance hatch and are instantly sucked out into the\nvacuum of space. Since no one sees you get sucked out, you are\ncondemned to float aimlessly through the dark void eternally...\nJust kidding. The pressure imbalance will make you swell up to twice your\nnormal size, your lungs will rupture, and you will soon\ndie from a lack of oxygen.")
                    print("\nFIN")
            elif 'control' or 'panel' in command:
                # Print text if the user investigates the control panel.
                print("\nThe control panel controls the engines. Call the co-captain before you turn\nthem off, though!\n")
            else:
                print("\nYou cannot investigate that.\n")
                
        elif 'use' in command:
            if 'intercom' in command and intercom:
                # Take control of the ship once again if the user uses the intercom and INTERCOM is true.
                print("\nYou: 'Alright, I made it to the engine room. If you don't turn the ship back over to me, I'll\nturn off the engines.'\nCo-captain: 'No! Don't do that. You can have the ship back.'\nAll of the doors unlock! You safely enter the cockpit and regain control of the ship.")
                finalbattle()
            elif 'intercom' in command and not intercom:
                # If the user tries to use the intercom while it is broken, print the following text.
                print("\nThe intercom is broken.\n")
            else:
                print("\nYou cannot use that.\n")
                
        elif command == 'inventory':
            # Print a list of the user's inventory.
            print("\n", inventory, "\n")
                
        elif command == 'location' and not fixed:
            # Describe the user's surroundings depending on whether or not the intercom is fixed.
            print(introtext1)
            
        elif command == 'location' and fixed:
            print(introtext2)
            
        elif command == 'ship':
            # Display a list of discovered/undiscovered rooms.
            ship()
            
        elif 'goto' or 'go to' in command:
            # Go to a specified room.
            goto(command)
            
        else:
            print("\nYou cannot do that.\n")
            
    return

                       
def helpList():
    """Displays a list of commands. CRED: GABE"""
    
    print("\nThese commands correspond to the following actions:\n\ngoto [room]: Type goto along with the name of the room if\nyou want to go to if you want to move there.")
    
    print("\ninvestigate [object]: Provides a more detailed description of an object.")
    
    print("\ntake [object]: Puts an object in your inventory.")
    
    print("\ntalk [person]: Starts up a conversation with that person.")
    
    print("\ngive [person] [item]: Gives that person the specified item.")
    
    print("\nuse [item]: Uses that item.")
    
    print("\nlocation: Describes your surroundings.")
    
    print("\nship: Tells you which parts of the ship you have discovered.")
    
    print("\ninventory: Prints your current inventory.\n")
    
    return

    
def ship():
    """Prints a list of the rooms in the ship and whether or not they have been discovered."""
    if beenToDining == True:
        print("\nDining Hall: Discovered")  
    elif beenToDining == False:
        print("\nDining Hall: Undiscovered")
    if beenToBathroom == False:
        print("\nBathroom: Undiscovered")
    elif beenToBathroom == True:
        print("\nBathroom: Discovered")
    if beenToSleeping == True:
        print("\nSleeping Space: Discovered")    
    elif beenToSleeping == False:
        print("\nSleeping Space: Undiscovered")
    if shieldAccess == True:
        print("\nShields Room: Discovered")
    elif shieldAccess == False:
        print("\nShields Room: Undiscovered")
    if engineAccess == True:
        print("\nEngine Room: Discovered\n")
    elif engineAccess == False:
        print("\nEngine Room: Undiscovered\n") 
        
    return


def goto(com):
    """Moves the user to the room specified by COM."""
    global shieldAccess
    global engineAccess
    
    if 'living' in com:
        livingQuarters()
    elif 'dining' in com:
        diningHall()
    elif 'sleep' in com:
        sleepingSpace()
    elif 'bathroom' in com:
        bathrooms()
    elif 'shield' in com and shieldAccess:
        shieldRoom()
    elif 'engine' in com and engineAccess:
        engineRoom()
    else:
        print("\nYou cannot do that.\n")
        
    return

#def quit():
    #"""This function allows the user to quit the game at any time."""
    #global condition
    
    #option = input("Are you sure you want to quit? (Yes or No) ")
    #option.lower()
    
    ##Takes the user's input. If the user inputs YES, CONDITION is set to True and thus all the while loops end. If the user inputs NO, the quit function ends 
    
    #if option == "yes":
        #condition = True
        
    #elif option == "no":
        #return

def talkJosh():
    """This is a function for the user's dialogue with Josh."""
    global talkedJosh
    global talkedJosh2
    global engineAccess
    
    if 'Josh' or 'josh' or 'repairman' in command:
        # Dialogue with Josh
        if engineAccess and not talkedJosh2:
            # If the user is asking about fixing the intercom for the first time, display this
            print("\nJosh: 'The intercom, huh? Yeah, I bet I could fix it. Wait...would we have to go through\nthe shield room? No I can't do that. That place creeps me out. I always feel some sort of paranormal\nspirit when I'm in there. If you could find my lucky teddy bear, though, I would consider it.'\n")
            talkedJosh2 = True
                        
        elif engineAccess and talkedJosh2:
            # Display this if the user is talking to Josh after the initial dialogue about the intercom
            print("\nJosh: 'Have you found my teddy bear yet?'\n")
                    
        elif not talkedJosh and not engineAccess:
            # Display this if the user is talking to Josh for the first time
            print("\nJosh: 'Hey Cap, looks like you had a nasty fall. Shame I can't fix\npeople- HAR HAR.'\n")
            talkedJosh = True		    
                
        elif talkedJosh and not engineAccess:
            # Display this if the user is not asking about the intercom and has talked to Josh before
            print("\nJosh: 'Have you given that traitor what he deserves yet?'\n")  
                    
    else:
        print("\nYou cannot do that.\n")    

    
def finalbattle():
    """A function detailing the rock/paper/scissors-like final battle, as well as the various endings."""
    
    global condition
    
    print("\nJust as victory has been achieved, the first mate gets your attention.\n'Captain! We're recieving a comms transmission!' You pick up the\nreciever to hear what sounds like Donald Duck playing a trumpet.\n'Hello Earthlings. We would like to inform you that your ship will soon\nbe scrap. As for the traitor amongst your ranks: you will be given a true hero's death.'\nYou call for all systems to be powered up and ready, sensing that\nthis battle might be your last.\n")
    
    print("Instructions for SPACE BATTLES: You can boost your Shields by typing in\n'shields', activate your cloaking device by typing in 'cloak', and fire\nyour artillery cannons by typing in 'artillery'. Shields beat Artillery,\nCloak beats Shields, and Artillery beats Cloak. Good Luck!\n")
    
    
    options = ["shields","cloak","artillery"]
    
    wins = 0
    
    losses = 0
    
    command = input("What will you do first? ")
    
    while not condition:
        # Repeat the game until CONDITION is true.
        
        # Choose a random move from "shields", "cloak", and "artillery" for the aliens to execute.
        aliennum = random.randint(0,2)
        
        alienresponse = options[aliennum]
        
        command = command.lower()
        
        if command in options:
            
            # What happens if the user inputs "shields" as their command:
            if "shields" in command:
                if alienresponse == "shields":
                    # Tie
                    print("\nYou both activate your shields! Nothing happens.\n")
                    
                    command = input("What are your orders, Captain? ")
                
                if alienresponse == "cloak":
                    # The user loses
                    print("\nYou put up your shields, but the alien ship cloaks and then\ncounterattacks!\n")
                    
                    losses = losses + 1
                
                    command = input("What are your orders, Captain? ")
                
                if alienresponse == "artillery":
                    # The user wins
                    print("\nThe alien ship fires its artillery but their beams can't get to\nyour hull! You successfully counterattack.\n")
                    
                    wins = wins + 1
                
                    command = input("What are your orders, Captain? ")
                
            # What to do if the user inputs "cloak" as their command:
                
            elif "cloak" in command:
                if alienresponse == "shields":
                    # The user wins
                    print("\nThe alien ship boosts their shields but lose track of your ship\nwhen you cloak. You now uncloak and successfully counterattack!\n")
                
                    wins = wins + 1
                
                    command = input("What are your orders, Captain? ")
                
                if alienresponse == "cloak":
                    # Tie
                    print("\nYou both activate your cloaking mechanisms! Nothing happens\n")
                
                    command = input("What are your orders, Captain? ")
                
                if alienresponse == "artillery":
                    # The user loses
                    print("\nThe alien ship fires its artillery and their beams directly hit your hull!\n")
                
                    losses = losses + 1
                
                    command = input("What are your orders, Captain? ")
                
            # What to do if the user inputs "artillery" as their command.
                
            elif "artillery" in command:
                if alienresponse == "shields":
                    # The user loses
                    print("\nYou fire your artillery but your beams can't get through their\nshields! They swiftly counterattack while your weapons are cooling down.\n")
                
                    losses = losses + 1
                
                    command = input("What are your orders, Captain? ")
                
                if alienresponse == "cloak":
                    # The user wins
                    print("\nThe alien ship cloaks but that won't stop you! Your artillery\nbeams make a direct hit onto their hull.\n")
                
                    wins = wins + 1
                
                    command = input("What are your orders, Captain? ")
                
                if alienresponse == "artillery":       
                    # Tie
                    print("\nYou both fire a barrage of high-powered laser beams, but at the spot\nin between your ships where they meet they are completely out of\nphase, and so cancel each other out.\n")
                
                    command = input("What are your orders, Captain? ")
                    
            # Ending and final choice      
                   
            if wins == 3:
                # If the user wins three games, they decide to save or leave the aliens. Descriptive text is printed accordingly.
                print("\nYour last attack breached their hull! You see the life signs on the\nalien ship start to fade. At this point, you have to ask yourself: do\nthey really deserve it?\n")
            
                choice = input("Will you save them or leave them? ")
            
                if choice == 'save them':
                    print("\nRegretfully you send your crew out in puddlejumpers to gather\nwhat survivors you can. Your crew informs you that they have\nfound the alien captain, Zorglog. You order them to bring him up\nto the cockpit.\n\nUpon arrival, Zorglog apologizes profusely for\nhis actions and begs for your forgiveness. When you grant it, the\notherworldy captain explains that he can reveal the secrets behind\nmany technologies known only to Xanaloids like\nhimself. You see a bright future ahead, with Humans and Xanaloids\nworking together and prospering.\n")
                    condition = True
                
                if choice == 'leave them':
                    print("\nAs the aliens are blasted from the confines of their ship in to\nthe dark, cold depths of space, you coast your way back home with\nACDC's 'Back in Black' blasting over the ship's intercom.\n")
                    condition = True
                
            if losses == 3:
                # If the user loses three games, they choose either slavery or death and descriptive text is printed accordingly.
                print("\nYou attempt to use your",command,"but the aliens fire an EMP weapon that\ncompletely disables every system on your ship. The alien captain boards your ship and offers you a choice:\n")
            
                finalchoice = input("Do you choose slavery or do you choose death? ")
            
                if finalchoice == "slavery":
                
                    print("\nAs the aliens prepare to board your ship and consign you and your crew\nmembers to a life of slavery, you wonder if becoming a captain was the best\ncareer choice. Then, out of a wormhole from the Nebulon-5 galaxy, a pod of\nspace whales comes to the rescue and eats the alien ship whole! Miraculously,\nthey miss your ship entirely. You count your lucky stars and hope\nnone of whales goes by the name Moby Dick.\n")
                    condition = True
            
                elif finalchoice == "death":
                
                    life = 10
                
                    result = random.randint(0,10)
                
                    if result == life:
                        print("\nDue to incredible luck, you made it out alive.\n")
                        condition = True
                
                    else:
                        print("\nYou died! lol\n")
                        condition = True
            
                else:
                    
                    #If the user misspells death or slavery they recieve this ending:
                    
                    print("\n'Their so-called Captain is completely unintelligible. Looks to be frothing\nat the mouth already. Well, we'd best put them out of their misery.'\nThe aliens beam back to their ship and fire a full salvo of weapons: nukes,\n high-powered lasers, even mini black holes. Right before the bombs detonate, you\nthink to yourself, 'If only I knew how to spell.'\n")
                    condition = True
                    
        elif command not in options:
            
            #if the user misspells "shield," "artillery," or "cloak," they get one loss:
            
            print("\nYou sit there and do nothing as the alien ship hits you with a\ndevastating attack!\n")
            
            losses = losses + 1
            
            command = input("What are your orders, Captain? ")        
                       
    print("FIN")
        
    return

main()



