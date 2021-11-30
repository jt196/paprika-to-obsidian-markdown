---
name: "Kenji's Foolproof Homemade Mayonnaise (with tweaks)"
source: ""
ingredients: 
  - [2.0, '', 'large egg yolks', '', '2 large egg yolks']
  - [2.0, 'tsp', 'Dijon mustard', '', '2 teaspoons Dijon mustard']
  - [1.0, 'tbsp', 'lemon juice or vinegar', '', '1 tablespoon lemon juice or vinegar']
  - [1.0, 'clove', 'garlic', 'coarsely chopped', '1 clove garlic, coarsely chopped']
  - [2.0, 'tbsp', 'water', '', '2 tablespoons water']
  - [500.0, 'ml', 'rapeseed oil', '', '500 ml rapeseed oil']
  - [0.5, 'tsp', 'salt', '', '1/2 tsp salt']
source: ""
difficulty: 
photo_thumbnail: _resources/73F00A59-3200-409D-B05D-77A164BB35EE-10329-0008DFEC9FA5E79A.jpg
image_url: None
total_time: 
notes: |
  NOTES: You can whisk in additional lemon juice to taste after the mayonnaise is finished if desired. Make sure to season it pretty aggressively: mayonnaise tastes very flat and greasy without enough salt. This mayonnaise can also be made in a regular blender or in a standing mixer fitted with a whisk attachment.
  KENJI’s FOOD PROCESSOR TECHNIQUE:
  1.  Pour the canola oil into 4 to 6 compartments of an ice cube tray and place in the freezer until fully frozen.
  2.  Combine the egg yolks, mustard, lemon juice, garlic if using, and 1 tablespoon water in the bowl of a food processor. Add 2 of the frozen oil cubes and run the machine until the large chunks are broken down, about 5 seconds. Remove the lid and scrape down the lid and sides with a rubber spatula. Add the remaining frozen oil cubes and run the machine again until the mayonnaise is smooth, about 5 seconds longer.
  3.  Transfer the contents to a medium bowl set in a heavy saucepan lined with a towel to stabilize it. Whisking constantly, slowly drizzle in the olive oil. Add salt and pepper to taste and whisk to combine. Whisk in up to 1 tablespoon more water, until the desired consistency is reached. The mayonnaise can be stored in a sealed container in the refrigerator for up to 2 weeks.
nutritional_info: []
description: |
rating: 0
prep_time: 
created: 2021-04-09 19:50:48
directions: |
  JAMES’ FOOD PROCESSOR TECHNIQUE:
  1. Combine egg yolks, mustard, acid, salt, garlic (if using) and 1 tbsp of water in SMALL food processor compartment with blade.
  2. Add a few tbsp of oil and run for about 20 seconds or so without adding any more oil. 
  3. Once it looks quite well combined, pour in the remaining oil, slowly to start with, making sure that any oil added is combined into the sauce. 
  4. When all the oil has been added. Taste for seasoning, adding more acid or salt if necessary. If the mayo is too thick, add up to 1 tbsp of water to loosen it up a bit.
  TO MAKE THE MAYONNAISE WITH AN IMMERSION BLENDER
  1.  Combine the egg yolks, mustard, lemon juice, garlic (if using), and 1 tablespoon water in a tall, narrow cup just wide enough that the head of the blender fits in the bottom. Carefully pour the canola oil on top. Slowly submerge the head of the blender, reaching the bottom of the cup. Holding the cup flat and steady, turn on the blender. It should create a vortex, slowly pulling the oil down and creating a smooth, creamy mayonnaise.
  2.  Slowly lift the head until all the oil is incorporated. Scrape the mixture out into a medium bowl set in a heavy saucepan lined with a towel to stabilize it. Whisking constantly, slowly drizzle in the olive oil. Add salt and pepper to taste and whisk to combine. Whisk in up to 1 tablespoon more water, until the desired consistency is reached. The mayonnaise can be stored in a sealed container in the refrigerator for up to 2 weeks.
categories: ['J Kenji Lopez-Alt', 'Sauces']
source_url: 
cook_time: 
servings: [500]
scale: 1
tags: 
  - recipes/authors/kenji
  - recipes/sauces
photos: 
 - './_resources/6A72D3C0-801B-4479-BCC1-1EE1C2A1034D-10329-0008DFEC2BBAFBA5.jpg'
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
