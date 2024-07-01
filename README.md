##Stock Analysis Dashboard##
This project is a comprehensive stock analysis dashboard designed to provide real-time insights and facilitate informed decision-making in financial markets.

##Key Features:##
1. Real-Time Data Visualization: Includes dynamic stock price and volume charts for up-to-date market analysis.
2. Curated Company News: Keeps users informed with relevant news articles to support investment decisions.
3. Financial Metrics: Displays essential financial ratios such as P/E ratio, Return on Equity (ROE), and Market Cap for deeper insights into company performance.
4. Intuitive User Interface: Built with HTML, CSS, and Django for seamless navigation and efficient tracking of market trends.

#Technologies Used:
HTML
CSS
Django

##Usage:##
**Clone the repository**
git clone https://github.com/amaanz/Stockers.git

cd Stockers

Set up django
pip install django pip install djangorestframework

#Navigate to the directory containing BrahmaCanteen, portalapp,manage.py,etc.

**Set up the database**
python manage.py makemigrations python manage.py migrate

**Create a superuser**
python manage.py createsuperuser

**Run the development server**
python manage.py runserver
