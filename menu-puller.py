import requests
from bs4 import BeautifulSoup

# Define the URL of the Yelp menu page
url = "https://www.yelp.com/menu/kyma-hudson-yards-new-york"

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all h2 elements
    h2_elements = soup.find_all("h2")

    # Loop through the h2 elements
    for i, h2 in enumerate(h2_elements):
        print("h2:", h2.text.strip())

        # Find the next h2 element or the end of the document
        next_h2 = h2_elements[i + 1] if i + 1 < len(h2_elements) else None

        # Find and print the corresponding h4 and p elements within the next div
        div = h2.find_next("div", class_="arrange_unit arrange_unit--fill")
        while div and (not next_h2 or div.find_next_sibling() != next_h2):
            h4_elements = div.find_all("h4")
            p_elements = div.find_all("p")


            for h4 in h4_elements:
                print("h4:", h4.text.strip())
            for p in p_elements:
                print("p:", p.text.strip())

            div = div.find_next("div", class_="arrange_unit arrange_unit--fill")
else:
    print("Failed to retrieve the page. Status code:", response.status_code)
