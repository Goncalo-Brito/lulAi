from pymongo import MongoClient
from datetime import datetime

# Initialize the MongoDB client and database
client = MongoClient('mongodb://localhost:27017/')
db = client['chatbot_db']

# Insert into Websites collection
website = {
    'website_url': 'https://example.com',
    'website_name': 'Example Website',
    'integration_date': datetime.now()
}
website_id = db.websites.insert_one(website).inserted_id
print(f"Website inserted with ID: {website_id}")

# Insert into Documents collection
document = {
    'document_name': 'Privacy Policy',
    'document_path': '/docs/privacy_policy.pdf',
    'document_type': 'pdf',
    'upload_date': datetime.now()
}
document_id = db.documents.insert_one(document).inserted_id
print(f"Document inserted with ID: {document_id}")

# Insert into Users collection
user = {
    'username': 'JohnDoe',
    'user_type': 'admin',
    'email': 'johndoe@example.com',
    'password': 'hashed_password',  # Hash the password in production
    'registered_date': datetime.now()
}
user_id = db.users.insert_one(user).inserted_id
print(f"User inserted with ID: {user_id}")

# Insert into ScrapedData collection - For Website
scraped_data_website = {
    'sourceType': 'website',  # Indicates that source_id refers to a website
    'source_id': website_id,  # Reference to website
    'scraped_content': 'This is the scraped content from the website.',
    'scrape_date': datetime.now()
}
scraped_id_website = db.scraped_data.insert_one(scraped_data_website).inserted_id
print(f"Scraped data (Website) inserted with ID: {scraped_id_website}")

# Insert into ScrapedData collection - For Document
scraped_data_document = {
    'sourceType': 'document',  # Indicates that source_id refers to a document
    'source_id': document_id,  # Reference to document
    'scraped_content': 'This is the scraped content from the document.',
    'scrape_date': datetime.now()
}
scraped_id_document = db.scraped_data.insert_one(scraped_data_document).inserted_id
print(f"Scraped data (Document) inserted with ID: {scraped_id_document}")

# Insert into UserQueries collection
user_query = {
    'scraped_id': scraped_id_website,  # Reference to scraped data (website)
    'user_id': user_id,                # Reference to user
    'query': 'What is the privacy policy?',
    'response': 'Our privacy policy is...',
    'rating': 5,
    'comment': 'Very helpful!',
    'query_date': datetime.now()
}
query_id = db.user_queries.insert_one(user_query).inserted_id
print(f"User query inserted with ID: {query_id}")

# Insert into TrainingData collection
training_data = {
    'website_id': website_id,  # Reference to website
    'data_type': 'text',
    'data': 'Training data for chatbot.',
    'training_date': datetime.now()
}
training_data_id = db.training_data.insert_one(training_data).inserted_id
print(f"Training data inserted with ID: {training_data_id}")

# Insert into Analytics collection
analytics = {
    'website_id': website_id,  # Reference to website
    'total_queries': 100,
    'success_rate': 95,
    'rating': 4.8,
    'totalfeedbacks': 50,
    'report_date': datetime.now()
}
analytics_id = db.analytics.insert_one(analytics).inserted_id
print(f"Analytics data inserted with ID: {analytics_id}")
