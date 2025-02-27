### Copyright Peiu Andreea - 314CA

## PHOTO GALLERY - Web Application

This is a simple web application for displaying and managing a photo gallery. Users can view images, upload new images, and log in to access additional features.

## Base.html
The base HTML template serves as the foundation for all pages in the web application. It includes the header, navigation menu, main content area, and footer.

### Design Choices
Utilizes a clean and simple layout for easy navigation and readability.
Integrates with Jinja2 templating to dynamically render content based on user sessions and data from the server. 

### Challenges
Ensuring compatibility across different screen sizes and browsers while maintaining a consistent layout.

-------------------------------------------------------------
##  Index.html
The index page displays a video background and dynamically loads image thumbnails from different categories.

### Design Choices
Uses a video background to create visual interest and engagement.
Thumbnails are organized by category for easy navigation and browsing.

### Challenges
Implementing the logic to dynamically load and display images from the server. Also, I found it hard to make a layering between the background video, the white box and the thumbnails in CSS, because the photo would become see-through too.

## Login.html

The login page allows users to log in to their accounts.

### Design Choices
Features a video background similar to the index page for consistency in design.
Provides a simple form for users to input their username and password.

### Chalenges
Ensuring secure authentication and handling error messages effectively.

## Upload.html

The upload page enables users to upload new images to the gallery.

### Design Choices

Includes a form for selecting an image file, renaming it, and choosing a category.

### Chalenges

Implementing file upload functionality securely and efficiently. I had trouble finding the paths to the photos. Also, the message that the photo was uploaded would show weird at the begining.

