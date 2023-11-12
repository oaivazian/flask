import requests
from bs4 import BeautifulSoup


# Function to format neighborhood name for URL
def format_neighborhood(neighborhood):
    return neighborhood.replace(" ", "_")


# Function to scrape and print restaurant information
def scrape_restaurants(neighborhood, cuisine):
    formatted_neighborhood = format_neighborhood(neighborhood)
    url = f"https://www.yelp.com/search?find_desc=restaurants&find_loc=New+York%2C+NY+10001&cflt={cuisine}&open_now=8352&attrs=OutdoorSeating&l=p%3ANY%3ANew_York%3AManhattan%3A{formatted_neighborhood}"

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")

        restaurants = soup.find_all("div", class_="arrange__09f24__LDfbs css-1qn0b6x")

        # Create a list to store restaurant names and descriptions
        restaurant_info = []

        for restaurant in restaurants:
            h3 = restaurant.find("h3", class_="css-1agk4wl")
            p = restaurant.find("p", class_="css-16lklrv")
            a = restaurant.find ("a", class_="css-19v1rkv")

            if h3 and p and a:
                restaurant_name = h3.text.strip()
                restaurant_description = p.text.strip()
                restaurant_link = a["href"]
                restaurant_info.append((restaurant_name, restaurant_description, restaurant_link))

        if restaurant_info:
            # Display numbered restaurant options
            print("Choose a restaurant:")
            for i, (name, description, link) in enumerate(restaurant_info, start=1):
                print(f"{i}. {name}\n   Description: {description}\n Link: https://www.yelp.com/{link}")

            # Prompt the user to select a restaurant
            choice = int(input("Enter the number of the restaurant you want: "))

            if 1 <= choice <= len(restaurant_info):
                selected_restaurant = restaurant_info[choice - 1]
                print("You selected:")
                print("Restaurant Name:", selected_restaurant[0])
                print("Description:", selected_restaurant[1])
                print("Link:", selected_restaurant[2])
            else:
                print("Invalid choice. Please enter a valid number.")
        else:
            print("No restaurants found in the selected neighborhood and cuisine.")

    else:
        print("Failed to retrieve the page. Status code:", response.status_code)


# List of Manhattan neighborhoods
neighborhoods = [
    "Alphabet City",
    "Battery Park",
    "Central Park",
    "Chelsea",
    "Chinatown",
    "Civic Center",
    "East Harlem",
    "East Village",
    "Financial District",
    "Flatiron",
    "Gramercy",
    "Greenwich Village",
    "Harlem",
    "Hell's Kitchen",
    "Inwood",
    "Kips Bay",
    "Koreatown",
    "Little Italy",
    "Lower East Side",
    "Manhattan Valley",
    "Marble Hill",
    "Meatpacking District",
    "Midtown East",
    "Midtown West",
    "Morningside Heights",
    "Murray Hill",
    "NoHo",
    "Nolita",
    "Roosevelt Island",
    "SoHo",
    "South Street Seaport",
    "South Village",
    "Stuyvesant Town",
    "Theater District",
    "TriBeCa",
    "Two Bridges",
    "Union Square",
    "Upper East Side",
    "Upper West Side",
    "Washington Heights",
    "West Village",
    "Yorkville"
]

# Prompt to select a neighborhood
print("Select a neighborhood:")
for i, neighborhood in enumerate(neighborhoods, start=1):
    print(f"{i}. {neighborhood}")

neighborhood_choice = int(input("Enter the number of the neighborhood you want: "))
selected_neighborhood = neighborhoods[neighborhood_choice - 1]

# Prompt to enter cuisine type
cuisine_type = input("Enter the cuisine type (e.g., Greek): ")

# Scrape and print restaurant information
scrape_restaurants(selected_neighborhood, cuisine_type)
