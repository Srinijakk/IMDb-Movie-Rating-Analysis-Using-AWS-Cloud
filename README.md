# 🎬 IMDb Movie Rating Analysis Using AWS Cloud

## 📌 Project Overview
This project utilizes AWS Cloud services to analyze and extract insights from IMDb movie datasets. It demonstrates how to design and deploy an **automated, scalable ETL pipeline** capable of handling large datasets for real-time analytics. The goal is to uncover trends related to **movie ratings, genres, directors, stars, and box office performance**, enabling users to explore movie metrics via interactive dashboards.

---

## 🎯 Objectives
- Design and implement a cloud-based ETL pipeline for IMDb data analysis.
- Uncover trends and correlations in movie ratings, genres, and financial success.
- Enable real-time reporting and interactive visualizations via dashboards.

---

## 🛠️ Tools & Technologies

| AWS Service              | Purpose                                                                 |
|--------------------------|-------------------------------------------------------------------------|
| **Amazon S3**            | Store raw IMDb datasets (CSV format)                                    |
| **AWS Glue**             | Perform ETL operations (cleaning, transforming, loading)                |
| **AWS Glue Crawler**     | Automatically infer schema and create data catalog                      |
| **Amazon Redshift**      | Store structured data for high-performance analytics                    |
| **AWS Lambda**           | Trigger ETL jobs on new S3 uploads                                      |
| **Amazon Athena**        | Run ad-hoc SQL queries on S3-stored data                                |
| **Amazon QuickSight**    | Create dashboards and visualizations                                    |
| **AWS CloudWatch**       | Monitor ETL pipelines and automation workflows                          |
| **AWS Glue Data Catalog**| Centralized metadata repository for all datasets                        |

---

## 📊 Dataset Description
The IMDb dataset includes the following fields:

- `Poster_Link`, `Series_Title`, `Released_Year`, `Certificate`, `Runtime`, `Genre`
- `IMDB_Rating`, `Overview`, `Meta_score`, `Director`
- `Star1`, `Star2`, `Star3`, `Star4`
- `No_of_Votes`, `Gross`

---

## 🚀 Project Workflow

### 1. Data Ingestion
- Upload IMDb dataset (CSV) to Amazon S3.

### 2. Schema Detection & Cataloging
- Use AWS Glue Crawler to detect schema and register it in the AWS Glue Data Catalog.

### 3. ETL Processing (AWS Glue)
- Handle missing values in `Gross`, `Meta_score`, and `IMDB_Rating`.
- Normalize and convert data types (e.g., `Runtime` to numeric).
- Load the cleaned and transformed data into Amazon Redshift.

### 4. Data Analysis
Using Redshift and Athena for querying:
- Top-rated movies by genre
- Impact of directors/stars on ratings and revenue
- Yearly box office income trends
- Correlation between rating, votes, and metascore

### 5. Data Visualization (Amazon QuickSight)
Create dashboards showing:
- Genre-wise IMDb rating distribution
- Top 10 movies by box office gross
- Director/star performance trends
- Correlation between votes and ratings

### 6. Automation & Monitoring
- Automate Glue job triggers using AWS Lambda when new data is uploaded to S3.
- Use CloudWatch for real-time monitoring of ETL job execution and error logs.

---

## 📈 Key Insights Delivered
- Identification of top-rated and highest-grossing movies
- Impact of genre, certification, and runtime on ratings
- Star/director influence on box office performance
- Relationship between IMDb rating and community engagement metrics

---

## 📦 Deliverables
- Fully automated AWS-based ETL pipeline
- Transformed and structured data stored in Amazon Redshift
- Ad-hoc analytical queries via Athena and Redshift
- Interactive dashboards using Amazon QuickSight
- Architecture diagram and project documentation

---

## 💡 Benefits
- Demonstrates end-to-end data engineering using AWS
- Real-world use case for cloud ETL and analytics
- Scalable and reusable data pipeline architecture
- Business insights for decision-making in the film industry

---

