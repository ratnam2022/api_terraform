# Creating AKS infra using Terraform and deploying CRUD API in AKS

## CRUD API Application: 
A Python Flask application is created for viewing, adding, updating and deleting employee details using API. 

### Development setup

#### Local development: 

##### Prerequisites:

* Docker Desktop
* AZ CLI
* AZ AKS
* Python3 and its requirements(Flask, Jinja2, MarkupSafe, itsdangerous)
* Postman
* Terraform

##### Steps:

* Clone the repo in the local environment where the Docker Desktop is available.
  ```
  git clone git@github.com:ratnam2022/api_terraform.git api_terraform
* Run the below-mentioned command to build docker image
  ```
  docker build -t api_app:latest .
* Run the below-mentioned command in order to run the docker container with the created image in a detached mode.
  ```
  docker run -d --name my-python-app -p 5001:5001 api_app:latest
* The python app will start executing in the docker container

##### Test the created app:

* Access the below-mentioned URL to test the availability of the deployed app. If the browser displays the message "The application is running smoothly" then the application is up and running.  
  ```
  http://localhost:5001/health
* For testing CRUD operations. Follow the below steps using postman.
  ###### Read: "GET" Method
  ```
  http://localhost:5001/employees
  ```
  ###### Create: "POST" Method.
  Use the same URL with the below-mentioned sample request body. Add a new header "Content-Type" with the value "application/json"
  ```
  {
        "department": "DevOps",
        "email": "Mathew@contoso.com",
        "name": "Mathew",
        "id": 3
  }
   ```
  ###### Update: "PUT" Method.
  Append the same URL with the employee id and also use the below-mentioned sample request body. Add a new header "Content-Type" with the value "application/json". This will update the department of Martin from IT to DevOps. 
  ```
  http://localhost:5001/employees/2
  ```
  ```
  {
        "department": "DevOps",
        "email": "Martin@contoso.com",
        "name": "Martin",
        "id": 2
  }
  ```
  ###### Delete: "DELETE" Method.
  Append the URL with the employee ID which details need to be cleared. The sample URL is provided below. This will delete the Employee whose ID is "1".
  ```
  http://localhost:5001/employees/1
  
### Automated Deployment: 

Github action is enabled for this repo which will perform the following actions.

* AKS infra build pipeline - Manual trigger to create new AKS environment using terraform
* Python Application deployment - Automated Trigger on each commit in the main branch

#### AKS infra build pipeline:

This pipeline will create the AKS cluster and its necessary components using Terraform(IaC) with minimal cluster configuration. The Terraform state file is not stored anywhere in this initial pipeline design. This pipeline needs to be triggered manually when we need to create new AKS cluster.

####  Python Application deployment:

This pipeline will deploy the python application in the AKS along with its service. It will get triggered automatically when we commit/merge the PR into main branch. This pipelien will also do a basic availability testing of the deployed application by validating the response of the Health endpoint. 

### Testing of AKS deployed application:

The testing of the AKS deployed app is as similar to the local testing. Replace the "localhost:port" part of the URL with the AKS loadbalancer external IP. The CRUD operations testing remains the same after modifying the URL. 

### Limitations and Assumptions:
In the current design, there are a few limitations and assumptions considering the provided time period. 

* Docker hub is used for storing and retrieving the images instead of ACR
* External IP of the Load balancer is used to communicate the docker container in AKS.
* CDN should be implemented in future architecture or enhancement.
* Static code scan should be implemented in future architecture or enhancement
* AKS is designed with minimal configuration
* Terraform state file should be stored in the Storage account as a part of the enhancement
* Helm charts should be used for deployment. 
* Self-hosted GitHub agents should be considered for the future enhancement
* All the sensitive data/credentials are stored in the GitHub secrets
