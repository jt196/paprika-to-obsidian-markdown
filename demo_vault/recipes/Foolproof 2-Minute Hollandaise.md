---
name: "Foolproof 2-Minute Hollandaise"
source: "Seriouseats.com"
ingredients: 
  - [1.0, '', 'egg yolk', '(about 35 grams)', '1 egg yolk (about 35 grams)']
  - [1.0, 'tsp', 'water', '(about 5 grams)', '1 teaspoon water (about 5 grams)']
  - [1.0, '', 'lemon', '(about 5 grams)', '1 teaspoon lemon juice from 1 lemon (about 5 grams)']
  - [0, '', 'Kosher salt', '', 'Kosher salt']
  - [1.0, '', 'stick butter', '(8 tablespoons, about 112 grams)', '1 stick butter (8 tablespoons, about 112 grams)']
  - [0, '', 'Pinch cayenne pepper or hot sauce', '(if desired)', 'Pinch cayenne pepper or hot sauce (if desired)']
source: "Seriouseats.com"
difficulty: 
photo_thumbnail: _resources/92AB5FA9-A205-4EAE-BD55-43C028165018.jpg
image_url: https://www.seriouseats.com/recipes/images/2013/04/20130417-hollandaise-video--200x150.jpg
total_time: 
notes: |
nutritional_info: []
description: |
rating: 5
prep_time: 1 minute
created: 2021-01-03 10:04:55
directions: |
  1. Combine egg yolk, water, lemon juice, and a pinch of salt in the bottom of a cup that barely fits the head of an immersion blender. Melt butter in a small saucepan over high heat, swirling constantly, until foaming subsides. Transfer butter to a 1 cup liquid measuring cup.
  2. Place head of immersion blender into the bottom of the cup and turn it on. With the blender constantly running, slowly pour hot butter into cup. It should emulsify with the egg yolk and lemon juice. Continue pouring until all butter is added. Sauce should be thick and creamy. Season to taste with salt and a pinch of cayenne pepper or hot sauce (if desired). Serve immediately, or transfer to a small lidded pot and keep in a warm place for up to 1 hour before serving. Hollandaise cannot be cooled and reheated. Check here for a full video walkthrough of the process.
categories: ['J Kenji Lopez-Alt', 'Sauces']
source_url: https://www.seriouseats.com/recipes/2013/04/foolproof-2-minute-hollandaise-recipe.html
cook_time: 2 minutes
servings: [1, 1]
scale: 1
tags: 
  - recipes/authors/kenji
  - recipes/sauces
photos: 
authors: |
  J Kenji Lopez-Alt
---
# Name: `=this.name` 

```dataviewjs
var servings = dv.current().servings
var scale = dv.current().scale
servings[1] ? dv.header(2, "Servings: " + (servings[0] * scale) + "-" + (servings[1]) * scale) : dv.header(2, "Servings: " + (servings[0] * scale)) 
```

```dataviewjs
var path = dv.current().photo_thumbnail
path === "None" ? "" : dv.paragraph('![image](' + path + ')') 
```

```dataviewjs
if (dv.current().description){
	dv.header(2, "Description: ")
	var description = dv.current().description;
	dv.paragraph(description);
}
```

```dataviewjs
dv.header(2, "Ingredients: ")
var i;
for (i=0; i < dv.current().ingredients.length; i++) {
	var amount = dv.current().ingredients[i][0];
	var unit = dv.current().ingredients[i][1];
	var name = dv.current().ingredients[i][2];
	var comment = dv.current().ingredients[i][3];
	var raw = dv.current().ingredients[i][4];
    if ( amount && name ) {
		// console.log("Amount: " + amount + ", Unit: " + unit + ", Name: " + name)
        // var servings = dv.current().servings
        var scale = dv.current().scale
        // servings[0] > 0 ? servings = dv.current().servings : servings = 1
        if (unit) {
            dv.paragraph("- " + (amount * scale).toFixed(1) + " " + unit + " " + name + " " + comment);
        } else {
            dv.paragraph("- " + (amount * scale).toFixed(1) + " " + name + " " + comment);
        }
    } else {
        dv.paragraph("- " + raw);
    }
}
```

```dataviewjs
if (dv.current().directions){
	dv.header(2, "Directions: ")
	var direction = dv.current().directions;
	dv.paragraph(direction);
}
```

```dataviewjs
if (dv.current().notes){
	dv.header(2, "Notes: ")
	var note = dv.current().notes;
	dv.paragraph(note);
}
```

```dataviewjs
var i;
if ( dv.current().photos ) {
    dv.header(2, "Photos: ")
    for (i=0; i < dv.current().photos.length; i++) {
	    var path = dv.current().photos[i];
	    var link = '![image](' + path + ')'
	    dv.paragraph(link);
    }
}
```
