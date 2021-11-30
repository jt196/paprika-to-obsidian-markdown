---
name: "Crispy Roast Potatoes"
source: "Seriouseats.com"
ingredients: 
  - [0, '', 'Kosher salt', '', 'Kosher salt']
  - [4.0, 'g', 'baking soda', '', '4g baking soda']
  - [2.0, 'kg', 'potatoes', '(peeled and cut into quarters, sixths, or eighths, depending on size)', '2kg potatoes (peeled and cut into quarters, sixths, or eighths, depending on size)']
  - [75.0, 'ml', 'extra-virgin olive oil', '(or duck fat, goose fat, or beef fat)', '75ml extra-virgin olive oil (or duck fat, goose fat, or beef fat)']
  - [1.0, '', 'handful rosemary leaves', '(picked, finely chopped)', '1 handful rosemary leaves (picked, finely chopped)']
  - [3.0, '', 'cloves garlic', 'medium minced', '3 cloves garlic, medium minced']
  - [0, '', 'Freshly ground black pepper', '', 'Freshly ground black pepper']
  - [1.0, '', 'handful parsley', '(fresh leaves, minced)', '1 handful parsley (fresh leaves, minced)']
source: "Seriouseats.com"
difficulty: 
photo_thumbnail: _resources/1DC12B87-B1C8-40C9-970F-D8E720F98A6D.jpg
image_url: https://www.seriouseats.com/recipes/images/2016/12/20161201-crispy-roast-potatoes-29.jpg
total_time: 
notes: |
nutritional_info: []
description: |
rating: 0
prep_time: 30 minutes
created: 2021-03-22 00:56:19
directions: |
  1. Adjust oven rack to center position and preheat oven to 450°F/230°C (or 400°F/200°C if using convection). Heat 2 quarts (2L) water in a large pot over high heat until boiling. Add 2 tablespoons kosher salt (about 1 ounce; 25g), baking soda, and potatoes and stir. Return to a boil, reduce to a simmer, and cook until a knife meets little resistance when inserted into a potato chunk, about 10 minutes after returning to a boil.
  2. Meanwhile, combine olive oil, duck fat, or beef fat with rosemary, garlic, and a few grinds of black pepper in a small saucepan and heat over medium heat. Cook, stirring and shaking pan constantly, until garlic just begins to turn golden, about 3 minutes. Immediately strain oil through a fine-mesh strainer set in a large bowl. Set garlic/rosemary mixture aside and reserve separately.
  3. When potatoes are cooked, drain carefully and let them rest in the pot for about 30 seconds to allow excess moisture to evaporate. Transfer to bowl with infused oil, season to taste with a little more salt and pepper, and toss to coat, shaking bowl roughly, until a thick layer of mashed potato–like paste has built up on the potato chunks.
  4. Transfer potatoes to a large rimmed baking sheet and separate them, spreading them out evenly. Transfer to oven and roast, without moving, for 20 minutes. Using a thin, flexible metal spatula to release any stuck potatoes, shake pan and turn potatoes. Continue roasting until potatoes are deep brown and crisp all over, turning and shaking them a few times during cooking, 30 to 40 minutes longer.
  5. Transfer potatoes to a large bowl and add garlic/rosemary mixture and minced parsley. Toss to coat and season with more salt and pepper to taste. Serve immediately.
categories: ['J Kenji Lopez-Alt', 'Potatoes']
source_url: https://www.seriouseats.com/recipes/2016/12/the-best-roast-potatoes-ever-recipe.html
cook_time: 1 hour 15 minutes
servings: [6, 8]
scale: 1
tags: 
  - recipes/authors/kenji
  - recipes/potatoes
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
