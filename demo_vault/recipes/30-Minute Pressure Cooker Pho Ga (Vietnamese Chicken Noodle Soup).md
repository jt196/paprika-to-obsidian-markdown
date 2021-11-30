---
name: "30-Minute Pressure Cooker Pho Ga (Vietnamese Chicken Noodle Soup)"
source: "Seriouseats.com"
ingredients: 
  - [2.0, 'tbsp', 'canola or vegetable oil', '', '2 tablespoons canola or vegetable oil']
  - [2.0, '', 'medium yellow onions', 'split in half', '2 medium yellow onions, split in half']
  - [1.0, '', 'small hand of ginger', 'roughly sliced', '1 small hand of ginger, roughly sliced']
  - [1.0, '', 'small bunch cilantro', '', '1 small bunch cilantro']
  - [3.0, '', 'star anise pods', '', '3 star anise pods']
  - [1.0, '', 'cinnamon stick', '', '1 cinnamon stick']
  - [4.0, '', 'cloves', '', '4 cloves']
  - [1.0, 'tsp', 'fennel seeds', '', '1 teaspoon fennel seeds']
  - [1.0, 'tsp', 'coriander seeds', '', '1 teaspoon coriander seeds']
  - [7.0, '', 'chicken drumsticks', '', '6 to 8 chicken drumsticks']
  - [0.25, 'cup', 'fish sauce', 'plus more to taste', '1/4 cup fish sauce, plus more to taste']
  - [2.0, 'tbsp', 'rock sugar or raw sugar', 'plus more to taste', '2 tablespoons rock sugar or raw sugar, plus more to taste']
  - [0, '', 'To Serve:', '', 'To Serve:']
  - [4.0, '', 'servings pho noodles', 'prepared according to package directions', '4 servings pho noodles, prepared according to package directions']
  - [1.0, '', 'small white or yellow onion', 'thinly sliced', '1 small white or yellow onion, thinly sliced']
  - [0.5, 'cup', 'thinly sliced scallions', '', '1/2 cup thinly sliced scallions']
  - [2.0, 'cup', 'mixed herbs', '(cilantro, basil, and mint)', '2 cups mixed herbs (cilantro, basil, and mint)']
  - [2.0, 'cup', 'trimmed bean sprouts', '', '2 cups trimmed bean sprouts']
  - [0, '', 'Thai chilis', 'Thinly sliced', 'Thai chilis, Thinly sliced ']
  - [2.0, '', 'limes', 'each cut into 4 wedges', '2 limes']
  - [0, '', 'Hoisin sauce', '', 'Hoisin sauce']
  - [0, '', 'Sriracha', '', 'Sriracha']
source: "Seriouseats.com"
difficulty: 
photo_thumbnail: _resources/5875FA54-32B8-47C0-889E-C02542922988.jpg
image_url: https://www.seriouseats.com/recipes/images/2015/01/20140108-pressure-cooker-pho-ga-vietnamese-chicken-noodle-soup-06-200x150.jpg
total_time: 
notes: |
nutritional_info: []
description: |
rating: 0
prep_time: 20 minutes
created: 2020-10-25 09:13:51
directions: |
  1. Heat oil in a pressure cooker over high heat until smoking. Add halved onions and ginger, cut side down. Cook without moving, reducing heat if smoking excessively, until onion and ginger are well charred, about 5 minutes.
  2. Add cilantro, star anise, cinnamon, cloves, fennel seed, coriander, and chicken to the pot. Add 2 quarts of water, the fish sauce, and the sugar to the pot. Seal the pressure cooker and bring it to high pressure over high heat. Cook on high pressure for 20 minutes, then shock under cold running water in the sink (or release pressure valve if using an electric pressure cooker).
  3. Open pressure cooker. Transfer chicken legs to a plate. Pour broth through a fine mesh strainer into a clean pot and discard solids. Skim any scum off the surface of the broth using a ladle, but leave the small bubbles of fat intact. Season broth to taste with more fish sauce and sugar if desired.
  4. To serve, place re-hydrated pho noodles in individual noodle bowls. Top with chicken legs, sliced onions, and scallions. Pour hot broth over chicken and noodles. Serve immediately, allowing guests to add herbs, bean sprouts, chilis, lime, and sauces as they wish.
categories: ['J Kenji Lopez-Alt', 'Soup', 'Vietnamese']
source_url: https://www.seriouseats.com/recipes/2015/01/30-minute-pressure-cooker-pho-ga-recipe.html
cook_time: 30 minutes
servings: [4, 6]
scale: 1
tags: 
  - recipes/authors/kenji
  - recipes/soup
  - recipes/world/asian/vietnamese
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
