import requests

## Intro- printed
hello = input("Welcome to my Weather Program! -- Press Enter to Continue")

## If user requests info by city
def by_city():
    city = input('Please Enter Your City Name: ')
    ## where to request from- my API key
    url = 'https://api.openweathermap.org/data/2.5/weather?q={},us&appid=23caf59a438de59d16d366601b1a9918&units=imperial'.format(city)
    res = requests.get(url)
    ## transferring data to Json for readability
    data = res.json()
    show_data(data)

    ## does the user want to go again?
    question = input('Do you want to do another search ? Type Yes or No: ')
    if question == 'Yes' or question == 'yes':
        main()
    if question == 'No' or question == 'no':
        print("Thank you for using my weather program. Have a nice day!")
        exit()

## If user requests info by zip code
def by_zip():
    zip_code = int(input('Please Enter Your Zip Code: '))
    ## where to request from- my API key
    url = 'https://api.openweathermap.org/data/2.5/weather?zip={},us&units=imperial&appid=23caf59a438de59d16d366601b1a9918'.format(zip_code)
    res = requests.get(url)
    ## transferring data to Json for readability
    data = res.json()
    show_data(data)

    ## does the user want to go again?
    question = input('Do you want to do another search ? Type Yes or No: ')
    if question == 'Yes' or question == 'yes':
        main()
    if question == 'No' or question == 'no':
        print("Thank you for using my weather program. Have a nice day!")
        exit()

## This will show data based on the user's request.
def show_data(data):
    temp = data['main']['temp']
    hightemp = data['main']['temp_max']
    lowtemp = data['main']['temp_min']
    wind_speed = data['wind']['speed']
    press = data['main']['pressure']
    latitude = data['coord']['lat']
    longitude = data['coord']['lon']
    humid = data['main']['humidity']
    description = data['weather'][0]['description']

    print('Current Temperature : {} degrees fahrenheit'.format(temp))
    print('High Temperature : {} degrees fahrenheit'.format(hightemp))
    print('Low Temperature : {} degrees fahrenheit'.format(lowtemp))
    print('Wind Speed : {} m/s'.format(wind_speed))
    print('Pressure : {} hPa'.format(press))
    print('Latitude : {}'.format(latitude))
    print('Longitude : {}'.format(longitude))
    print('Humidity : {} %'.format(humid))
    print('Description : {}'.format(description))

## Main function! 
def main():
    while True:
        answer = input("If you would like to request weather information, please choose from the following.\nType C to request information by city.\nType Z to request information by zip code.\n")
        if answer == 'C' or answer == 'c':
            try:
                by_city()
            except Exception:
                print("That didn't work. Try again, please!")
                by_city()
        if answer == 'z' or answer == 'Z':
            try:
                by_zip()

            except Exception:
                print("That didn't work. Try again, please!")
                by_zip()
        else:
            print("Unfortunately, that is not an option we support. Please try again.")

main()