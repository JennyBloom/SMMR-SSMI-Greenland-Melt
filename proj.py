#------------------------------------------------------------------------------
# Project 1 CSCI1310: Designed and developed in 2015
# - Jenny Bloom with help from Collin Duncan
# - Data source: National Snow and Ice Data Center, Waleed Abdalati
# - Preprocessed XPGR files: by Jenny Bloom with Mike MacFerrin
# - This code opens 365 image .tif files of Greenland for 2007.
# - It then reads each pixel and each image and classifies to a threshold
# - Threshold indicates melting pixels. Melted count is stored in .txt output.
# - User prompted to explore melt by month for 2007.
#------------------------------------------------------------------------------



import os
try:
    from PIL import Image
except ImportError:
    print ("PIL import failed forever") #if modules not found, user prompted
    quit()
try:
    from progress.bar import Bar
except ImportError:
    print ("Please install Progress 1.2 or higher and try again")
    quit()

months = {} #Create universe (dictionary of months)
has_run = 0 #Allows for progress bar to count file iterations.

def main():

    os.system("clear") #Keep it clean, unlike my life.

    print ("\n---LEGEND---\n") #Legend for user prompt choices of months.
    print ("[jan]uary\n[feb]ruary\n[mar]ch\n[apr]il\n[may]\n[jun]e\n[jul]y\n[aug]ust\n[sep]tember\n[octb] - october\n[nov]ember\n[dec]ember\n[total]\n")
    var = input("Enter your selection acording to the codes above,\nor type [Q] to Quit: ") #user input is variable, var.
    if var == "Q" or var == "q": #quit if user selects Q.
        if has_run == 0:
            quit()
        else:
            log_output()
            quit()
    elif var not in months:
        if has_run == 0:
            print (process(var))
            input("\nPress any key to continue...")
            main()
        else:
            print ("Error: Variable incorrect, please try again.")
            input("\nPress any key to continue...")
            main()
    else:
        print (process(var))
        input("\nPress any key to continue...")
        main()

    return

def process(arg):

    if has_run != 0:
        if arg == "total":
            return str("The total melted pixels are: " + str(months[arg]) + "\nTotal area melted in km^2: " + str(months['area']))
        else:
            return str(months[arg])
    else:
        pass

    threshold = float(-0.0158) #Minimum threshold to define a melting pixel
    current = os.getcwd() #Get current working directory and store to variable
    melt = 0 #Set counters
    fnum = 0
    jan = feb = mar = apr = may = jun = jul = aug = sep = octb = nov = dec = 0

    for grub in os.listdir(current):
        if grub.endswith(".tif"):
            fnum +=1 #Find number of files for max value for loading bar

    coords = [] #Initialize lists for later
    totalmelt = []

    bar = Bar('Processing', fill=bytes((219,)).decode('cp437'), suffix=str(fnum)+" FILES", max=fnum) #initialize loading bar

    for file in os.listdir(current): #Iterate through working dir
        if os.path.exists(file):
            if file.endswith(".tif"): #Make sure we're using the right files
                fname = os.path.splitext(file)[0]
                day = fname[4:7] #Extract individual day from filename
                im = Image.open(file)
                melt = 0
                for x in range(0,60):
                    for y in range(0,109):
                        p = round(im.getpixel((x,y)), 4) #Store location of current pixel into var p
                        if p >= threshold:
                            combined = str(x) + "-" + str(y) #Combine pixel axis into single string location and...
                            if combined not in coords: #...check to see if we've done this pixel yet if it's melting
                                melt += 1
                                coords.append( combined )
                totalmelt.append( melt ) #Append the final melt value to a new lists of melt values to sum
                if int(day) <= 31:
                    jan += melt
                elif 32 <= int(day) <= 59:
                    feb += melt
                elif 60 <= int(day) <= 90:
                    mar += melt
                elif 91 <= int(day) <= 120:
                    apr += melt
                elif 121 <= int(day) <= 151:
                    may += melt
                elif 152 <= int(day) <= 181:
                    jun += melt
                elif 182 <= int(day) <= 212:
                    jul += melt
                elif 213 <= int(day) <= 243:
                    aug += melt
                elif 244 <= int(day) <= 273:
                    sep += melt
                elif 274 <= int(day) <= 304:
                    octb += melt
                elif 305 <= int(day) <= 334:
                    nov += melt
                else:
                    dec += melt
        else:
            path_err(file)
            quit()
        bar.next() #Increment loading bar

    bar.finish()
    total = sum(totalmelt) #...sum the list, giving us a yearly total of melted pixels

    months['jan'] = jan
    months['feb'] = feb
    months['mar'] = mar
    months['apr'] = apr
    months['may'] = may
    months['jun'] = jun
    months['jul'] = jul
    months['aug'] = aug
    months['sep'] = sep
    months['octb'] = octb
    months['nov'] = nov
    months['dec'] = dec
    months['total'] = total

    global has_run #Making global
    has_run = 1 #Reassigned to 1 so known it has been run

    global area
    area = melt_area(total)
    months['area'] = area

    if arg not in months:
        return str("Error: Variable incorrect, please try again.")
    elif arg == "total":
        return str("The total melted pixels are: " + str(months[arg]) + "\nTotal area melted in KM^2: " + str(area))
    else:
        return str(months[arg])

def melt_area(tea): #tea = new variable for total.
    annual_melt = int(tea * (25 ** 2))
    return annual_melt

def path_err(tried_file):
    print ("ERROR: File doesn't exist" + str(tried_file))
    return

def log_output():
    of = open("log.txt", "a") #appends the data, form of "w"
    of_size = os.path.getsize("log.txt")

    if of_size >= 327680000:
        of.truncate(0)
    else:
        pass

    of.write("\n")
    of.write("---OUTPUT LOG---")
    of.write("\n")
    of.write("- Jan: " + str(months['jan']) + "  -")
    of.write("\n")
    of.write("- Feb: " + str(months['feb']) + "  -")
    of.write("\n")
    of.write("- Mar: " + str(months['mar']) + "  -")
    of.write("\n")
    of.write("- Apr: " + str(months['apr']) + "  -")
    of.write("\n")
    of.write("- May: " + str(months['may']) + "  -")
    of.write("\n")
    of.write("- Jun: " + str(months['jun']) + "  -")
    of.write("\n")
    of.write("- Jul: " + str(months['jul']) + "  -")
    of.write("\n")
    of.write("- Aug: " + str(months['aug']) + "  -")
    of.write("\n")
    of.write("- Sep: " + str(months['sep']) + "  -")
    of.write("\n")
    of.write("- Oct: " + str(months['octb']) + "  -")
    of.write("\n")
    of.write("- Nov: " + str(months['nov']) + "  -")
    of.write("\n")
    of.write("- Dec: " + str(months['dec']) + "  -")
    of.write("\n")
    of.write("-      " + "      " + " -")
    of.write("\n")
    of.write("TOTAL: " + str(months['total']))
    of.write("\n")
    of.write("AREA MELTED in KM^2: " + str(months['area']))
    of.write("\n")
    of.write("---------------")
    of.close()
    return

main()
