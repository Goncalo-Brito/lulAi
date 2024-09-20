from pymongo import MongoClient
from datetime import datetime

client = MongoClient('mongodb://localhost:27017/')
db = client['chatbot_db']

website = {
    'website_url': 'https://example.com',
    'website_name': 'Example Website',
    'integration_date': datetime.now()
}
website_id = db.websites.insert_one(website).inserted_id
print(f"Website inserted with ID: {website_id}")

document = {
    'document_name': 'Privacy Policy',
    'document_path': '/docs/privacy_policy.pdf',
    'document_type': 'pdf',
    'upload_date': datetime.now()
}
document_id = db.documents.insert_one(document).inserted_id
print(f"Document inserted with ID: {document_id}")

user = {
    'username': 'JohnDoe',
    'user_type': 'admin',
    'email': 'johndoe@example.com',
    'password': 'hashed_password',
    'registered_date': datetime.now()
}
user_id = db.users.insert_one(user).inserted_id
print(f"User inserted with ID: {user_id}")

scraped_data_website = {
    'sourceType': 'website',  
    'source_id': website_id, 
    'scraped_content': 'This is the scraped content from the website.',
    'scrape_date': datetime.now()
}
scraped_id_website = db.scraped_data.insert_one(scraped_data_website).inserted_id
print(f"Scraped data (Website) inserted with ID: {scraped_id_website}")

scraped_data_document = {
    'sourceType': 'document',
    'source_id': document_id,
    'scraped_content': 'This is the scraped content from the document.',
    'scrape_date': datetime.now()
}
scraped_id_document = db.scraped_data.insert_one(scraped_data_document).inserted_id
print(f"Scraped data (Document) inserted with ID: {scraped_id_document}")

user_query = {
    'scraped_id': scraped_id_website,
    'user_id': user_id,              
    'query': 'What is the privacy policy?',
    'response': 'Our privacy policy is...',
    'rating': 5,
    'comment': 'Very helpful!',
    'query_date': datetime.now()
}
query_id = db.user_queries.insert_one(user_query).inserted_id
print(f"User query inserted with ID: {query_id}")

training_data = {
    'website_id': website_id,
    'data_type': 'text',
    'data': 'Training data for chatbot.',
    'training_date': datetime.now()
}
training_data_id = db.training_data.insert_one(training_data).inserted_id
print(f"Training data inserted with ID: {training_data_id}")

analytics = {
    'website_id': website_id,  
    'total_queries': 100,
    'success_rate': 95,
    'rating': 4.8,
    'totalfeedbacks': 50,
    'report_date': datetime.now()
}
analytics_id = db.analytics.insert_one(analytics).inserted_id
print(f"Analytics data inserted with ID: {analytics_id}")
