__author__ = 'Nath'
#Health Statistics Program - written by pynetq 10/9/13
#This program will take in user input to compute various health stats used by
#health information management professionals V0.2

running = True

print "This is a program that will compute vital health statistics used by Health Information Management Professionals:"
print "As of now, this program can only compute Average Length of Stay(ALoS) -  Discharge Days / Total Discharges"
print "Average Daily Inpatient Census - Total Inpatient Service Days / Month"

compute_c = int(raw_input("\nPress 1 to compute Average Length of Stay || Press 2 to compute Average Daily Inpatient Census: "))

if compute_c == 1:
    print "\n---Average Length of Stay---"
    dischargeDays = float(raw_input("\nType in the number of Discharge Days: "))
    totalDischarges = float(raw_input("Type in the number of Total Discharges: "))

    ALOS = dischargeDays / totalDischarges

    print "%.1f" % ALOS+" days"

if compute_c == 2:
    print "\n---Average Daily Inpatient Census---"
    IPSD = float(raw_input("\nType in the total inpatient service days: "))
    month_p = raw_input("Type in the first 3 letter of the month: ")
    month_p = month_p.capitalize()
    months = {"Jan": 31, "Feb": 28, "Mar": 31, "Apr": 30, "May": 31, "Jun": 30, "Jul": 31, "Aug": 31, "Sep": 31, "Oct": 31, "Nov": 30, "Dec": 31}
    ADIC = IPSD / months[month_p]
    print "%.1f" % ADIC+" days"

while running == True:
    choice = raw_input("Would you like to enter another string? type yes or no: ")
    choice = choice.lower()
    if choice[0] == "y":
        running == True
        compute_c = int(raw_input("\nPress 1 to compute Average Length of Stay || Press 2 to compute Average Daily Inpatient Census: "))

        if compute_c == 1:
            print "\n---Average Length of Stay---"
            dischargeDays = float(raw_input("\nType in the number of Discharge Days: "))
            totalDischarges = float(raw_input("Type in the number of Total Discharges: "))
            ALOS = dischargeDays / totalDischarges
            print "%.1f" % ALOS+" days"
        if compute_c == 2:
            print "\n---Average Daily Inpatient Census---"
            IPSD = float(raw_input("\nType in the total inpatient service days: "))
            month_p = raw_input("\nType in the first 3 letter of the month: ")
            month_p = month_p.capitalize()
            months = {"Jan": 31, "Feb": 28, "Mar": 31, "Apr": 30, "May": 31, "Jun": 30, "Jul": 31, "Aug": 31, "Sep": 31, "Oct": 31, "Nov": 30, "Dec": 31}
            print IPSD / months[month_p]
    elif choice[0] == "n":
        running = False
        print "Program Ended"
