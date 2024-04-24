# Django Search Engine Project

## Overview
This project is a search engine built using Django, a high-level Python web framework that encourages rapid development and clean, pragmatic design. The search engine is designed to index and search articles stored in a PostgreSQL database.

## Features
- **Article Management**: Admins can add, edit, and delete articles through the Django admin interface.
- **Search Functionality**: Users can search for articles by keywords found in the article titles or bodies.

## Technical Details
- **Framework**: Django 5.0
- **Database**: PostgreSQL
- **Models**: `Article` model with fields for title and body.

## Setup and Installation
1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Install required packages:
   ```
   pip install -r requirements.txt
   ```
3. Set up the database:
   ```
   python manage.py migrate
   ```
4. Create an admin user:
   ```
   python manage.py createsuperuser
   ```
5. Run the development server:
   ```
   python manage.py runserver
   ```
6. Access the admin panel at `http://127.0.0.1:8000/admin` to manage articles.

## Usage
To search for articles, navigate to the main page and use the search bar to enter your query. The system will display articles that match the search criteria.

## Contributing
Contributions to this project are welcome. Please fork the repository and submit a pull request with your features or fixes.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
