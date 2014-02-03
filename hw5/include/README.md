Homework 5.0
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
=====

Write an aggregation expression to calculate the average population of a zip code (postal code) by state. As before, the postal code is in the _id field and is unique. The collection is assumed to be called "zips" and you should name the key in the result set "average_pop".
```
> db.zips.aggregate([{$group:{_id:"$state", average_pop:{$avg:"$pop"}}}])
```
=====

Write an aggregation query that will return the postal codes that cover each city. The results should look like this:
		
```
{
	"_id" : "CENTREVILLE",
	"postal_codes" : [
				"22020",
				"49032",
				"39631",
				"21617",
				"35042"
			 ]
},
```

```
> db.zips.aggregate([{$group:{_id:"$city", postal_codes:{$addToSet:"$_id"}}}])
```
=====

Again thinking about the zip code database, write an aggregation query that will return the population of the postal code in each state with the highest population. It should return output that looks like this:
```
{
	"_id" : "WI",
	"pop" : 57187
},
{
	"_id" : "WV",
	"pop" : 70185
},

..and so on
```

```
> db.zips.aggregate([{$group:{_id:"$state", pop:{$max:"$pop"}}}])
```
=====

Write an aggregation query with a single projection stage that will transform the documents in the zips collection from this:
```
{
	"city" : "ACMAR",
	"loc" : [
		-86.51557,
		33.584132
	],
	"pop" : 6055,
	"state" : "AL",
	"_id" : "35004"
}
```
to documents in the result set that look like this:

```
{
	"city" : "acmar",
	"pop" : 6055,
	"state" : "AL",
	"zip" : "35004"
}
```

```
> db.zips.aggregate([{
  	$project:
  	{
      		_id:0,
      		city:{$toLower:"$city"},
      		pop:1,
      		state:1,
      		zip:'$_id'
  	}
  }])
```
=====

Again, thinking about the zipcode collection, write an aggregation query with a single match phase that filters for zipcodes with greater than 100,000 people.
```
> db.zips.aggregate([{$match:{pop:{$gt:100000}}}])
```
=====


=====

