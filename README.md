# temperature-app

## Overview

This project includes a **temperature conversion web application** built using Python (Flask) and contains a **CI/CD pipeline** for building and deploying the application using Docker. It also integrates **Prometheus** for monitoring the application and **Grafana** for visualizing metrics.

In this README, we will outline all the steps involved in setting up this infrastructure, including:

- Dockerizing the Python application.
- Setting up Jenkins for the CI/CD pipeline.
- Setting up Prometheus and Grafana for monitoring and visualization.
- Configuring alerts for system performance metrics.

---

## Table of Contents

1. [Dockerizing the Application](#dockerizing-the-application)
2. [Setting Up Jenkins CI/CD Pipeline](#setting-up-jenkins-cicd-pipeline)
3. [Monitoring Setup (Prometheus & Grafana)](#monitoring-setup-prometheus--grafana)
   - [Prometheus Setup](#prometheus-setup)
   - [Grafana Setup](#grafana-setup)
4. [Application](#application)
5. [Webhook](#webhook)
## Dockerizing the Application

This project involves running three containers and one test container:

1. **Temperature Application Container**: This container runs the Flask-based temperature conversion application. 
2. **Prometheus Container**: This container collects and stores metrics for monitoring the application.
3. **Grafana Container**: This container visualizes the metrics collected by Prometheus in real-time.
4. **Test Container**: This container is used to run automated tests to verify the functionality of the application.

Look at Documentation/docker1.png, Documentation/docker2.png, Documentation/docker3.png

---

## Setting Up Jenkins CI/CD Pipeline

## The pipeline consists of the following stages:

Checkout - This stage checks out the latest code from the GitHub repository.
Stop Existing Containers - This stage stops any running containers and cleans up the Docker environment.
Build - This stage builds the Docker image for the application.
Test - This stage runs automated tests inside a temporary test container.
Deploy to Production - This stage deploys the application using Docker Compose if all tests pass.

## Instruction for working with Jenkins

## Step 1: Install Jenkins
To install Jenkins, use the following Docker command:
docker run -d -p 8080:8080 -p 50000:50000 jenkins/jenkins:lts

Or it can be install on local environment.

## Step 2: Create Jenkinsfile
The Jenkinsfile defines the CI/CD pipeline for the project.
In our project it exist inside the folder /jenkins

## Step 3: Install Plugins:
In Jenkins, make sure to install the necessary plugins for Docker, such as:

Docker Pipeline
GitHub Integration
Blue Ocean (for a better UI)

## Step4: Create item pipeline
Documents/image1.png

## Step5. Configure setting for pipeline
Add the name of the GitHub project
In Pipeline section choose Pipeline script for SCM 
And write name of repo and name of the branch /main.
Script path to the jenkis file path: jenkins/Jenkinsfile
Documents/image2.png
Documents/image3.png
Documents/image4.png


---

## **Monitoring Setup (Prometheus & Grafana)**


   ## Prometheus Setup
Open your web browser and navigate to **http://localhost:9090** (default Prometheus URL).

Prometheus will collect metrics from your application and the host machine. To configure Prometheus, create a prometheus.yml file.


We  can configure Prometheus alerts by defining alert rules in a alerts.rules.yml

Look at Documentation/prometheus1.png, Documentation/prometheus2.png

---

   ## Grafana Setup
   ## Step 1
   1. Open your web browser and navigate to **http://localhost:3000** (default Grafana URL).
   2. Log in with your Grafana credentials. The default login is:
      - **Username**: `admin`
      - **Password**: `admin` (or the password you've set during setup)
   3. Once logged in, you will be directed to the **Grafana home dashboard**.


  ## Step 2 Add Prometheus as Data Source
1. Add Prometheus as Data Source
2. Log in to Grafana and click on "Configuration" (gear icon) in the left sidebar.
3. Select "Data Sources", then click "Add data source".
4. Choose Prometheus as the data source.
5. Set the URL to http://prometheus:9090 (the Prometheus service name in Docker Compose).
6. Click "Save & Test" to ensure Grafana can connect to Prometheus.


## **Step 3: Create a New Folder for Dashboards**

1. On the **left sidebar**, click on the **"+"** (Create) icon.
2. From the dropdown menu, select **"Folder"** to create a new folder.
3. In the **"Create Folder"** dialog:
   - Name your folder based on the type of metrics you are going to monitor. For example:
     - `Temperature Monitoring` for application-specific metrics.
     - `System Health` for system-wide monitoring (CPU, memory, disk, etc.).
     - `App Metrics` for more detailed application performance metrics.
4. Click **Save** to create the folder.
5. The new folder will appear in the left sidebar under the **"Folders"** section.

## Step 4: Create a New Dashboard

1. To create a new dashboard, click on the **"+"** (Create) icon in the left sidebar again.
2. Select **"Dashboard"** from the dropdown menu. This will create a new empty dashboard.
3. Once in the empty dashboard, click on **"Add Panel"** to add a new visualization panel.
4. In the **Panel Editor**, choose **Prometheus** as the data source (ensure Prometheus is set up as a data source in Grafana).
5. Write the appropriate **Prometheus query** to visualize the metric you want to monitor. Here are some examples of common queries:

## Step 5: Create Alerts in Grafana
In the dashboard, click on the Panel Title and select Edit.
Go to the Alert tab.
Set up alert conditions (e.g., when CPU usage is greater than 80% for 5 minutes).
Define the alert rule and the severity.
Set up notifications (you can skip this step if you don't need notifications).

Look at the Documentation/grafana(1-5).png

---

## Application

 Open your web browser and navigate to **http://localhost:5000** (default app URL).Look at the Documents/app.png

## Webhook
1. Install GitHub Plugin (if not installed)
First, make sure you have the GitHub plugin installed on Jenkins to integrate GitHub with Jenkins. Here's how to do that:

Navigate to Jenkins > Manage Jenkins > Manage Plugins.
Under the Available tab, search for GitHub Plugin.
Install the plugin and restart Jenkins.

2. Configure GitHub Integration in Jenkins
Go to Jenkins > Manage Jenkins > Configure System.
Find the GitHub section under the GitHub Servers section.
Add a new GitHub server:
GitHub API URL: https://api.github.com
Credentials: Add GitHub credentials if they are not already configured (you will need a GitHub token to authenticate).

3. Set Up a Webhook in GitHub
Now, set up a webhook in your GitHub repository that will notify Jenkins of any pull requests.
Go to your GitHub repository.
Click on Settings > Webhooks.
Click Add webhook.
In the Payload URL field, enter the Jenkins URL to trigger builds, e.g., http://<jenkins-server>/github-webhook/.
Set the Content type to application/json.
Select Let me select individual events and check Pull requests.
Make sure the Active box is checked and click Add webhook.

4. Configure Jenkins Job to Listen to GitHub Events
In your Jenkins pipeline job configuration, add a trigger for GitHub events. Follow these steps:

Go to Jenkins > Your Job > Configure.
In the Build Triggers section, check GitHub hook trigger for GITScm polling.
This will allow Jenkins to listen for GitHub webhook events (like pull requests) and trigger the build automatically.


5. Update Your Jenkinsfile (Optional)

