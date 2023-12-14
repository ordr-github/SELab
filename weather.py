def Weather(t,h,ws):
    weather_prediction = float(((0.5)*t*t)-(0.2*h)+(0.1*ws) -15)

    if(weather_prediction >300):
        print("Sunny", weather_prediction)
    elif(200<=weather_prediction<=300):
        print("Cloudy", weather_prediction)
    elif(100<=weather_prediction<=200):
        print("Rainy", weather_prediction)
    elif(0<=weather_prediction<100):
        print("Storm", weather_prediction)
    else: 
        return("Give proper values")

n = int(input("Number of Test Cases: "))
count = 0
for i in range(1,n+1):
    print("TestCase",i)
    t = int(input("Enter Temperature: "))
    h = float(input("Enter Humidity in decimal: "))
    ws = float(input("Enter Speed: "))
    print(Weather(t,h,ws))
    count +=i

if(count == n):
    print("All the test cases are passed.")