---
name: "Tahini Sauce with Garlic and Lemon"
source: "Seriouseats.com"
ingredients: 
  - [1.0, '', 'whole head garlic', '(about 20 cloves)  broken into individual unpeeled cloves', '1 whole head garlic, broken into individual unpeeled cloves (about 20 cloves)']
  - [2.5555555555555554, '', 'lemons', '(160ml)', '2/3 cup fresh juice from 3 to 4 lemons (160ml)']
  - [0.5, 'tsp', 'ground cumin', '(2g)', '1/2 teaspoon ground cumin (2g)']
  - [1.0, '', 'generous cup tahini paste', '(about 10 ounces; 300g by weight)', '1 generous cup tahini paste (about 10 ounces; 300g by weight)']
  - [0, '', 'Cold water', '', 'Cold water']
  - [0, '', 'Kosher salt', '', 'Kosher salt']
source: "Seriouseats.com"
difficulty: Easy
photo_thumbnail: _resources/7ce57e07-201b-499f-9790-622f7f99093e.jpg
image_url: https://www.seriouseats.com/thmb/k9l0-N6tnfwO0TynAN0j9QXVqqU=/450x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/__opt__aboutcom__coeus__resources__content_migration__serious_eats__seriouseats.com__recipes__images__2016__03__20160411-tahini-sauce-hummus-vegan-sauce-ef89477af849437782b0fe12ed26d918.jpg
total_time: 
notes: |
nutritional_info: []
description: |
rating: 0
prep_time: 
created: 2021-10-30 13:54:38
directions: |
  Combine garlic and lemon juice in a blender. Pulse until a pulpy puree is formed, about 15 short pulses. Transfer to a fine mesh strainer set over a large bowl. Press out as much liquid as you can with the back of a spoon or a rubber spatula, then discard solids.
  Add cumin and tahini paste to lemon/garlic juice and whisk to combine. The mixture will seize up and turn pasty. Add water a few tablespoons at a time, whisking in between each addition, until a smooth, light sauce is formed. The tahini sauce should very slowly lose its shape if you let ribbons of it drop from the whisk into the bowl. Season to taste with salt. Refrigerate for up to 1 1/2 weeks.
categories: ['J Kenji Lopez-Alt', 'Middle East', 'Sauces']
source_url: https://www.seriouseats.com/israeli-style-tahini-sauce-recipe
cook_time: 5 mins
servings: [2]
scale: 1
tags: 
  - recipes/authors/kenji
  - recipes/world/middleeast
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
