---
name: "Austrian-Style Potato Salad (Erdäpfelsalat)"
source: "Seriouseats.com"
ingredients: 
  - [1.0, 'kg', 'potatoes', 'peeled,  quartered,  and cut into 1/2-inch-thick slices,  peels reserved separately - see note', '1kg potatoes, peeled, quartered, and cut into 1/2-inch-thick slices, peels reserved separately - see note']
  - [0, '', 'Kosher salt', '', 'Kosher salt']
  - [45.0, 'ml', 'white wine vinegar', 'divided,  plus more to taste', '45ml white wine vinegar, divided, plus more to taste']
  - [60.0, 'ml', 'extra-virgin olive oil', '', '60ml extra-virgin olive oil']
  - [15.0, 'ml', 'Dijon mustard', '', '15ml Dijon mustard']
  - [90.0, 'g', 'red onion', '(minced - from about 1 small onion)', '90g red onion, (minced - from about 1 small onion)']
  - [2.0, 'tbsp', 'chives', 'minced', '2 tablespoons chives, minced']
  - [120.0, 'ml', 'chicken stock', '', '120ml chicken stock']
  - [10.0, 'g', 'sugar', '', '10g sugar']
  - [0, '', 'black pepper', '', 'black pepper']
source: "Seriouseats.com"
difficulty: 
photo_thumbnail: _resources/F17C7BA5-E2F8-4AFC-B242-C463659CB294.jpg
image_url: https://www.seriouseats.com/recipes/images/2017/07/20170630-austrian-potato-salad-erdapfelsalat-19.jpg
total_time: 
notes: |
nutritional_info: []
description: |
rating: 0
prep_time: 25 minutes
created: 2020-06-28 12:47:59
directions: |
  1. Place sliced potatoes in a large saucier or Dutch oven and cover with water. Season generously with salt. Place potato skins in a fine-mesh strainer and place on top of pot. Add just enough water to submerge potato skins. Bring to a boil over high heat and simmer until potatoes are tender, about 15 minutes.
  2. Discard potato skins, drain potatoes, and transfer to a rimmed baking sheet. Immediately sprinkle with 2 tablespoons (30ml) vinegar and set aside to cool. When they are cool enough to handle, transfer potatoes to a large bowl.
  3. Add remaining vinegar, olive oil, mustard, red onion, chives, chicken stock, and sugar. Using a rubber spatula or wooden spoon, roughly stir and fold mixture so that potatoes release some starch and liquid begins to thicken a little. Season to taste with more salt and white or black pepper. Set aside to rest for at least 30 minutes and up to overnight. (If resting longer than 4 hours, cover bowl and transfer to refrigerator.) Stir again vigorously to thicken dressing; it should have a loose but not soupy consistency. If it's too thick, thin it out with a little extra water or chicken stock and re-season. Serve cold or at room temperature.
categories: ['J Kenji Lopez-Alt', 'Potatoes', 'Pressure Cooker', 'Salad']
source_url: https://www.seriouseats.com/recipes/2017/07/erdapfelsalat-austrian-style-potato-salad-recipe.html
cook_time: about 1 1/2 hours
servings: [6]
scale: 1
tags: 
  - recipes/authors/kenji
  - recipes/potatoes
  - recipes/pressurecooker 
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
