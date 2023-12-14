def Weather(t, h, ws):
    weather_prediction = float(((0.5) * t * t) - (0.2 * h) + (0.1 * ws) - 15)

    if weather_prediction > 300:
        return "Sunny", weather_prediction
    elif 200 <= weather_prediction <= 300:
        return "Cloudy", weather_prediction
    elif 100 <= weather_prediction <= 200:
        return "Rainy", weather_prediction
    elif 0 <= weather_prediction < 100:
        return "Storm", weather_prediction
    else:
        return "Give proper values"


filename = "wpimport.txt"
with open(filename, 'r') as file:
    lines = file.readlines()

# Extract the number of test cases
n = int(lines[0])

count = 0
for i in range(1, n + 1):
    data = list(map(float, lines[i].split()))
    t, h, ws = data[:3]  # Assuming each line contains Temperature, Humidity, Wind_Speed
    result, prediction = Weather(t, h, ws)
    print(f"TestCase {i}: {result} {prediction}")
    count += i

if count == n:
    print("All the test cases are processed.")
