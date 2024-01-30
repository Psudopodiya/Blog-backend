<h1>Wildlife Whisperers Project</h1>
<h3>Overview</h3>
<p>Wildlife Whisperers is a dynamic web application designed to connect nature enthusiasts. This application provides a platform for users to share their experiences, thoughts, and insights through blogs, as well as engage with the community through comments and interactions. The project leverages Django, a high-level Python web framework, to ensure rapid development and clean, pragmatic design.</p>


<ul>
<li> <h3>Features</h3>

<ul>
<li>User Authentication: Register, Login, and Profile management.
<li>Blog Management: Create, view, and manage blogs.
<li>Comment System: Users can comment on blogs.
<li>Image Uploads: Support for profile and blog cover image uploads.
</ul>


<li><h3>URL Configuration</h3>
The application's URL routing is defined in wildlife_wisperers/urls.py. It includes:
<ul>
<li>Admin routes for Django's admin interface.
<li>User-related routes (login, register, profile).
<li>Blog-related routes (blog list, create blog).
<ul>
For detailed URL patterns, refer to the code comments in the urls.py files.

<li><h3>Models</h3>
The application defines the following models:
<ul>
<li>CustomUser: An extension of Django's default user model to include additional fields like birthdate and profile_image.
<li>Blog: Represents a blog post with fields such as title, content, category, and cover_image.
<li>Comment: Represents comments made by users on blog posts.
</ul>

<li><h3>Serializers</h3>
Serializers convert complex data types to JSON for API responses and vice versa. The application uses:
<ul>
<li>CustomUserSerializer and UserProfileSerializer for user-related operations.
<li>BlogSerializer for blog operations.
<li>CommentSerializer for comment operations.
</ul>


<li><h3>Views</h3>
The application's views are responsible for handling requests and returning responses. It includes views for user authentication, blog creation and listing, and profile management. The views utilize Django Rest Framework's @api_view decorator to define API endpoints.

<li><h3>Permissions</h3>
The application uses Django Rest Framework's permission classes to manage access to different views. It includes both IsAuthenticated for authenticated users and AllowAny for public access.

<li><h3>Running the Project</h3>
To run the project locally:
<ul>
<li>Clone the repository.
<li>Install the required dependencies.
<li>To run the project perform the below:.
<ul>
    <li>Create a virtual environment
</ul>
</ul>

</ul>
For more information on Django and Django Rest Framework, visit:

Django: https://www.djangoproject.com/
Django Rest Framework: https://www.django-rest-framework.org/
This README provides a high-level overview of the Wildlife Whisperers project. For more detailed information, please refer to the source code and comments within each file.