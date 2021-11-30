---
name: "Mexican Street Corn Salad (Esquites)"
source: "Seriouseats.com"
ingredients: 
  - [2.0, 'tbsp', 'vegetable oil', '(30ml)', '2 tablespoons (30ml) vegetable oil']
  - [4.0, '', 'ears fresh corn', '(about 3 cups fresh corn kernels)  shucked,  kernels removed', '4 ears fresh corn, shucked, kernels removed (about 3 cups fresh corn kernels)']
  - [0, '', 'Kosher salt', '', 'Kosher salt']
  - [2.0, 'tbsp', 'mayonnaise', '(30ml)', '2 tablespoons (30ml) mayonnaise']
  - [2.0, 'oz', 'feta or Cotija cheese', '(60g)  finely crumbled', '2 ounces (60g) feta or Cotija cheese, finely crumbled']
  - [0.5, 'cup', 'finely sliced scallions', 'green parts only', '1/2 cup finely sliced scallions, green parts only']
  - [0.5, 'cup', 'fresh cilantro leaves', '(1/2 ounce)  finely chopped', '1/2 cup (1/2 ounce) fresh cilantro leaves, finely chopped']
  - [1.0, '', 'jalapeño pepper', 'seeded and stemmed,  finely chopped', '1 jalapeño pepper, seeded and stemmed, finely chopped']
  - [1.5, '', 'medium cloves garlic', '(about 1 to 2 teaspoons)  pressed or minced on a Microplane grater', '1 to 2 medium cloves garlic, pressed or minced on a Microplane grater (about 1 to 2 teaspoons)']
  - [1.0, '', 'lime', '(15ml)', '1 tablespoon  fresh juice from 1 lime']
  - [0, '', 'Chili powder or hot chili flakes', 'to taste', 'Chili powder or hot chili flakes, to taste']
source: "Seriouseats.com"
difficulty: 
photo_thumbnail: _resources/7094BB4E-016D-4B8E-BFEB-13031DF86E59.jpg
image_url: https://www.seriouseats.com/2019/07/20190901-esquites-reshoot-vicky-wasik-1.jpg
total_time: 
notes: |
nutritional_info: []
description: |
rating: 0
prep_time: 15 minutes
created: 2020-12-06 12:24:46
directions: |
  1. Heat oil in a large nonstick skillet or wok over high heat until shimmering. Add corn kernels, season to taste with salt, toss once or twice, and cook without moving until charred on one side, about 2 minutes. Toss corn, stir, and repeat until charred on second side, about 2 minutes longer. Continue tossing and charring until corn is well charred all over, about 10 minutes total. Transfer to a large bowl.
  2. Add mayonnaise, cheese, scallions, cilantro, jalapeño, garlic, lime juice, and chili powder and toss to combine. Taste and adjust seasoning with salt and more chili powder to taste. Serve immediately.
categories: ['J Kenji Lopez-Alt', 'Mexican', 'Salad']
source_url: https://www.seriouseats.com/recipes/2012/07/esquites-mexican-street-corn-salad-recipe.html
cook_time: 15 minutes
servings: [4]
scale: 1
tags: 
  - recipes/authors/kenji
  - recipes/world/southamerica/mexican
  - recipes/salad
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
