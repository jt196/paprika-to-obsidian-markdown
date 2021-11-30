---
name: "Japanese Pork and Cabbage Dumplings (Gyoza)"
source: "Seriouseats.com"
ingredients: 
  - [0, '', 'For the Dumplings:', '', 'For the Dumplings:']
  - [1.0, 'lb', 'finely minced Napa cabbage', '(about 1/2 a medium head)', '1 pound finely minced Napa cabbage (about 1/2 a medium head)']
  - [1.0, 'tbsp', 'kosher salt', 'divided', '1 tablespoon kosher salt, divided']
  - [1.0, 'lb', 'ground pork shoulder', '', '1 pound ground pork shoulder']
  - [1.0, 'tsp', 'white pepper', '', '1 teaspoon white pepper']
  - [1.0, 'tbsp', 'minced fresh garlic', '(about 3 medium cloves)', '1 tablespoon minced fresh garlic (about 3 medium cloves)']
  - [1.0, 'tsp', 'minced fresh ginger', '', '1 teaspoon minced fresh ginger']
  - [2.0, 'oz', 'minced scallions', '(about 3 whole scallions)', '2 ounces minced scallions (about 3 whole scallions)']
  - [2.0, 'tsp', 'sugar', '', '2 teaspoons sugar']
  - [1.0, '', 'package dumpling wrappers', '(40 to 50 wrappers)', '1 package dumpling wrappers (40 to 50 wrappers)']
  - [0, '', 'Vegetable or canola oil for cooking', '', 'Vegetable or canola oil for cooking']
  - [0, '', 'For the Sauce:', '', 'For the Sauce:']
  - [0.5, 'cup', 'rice vinegar', '', '1/2 cup rice vinegar']
  - [0.25, 'cup', 'soy sauce', '', '1/4 cup soy sauce']
  - [2.0, 'tbsp', 'chili oil', '(optional)', '2 tablespoons chili oil (optional)']
source: "Seriouseats.com"
difficulty: 
photo_thumbnail: _resources/B2957ED3-1317-47E9-8CD4-AA71EC0170E3.jpg
image_url: https://www.seriouseats.com/recipes/images/2015/03/20150309-gyoza-how-to-japanese-dumpling-recipe-01.jpg
total_time: 
notes: |
nutritional_info: []
description: |
rating: 0
prep_time: 1 hour
created: 2020-06-28 12:47:18
directions: |
  1. For the Dumplings: Combine cabbage and 2 teaspoons salt in a large bowl and toss to combine. Transfer to a fine mesh strainer and set it over the bowl. Let stand at room temperature for 15 minutes.
  2. Transfer cabbage to the center of a clean dish towel and gather up the edges. Twist the towel to squeeze the cabbage, wringing out as much excess moisture as possible. Discard the liquid.
  3. Combine pork, drained cabbage, remaining teaspoon salt, white pepper, garlic, ginger, scallions, and sugar in a large bowl and knead and turn with clean hands until the mixture is homogenous and starting to feel tacky/sticky. Transfer a teaspoon-sized amount to a microwave-safe plate and microwave on high power until cooked through, about 10 seconds. Taste and adjust seasoning with more salt, white pepper, and/or sugar if desired.
  4. Set up a work station with a small bowl of water, a clean dish towel for wiping your fingers, a bowl with the dumpling filling, a parchment-lined rimmed baking sheet for the finished dumplings, and a stack of dumpling wrappers covered in plastic wrap.
  5. To form dumplings, hold one wrapper on top of a flat hand. Using a spoon, place a 2 teaspoon- to 1 tablespoon-sized amount of filling in the center of the wrapper. Use the tip of the finger on your other hand to very gently moisten the edge of the wrapper with water (do not use too much water). Wipe fingertip dry on kitchen towel.
  6. Working from one side, carefully seal the filling inside the wrapper by folding it into a crescent shape, pleating in edge as it meets the other (see here for more detailed step by step instructions). Transfer finished dumplings to the parchment lined baking sheet.
  7. At this point the dumplings may be frozen by placing the baking sheet in the freezer. Freeze dumplings for at least 30 minutes then transfer to a zipper-lock freezer bag for long-term storage. Dumplings can be frozen for up to 2 months and cooked directly from the freezer.
  8. To Cook: Heat 1 tablespoon of vegetable oil in a medium non-stick skillet over medium heat until shimmering. Add as many dumplings as will fit in a single layer and cook, swirling pan, until evenly golden brown on the bottom surface, about 1 1/2 minutes.
  9. Increase heat to medium-high, add 1/2 cup of water and cover tightly with a lid. Let dumplings steam for 3 minutes (5 minutes if frozen), then remove lid. Continue cooking, swirling pan frequently and using a thin spatula to gently dislodge the dumplings if they've stuck to the bottom of the pan, until the water has fully evaporated and the dumplings have crisped again, about 2 minutes longer. Slide dumplings onto a plate, turning them crisped-side-up before serving with the sauce.
  10. For the Sauce: Combine vinegar, soy sauce, and chili oil.
categories: ['Dumplings', 'J Kenji Lopez-Alt', 'Japanese', 'Noodles']
source_url: https://www.seriouseats.com/recipes/2015/03/the-best-japanese-pork-and-cabbage-dumplings-gyoza-recipe.html
cook_time: 1 hour
servings: [40, 50]
scale: 1
tags: 
  - recipes/dumplings
  - recipes/authors/kenji
  - recipes/world/asian/japanese
  - recipes/noodles
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
