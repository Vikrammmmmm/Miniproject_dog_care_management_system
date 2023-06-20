html = """
<!DOCTYPE html>
<html>
<head>
    <title>Dog Care Website</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f5f5f5;
            margin: 0;
            padding: 20px;
        }

        h1 {
            color: #333;
        }

        p {
            color: #666;
        }

        ul {
            color: #666;
            padding-left: 20px;
        }

        form {
            background-color: #fff;
            border-radius: 5px;
            padding: 20px;
            margin-top: 20px;
        }

        label {
            color: #333;
        }

        input[type="text"],
        input[type="email"],
        input[type="number"],
        textarea {
            width: 100%;
            padding: 10px;
            border-radius: 5px;
            border: 1px solid #ccc;
            margin-bottom: 10px;
        }

        input[type="submit"] {
            background-color: #333;
            color: #fff;
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }

        input[type="submit"]:hover {
            background-color: #555;
        }
    </style>
</head>
<body>
    <h1>Welcome to the Dog Care Website!</h1>
    <p>Learn about dog care and different dog breeds.</p>
    <h2>About Dog Care</h2>
    <p>Dog care involves providing proper nutrition, exercise, grooming, and healthcare to ensure the well-being of your furry friend.</p>
    <h2>Popular Dog Breeds</h2>
    <ul>
        <li>Labrador Retriever</li>
        <li>German Shepherd</li>
        <li>Golden Retriever</li>
        <li>Bulldog</li>
        <li>Poodle</li>
    </ul>
    <title>Pet Shopping and Adoption Form</title>
	<style>
		body {
			background-image:url("https://cdn.wallpapersafari.com/32/78/dTuctf.jpg");
		}
		form {
			max-width: 500px;
			margin: 0 auto;
			padding: 50px;
			border: 1px solid green;
			border-radius: 5px;
		}
		input[type=text], input[type=email], textarea {
			width: 100%;
			padding: 12px 20px;
			margin: 8px 0;
			box-sizing: border-box;
			border: 2px solid #ccc;
			border-radius: 4px;
			resize: vertical;
			rows: 5;
		}
		input[type=submit] {
			background-color: #4CAF50;
			color: white;
			padding: 12px 20px;
			border: none;
			border-radius: 4px;
			cursor: pointer;
		}
		input[type=submit]:hover {
			background-color: #45a049;
		}
		.container {
			border-radius: 5px;
			background-color: #f2f2f2;
			padding: 10px;
		}
        </style>
</head>
<body>
	<form>
		<h2 style="text-align:center;">Pet Shopping and Adoption Form</h2>
		<div class="container">
			<label for="name"><b>Name</b></label>
			<input type="text" placeholder="Enter Name" name="name" required>

			<label for="email"><b>Email Address</b></label>
			<input type="email" placeholder="Enter Email" name="email" required pattern="[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$">

			<label for="pet"><b>Pet Required/Other Products(Mention with appropriate name)</b></label>
			<input type="text" placeholder="Enter Pet Required" name="pet" required>

			<label for="message"><b>Ask Your Query Here</b></label>
			<textarea placeholder="Enter Message" name="message" required></textarea>

			<button type="submit">Submit</button>
		</div>
	</form>

	<script>
		const form = document.querySelector('form');
		form.addEventListener('submit', (event) => {
			event.preventDefault();
			const name = form.elements['name'].value;
			const email = form.elements['email'].value;
			const pet = form.elements['pet'].value;
			const message = form.elements['message'].value;
			console.log(`Name: ${name}\nEmail: ${email}\nPet Required: ${pet}\nMessage: ${message}`);
			alert('Thank you for submitting the form!');
			form.reset();
		});
	</script>
</body>
</html>
"""

# Save the HTML content to a file
with open('index.html', 'w') as file:
    file.write(html)
    
    import sqlite3

# Establish a connection to the database
conn = sqlite3.connect("/content/dog care 2 .html")

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Create a table to store user information if it doesn't already exist
cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    age INTEGER,
                    email TEXT
                )''')

# Assume you have obtained user information from the website form
user_name = "John Doe"
user_age = 25
user_email = "john@example.com"

# Insert user information into the database
cursor.execute('''INSERT INTO users (name, age, email)
                  VALUES (?, ?, ?)''', (user_name, user_age, user_email))

# Commit the changes to the database
conn.commit()

# Close the database connection
conn.close()
    
   