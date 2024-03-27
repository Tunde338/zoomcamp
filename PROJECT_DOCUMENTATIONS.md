**Project Overview**

**Title:  Real-time Cryptocurrency Data Pipeline**

The Real-time Cryptocurrency Data Pipeline project is a sophisticated system engineered to collect, process, analyze, and visualize cryptocurrency data in real-time. This comprehensive pipeline integrates advanced technologies and cloud services to ensure seamless data management and insightful visualization of cryptocurrency trends.

**Project Aim**
Project Goal: Empower Informed Cryptocurrency Investment

My project aims to keep users updated on digital currency trends, helping them identify investment opportunities and offering personalized advice. By providing real-time insights and promoting financial literacy, I want strive to be a trusted resource for individuals navigating the cryptocurrency market.

**Link to the project architectuer**
https://github.com/Tunde338/zoomcamp/blob/zoomcamp/project_images/zoomcamp%20data%20arc.png

**Project Structure Outline:**

Data Collection (Kafka):

Apache Kafka serves as the streaming tool for ingesting real-time cryptocurrency data from various sources. Kafka's distributed architecture ensures scalability and fault tolerance, making it suitable for handling high volumes of streaming data.
Data Lake (Google Cloud Storage - GCS):

**Link to the image of Producer and Consumer runnung**
Producer: https://github.com/Tunde338/zoomcamp/blob/zoomcamp/project_images/producer_sending_data.png
Consumer: https://github.com/Tunde338/zoomcamp/blob/zoomcamp/project_images/consumer_recieving_data.png


Google Cloud Storage acts as the data lake for storing raw cryptocurrency data. GCS provides high durability, scalability, and low-latency access to data, facilitating efficient data ingestion and storage.
Orchestration (Mage):

**Link to mage pipelie image**
https://github.com/Tunde338/zoomcamp/blob/zoomcamp/project_images/mage_pipe_line.png


Mage is utilized as the orchestration tool to manage the workflow of the data pipeline. Mage facilitates the movement of data from GCS to BigQuery for storage and analysis, ensuring seamless coordination and execution of pipeline tasks.
Data Warehousing (Google BigQuery):

**Link to the Mage image, which triggers every two minutes.**
https://github.com/Tunde338/zoomcamp/blob/zoomcamp/project_images/mage%20running%20sucessfully.png



Google BigQuery serves as the data warehouse for storing processed cryptocurrency data. BigQuery offers a fully managed, highly scalable, and cost-effective solution for storing and querying large datasets, making it suitable for analytics and data warehousing.
Analytics (dbt - Data Build Tool):

dbt (Data Build Tool) is employed for performing analytics on cryptocurrency data. dbt enables data transformation and modeling in SQL, providing a structured and repeatable way to build data pipelines for analytics purposes.

**Liink to dbt lineage**
https://github.com/Tunde338/zoomcamp/blob/zoomcamp/project_images/dbt_lineage.png


Visualization (Looker):

Looker is utilized as the visualization tool for creating interactive dashboards and reports to visualize cryptocurrency data insights. Looker's user-friendly interface and powerful visualization capabilities enable users to explore and analyze data effectively.

**Dashboard link:**
https://lookerstudio.google.com/reporting/898616a0-240f-4146-ab5b-8ca9552f7aca


**Workflow:**

Real-time cryptocurrency data is ingested into Kafka from various sources.
Kafka streams are persisted to Google Cloud Storage (GCS) as raw data.
Mage orchestrates the pipeline, facilitating the movement of data from GCS to BigQuery for storage and analysis.
dbt performs data transformation and modeling on the stored cryptocurrency data, preparing it for analytics.
Looker connects to BigQuery to create interactive dashboards and visualizations for monitoring cryptocurrency trends and performance metrics.

**Deployment:**

The pipeline is deployed on Docker containers running on virtual machines (VMs). Docker provides a lightweight and portable environment for containerized deployment, while VMs offer scalability and isolation for running containerized applications.

**Benefits:**

Real-time Insights: The pipeline provides real-time insights into cryptocurrency market trends and performance, enabling timely decision-making.
Scalability: Leveraging cloud-native technologies ensures scalability to handle growing data volumes and user demands.
Cost-effectiveness: Utilizing managed services like GCS, BigQuery, and Looker minimizes infrastructure costs and overhead.
Flexibility: The modular architecture of the pipeline allows for easy integration of additional data sources, analytics tools, and visualization platforms.

**Future Enhancements:**

Integration of additional data sources to enrich cryptocurrency analytics.
Implementation of advanced machine learning models for predictive analytics and anomaly detection.
Enhancement of visualization capabilities to provide deeper insights and actionable intelligence.
The Real-time Cryptocurrency Data Pipeline project empowers users with actionable insights and strategic intelligence, enabling them to navigate and capitalize on the dynamic cryptocurrency markets effectively.



**Prerequisites for Running the Real-time Cryptocurrency Data Pipeline:**

Programming Languages:

Python: The project is primarily developed using Python for implementing various components of the pipeline.
SQL: Knowledge of SQL is beneficial for working with databases and performing data analysis.
Libraries and Dependencies:

confluent_kafka: 
Required for interacting with Apache Kafka and ingesting real-time cryptocurrency data streams.

google-cloud-storage:
Necessary for accessing and managing data stored in Google Cloud Storage (GCS).

pandas: 
Essential for data manipulation and analysis tasks, providing efficient data structures and functions.

requests: 
Used for making HTTP requests, particularly in fetching external data sources or interacting with APIs.
Setting Up Databases and External Services:

Google Cloud Storage (GCS):
Create a Google Cloud Platform (GCP) account and set up a GCS bucket to store raw cryptocurrency data.

Apache Kafka:
Install and configure Apache Kafka to set up a streaming platform for ingesting real-time data streams.

Google BigQuery (Optional):
If utilizing Google BigQuery for data warehousing and analysis, provision a BigQuery dataset to store processed cryptocurrency data.

**Step-by-Step Installation Guide:**

Install Python:

Download and install Python from the official Python website (https://www.python.org/).
Follow the installation instructions for your operating system.

Install Required Python Libraries:

Open a terminal or command prompt.
Use pip, the Python package manager, to install the necessary libraries:


pip install confluent_kafka google-cloud-storage pandas requests
Set Up Google Cloud Storage (GCS):

Sign in to the Google Cloud Console (https://console.cloud.google.com/).
Create a new project or select an existing one.
Navigate to the Cloud Storage section and create a new bucket to store cryptocurrency data.

Install Apache Kafka:

Download Apache Kafka from the official website (https://kafka.apache.org/downloads).
Follow the installation instructions provided in the Kafka documentation.
Set Up Google BigQuery (Optional):

Sign in to the Google Cloud Console.
Navigate to the BigQuery section and create a new dataset to store processed cryptocurrency data.















Pipeline Overview:

