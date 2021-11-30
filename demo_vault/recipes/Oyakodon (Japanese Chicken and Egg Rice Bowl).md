---
name: "Oyakodon (Japanese Chicken and Egg Rice Bowl)"
source: "Seriouseats.com"
ingredients: 
  - [240.0, 'ml', 'dashi', 'or the equivalent in Hondashi', '240ml dashi, or the equivalent in Hondashi']
  - [15.0, 'ml', 'soy sauce', 'plus more to taste', '15ml soy sauce, plus more to taste']
  - [30.0, 'ml', 'dry sake', '', '30ml dry sake']
  - [1.0, 'tbsp', 'sugar', 'plus more to taste', '1 tablespoon sugar, plus more to taste']
  - [1.0, '', 'large onion', '(slivered - about 6 ounces; 170g)', '1 large onion (slivered - about 6 ounces; 170g)']
  - [340.0, 'g', 'chicken thighs', '(boneless, skinless - thinly sliced)', '340g chicken thighs (boneless, skinless - thinly sliced)']
  - [3.0, '', 'thinly sliced scallions', 'divided', '3 thinly sliced scallions, divided']
  - [2.0, '', 'stems mitsuba', '', '2 stems mitsuba ']
  - [4.0, '', 'large eggs', '', '4 large eggs']
  - [0, '', '**To Serve:**', '', '**To Serve:**']
  - [2.0, 'cup', 'cooked white rice', '', '2 cups cooked white rice']
  - [0, '', 'Togarashi', '(see note)', 'Togarashi (see note)']
source: "Seriouseats.com"
difficulty: 
photo_thumbnail: _resources/3873A167-623A-4BD3-B69E-00F1C6BBDF96.jpg
image_url: https://www.seriouseats.com/recipes/images/2016/08/20160802-oyakodon-4-200x150.jpg
total_time: 
notes: |
nutritional_info: []
description: |
rating: 0
prep_time: 20 minutes
created: 2020-08-12 09:27:03
directions: |
  1. Combine dashi, soy sauce, sake, and sugar in a small saucepan and bring to a simmer over high heat. Adjust heat to maintain a strong simmer. Stir in onion and cook, stirring occasionally, until onion is half tender, about 5 minutes. Add chicken pieces and cook, stirring and turning chicken occasionally, until chicken is cooked through and broth has reduced by about half, 5 to 7 minutes for chicken thighs or 3 to 4 minutes for chicken breast. Stir in half of scallions and all of mitsuba (if using), then season broth to taste with more soy sauce or sugar as desired. The sauce should have a balanced sweet-and-salty flavor.
  2. Reduce heat to a bare simmer. Beat eggs lightly with chopsticks in a medium bowl. Pour eggs into pot in a thin, steady stream (see note), holding your chopsticks over edge of bowl to help distribute eggs evenly (see video above). Cover and cook until eggs are cooked to desired doneness, about 1 minute for runny eggs or 3 minutes for medium-firm.
  3. To Serve: Transfer hot rice to a single large bowl or 2 individual serving bowls. Top with egg and chicken mixture, pouring out any excess broth from saucepan over rice. Add an extra egg yolk to center of each bowl, if desired (see note). Garnish with remaining half of sliced scallions and togarashi. Serve immediately.
categories: ['J Kenji Lopez-Alt', 'Japanese', 'Meat', 'Rice']
source_url: https://www.seriouseats.com/recipes/2016/08/oyakodon-japanese-chicken-and-egg-rice-bowl-recipe.html
cook_time: 20 minutes
servings: [2]
scale: 1
tags: 
  - recipes/authors/kenji
  - recipes/world/asian/japanese
  - recipes/meat
  - recipes/rice
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
