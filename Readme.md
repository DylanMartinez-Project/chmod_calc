
### Chmod Calculator App
This repository contains a basic Chmod Calculator application written in Python. It utilizes Streamlit, a Python framework for building interactive web applications. The app allows users to calculate and visualize file permission modes using the chmod octal values.

### Technologies Used
- Python
- Streamlit
- Virtual Environment (venv)
- Linux
- Docker

### What is Streamlit?
Streamlit is a powerful Python library used for creating and sharing custom web applications for machine learning and data science projects. With Streamlit, you can easily turn your data analysis scripts into interactive web apps without the need for extensive web development knowledge. It provides a simple and intuitive way to build user interfaces, allowing you to focus on showcasing your data and models.

### Virtual Environment (venv)
Virtual Environment, commonly abbreviated as venv, is a tool in Python that helps create isolated Python environments. It allows you to install and manage specific packages and dependencies for a project without interfering with other Python projects on the same machine. Using venv ensures that your project's dependencies are contained within a separate environment, reducing conflicts and ensuring reproducibility.

### Linux
Linux is an open-source operating system kernel used by many different distributions, such as Ubuntu, Fedora, and CentOS. It provides a robust and reliable foundation for various applications, including web servers, data centers, and embedded systems. Linux offers a command-line interface (CLI) that allows users to interact with the operating system using text commands, providing flexibility and powerful control over the system.

## Chmod Octal Values
The chmod command in Linux is used to change file permissions. It uses octal values to represent different permission modes for files and directories. Each digit in the octal value represents the permissions for different user groups: owner, group, and others.

- 0 - No permission
- 1 - Execute permission
- 2 - Write permission
- 3 - Write and execute permissions
- 4 - Read permission
- 5 - Read and execute permissions
- 6 - Read and write permissions
- 7 - Read, write, and execute permissions
<p> For example, if you set the permission mode to 755, it means the owner has read, write, and execute permissions, while the group and others have only read and execute permissions.

Repository Structure
- chmod.py: Python code for the Chmod Calculator application.
- Pip file containing the necessary dependencies for the project.
- Dockerfile: Dockerfile to build a Docker image for the application. ( This needs to be built into a multi arch image)
manifest.yaml: A basic Kubernetes manifest file to deploy the application in a Kubernetes cluster. (deployment,svc)
- Docker Image - The Docker image for the Chmod Calculator application is available on Docker Hub at the following registry: https://hub.docker.com/r/dielawnk8s/chmodcalcapp.

Kubernetes Deployment
To deploy the application in a Kubernetes cluster, you can use the included manifest.yaml file. Make sure you have a running Kubernetes cluster and the kubectl command-line tool installed. Run the following command to deploy the application:


kubectl apply -f chmod.yaml
This will create the necessary resources in your Kubernetes cluster to run the Chmod Calculator application.

Feel free to explore the code and customize it according to your needs. If you have any questions or suggestions, please feel free to reach out.

Happy coding!
