---
name: "Updated No-Knead Bread"
source: "Cooking.nytimes.com"
ingredients: 
  - [400.0, 'g', 'bread flour', '', '400 grams bread flour']
  - [8.0, 'g', 'salt', '', '8 grams salt']
  - [2.0, 'g', 'instant or “rapid rise” yeast', '', '2 grams instant or “rapid rise” yeast ']
  - [280.0, 'g', 'warm water', '', '280 grams warm water ']
  - [0.125, 'tsp', 'white vinegar or lemon juice', '', '⅛ teaspoon white vinegar or lemon juice']
  - [0, '', 'Rice flour or extra bread flour', 'for dusting', 'Rice flour or extra bread flour, for dusting']
  - [690.0, 'g', 'total', '', '690g total']
source: "Cooking.nytimes.com"
difficulty: Easy
photo_thumbnail: _resources/FB1FF636-D16D-4C81-A4D7-E235F408F0EB.jpg
image_url: https://static01.nyt.com/images/2021/05/05/dining/03Kenjirex1/merlin_186913560_24dd1c65-b972-47db-86a8-8b8b010ab741-articleLarge.jpg
total_time: 
notes: |
  I’d put the baking temp a little lower for a larger loaf - maybe 200C or so. 
nutritional_info: []
description: |
rating: 0
prep_time: 
created: 2021-06-14 11:16:29
directions: |
  **Mix the dough:** Combine the flour, salt and yeast in a large bowl and mix with your hands until mostly homogenous. Combine the water and vinegar or lemon juice, then add to the bowl. Form one hand into a stiff claw, and stir with it until no dry flour remains and the dough forms a sticky, shaggy ball. Roll the ball around the bowl until most of the dough is part of the same large mass. The mixing process should take no more than 30 to 45 seconds.
  Scrape your dough-covered hand with your clean hand or with a metal or plastic dough scraper to get most of the dough into the bowl, then invert a tall-sided medium metal or glass bowl (or a cutting board) and place it on top of the large bowl, tapping it to ensure a tight seal. Let dough rest at least 12 hours and up to 18 hours at room temperature, 16-21C\. When the dough is done resting, it should appear very bubbly and wet.
  **Shape the loaf:** Wipe out any moisture collected inside the medium bowl. Dust a dish towel thoroughly on one side with rice flour or bread flour, then line the medium bowl with the towel, floured-side up. Generously flour your work surface. Sprinkle flour around the edges of the dough in the large bowl, then tilt the bowl over your floured work surface, using your fingertips to ease the dough away from the bowl until it all tips out. (Some bits of the dough will stick to the bowl, this is OK; leave them behind.)
  Working gently but quickly to avoid deflating the dough, using one hand, reach under one side with your fingertips, stretch the dough, and fold it over itself into the center. Repeat three more times until each side of the dough has been folded over the top. Using the sides of your hands instead of your fingertips and as much extra flour as necessary to prevent sticking, flip the dough over. With your palms up and hands placed flat on the work surface, gently tuck the dough together underneath until the top surface is relatively smooth and taut.
  **Proof the loaf:** Carefully lift the dough, place it smooth-side up into the towel-lined bowl, and dust lightly with rice flour or bread flour. Cover the bowl with a large baking sheet and allow the dough ball to rise until it roughly doubles in volume and doesn’t spring back readily when you poke it with a fingertip, about 2 hours. Meanwhile, wash out the large bowl and have it ready.
  **Heat the oven:** At least 30 minutes before baking, adjust oven rack to lower-middle position and heat oven to 230C (convection) 260C (normal). When dough is ready, invert the bowl and baking sheet so that the dough is lying on the sheet. (The sheet will end up inverted.) Lift off the bowl and carefully lift off the kitchen towel. If it sticks at all, be very gentle when coaxing the dough off; the goal is to minimize the loss of gases trapped inside.
  **Bake the bread:** Splash some water inside the larger metal bowl, then invert it onto the baking sheet over the dough. Transfer the whole thing to the oven, reduce oven temperature to 210C (convection)/230C (normal), and bake for 25 minutes. Using oven mitts or dry kitchen towels, remove the bowl and continue baking until the loaf is as dark as you’d like it, 15 to 25 minutes longer. Remove the bread, transfer to a cooling rack, and allow to cool completely before cutting it open.
categories: ['Baking', 'J Kenji Lopez-Alt']
source_url: https://cooking.nytimes.com/recipes/1022147-updated-no-knead-bread
cook_time: 1 hour
servings: [1]
scale: 1
tags: 
  - recipes/baking
  - recipes/authors/kenji
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
