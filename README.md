# Selenium Scraper

This Python script uses Selenium to scrape football (soccer) data from the website [adamchoi.co.uk](https://adamchoi.co.uk/overs/detailed). It allows you to select a country and retrieve all the teams' scores in that country. This README provides an overview of the technologies and libraries used in the project.

## Technologies Used

- **Selenium:** Selenium is a web testing framework that allows you to automate web interactions. In this project, it is used to control the web browser and extract data from the website.

- **webdriver_manager:** The `webdriver_manager` library simplifies the process of managing web drivers for Selenium. It automatically downloads and manages the appropriate driver for your browser.

- **Pandas:** Pandas is a powerful data manipulation and analysis library in Python. It is used here to store the scraped data in a structured DataFrame and export it to a CSV file.

- **Chrome WebDriver:** The script uses the Chrome WebDriver to interact with the Chrome browser.

## Script Explanation

- The script navigates to the adamchoi.co.uk website using Selenium and Chrome WebDriver.

- It clicks the "All matches" button on the page to load all match data.
- You can select a specific country from the dropdown menu, and the script waits for the page to dynamically load the data.
- It scrapes data such as match date, home team, score, and away team and stores it in lists.
- Finally, it creates a Pandas DataFrame and exports the data to a CSV file named "{your country}.csv." you can change this name in the script.

## Example output
The scraped data is stored in a CSV file and can be easily analyzed or used for further processing.
```yaml
         date    home-team   score    away-team
0  2023-09-01     Cerezo     3 - 1     Oita
1  2023-08-28     Fagiano   1 - 2     Nagoya
2  2023-08-27     Yokohama   2 - 0     Sagan
3  2023-08-26     Shimizu   1 - 1     Kobe
4  2023-08-26     Tosu     0 - 0     Gamba
...
```
