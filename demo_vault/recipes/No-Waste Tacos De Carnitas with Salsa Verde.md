---
name: "No-Waste Tacos De Carnitas with Salsa Verde"
source: "Seriouseats.com"
ingredients: 
  - [2.0, '', 'medium onions', '', '2 medium onions']
  - [0.5, 'cup', 'chopped cilantro', '', '1/2 cup chopped cilantro']
  - [3.0, 'lb', 'boneless pork butt', '(shoulder)  rind removed,  cut into 2-inch cubes', '3 pounds boneless pork butt (shoulder), rind removed, cut into 2-inch cubes']
  - [0, '', 'Kosher salt', '', 'Kosher salt']
  - [1.0, '', 'medium orange', '', '1 medium orange']
  - [6.0, '', 'cloves garlic', 'split in half', '6 cloves garlic, split in half']
  - [2.0, '', 'bay leaves', '', '2 bay leaves']
  - [1.0, '', 'cinnamon stick', 'broken into three or four pieces', '1 cinnamon stick, broken into three or four pieces']
  - [0.25, 'cup', 'vegetable oil', '', '1/4 cup vegetable oil']
  - [6.0, '', 'medium tomatillos', '(about 1 1/2 pounds)  peeled and split in half', '6 medium tomatillos (about 1 1/2 pounds), peeled and split in half']
  - [2.0, '', 'jalapeño peppers', 'split in half lengthwise,  stem removed', '2 jalapeño peppers, split in half lengthwise, stem removed']
  - [3.0, '', 'limes', 'cut into wedges', '3 limes']
  - [1.0, 'cup', 'crumbled queso fresco or feta', '', '1 cup crumbled queso fresco or feta']
  - [24.0, '', 'corn tortillas', '', '24 corn tortillas']
source: "Seriouseats.com"
difficulty: 
photo_thumbnail: _resources/1657BFC9-C2B0-449C-975F-9508906F876B.jpg
image_url: https://www.seriouseats.com/recipes/images/2016/06/20100729-carnitas-09.jpg
total_time: 
notes: |
nutritional_info: []
description: |
rating: 0
prep_time: 45 minutes
created: 2020-12-06 12:22:56
directions: |
  1. Adjust oven rack to middle position and preheat oven to 275 degrees. Cut one onion into fine dice and combine with cilantro. Refrigerate until needed. Split remaining onion into quarters. Set aside. Season pork chunks with 1 tablespoon salt and place in a 9 by 13 glass casserole dish. The pork should fill the dish with no spaces. Split orange into quarters and squeeze juice over pork. Nestle squeezed orange pieces into casserole. Add 2 onion quarters, 4 cloves garlic, bay leaves, and cinnamon stick to casserole. Nestle everything into an even layer. Pour vegetable oil over surface. Cover dish tightly with aluminum foil and place in oven. Cook until pork is fork tender, about 3 1/2 hours.
  2. Set large fine-meshed strainer 1 quart liquid measure or bowl. Using tongs, remove orange peel, onion, garlic, cinnamon stick, and bay leaves from pork. Transfer pork and liquid to strainer. Let drain for 10 minutes. Transfer pork back to casserole. You should end up with about 1/2 cup liquid and 1/2 cup fat. Using a flat spoon or de-fatter, skim fat from surface and add back to pork. Shred pork into large chunks with fingers or two forks. Season to taste with salt. Refrigerate until ready to serve. Transfer remaining liquid to medium saucepot.
  3. Add tomatillos, remaining 2 onion quarters, remaining 2 garlic cloves, and jalapeños to saucepot with strained pork liquid. Add water until it is about 1-inch below the top of the vegetables. Bring to a boil over high heat, reduce to a simmer, and cook until all vegetables are completely tender, about 10 minutes. Blend salsa with hand blender or in a stand-up blender until smooth. Season to taste with salt. Allow to cool and refrigerate until ready to use.
  4. To serve: Place casserole dish with pork 4-inches under a high broiler and broil until brown and crisp on surface, about 6 minutes. Remove pork, stir with a spoon to expose new bits to heat, and broil again for 6 more minutes until crisp. Tent with foil to keep warm.
  5. Meanwhile, heat tortillas. Preheat an 8-inch non-stick skillet over medium-high heat until hot. Working one tortilla at a time, dip tortilla in bowl filled with water. Transfer to hot skillet and cook until water evaporates from first side and tortilla is browned in spots, about 30 seconds. Flip and cook until dry, about 15 seconds longer. Transfer tortilla to a tortilla warmer, or wrap in a clean dish towel. Repeat with remaining tortillas.
  6. To eat, stack two tortillas on top of each other. Add two to three tablespoons carnitas mixture to center. Top with salsa verde, chopped onions and cilantro, and queso fresco. Serve with lime wedges.
categories: ['J Kenji Lopez-Alt', 'Meat', 'Mexican']
source_url: https://www.seriouseats.com/recipes/2010/07/no-waste-tacos-de-carnitas-with-salsa-verde-recipe.html
cook_time: 4 1/2 hours
servings: [4, 6]
scale: 1
tags: 
  - recipes/authors/kenji
  - recipes/meat
  - recipes/world/southamerica/mexican
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
