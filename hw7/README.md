Homework 7
=====

#### Homework 7.7

You have been tasked to cleanup a photosharing database. The database consists of two collections, albums, and images. Every image is supposed to be in an album, but there are orphan images that appear in no album. Here are some example documents (not from the collections you will be downloading). 
```
> db.albums.findOne()
{
	"_id" : 67
	"images" : [
		4745,
		7651,
		15247,
		17517,
		17853,
		20529,
		22640,
		27299,
		27997,
		32930,
		35591,
		48969,
		52901,
		57320,
		96342,
		99705
	]
}

> db.images.findOne()
{ "_id" : 99705, "height" : 480, "width" : 640, "tags" : [ "dogs", "kittens", "work" ] }
```

From the above, you can conclude that the image with _id = 99705 is in album 67. It is not an orphan.

Your task is to write a program to remove every image from the images collection that appears in no album. Or put another way, if an image does not appear in at least one album, it's an orphan and should be removed from the images collection. 

Start by using mongoimport to import your albums.json and images.json collections.

When you are done removing the orphan images from the collection, there should be 89,737 documents in the images collection. To prove you did it correctly, what are the total number of images with the tag 'kittens" after the removal of orphans? As as a sanity check, there are 49,932 images that are tagged 'kittens' before you remove the images. 
Hint: you might consider creating an index or two or your program will take a long time to run
```
$ mongoimport -d photosharing -c albums --drop < albums.json
$ mongoimport -d photosharing -c images --drop < images.json
$ mongo

> use photosharing
> db.images.count()
100000

> db.images.aggregate([{$match: {tags:"kittens"}},{$group: {_id:"", total: {$sum: 1}}}])
{ "result" : [ { "_id" : "", "total" : 49932 } ], "ok" : 1 }

> db.albums.ensureIndex({images:1})
```
