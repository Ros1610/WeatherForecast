import requests
API_KEY = "********************************"


def get_data(place, forecast_days):

    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    content = response.json()

    data = content["list"]
    forecast_days *= 8
    filtered_data = data[:forecast_days]

    return filtered_data


if __name__ == "__main__":
    print(get_data(place="Tokyo", forecast_days=1, kind="Sky"))