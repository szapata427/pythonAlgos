import requests

# def add(n):
#     string = str(n)
#     total = 0
#     for x in string:
#         total += int(x)
#     print(total)


# add(29)

# matrix = [[1, 0, 0], 
#           [0, 5, 0], 
#           [0, 0, 3]]


# def isDiagonalMatrix(matrix):
#     rows = len(matrix)
    
#     columns = rows
#     print(columns)
#     for x in matrix:
#         print(len(x))
#         print(x)
#         if len(x) != rows:
#             return False
    
#     return True

# isDiagonalMatrix(matrix)


# def alarmClock(setTime, timeToSet):
#     setTimeArray = setTime.split(':')
#     setTimeHour = setTimeArray[0]
#     setTimeMin = setTimeArray[1]

#     timeToSetArray = timeToSet.split(':')
#     timeToSetHour = timeToSetArray[0]
#     timeToSetMin = timeToSetArray[1]
    
    
#     maxhour = 23
#     minhour = 0
    
#     maxminute = 59
#     minminute = 0
    
    
#     hourdifference = int(setTimeHour) - int(timeToSetHour)
#     minDifference = int(setTimeMin) - int(timeToSetMin)
    
#     gouphour = False
#     godownhour = False
    
#     goUpMin = False
#     goDownMin = False
    
#     godowndifference = abs(hourdifference - maxhour)
#     goupdifference  = abs(hourdifference - minhour)
    
#     downminDifference = abs(minDifference - maxminute)
#     upminDifference  = abs(minDifference - minminute)
    
    
#     if godowndifference == goupdifference:
#         same = True

#     if godowndifference < goupdifference:
#         print(godowndifference)
#         godownhour = True
#     else:
#         print(goupdifference)
#         gouphour = True
    

#     if downminDifference == upminDifference:
#         samemin = True

#     if downminDifference < upminDifference:
#         print(downminDifference)
#         goDownMin = True
#     else:
#         print(upminDifference)
#         goUpMin = True
    

#     print(godowndifference)

#     alarmHour = 0
#     alarmMin = 0
    
#     print(godownhour)
#     if same == True:
#         alarmHour = 0
#     elif godownhour == True:
#         alarmHour = godowndifference
#     else: 
#         alarmHour = goupdifference
        
#     if samemin == True:
#         alarmMin = 0
#     elif goDownMin == True:
#         alarmMin = downminDifference
#     else: 
#         alarmMin = upminDifference
    
#     result = alarmHour + alarmMin
    
#     return result

# print(alarmClock("08:45", "08:00"))





# def birthdayCakeCandles(ar):
#     count = 0
#     max = 0
#     for x in ar:
#         if x >= max:
#             max = x

#     for k in ar:
#         if k == max:
#             count += 1

#     return count



# candlesArray = [10,18,90,90,13,90,75,90,8,90,43]
# # candlesArray = [4,3,2,1,3]
# print(birthdayCakeCandles(candlesArray))


# def nearestgreates(a):
#     barray = []
    
#     currentindex = 0
#     secondround = False
#     currentvalue = 0

#     for x in a:
#         if secondround == False:
#             currentvalue = x
            

#         if a.index(x) == 0:
#             barray.append(x)
#             currentindex += 1
#             continue

#         indexvalue = a[currentindex]


#         if currentvalue < x:
#             barray.append(indexvalue)
#             currentindex += 1
#             secondround = False

#         elif currentindex == len(a):
#             barray.append(-1)
#             secondround = False
#             currentindex += 1
#         else:
#             secondround = True
        
#     return barray



# a = [1, 4, 2, 1, 7, 6]
# print(nearestgreates(a))


# def timeConversion(s):
#     timestring = s.split(':')
#     hour = timestring[0]
#     mins = timestring[1]
#     miliseconds = timestring[2]

#     start = 0
#     upto = 0
#     downto = 12

#     middle = 12
#     finalhour = 0
#     if 'PM' in miliseconds:
#         upto = int(hour) - start
#         if int(hour) == 12:
#             finalhour = hour
#         else:
#             finalhour = abs(upto + middle)
#         if len(str(finalhour)) == 1:
#             finalhour = '0' + str(finalhour)
#         finaltime = str(finalhour) + ':' + mins + ':' + miliseconds.replace('PM', "")

#     if 'AM' in miliseconds:
#         upto = int(hour) - start
#         if int(hour) == 12:
#             finalhour = 0
#         else:

#             finalhour = abs(upto)
#         if len(str(finalhour)) == 1:
#             finalhour = '0' + str(finalhour)
#         finaltime = str(finalhour) + ':' + mins + ':' + miliseconds.replace('AM', "")
#     print(finaltime)


# timeConversion('06:40:03AM')



# def miniMaxSum(arr):
#     currentindex = 0
#     sumarray = []

#     sum = 0
#     for x in arr:
#         if currentindex == arr.index(x):
#             for y in arr:
#                 if currentindex != arr.index(y):
#                     sum += y
#             sumarray.append(sum)
#             sum = 0   
#             currentindex += 1

#     max = 0
#     min = 0
#     for k in sumarray:
#         if sumarray.index(k) == 0:
#             min = k
#         if k >= max:
#             max = k
#         if k <= min:
#             min = k

#     print(min, max)
# print(miniMaxSum([5,5,5,5,5]))



# def oddNumbers(l, r):
#     numbers = list(range(l, r+1))
#     oddnumbers = []
#     for x in numbers:
        
#         if x % 2 != 0:
#             oddnumbers.append(x)
#     return oddnumbers

# print(oddNumbers(2, 5))


# def getTopicCount(topic):

#     url = f'https://en.wikipedia.org/w/api.php?action=parse&section=0&prop=text&format=json&page={topic}'
#     r = requests.get(url)
#     info = r.json()
#     data = info['parse']

#     text = data["text"]

#     textsring = str(text)

#     print(textsring.count(topic))


def numberOfPaths(a):
    p = len(a)
    q = len(a[0])
    blocked = False
    if p == 0 or q == 0:
        return 0

    ok = [1 for i in range(q)] 

    for x in a:
        for k in x:
            if k == 0:
                blocked = True
                break
    for i in range(p - 1): 
        for j in range(1, q): 
            ok[j] += ok[j - 1]
    if blocked: 
        return ok[q - 2]
    else:
        return ok[q - 1] 



a = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
print(numberOfPaths(a))
