import csv

def main():
    with open('article-Devices.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        #open txt file to write results for exercise 1 to
        f = open("percentage_of_mobile_and_tablet.txt","w+")
        f.write("The percentage of people visiting the page via a mobile phone or a tablet device is ")
        line_count = 0
        total = 0
        total_mobile_tablet = 0
        total_mobile = 0
        for row in csv_reader:
            #loop through rows
            line_count = line_count + 1

            #omit first row (headers)
            if line_count == 1:
                continue

            # sum of "total"
            total = total + int(row['Total'])

            # sum of "tablet" and "mobile"
            total_mobile_tablet = total_mobile_tablet + int(row['Mobile']) + int(row['Tablet'])

            # sum of "mobile"
            total_mobile = total_mobile + int(row['Mobile'])

        percentage_mobile_tablet = 'n/a'

        if total > 0:
            percentage_mobile_tablet = total_mobile_tablet/total*100
        
        #write result to .txt file
        f.write(str(percentage_mobile_tablet)+ "%")

        print("Percentage of mobile and tablet: " + str(percentage_mobile_tablet) + "%")

        #mean of "mobile"
        mean_mobile = total_mobile/line_count

        print("Mean of mobile: " + str(mean_mobile))

    with open('article-Devices.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        f = open("mobile_greater_than_mean.txt","w+")
        f.write("Mobile \t | Date \n")
        for row in csv_reader:
            #loop through rows
            line_count = line_count + 1

            #omit first row (headers)
            if line_count == 1:
                continue

            #loop through number of page views on mobile
            if int(row['Mobile']) > mean_mobile:
                f.write(row['Mobile'] + '\t | ' +  row['Date'] + '\n')
            
        f.close()

if __name__ == "__main__":
    main()