# 0x10. Python - Network #0

## Description

This project covers fundamental concepts and techniques related to working with networks in Python. Key topics include:

- Understanding URLs and HTTP
- Parsing and reading URLs
- Schemes in HTTP URLs
- Domain names and sub-domains
- Defining port numbers in URLs
- Query strings
- HTTP requests and responses
- HTTP headers and message bodies
- HTTP request methods
- HTTP response status codes
- HTTP Cookies
- Making requests with cURL
- Understanding what happens when you type a URL in your browser (at the application level)

## Project Tasks

### [0. cURL body size](./0-body_size.sh)
Write a Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response.

### [1. cURL to the end](./1-body.sh)
Write a Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response.

### [2. cURL Method](./2-delete.sh)
Write a Bash script that sends a DELETE request to the URL passed as the first argument and displays the body of the response.

### [3. cURL only methods](./3-methods.sh)
Write a Bash script that takes in a URL and displays all HTTP methods the server will accept.

### [4. cURL headers](./4-header.sh)
Write a Bash script that takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response.

### [5. cURL POST parameters](./5-post_params.sh)
Write a Bash script that takes in a URL, sends a POST request to the passed URL, and displays the body of the response.

### [6. Find a peak](./6-peak.py)
Technical interview preparation: Write a Python function that finds a peak in a list of unsorted integers.

### [7. Only status code](./100-status_code.sh)
Write a Bash script that sends a request to a URL passed as an argument, and displays only the status code of the response.

### [8. cURL a JSON file](./101-post_json.sh)
Write a Bash script that sends a JSON POST request to a URL passed as the first argument, and displays the body of the response.

### [9. Catch me if you can!](./102-catch_me.sh)
Write a Bash script that makes a request to `0.0.0.0:5000/catch_me` that causes the server to respond with a message containing "You got me!", in the body of the response.

## Author

Lana Samson
