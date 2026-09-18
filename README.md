# Web Scraping with BeautifulSoup

A simple Python web scraping project that uses **Requests** and **BeautifulSoup** to extract information from a webpage.

## Project Description

This project demonstrates the basics of web scraping in Python.

It sends an HTTP request to a webpage, retrieves the HTML content, and uses BeautifulSoup to parse the HTML and extract useful information.

The project performs two main tasks:

1. Extracts **all links** (`<a>` tags) from a webpage.
2. Finds elements belonging to a **specific HTML class** and extracts their names/text and associated links.

## Technologies Used

* **Python**
* **Requests** — Used to send HTTP requests and retrieve webpage content.
* **BeautifulSoup** — Used to parse HTML and extract information from the webpage.

## Installation

Clone the repository or download the project files.

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment.

### Windows

```bash
venv\Scripts\activate
```

### Linux/macOS

```bash
source venv/bin/activate
```

Install the required dependencies:

```bash
pip install requests beautifulsoup4
```

## How It Works

The program first sends a request to the target webpage using the Requests library.

```python
response = requests.get(url)
```

The returned HTML is then passed to BeautifulSoup:

```python
soup = BeautifulSoup(response.text, "html.parser")
```

BeautifulSoup can then be used to search through the HTML.

### Getting All Links

The project searches for all `<a>` elements:

```python
links = soup.find_all("a")
```

For each link, the program can retrieve the URL from the `href` attribute:

```python
for link in links:
    print(link.get("href"))
```

### Getting Links and Names from a Particular Class

The program can also search for elements with a specific HTML class:

```python
elements = soup.find_all(class_="class-name")
```

y
```
