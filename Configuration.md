App Configuration

1. Root
   The root folder for Django will `app/` 

2. Databases:
   
   the system will use CockroachDB during the development.
   
   connection guide: https://www.cockroachlabs.com/docs/stable/connect-to-the-database.html?filters=python&filters=django

   there are 2 databses created:

   * bgdev : for deveopment (commonly used between all involoved)
     credentials are stored in .env file
   * baseguidedb : for production


   we will have second Database using MongoDB & mongoengine monule.
   we will be using one Database currently for the solution, we will diferentiate the names of the collections ( we will discuss this soon)

   connection guide : https://www.mongodb.com/compatibility/mongodb-and-django

   database name : baseguide
   connection : mongodb+srv://<username>:<password>@baseguide.hremfev.mongodb.net/?retryWrites=true&w=majority

   usernames:
   * bgdev
      credentials will be stored in the .env file
   * baseguide


3. Utilities module:
   
   we added utilities module, that will be common module where custom utilities and classes that will be used in multiple django modules.

4. static:

   we will use S3 bucket and cloudfront for CDNAWS credentials, bucketname, and cdn URL will be stored in the .env



5. emails
   
   we have AWS SES service active for baseguide, we can currently use the SES .
   use module dganjo_ses
   https://pypi.org/project/django-ses/


