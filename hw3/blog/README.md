Homework 3
=====

#### Homework 3.2

In this homework you will be enhancing the blog project to insert entries into the posts collection. After this, the blog will work. It will allow you to add blog posts with a title, body and tags and have it be added to the posts collection properly.

The areas where you need to add code are marked with XXX. You need only touch the BlogPostDAO.py file. There are three locations for you to add code for this problem. Scan that file for XXX to see where to work.

As a reminder, to run your blog you type
```
python blog.py
```

To play with the blog you can navigate to the following URLs
```
http://localhost:8082/
http://localhost:8082/signup
http://localhost:8082/login
http://localhost:8082/newpost
```

You will be proving that it works by running our validation script as follows: 
```
python validate.py
```

You need to run this in a separate terminal window while your blog is running and while the database is running. It makes connections to both to determine if your program works properly. Validate connects to localhost:8082 and expects that mongod is running on localhost on port 27017.

#### Homework 3.3

In this homework you will add code to your blog so that it accepts comments. You will be using the same code as you downloaded for HW 3.2.

Once again, the area where you need to work is marked with an XXX in the blogPostDAO.py file. There are one location. You don't need to figure out how to retrieve comments for this homework because the code you did in 3.2 already pulls the entire blog post (unless you specifically projected to eliminate the comments) and we gave you the code that pulls them out of the JSON document.

This assignment has fairly little code, but it's a little more subtle than the previous assignment because you are going to be manipulating an array within the Mongo document. For the sake of clarity, here is a document out of the posts collection from a working project.
```
{
	"_id" : ObjectId("509df76fbcf1bf5b27b4a23e"),
	"author" : "erlichson",
	"body" : "This is a blog entry",
	"comments" : [
		{
			"body" : "This is my comment",
			"author" : "Andrew Erlichson"
		},
		{
			"body" : "Give me liberty or give me death.",
			"author" : "Patrick Henry"
		}
	],
	"date" : ISODate("2012-11-10T06:42:55.733Z"),
	"permalink" : "This_is_a_blog_post_title",
	"tags" : [
		"cycling",
		"running",
		"swimming"
	],
	"title" : "This is a blog post title"
}
```

Note that you add comments in this blog from the blog post detail page, which appears at
```
http://localhost:8082/post/post_slug
```

where post_slug is the permalink. For the sake of eliminating doubt, the permalink for the example blog post above is http://localhost:8082/post/This_is_a_blog_post_title
You will run validation.py to check your work, much like the last problem. Validation.py will run through and check the requirements of HW 3.2 and then will check to make sure it can add blog comments, as required by this problem, HW 3.3. It checks the web output as well as the database documents.

```
python validate.py
```
