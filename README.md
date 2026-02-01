# PIPECRAFT – Reliable Data Pipelines for Analytics

## Project Overview
___________________
- PIPECRAFT is a data engineering project designed to demonstrate how raw data is ingested, processed, and transformed into analytics-ready datasets. The project simulates a real-world data pipeline by following structured ETL principles commonly used in professional data engineering environments.
- The primary focus of PIPECRAFT is reliability and clarity. Raw data is collected from external sources, cleaned and transformed using Python, and loaded into a relational database where it can be queried for analytical use. The project reflects how data engineering supports analytics and decision-making by preparing clean and consistent data.

## Objectives
_____________________
- * Ingest raw data from external APIs
- * Separate raw and processed data layers
- * Perform data cleaning and transformation using Python
- * Load processed data into a relational database
- * Create analytics-ready tables using SQL
- * Demonstrate pipeline automation and execution flow
- * Follow modular and maintainable project structure

## Project Structure
________________________
PIPECRAFT/
* data/
  * raw/
    * api_raw_data.csv
  * processed/
    * cleaned_data.csv
* ingestion/
  * fetch_api_data.py
* transformation/
  * clean_transform.py
* loading/
  * load_to_db.py
* sql/
  * analytics_tables.sql
* automation/
  * pipeline_runner.py
* config/
  * db_config.py
* requirements.txt
* README.md

## Data Ingestion
_________________
- The data ingestion layer is responsible for collecting raw data from an external API. The ingested data is stored in its original form without modification. This separation ensures traceability and allows the pipeline to be reprocessed if required.

## Data Transformation
_____________
- The transformation layer processes the raw data and prepares it for analytical use. This includes removing duplicate records, validating values, formatting fields, and applying basic data quality checks. Cleaned data is stored separately to maintain a clear distinction between raw and processed datasets.

## Data Loading
_______________
- The processed data is loaded into a relational database using Python. Tables are created with appropriate data types to ensure consistency and reliability. This database acts as the source of truth for downstream analytics and reporting.

## SQL Analytics Layer
_____________
- SQL scripts are used to create analytical tables and summaries from the loaded data. This layer demonstrates how data engineers prepare structured datasets that can be directly consumed by analysts and BI tools.

## Pipeline Automation
___________________
- The pipeline execution is automated using a Python runner script. This script orchestrates the ingestion, transformation, and loading steps in the correct sequence, simulating scheduled and repeatable pipeline execution.

## Tools and Technologies
____________________
* Python
* SQL
* pandas
* REST APIs
* MySQL
* Modular scripting

## Project Outcomes
______________________
* Practical understanding of ETL pipeline design
* Experience with API-based data ingestion
* Hands-on data transformation using Python
* Integration of Python with relational databases
* Creation of analytics-ready datasets
* Exposure to automation and pipeline execution concepts

## Conclusion
_____________________
PIPECRAFT demonstrates how data engineering enables analytics by ensuring that raw data is transformed into reliable and structured datasets. The project reflects real-world data pipeline practices and is suitable for entry-level data engineering, analytics engineering, and data analytics roles.
