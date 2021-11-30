---
name: "Thin and Crispy French Fries"
source: "Seriouseats.com"
ingredients: 
  - [900.0, 'g', 'russet potatoes', '(about 4 large potatoes, peeled and cut into 1/4-inch by 1/4-inch fries. Keep raw potato sticks submerged in a bowl of water after cutting)', '900g russet potatoes (about 4 large potatoes, peeled and cut into 1/4-inch by 1/4-inch fries. Keep raw potato sticks submerged in a bowl of water after cutting)']
  - [30.0, 'ml', 'distilled white vinegar', '', '30ml distilled white vinegar']
  - [0, '', 'Kosher salt', '', 'Kosher salt']
  - [5.0, 'l', 'oil', '', '1.9l oil']
source: "Seriouseats.com"
difficulty: 
photo_thumbnail: _resources/7E0D3CCF-57DE-458E-A1A2-45309CBE7EC1.jpg
image_url: https://www.seriouseats.com/2018/04/20180309-french-fries-vicky-wasik-15.jpg
total_time: 
notes: |
nutritional_info: []
description: |
rating: 0
prep_time: 40 minutes
created: 2020-06-27 18:13:21
directions: |
  1. Place potatoes and vinegar in a saucepan and add 2 quarts (1.9L) water and 2 tablespoons (24g) salt. Bring to a boil over high heat. Boil for 10 minutes. Potatoes should be fully tender, but not falling apart. Drain and spread on a paper towel–lined rimmed baking sheet. Allow to dry for 5 minutes.
  2. Meanwhile, heat oil in a 5-quart Dutch oven or large wok over high heat to 400°F (204°C). Add one-third of fries to oil; oil temperature should drop to around 360°F (182°C). Cook for 50 seconds, agitating occasionally with a wire mesh spider, then remove to a second paper towel–lined rimmed baking sheet. Repeat with remaining potatoes (working in 2 more batches), allowing oil to return to 400°F after each addition. Allow potatoes to cool to room temperature, about 30 minutes. Continue with step 3, or, for best results, freeze potatoes at least overnight or up to 2 months.
  3. Return oil to 400°F over high heat. Fry half of potatoes until crisp and light golden brown, about 3 1/2 minutes, adjusting heat to maintain a temperature of around 360°F. Drain in a bowl lined with paper towels and season immediately with kosher salt. Cooked fries can be kept hot and crisp on a wire rack set in a sheet tray in a 200°F (90°C) oven while second batch is cooked. Serve immediately.
categories: ['J Kenji Lopez-Alt', 'Potatoes']
source_url: https://www.seriouseats.com/recipes/2010/05/perfect-french-fries-recipe.html
cook_time: 1 hour 15 minutes (excluding optional overnight freeze)
servings: [4]
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
