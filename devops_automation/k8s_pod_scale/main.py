import requests
import subprocess

def get_weather_data(city):
    """Fetches weather data for a specific city using WeatherAPI."""
    
    api_key = '91da448afecb4b83af642416241310'   # Replace with your valid WeatherAPI key
    base_url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"

    response = requests.get(base_url)
    data = response.json()

    if 'error' in data:
        print(f"Error fetching data for {city}: {data['error']['message']}")
        return

    weather = data['current']['condition']['text']
    temp_c = data['current']['temp_c']

    print(f"Weather in {city}: {weather}, Temperature: {temp_c} ℃")

    # Check weather condition
    if "Heavy rain" in weather:
        print("Weather condition is heavy rain. Scaling the number of pods in AKS...")
        scale_aks_pods(namespace='blogging-app', deployment_name='bankapp', replicas=3)
    else:
        print("Weather condition is not heavy rain. No scaling action is required.")


def scale_aks_pods(namespace, deployment_name, replicas):
    """Scales the number of pods for a specific deployment using kubectl."""
    try:
        subprocess.run([
            'kubectl', 'scale',
            f'deployment/{deployment_name}',
            f'--replicas={replicas}',
            '-n', namespace
        ], check=True)

        print(f"Scaled the deployment {deployment_name} to {replicas} pods.")

    except subprocess.CalledProcessError as e:
        print(f"Failed to scale pods: {e}")


# Example usage:
get_weather_data('London')
