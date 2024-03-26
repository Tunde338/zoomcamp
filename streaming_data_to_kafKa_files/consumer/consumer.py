from confluent_kafka.admin import AdminClient, NewTopic
from confluent_kafka import Consumer, KafkaError
import json
from google.cloud import storage
import pandas as pd
import os
import time

key_path = os.path.join(r'C:\Users\HP\capstone_project\data-engineering-zoomcamp\06-streaming\python\kafka_project', 'key.json')

BOOTSTRAP_SERVERS = 'localhost:9092'
KAFKA_TOPIC = 'coinbase'
GROUP_ID = 'my_consumer_group'
GCS_BUCKET_NAME = 'data_tlk_388'
GCS_FILE_NAME = 'codebase_market_data_new.csv'

# Configure the consumer
consumer_conf = {
    'bootstrap.servers': BOOTSTRAP_SERVERS,
    'group.id': GROUP_ID,
    'auto.offset.reset': 'earliest',
}

# Create a Kafka consumer instance
consumer = Consumer(consumer_conf)

# Create an AdminClient for topic creation
admin_client_conf = {'bootstrap.servers': BOOTSTRAP_SERVERS}
admin_client = AdminClient(admin_client_conf)

# Check if the topic exists, and create it if not
existing_topics = admin_client.list_topics().topics
if KAFKA_TOPIC not in existing_topics:
    new_topic = NewTopic(KAFKA_TOPIC, num_partitions=1, replication_factor=1)
    admin_client.create_topics([new_topic])

# Subscribe to the Kafka topic
    
consumer.subscribe([KAFKA_TOPIC])

# Initialize GCS client
gcs_client = storage.Client.from_service_account_json(key_path)

try:
    while True:
        # Poll for messages
        msg = consumer.poll(1.0)

        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                continue
            else:
                print(f"Error: {msg.error()}")
                break

        # Process the received message
        try:
            market_data = json.loads(msg.value().decode('utf-8'))
            print(f"Received market data: {market_data}")

            # Convert market data to Pandas DataFrame
            market_df = pd.DataFrame([market_data])

            # Define data types
            data_types = {
                'exchangeId': str,
                'rank': pd.Int64Dtype(),
                'baseSymbol': str,
                'baseId': str,
                'quoteSymbol': str,
                'quoteId': str,
                'priceQuote': float,
                'priceUsd': float,
                'volumeUsd24Hr': float,
                'percentExchangeVolume': float,
                'tradesCount24Hr': pd.Int64Dtype(),
                'updated': 'datetime64[ns]'
            }

            # Convert data types and handle missing values
            # Specify fill values for missing values
            fill_values = {'rank': pd.NA, 'tradesCount24Hr': pd.NA, 'updated': pd.NA}
            market_df = market_df.fillna(fill_values)


            


            # Write the data to Google Cloud Storage as CSV
            bucket = gcs_client.get_bucket(GCS_BUCKET_NAME)
            blob = bucket.blob(GCS_FILE_NAME)

            # Read existing content if it exists
            existing_content = blob.download_as_string() if blob.exists() else ""

            if isinstance(existing_content, bytes):
                existing_content = existing_content.decode('utf-8')

            # Append the new data to the existing content
            new_content = existing_content + market_df.to_csv(index=False, header=not blob.exists())

            # Upload the updated content to the blob
            blob.upload_from_string(new_content, content_type='text/csv')


            # Introduce a delay to avoid rate limits (adjust as needed)
            time.sleep(2)  # You can adjust the sleep duration based on your needs

        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")

except KeyboardInterrupt:
    print("Consumer terminated by user.")
finally:
    # Close down consumer to commit final offsets.
    consumer.close()


