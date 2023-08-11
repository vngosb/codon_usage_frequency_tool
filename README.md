# final_project
Advanced Practical Computer Concepts Final Project - Codon Usage Frequency Tool

# Overview

This repository contains a set of codes designed to process DNA sequences, translate them into protein sequences, and display triplet frequencies. The code consists of a CGI script for server-side processing, an HTML form for user input, and a JavaScript file to enhance the user interface.

# Implementation

- `final_project.cgi`: This CGI script takes a DNA sequence as input, processes it, and returns a JSON response containing a protein sequence and triplet frequency information.

- `index.html`: This HTML file provides a user interface where users can input their DNA sequence. It utilizes jQuery and the JavaScript file to handle form submission and display results.

- `script.js`: This JavaScript file handles the form submission, makes an AJAX request to the CGI script, and updates the HTML page with the processed results.

# Requirements

- A web server that supports CGI scripting.
- Python with the `jinja2`.
- A compatible web browser (for displaying the HTML interface and JavaScript functionality).

# Usage

1. Clone this repository to your web server's directory.

2. Make sure that the CGI script is executable. You might need to set appropriate permissions using `chmod +x final_project.cgi`.

3. Set up the web server to handle CGI scripts. Consult your web server's documentation for guidance.

4. Access the `index.html` file using a web browser.

5. Enter your DNA sequence in the input field and click the "Search" button.

6. The protein sequence and triplet frequency information will be displayed on the page.

7. If needed, modify the CSS styles in `style.css` to customize the appearance of the HTML page.


