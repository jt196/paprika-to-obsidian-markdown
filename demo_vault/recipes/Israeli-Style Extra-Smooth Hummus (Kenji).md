---
name: "Israeli-Style Extra-Smooth Hummus (Kenji)"
source: "Seriouseats.com"
ingredients: 
  - [225.0, 'g', 'dried chickpeas', '', '225g dried chickpeas']
  - [2.0, 'tsp', 'baking soda', '', '2 teaspoons baking soda']
  - [0, '', 'Kosher salt', '', 'Kosher salt']
  - [1.0, '', 'onion', 'split in half - small', '1 onion']
  - [1.0, '', 'stalk celery', 'small', '1 stalk celery - small']
  - [1.0, '', 'carrot', '', '1 carrot']
  - [2.0, '', 'medium cloves garlic', 'small', '2 medium cloves garlic - small']
  - [2.0, '', 'bay leaves', '', '2 bay leaves']
  - [350.0, 'ml', 'Tahini Sauce With Garlic and Lemon', '', '350ml Tahini Sauce With Garlic and Lemon']
  - [0, '', '**To Garnish**', '', '**To Garnish**']
  - [0, '', 'Extra-virgin olive oil', '', 'Extra-virgin olive oil']
  - [0, '', "Za'atar", '', "Za'atar"]
  - [0, '', 'paprika', '', 'paprika']
  - [0, '', 'warmed whole chickpeas', '', 'warmed whole chickpeas']
  - [0, '', 'chopped fresh parsley leaves', '', 'chopped fresh parsley leaves']
source: "Seriouseats.com"
difficulty: Easy
photo_thumbnail: _resources/2288CFF2-0C35-4733-A598-84099D9ADC22.jpg
image_url: https://www.seriouseats.com/recipes/images/2016/03/20160411-tahini-sauce-hummus-vegan-19.jpg
total_time: 
notes: |
nutritional_info: []
description: |
rating: 0
prep_time: 15 minutes
created: 2021-03-17 13:14:47
directions: |
  1. Combine beans, 1 teaspoon (6g) baking soda, and 2 tablespoons (24g) kosher salt in a large bowl and cover with 6 cups (1.4L) cold water. Stir to dissolve salt and baking soda. Let stand at room temperature overnight. Drain and rinse beans thoroughly.
  2. Place beans in a large Dutch oven or saucepan. Add remaining baking soda, 1 tablespoon (12g) salt, onion, celery, carrot, garlic, and bay leaves. Add 6 cups (1.4L) water and bring to a boil over high heat. Reduce to a simmer, cover with lid slightly cracked, and cook until beans are completely tender, to the point of falling apart, about 2 hours. Check on beans occasionally and top up with more water if necessary; they should be completely submerged at all times.
  3. Discard onion, celery, and bay leaves. Transfer chickpeas, carrot, and garlic to a food processor or high-powered blender (such as a Vitamix, BlendTec, or Breville Boss; see note) with enough cooking liquid to barely cover them. Cover blender, taking out the central insert on the blender lid.
  4. Place a folded kitchen towel over the hole in the center of the lid to allow steam to escape. Holding the towel down firmly, turn the blender to the lowest possible speed and slowly increase speed to high. If the mixture becomes too thick to blend, add cooking liquid until it has the texture of a very thick milkshake, always starting the blender on low speed before increasing to high. If your blender comes with a push-stick for thick purées, use it. Continue blending until completely smooth, about 2 minutes.
  5. Transfer hot chickpea mixture to a large bowl. Whisk in tahini sauce. Whisk in salt to taste. Transfer to a sealed container and allow to cool to room temperature. It should thicken up until it can hold its shape when spooned onto a plate.
  6. Serve hummus on a wide, shallow plate, drizzled with olive oil and sprinkled with za'atar, paprika, warmed whole chickpeas, and/or chopped parsley. Leftover hummus can be stored in the refrigerator for up to 1 week. Allow to come to room temperature before serving.
categories: ['J Kenji Lopez-Alt', 'Middle East', 'Sauces']
source_url: https://www.seriouseats.com/recipes/2016/03/israeli-style-extra-smooth-hummus-recipe.html
cook_time: 2 hours 15 minutes, plus overnight soak if using dried chickpeas
servings: [5, 8]
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
