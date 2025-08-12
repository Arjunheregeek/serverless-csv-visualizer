# Serverless CSV Data Visualizer 📊✨  
A fully serverless web application built on AWS that allows users to upload a CSV file, process the data in real-time, and visualize the results as an interactive bar chart. This project demonstrates a modern, event-driven architecture using core cloud services.

## 🌐 Live Demo  
[🔗 Click here to try the app!](http://arjun-gupta-csv-visualizer-app.s3-website.eu-north-1.amazonaws.com/)

---

## 🚀 Key Features  
- **Interactive Front-End** 🎨: A responsive and visually appealing user interface where users can upload files.  
- **Serverless Back-End** 🖥️: The entire back-end is powered by AWS Lambda, requiring no server management.  
- **Real-Time Processing** ⚡: Data is processed and visualized instantly upon upload.  
- **Scalable & Cost-Effective** 💰: The architecture scales automatically to handle demand and leverages the AWS Free Tier, making it highly cost-efficient.  

---

## 🏗️ Architecture  
This project uses a simple yet powerful serverless architecture:  
- **Amazon S3** 🗂️: Hosts the static front-end web application (index.html, CSS, JS).  
- **Amazon API Gateway** 🌐: Provides a secure and scalable HTTP endpoint that the front-end can call.  
- **AWS Lambda** 🛠️: Contains the Python code that processes the CSV data using the Pandas library. It's triggered by the API Gateway.  
- **AWS IAM** 🔒: Provides a secure role with the exact permissions needed for the Lambda function to operate, following the principle of least privilege.  

---

## 🛠️ Tech Stack  
- **Cloud** ☁️: AWS (S3, Lambda, API Gateway, IAM)  
- **Back-End** 🐍: Python, Pandas  
- **Front-End** 🌐: HTML5, CSS3, JavaScript (with HTML Canvas for visualization)  

---

## 📖 How It Works  
1. The user visits the static website hosted on **Amazon S3**.  
2. When the user uploads a CSV file and clicks "Generate Chart," the **JavaScript** on the page sends the file's content to the **API Gateway** endpoint via a POST request.  
3. The **API Gateway** triggers the **AWS Lambda** function, passing the CSV data in the request body.  
4. The **Python script** in Lambda uses the **Pandas library** to read the data, perform a `groupby()` aggregation to calculate the average price per category, and formats the result as a JSON object.  
5. The **Lambda function** returns the JSON result back to the **API Gateway**.  
6. The front-end **JavaScript** receives the JSON data and uses the **HTML Canvas API** to draw an animated bar chart, providing an instant visualization to the user.  

---

## 👨‍💻 About the Creator  
I am an **AI Engineer** with experience in building innovative and impactful projects. I have worked on numerous projects, including those that are more advanced and complex than this one. My passion lies in leveraging technology to solve real-world problems and creating solutions that are scalable, efficient, and user-friendly.