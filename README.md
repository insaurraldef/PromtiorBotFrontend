Promtior Chat Bot Frontend

A Web Interface for the Promtior Chatbot

Project Overview

This project implements a user-friendly web interface for interacting with the Promtior chatbot. The interface is designed to send user queries to the backend chatbot API and display the responses in real-time. The solution uses Flask as the web framework and HTML/CSS/JavaScript for building the frontend.

The frontend facilitates seamless communication between users and the backend chatbot, making the chatbot more accessible for end users without requiring knowledge of APIs or Postman.

The development involved:
	1.	Integration with the Backend API: Configuring the frontend to communicate with the /chatbot endpoint of the backend.
	2.	Responsive UI Design: Ensuring the interface works smoothly across various devices.
	3.	Error Handling: Providing meaningful feedback to users when the chatbot is unreachable or encounters an error.

 Features

	1.	Interactive Web UI: A simple yet effective interface where users can type their questions and receive responses in a conversational format.
	2.	Backend Communication: All queries are sent to the backend chatbot API via a POST request, and the responses are displayed in the chat window.
	3.	Dynamic Styling: Designed using CSS to enhance the user experience with a visually appealing interface.
	4.	Error Handling: Displays error messages if the backend is unreachable or fails to process the query.

 Architecture and Components

	1.	Flask App:
	•	Hosts the web interface and handles user queries.
	•	Sends POST requests to the backend chatbot API and renders the responses.
	2.	Static Files:
	•	static/: Contains CSS, JavaScript, and image files for styling and functionality.
	•	templates/: Contains the HTML template (index.html) for rendering the frontend.
	3.	Backend API Communication:
	•	Sends user input from the web form to the backend /chatbot endpoint using JavaScript’s fetch() method.


 Improvements and Future Work

	•	Enhanced UI/UX: Add more animations, user guidance, or tooltips.
	•	Authentication: Implement user login for secure interactions.
	•	Logging: Track queries and responses for debugging and analytics.

 Enjoy the Promtior chatbot with a smooth and interactive web experience!

Created by Franco!
