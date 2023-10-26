import time

#print(time.ctime(0)) # convert a time expressed in seconds since epoch to a readable string. epoch = when your computer think time began (refenrece point)

#print(time.time()) # return current seconds since epoch

#----------------1 SPOSOB------------

#print(time.ctime(time.time())) # current date


#-----------------2 SPOSOB--------------

#time_object = time.localtime() #local time
#time_object - time.gmtime() # UTC time
#print(time_object)
#local_time =  time.strftime("%B %d %Y %H:%M:%S", time_object)
#print(local_time)

#time_string = "20 April, 2020"
#time_object = time.strptime(time_string, "%d %B, %Y")
#print(time_object) #

# (year, motnth, day, hours, minutes, secds, #day of the week, #day of the year, dst)

#time_tuple = (2020, 4, 20, 4, 20 ,0, 0, 0, 0)
#time_string =  time.asctime(time_tuple); # converts tuple time to string
#time_string = time.mktime(time_tuple) # seconds since epoch
#print(time_string)
