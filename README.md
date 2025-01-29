
The **Journey AI** web application is a comprehensive system that leverages multiple APIs and web scraping techniques to provide travel suggestions based on user inputs. Below is a detailed breakdown of the components and their functionalities:

---

### **1. Main.py**
This is the core API file that orchestrates the entire process. It receives user inputs, processes them, and returns a JSON response with travel suggestions.

#### **Inputs:**
- **Weather**: Desired weather conditions (e.g., sunny, rainy, snowy).
- **Biome**: Preferred environment (e.g., beach, mountain, forest).
- **Budget**: Travel budget (e.g., low, medium, high).

#### **Outputs:**
A JSON file containing 6 travel suggestions. Each suggestion includes:
- City name (in English and Persian/Farsi).
- Weather information.
- General information about the city.
- Three image links related to the city.

#### **JSON Format:**
```json
{
  "1": {
    "name": {
      "en": {"country": "France", "city": "Paris"},
      "fa": {"country": "فرانسه", "city": "پاریس"}
    },
    "weather": "Sunny, 25°C",
    "info": "Paris is the capital of France, known for its art, fashion, and culture.",
    "image": {
      "a": "https://unsplash.com/paris_image1",
      "b": "https://unsplash.com/paris_image2",
      "c": "https://unsplash.com/paris_image3"
    }
  },
  "2": {
    ...
  }
}
```

#### **Workflow:**
1. Receive user inputs (weather, biome, budget).
2. Call `Chatgpt.py` to get 6 city suggestions.
3. For each city:
   - Call `Wiki.py` to fetch city information.
   - Call `Unsplash.py` to fetch 3 image links.
   - Call `Openweather.py` to fetch weather information.
4. Compile the data into the JSON format and return it.

---

### **2. Chatgpt.py**
This module interacts with the OpenAI API to generate city suggestions based on user inputs.

#### **Inputs:**
- **Weather**: Desired weather conditions.
- **Biome**: Preferred environment.
- **Budget**: Travel budget.

#### **Outputs:**
- A JSON-formatted string containing 6 city suggestions.

#### **Example Output:**
```json
[
  {"city": "Paris", "country": "France"},
  {"city": "Tokyo", "country": "Japan"},
  {"city": "New York", "country": "USA"},
  {"city": "Sydney", "country": "Australia"},
  {"city": "Cape Town", "country": "South Africa"},
  {"city": "Rio de Janeiro", "country": "Brazil"}
]
```

#### **Workflow:**
1. Send a prompt to the OpenAI API with the user inputs.
2. Parse the API response to extract city and country names.
3. Return the data in JSON format.

---

### **3. Wiki.py**
This module uses web scraping (with the `BeautifulSoup4` library) to fetch information about a city from Wikipedia.

#### **Inputs:**
- **City Name**: The name of the city to search for.

#### **Outputs:**
- A string containing general information about the city.

#### **Example Output:**
```
"Paris is the capital and most populous city of France, known for its art, fashion, and culture. It is home to landmarks like the Eiffel Tower and the Louvre Museum."
```

#### **Workflow:**
1. Construct the Wikipedia URL for the city.
2. Use `BeautifulSoup4` to scrape the page and extract relevant information.
3. Return the extracted data as a string.

---

### **4. Unsplash.py**
This module interacts with the Unsplash API to fetch images related to a city.

#### **Inputs:**
- **City Name**: The name of the city to search for.

#### **Outputs:**
- Three image links in JSON format.

#### **Example Output:**
```json
{
  "a": "https://unsplash.com/paris_image1",
  "b": "https://unsplash.com/paris_image2",
  "c": "https://unsplash.com/paris_image3"
}
```

#### **Workflow:**
1. Send a request to the Unsplash API with the city name.
2. Parse the API response to extract image links.
3. Return the top 3 image links.

---

### **5. Openweather.py**
This module interacts with the OpenWeather API to fetch weather information for a city.

#### **Inputs:**
- **City Name**: The name of the city to search for.

#### **Outputs:**
- A string containing weather information (e.g., temperature, conditions).

#### **Example Output:**
```
"Sunny, 25°C"
```

#### **Workflow:**
1. Send a request to the OpenWeather API with the city name.
2. Parse the API response to extract weather details.
3. Return the weather information as a string.

---

### **System Architecture**
1. **Frontend**: User inputs are collected via a web interface.
2. **Backend**:
   - `Main.py` acts as the controller, coordinating between modules.
   - `Chatgpt.py`, `Wiki.py`, `Unsplash.py`, and `Openweather.py` handle specific tasks.
3. **APIs**:
   - OpenAI API for city suggestions.
   - Unsplash API for images.
   - OpenWeather API for weather data.
4. **Web Scraping**: Wikipedia is scraped using `BeautifulSoup4` for city information.

---

### **Example Workflow**
1. User inputs:
   - Weather: Sunny
   - Biome: Beach
   - Budget: Medium
2. `Main.py` calls `Chatgpt.py` to get 6 city suggestions.
3. For each city:
   - Fetch city info using `Wiki.py`.
   - Fetch images using `Unsplash.py`.
   - Fetch weather using `Openweather.py`.
4. Compile the data into JSON and return it to the user.

---

### **Technologies Used**
- **Programming Language**: Python
- **Web Framework**: Flask
- **APIs**: OpenAI, Unsplash, OpenWeather
- **Web Scraping**: BeautifulSoup4
- **Data Format**: JSON

---

This system provides a seamless and intelligent way for users to plan their travels based on their preferences.
