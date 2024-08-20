# Introduction

## What's data engineering?
Data engineering is the practice of designing and building software for collecting, storing, and managing data. The most common goal in data engineering is to enable stakeholders (such as product managers, marketing, or the C-suite) to make informed decisions with data. Other common goals are providing data to external users, features for a machine learning model, or empowering applications to react to events.

## What's workflow?

In data engineering, a workflow is a series of automated steps or tasks that process, transform, and move data from one system or format to another. It’s like a blueprint that outlines how data should flow through various stages, from ingestion to processing, storage, and eventually to its end use, such as reporting or analysis.

### Example
Imagine you're collecting user activity data from a website. A typical workflow might look like this:
1. **Ingestion**: Collect clickstream data from the website in real-time using Apache Kafka.
2. **Processing**: Use Apache Spark to clean and aggregate the data, such as calculating daily active users.
3. **Storage**: Store the processed data in a data warehouse like BigQuery for further analysis.
4. **Quality** Checks: Ensure the data is accurate and complete before making it available for reporting.
5. **Serving**: Provide access to this data through a dashboard in tools like Tableau or Looker, where the business team can analyze trends.

## What's an orchestrator?

A workflow orchestrator is a tool or platform that manages the execution, scheduling, and coordination of a series of tasks or jobs in a data engineering pipeline. It ensures that these tasks are executed in the correct order, handles dependencies between them, and manages any failures or retries that might occur during the workflow.


### Key Functions of a Workflow Orchestrator:
1. **Task Scheduling**: allow you to schedule when tasks should run—whether it's at a specific time, on a regular interval, or in response to an event.
2. **Dependency Managemen**t: Many workflows involve tasks that must be executed in a specific sequence. An orchestrator manages these dependencies, ensuring that a task only runs when its prerequisite tasks have successfully completed.
3. **Monitoring and Logging**: Orchestrators provide tools to monitor the status of workflows and tasks, offering insights into whether they’ve succeeded, failed, or are in progress. They also log details about the execution, which can be useful for troubleshooting.
4. **Failure Handling and Retries**: If a task fails, an orchestrator can automatically retry it, skip it, or trigger an alert. This helps to make workflows more resilient and less prone to manual intervention.

### Common Workflow Orchestrators
- **Apache Airflow**: The most popular open-source orchestrator. Task-centric orchestrator.
- **Prefect**: API-first approach orchestrator.
- **Dagster**: Asset-centric orchestrator
- **Luigi**: Developed by Spotify, Luigi is another open-source orchestration tool that focuses on long-running batch processes.