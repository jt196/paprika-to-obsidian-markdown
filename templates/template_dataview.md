---
name: $recipe_name
source: $recipe_source
ingredients: $recipe_ingredients
source: $recipe_source
difficulty: $recipe_difficulty
photo_thumbnail: $recipe_photo
image_url: $recipe_image_url
total_time: $recipe_total_time
notes: |$recipe_notes
nutritional_info: $recipe_nutritional_info
description: |$recipe_description
rating: $recipe_rating
prep_time: $recipe_prep_time
created: $recipe_created
directions: |$recipe_directions
categories: $recipe_categories
source_url: $recipe_source_url
cook_time: $recipe_cook_time
servings: $recipe_servings
scale: $recipe_scale
tags: $recipe_tags
photos: $photo_list
authors: |$my_authors
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
