# Challenge DevSecOps/SRE

## Contents

- 📝[Project Description](#description)
- 🧩[Assumptions](#assumptions)
- 📥[Evidence of the Request](#evidence-of-the-request)
- 🖥️[Architecture](#architecture)
- 🚨[How to Contribute](#how-to-contribute)
- 🔧[Future Improvements](#future-improvements)
- 🔒[Managing Sensitive Files](#managing-sensitive-files)
- 💬[Comments](#comments)
- 🎉[Acknowledgments and Credits](#acknowledgments-and-credits)
- 📜[License](#license)
- ⏳[Contact](#contact)

## 📝Description

This project addresses the challenge of creating a system for ingesting, storing, and exposing data, specifically designed for advanced analytics. The system is developed to:

1. 📥**Ingest Data**: Utilize a **Pub/Sub** schema to manage and process incoming data messages efficiently. This approach ensures scalable and reliable data ingestion.

2. 🗄️**Store Data**: Implement a **database** optimized for analytical queries to store the ingested data, facilitating complex and performance-efficient data analysis.

3. 🌐**Expose Data**: Provide an **HTTP endpoint** that serves the stored data upon request, making it accessible for consumption by third parties.

To achieve these goals, the project uses:

- **Infrastructure as Code (IaC)**: For defining and deploying infrastructure components, ensuring consistency and repeatability.

  - **Tools Used:**

    - **Terraform** was used for deploying cloud infrastructure, allowing for consistent and version-controlled infrastructure across multiple environments.

    - **Ansible** was employed for server provisioning and configuration management, chosen for its simplicity and ability to automate complex tasks across multiple servers without the need for agents.

- **CI/CD Implementation**: For automating the deployment process and ensuring that changes are integrated and tested continuously.

  - **Tool Selection**

    - **GitHub Actions**: Since this project is hosted on GitHub, is an excellent choice for implementing a pipeline.

      - It is a native tool that allows workflow automation directly in the repository, with easy integration for testing, deployment, and other processes.

  - **Pipeline Configuration**

    - **Continuous Integration (CI)**: Is configured to automatically run every time a commit is made to the develop and master branches. The main steps are:

      1. **Code Verification**:

         - **Linting**: Run a tool like **flake8** to ensure the code adheres to Python style conventions.

         - **Formatting**: Use **black** to consistently format the code.

      2. **Unit Testing**:

         - **Pytest**: Ensure all tests pass.

           - This can be done in a specific virtual environment to ensure consistency.

      3. **Test Coverage**:

         - **Code Coverage**: Use **pytest-cov** to generate a report and upload it to a service like **Codecov** or **Coveralls** for additional analysis.

      4. **Build**:

         - **Docker**: Image of the application to ensure that all changes can be packaged correctly.

    - **Continuous Deployment (CD)**: Is triggered automatically after the CI tests pass and can include the following steps:

      1. **Deployment to Testing Environments**:

         - Deploy the application to a staging environment using **Docker Compose** or **Kubernetes**. This allows validations in a controlled environment before moving the changes to production.

      2. **Code Review**:

         - Configure a manual or automated review to have an administrator approve changes before deploying to production.

      3. **Deployment to Production**:

         - Once approved, deploy the new version to production. Depending on the infrastructure, this could include:

            - **Docker Desktop**: Local environment.

            - **Kubernetes**: Apply manifests to update the pods and services in production.

      4. **Notifications**:

         - Configure Slack or email notifications to inform the team of the success or failure of the deployment.

  - **Continuous Improvement**: Can be improved in the future to include:

    - **Integration and E2E Testing**: Add integration and end-to-end tests to ensure all parts of the system work well together.

    - **Automated Rollbacks**: Implement automatic rollback mechanisms in case of failures during production deployment.

    - **Security**: Include security scanners like Bandit to identify vulnerabilities in the code before deployment.

- **Quality Testing, Monitoring, and Alerting**: To maintain the system’s health and performance, incorporating integration tests, and real-time monitoring.

  - and alerting mechanisms using **Prometheus / Grafana** for monitoring and Alertmanager for notifying on critical issues.

## 🧩Assumptions

During the implementation of the solution, the following assumptions were made:

- **Data Format**: It is assumed that the input data follows the format specified in the challenge statement. Any variations in format may require additional adjustments.

- **Execution Environment**: The development was done under the assumption that the execution environment has Python **[3.12.4]** and the necessary libraries installed. Specific details about the environment are outlined below.

- **Dependencies**: The project depends on certain libraries specified in the **`requirements.txt`** file. It is assumed that these libraries are available in the specified versions.

## 📤Evidence of the Request

- To demonstrate that the POST request to the endpoint was successfully made, a Python script **`api.py`** was executed to send the specified data. Below is the output from the request:

![alt text][json]

- This snapshot demonstrates how to send a POST request to the endpoint and verify the response. The response confirms that the request was received and processed successfully.

## 🖥️Architecture

For detailed information on the system's architecture, including design decisions and component interactions, refer to the [Architecture Guide](docs/ARCHITECTURE.md).

## 🖥️How to Contribute

To contribute to this project, please check out our [Contribution Guide](docs/CONTRIBUTING.md) for instructions on setting up your development environment and the process for submitting contributions.

Describe how to contribute to the project’s documentation

## 🔧**Future Improvements**

While the current solution addresses the core functionalities required, there are several areas where enhancements could be made to further optimize and extend the system:

### **1. Algorithm Optimization**

- **Current State**: The existing algorithm is functional but may become a bottleneck with very large datasets.
- **Proposed Improvement**: Optimize the algorithm to handle larger volumes of data more efficiently. Techniques such as indexing, partitioning, or more efficient search algorithms could be explored to improve performance.

### **2. Error Handling**

- **Current State**: Basic error handling is implemented.
- **Proposed Improvement**: Enhance error handling to cover a wider range of potential issues. This includes adding more comprehensive validation for input data, implementing more specific exception handling, and providing detailed error messages to help with debugging.

### **3. Additional Documentation**

- **Current State**: Documentation is present but may lack depth in certain areas.
- **Proposed Improvement**: Expand the documentation to include:
  - Detailed architecture diagrams and explanations.
  - Design decisions and trade-offs.
  - Instructions for extending or modifying the codebase to accommodate new features.

### **4. Additional Testing**

- **Current State**: Basic unit tests are implemented.
- **Proposed Improvement**: Expand testing coverage to include:
  - Edge cases and boundary conditions.
  - Integration tests to ensure that different components of the system work together as expected.
  - Load and stress testing to evaluate the system's performance under high traffic conditions.

### **5. Monitoring and Logging Integration**

- **Current State**: Basic logging is implemented, but real-time monitoring and advanced logging are not integrated.
- **Proposed Improvement**: Integrate a comprehensive monitoring and logging solution to enhance system observability and troubleshooting:
  - **Prometheus and Grafana**: Implement Prometheus for metrics collection and Grafana for visualizing these metrics. This setup will help in monitoring system performance, resource usage, and identifying potential issues in real-time.
  - **ELK Stack (Elasticsearch, Logstash, Kibana)**: Deploy the ELK Stack to aggregate logs, provide powerful search capabilities, and create dashboards for visualizing log data. This will assist in identifying trends, troubleshooting issues, and maintaining system health.

### **6. Security Enhancements**

- **Current State**: Basic security measures are in place.
- **Proposed Improvement**: Implement additional security measures such as:
  - Encryption for data at rest and in transit.
  - Regular security audits and vulnerability assessments.
  - Implementing access controls and user authentication mechanisms.

## 🔒Managing Sensitive Files

### `.env` Files

- **Description**: The **`.env`** file contains essential environment variables for project configuration, such as credentials and API keys.
- **Setup**: Create a **`.env`** file in the root of the project using the **`.env-example.txt`** file as a reference. Fill it with your own variables.
- **Important**: The **`.env`** file is listed in **`.gitignore`** to prevent it from being uploaded to the repository.

### JSON Files

- **Description**: The **`data.json`** file may contain environment-specific or sensitive data.
- **Example File**: Use the **`json-example.txt`** file as a reference to understand the structure of the JSON file. Do not include sensitive data in the repository.

## 💬Comments

The current implementation provides a functional system for data ingestion, storage, and exposure. These future improvements are aimed at enhancing the system's performance, reliability, and maintainability. Feedback and suggestions for further enhancements are welcome.

>[!WARNING]
>
>- Some features may require additional configuration based on your environment.
>
>[!IMPORTANT]
>
> **Dependency Updates**: Keep dependencies up to date by running:
>
> ```bash
> pip install --upgrade -r requirements.txt
> ```
>
>[!NOTE]
>
>- For detailed documentation and setup instructions, refer to the docs/ directory.

## 🎉Acknowledgments and Credits

- **Libraries and Tools**: Thanks to Library Name and Tool Name for their excellent documentation and support.

- **Tutorials and Guides**: Special thanks to Tutorial/Guide Name for providing a valuable resource during development.

## 📜License

- This project is licensed under the MIT License. See the LICENSE file for more details.

## ⏳Contact

Thank you for considering my submission. If you have any questions or need further clarification, please feel free to reach out to me via [email](mailto:omaciasnarvaez@gmail.com).

[json]: assets/images/json.png
