
# Zip Code to Latitude and Longitude API

A Django API for effortlessly retrieving latitude and longitude coordinates based on a given zip code. Powered by OpenStreetMap Nominatim.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Securing the API](#securing-the-api)
- [License](#license)

## Prerequisites

Before using this API, make sure you have Python, Django, and the required packages installed. Use the following command to install dependencies:

```bash
pip install -r requirements.txt
```


## Getting Started

1. Clone the repository:

```bash
git clone https://github.com/yourusername/zip-code-api.git
cd zip-code-api
```
2. Create a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use "venv\Scripts\activate"
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```
4. Apply migrations and start the development server:

```bash
python manage.py migrate
python manage.py runserver
```

## Usage

To retrieve latitude and longitude for a specific zip code, make a GET request to the following endpoint:

```ruby
http://localhost:8000/api/get_location/?zip_code=YOUR_ZIP_CODE
```

Replace YOUR_ZIP_CODE with the desired zip code.

Example:

```ruby
http://localhost:8000/api/get_location/?zip_code=10001
```
The response will be in JSON format:

```json
{
    "zip_code": "10001",
    "latitude": 40.748817,
    "longitude": -73.9947645
}
```


## Securing the API
To secure the API, consider implementing authentication and authorization mechanisms provided by Django Rest Framework. Consult the DRF documentation for more details.

## Summurry
The Django API provides seamless access to latitude and longitude coordinates by inputting a zip code. It simplifies location-based operations by offering effortless retrieval of geographic data. This API streamline processes that require geographical coordinates, enhancing efficiency in various applications such as mapping, weather forecasting, and location-based services. With its integration into Django, developers can easily incorporate this functionality into their projects, reducing the complexity of handling geographic data. Overall, it offers a convenient solution for accessing location coordinates based on zip codes within Django applications.

## License
This project is licensed under the MIT License - see the LICENSE file for details.


## Happy coding! 🚀
