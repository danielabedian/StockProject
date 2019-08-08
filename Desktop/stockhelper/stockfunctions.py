#import requests
import os
import shutil
import time
import datetime
from selenium import webdriver
#from bs4 import BeautifulSoup
from csv import writer
from csv import reader


#first thing we want to do is get the driver
#--------user_input-------------------------
#stock = ""
#end_month = ""
#end_year = ""
#years = ""
#percent_input = ""
#above_below = ""
#end_date = ""
#start_timestamp = ""
#timestamp_input = ""
#---------chrome_path and Driver-----------------
chrome_path = r"chromedriver_win32\chromedriver.exe"
#String downloadFilepath = "/data/monthly";
#------------month frequency------------------------


current_location = os.getcwd()






#(called first) gets the user input for accurate information, then creates appropriate variables to use in the next methods 
def user_inputs(stock, end_month, end_year, years, percent_input, above_below):
    #stock = input("Enter stock ticker: ")
    #end_month = input("enter month in 2 digit form: ")
    #end_year = input("enter year in 4 digit form: ")
    #years = input("Enter 5, 10, 15, or 20 for years: ")
    #percent_input = input("Enter percentage: ")
    #above_below = input("Enter A for above B for below: ")
    if int(end_month) < 10:
        end_month = "0" + end_month
    end_date = "01/"+ str(end_month) + '/' + str(end_year)
    timestamp_input = int(time.mktime(datetime.datetime.strptime(end_date, "%d/%m/%Y").timetuple()))
    if int(years) == 5:
        end_year = int(end_year) - 5
        start = "01/"+ str(end_month) + '/' + str(end_year)
    elif int(years) == 10:
        end_year = int(end_year) - 10
        start = "01/"+ str(end_month) + '/' + str(end_year)
    elif int(years) == 15:
        end_year = int(end_year) - 15
        start = "01/"+ str(end_month) + '/' + str(end_year)
    elif int(years) == 20:
        end_year = int(end_year) - 20
        start = "01/"+ str(end_month) + '/' + str(end_year)
    start_timestamp = int(time.mktime(datetime.datetime.strptime(start, "%d/%m/%Y").timetuple()))
    return(timestamp_input, start_timestamp)
    #stock, end_month, end_year, years, percent_input, above_below,
# (called second) opens google chrome, goes to appropriate url, downloads the file, and moves the file to the appropriate folder
def get_information(stock, start_timestamp, timestamp_input):
    options = webdriver.ChromeOptions()
    preferences = {"download.default_directory": (current_location +"\data\monthly"), "safebrowsing.enabled": "false"}
    options.add_experimental_option("prefs", preferences)
    driver =  webdriver.Chrome(chrome_options=options, executable_path=r"chromedriver_win32\chromedriver.exe")
    driver.get('https://finance.yahoo.com/quote/'+stock+'/history?period1='+ str(start_timestamp) +'&period2='+ str(timestamp_input) +'&interval=1mo&filter=history&frequency=1mo')
    exists = os.path.isfile(current_location +'\data\monthly\\'+stock+'.csv')
    if exists:
        os.remove(current_location +'\data\monthly\\'+stock+'.csv')
    exists = os.path.isfile(current_location +'\data\monthly\\'+stock+'mod.csv')
    if exists:
        os.remove(current_location +'\data\monthly\\'+stock+'mod.csv')
    driver.find_element_by_xpath("""//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[1]/div[2]/span[2]""").click()
    time.sleep(5)
    #os.rename('/Users/Admin/Downloads/'+stock+'.csv', '/Users/Admin/Desktop/Projects/StockProject/data/monthly/'+stock+'.csv')
    driver.quit()

# (called third) opens the file and creates a new file, adds a new column for percent increase, and filters data appropriatley
def filter_data(stock, above_below, percent_input):
    with open('data/monthly/'+stock+'.csv', 'r') as csv_file:
        with open('data/monthly/'+stock+'mod.csv', 'w')as mod_file:
            csv_reader = reader(csv_file)
            csv_writer = writer(mod_file)
            headers = ['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', "Volume", "Percent"]
            csv_writer.writerow(headers)
            for row in csv_reader:
                date = row[0]
                if date != 'Date':
                    opens = row[1]
                    if opens != 'null' :     
                        high = row[2]
                        low = row[3]
                        closes = row[4]
                        adj_close = row[5]
                        volume = row[6]
                        percent = str(((float(closes) - float(opens))/float(opens))*100.0) + '%'
                        if(above_below == 'A'):                    
                            if ((float(closes)-float(opens))/float(opens))*100.0 >= float(percent_input):
                                csv_writer.writerow([date, opens, high, low, closes, adj_close, volume, percent])
                        else:
                            if ((float(closes)-float(opens))/float(opens))*100.0 <= float(percent_input):
                                csv_writer.writerow([date, opens, high, low, closes, adj_close, volume, percent])
#(called fourth) looks through the new file and gives important information in a text file
def give_info(stock, years, percent_input, above_below):
    January = 0
    February = 0
    March = 0
    April = 0
    May = 0
    June = 0
    July = 0
    August = 0
    September = 0
    October = 0
    November = 0
    December = 0
    file = open('data/monthly/'+stock+'mod.csv')
    data = reader(file)
    count = 0
    for row in data:
        count +=1
        if count%2 != 0:
            if '-01-01' in row[0]:
                January += 1
            if '-02-01' in row[0]:
                February += 1
            if '-03-01' in row[0]:
                March += 1
            if '-04-01' in row[0]:
                April += 1
            if '-05-01' in row[0]:
                May += 1
            if '-06-01' in row[0]:
                June += 1
            if '-07-01' in row[0]:
                July += 1
            if '-08-01' in row[0]:
                August += 1
            if '-09-01' in row[0]:
                September += 1
            if '-10-01' in row[0]:
                October += 1
            if '-11-01' in row[0]:
                November += 1
            if '-12-01' in row[0]:
                December += 1

    file.close()
    file = open('data/monthly/'+stock+'mod.txt', "w")
    file.write('The stock in question is: '+ str(stock)+'\n')
    file.write('The years in question is: '+ str(years)+'\n')
    file.write('The percent in question is: '+ str(percent_input)+'\n')
    file.write('This is every time a month was ')
    if(above_below == 'A'): 
        file.write('above')
    else:
        file.write('below')
    file.write(' the percent in question \n')
    file.write('Jan = ' + str(January)+'\n')
    file.write('Feb = ' + str(February)+'\n')
    file.write('Mar = ' + str(March)+'\n')
    file.write('Apr = ' + str(April)+'\n')
    file.write('May = ' + str(May)+'\n')
    file.write('Jun = ' + str(June)+'\n')
    file.write('Jul = ' + str(July)+'\n')
    file.write('Aug = ' + str(August)+'\n')
    file.write('Sep = ' + str(September)+'\n')
    file.write('Oct = ' + str(October)+'\n')
    file.write('Nov = ' + str(November)+'\n')
    file.write('Dec = ' + str(December)+'\n')
    file.close()

