# Enhanced Expense Tracker WebApp

This project builds upon the previous "Expense Tracker WebApp" (Project3) by introducing an essential new feature - currency conversion. This enhancement allows users to enter expenses in various currencies which are then automatically converted to US Dollars, facilitating a unified view of financial data. The application leverages Python, Flask, PyMongo, HTML, CSS, JS, and integrates the currencylayer API for real-time currency conversion.

## Features

- **Currency Conversion**: Integrate currencylayer API to convert expenses entered in any of 168 different currencies to US Dollars, ensuring consistent financial tracking.
- **Expense Logging**: Users can log expenses with enhanced fields including description, category, cost, currency, and date.
- **Expense Tracking and Categorization**: Retains all functionalities from Project3 with the added ability to handle multiple currencies, enhancing the app's usability for international users.

## Setup and Installation

1. **Environment Setup**: Clone the Project4 repository and set up a new virtual environment in PyCharm with Python 3.8.
2. **Install Dependencies**: Run `pip install Flask Flask-WTF wtforms dnspython Flask-PyMongo requests` to install necessary packages.
3. **API Configuration**: Sign up for currencylayer API and obtain your unique API key. Insert this key into the `currency_converter` function in `app.py`.
4. **Database Connection**: Configure your MongoDB Atlas Cloud connection to ensure smooth data handling.

## Running the Application

1. **Start the Application**: Navigate to the project directory and run `python app.py` to start the Flask server.
2. **Access the WebApp**: Open a web browser and go to `http://localhost:5000` to start using the application.
3. **Add Expenses**: Use the "Add an Expense" feature to log expenses in any supported currency, which will be automatically converted to USD.

## Development Notes

- Ensure that your MongoDB Atlas Cloud is accessible during development and deployment.
- Keep your API key confidential to prevent unauthorized use.
- Regularly update the dependencies to mitigate potential security vulnerabilities.

## Contributions

Contributions to "Project4" are welcome. Please fork the repository, make your changes, and submit a pull request for review.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details.

## Contact

For support or queries, reach out via email at [YourEmail@example.com].

Enjoy enhanced financial tracking with "Project4", your comprehensive tool for managing expenses in any currency!
