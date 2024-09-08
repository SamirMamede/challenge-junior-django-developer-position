## Challenge-Junior-Django-Developer-Position
We are currently looking for a Junior Django Developer who will be tasked with developing the data models and public web pages for a **Film Review Management Platform**.

### Key Responsibilities:
- Model the data structure for a User table and a Review table based on the provided especifications.

### Data Modeling Reference:

For the User Table, the developer will need to ensure fields for id, username, email and password are modeled correctly, witch are essential for use management(use django contrib auth feature).

For the Review Table, the structure will include fields for:
- **id**: A primary key integer field that  uniquely identifies each review.
- **title**: A string field to store the title of the review limited to 200 characters.
- **status**: An integer field to store the status of the review (Draft or Published).
- **body**: A text field to store the main content of the review.
- **author_id**: An integer field to create a relationship between the review and the user who authored it,  referencing the User table's primary key.
- **rating**: An integer field to store the rating of the review (BAD, POOR, FAIR, GOOD, EXCELLENT, EXCEPTIONAL).
- **published_at**: A datetime field to store when the review was published.
- **created_at**: A datetime field to store when the review record was created.
- **updated_at**: A datetime field to store when the review record was lats updated.

### Skills and Qualifications:
- Experience with Python and Django Framework.
- Understanding of database modeling and Django ORM.
