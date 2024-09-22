# Project-Bus-Finder
An streamlit App created with the extracted data using selenium and python

1. Introduction
      The Bus Availability Finder project aims to provide users with a streamlined platform for checking bus availability and booking options. Using web scraping and data       visualization, the application allows users to filter bus routes based on various criteria.

2. Objectives
      *To scrape bus route data from the Redbus website.
      *To collect bus details such as name, type, timings, duration, price, ratings, and available seats.
      *To store the scraped data in a MySQL database for efficient querying.
      *To develop a user-friendly interface using Streamlit that enables users to filter and search for buses.
3. Tools and Technologies
      Selenium: For web scraping bus route data.
      Pandas: For data manipulation and cleaning.
      MySQL: For storing the data.
      Streamlit: For creating an interactive web application.
      Python: As the primary programming language.
4. Methodology
      # Web Scraping
          Utilize Selenium to navigate through the Redbus website and extract route links and names.
          Implement pagination handling to ensure data from multiple pages is collected.
          Extract bus details by clicking on each route and scrolling through the details page.
      # Data Storage
          Clean the data by removing unnecessary columns and handling missing values.
          Store the processed data into a MySQL database for future retrieval and analysis.
      # Streamlit Application
          Create filters for users to search by route, price range, minimum ratings, and available seats.
          Display filtered results in a user-friendly format, including clickable links for detailed route information.
5. Data Cleaning
      *Normalize price and rating formats.
      *Handle missing values and duplicates to ensure data integrity.
6. Results
      *The application successfully retrieves and displays bus details based on user-selected filters.
      *Users can interact with the data easily and find buses that meet their needs.
7. Conclusion
      The Bus Availability Finder project effectively combines web scraping, data management, and interactive visualization to create a valuable tool for bus travelers. The use of Streamlit ensures a seamless user experience while providing powerful filtering options.

8. Future Enhancements
      *Integration of additional data sources for more comprehensive route options.
      *User authentication for personalized experiences.
      *Mobile-responsive design to enhance accessibility.
