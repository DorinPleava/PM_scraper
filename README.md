# PM_scraper
Stores the scrapped info for finding the best precious metals prices

This API only stores the informations required
It will be consumed by a react app later (or anything)

TODO:
Add authentication for POST
Add comparation to spot silver price to see premiums (will be done in the reactjs app)
Compare same piece with different websites (link them by name???)
Link product name across multiple websites


API:

Adds a product with all the necessary stuff
If it already exists update the foreign table with its price 
POST: /product

Gets list of all products (with filters maybe) and the current price
GET: /products

View price performance
GET: /products/product_id
