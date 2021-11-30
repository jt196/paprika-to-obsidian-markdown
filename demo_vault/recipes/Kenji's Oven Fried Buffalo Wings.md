---
name: "Kenji's Oven Fried Buffalo Wings"
source: ""
ingredients: 
  - [2.5, 'lb', 'chicken wings', '(450g to 1.7kg)  cut into drumettes and flats', '1 to 4 pounds (450g to 1.7kg) chicken wings, cut into drumettes and flats']
  - [1.0, 'tsp', 'baking powder per pound of chicken wings', '(5g)', '1 teaspoon (5g) baking powder per pound of chicken wings']
  - [1.0, 'tsp', 'kosher salt per pound of chicken wings', '(5g)', '1 teaspoon (5g) kosher salt per pound of chicken wings']
  - [2.0, 'tbsp', 'unsalted butter per pound of chicken wings', '(1 ounce; 55g)', '2 tablespoons (1 ounce; 55g) unsalted butter per pound of chicken wings']
  - [2.0, 'tbsp', "Frank's RedHot Sauce per pound of chicken wings", '(1 ounce; 60ml)', "2 tablespoons (1 ounce; 60ml) Frank's RedHot Sauce per pound of chicken wings"]
  - [0, '', 'Blue cheese dressing', 'for serving', 'Blue cheese dressing, for serving']
  - [0, '', 'Celery sticks', 'for serving', 'Celery sticks, for serving']
source: ""
difficulty: 
photo_thumbnail: _resources/D8D1056C-CB33-47B0-B860-2E66A808824B-10329-0008D908441F58E3.jpg
image_url: None
total_time: 
notes: |
  - Try adding a bit of honey to the sauce
nutritional_info: []
description: |
  The secret to baked wings that taste just like real-deal, deep-fried Buffalo wings? Some baking powder. But, of course, this wouldn't be The Food Lab unless we tested 28 variations first to confirm.
  WHY THIS RECIPE WORKS:
  - Air-drying the wings overnight helps them crisp up faster when you bake them, which corresponds to juicier meat in the end.
  - Baking powder adds surface area to the chicken wings, intensifying their crunch.
rating: 0
prep_time: 
created: 2021-04-09 17:14:54
directions: |
  1. Line a rimmed baking sheet with aluminum foil and set a wire rack inside. Carefully dry chicken wings with paper towels. In a large bowl, combine wings with baking powder and salt and toss until thoroughly and evenly coated. Place on rack, leaving a slight space between each wing. Repeat with remaining 2 batches of wings.
  2. Place baking sheet with wings in refrigerator and allow to rest, uncovered, at least 8 hours and up to 24 hours.
  3. Adjust oven rack to upper-middle position and preheat oven to 450°F (230°C). Add chicken wings and cook for 20 minutes. Flip wings and continue to cook until crisp and golden brown, 15 to 30 minutes longer, flipping a few more times towards the end.
  4. Meanwhile, combine butter and hot sauce in a small saucepan and cook over medium heat, whisking until combined. Transfer wings to a large bowl, add sauce, and toss to thoroughly coat. Serve wings immediately with blue cheese dressing and celery sticks, conspicuously shunning anyone who says that real Buffalo wings must be fried.
categories: ['Air Fryer', 'J Kenji Lopez-Alt', 'Meat', 'USA']
source_url: 
cook_time: 
servings: [1]
scale: 1
tags: 
  - recipes/baking/airfryer
  - recipes/authors/kenji
  - recipes/meat
  - recipes/world/usa
photos: 
 - './_resources/B47E44B6-47F4-4BD7-80D3-464357741BF5-10329-0008D782A8D62B30.jpg'
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
