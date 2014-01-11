Homework 5.0
=====

Write the aggregation query that will find the number of products by category of a collection that has the form:
```
{
	"_id" : ObjectId("50b1aa983b3d0043b51b2c52"),
	"name" : "Nexus 7",
	"category" : "Tablets",
	"manufacturer" : "Google",
	"price" : 199
}
```

Have the resulting key be called "num_products," as in the video lesson. Hint, you just need to change which key you are aggregating on relative to the examples shown in the lesson.
Please double quote all keys to make it easier to check your result.
```
> db.products.aggregate([{$group: {_id:"$category", num_products:{$sum:1}}}])
```
=====

Suppose we have a collection of populations by postal code. The postal codes in are in the _id field, and are therefore unique. Documents look like this:
```
{
	"city" : "CLANTON",
	"loc" : [
		-86.642472,
		32.835532
	],
	"pop" : 13990,
	"state" : "AL",
	"_id" : "35045"
}
```

Write an aggregation query to sum up the population (pop) by state and put the result in a field called population.
```
> db.zips.aggregate([{$group:{_id:"$state", population:{$sum:"$pop"}}}])
```
