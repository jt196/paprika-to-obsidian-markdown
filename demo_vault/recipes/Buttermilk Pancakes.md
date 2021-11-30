---
name: "Buttermilk Pancakes"
source: "Cooking.nytimes.com"
ingredients: 
  - [2.0, 'cup', 'all-purpose flour', '', '2 cups all-purpose flour']
  - [3.0, 'tbsp', 'sugar', '', '3 tablespoons sugar']
  - [1.0, 'tsp', 'baking powder', '', '1 teaspoons baking powder']
  - [1.0, 'tsp', 'baking soda', '', '1 teaspoons baking soda']
  - [0.25, 'tsp', 'cinnamon', '(optional)', '¼ tsp cinnamon (optional)']
  - [1.0, 'tsp', 'vanilla', '', '1 tsp vanilla']
  - [1.25, 'tsp', 'kosher salt', '', '1 ¼ teaspoons kosher salt']
  - [2.5, 'cup', 'buttermilk', '', '2 ½ cups buttermilk']
  - [2.0, '', 'large eggs', '', '2 large eggs']
  - [3.0, 'tbsp', 'unsalted butter', 'melted', '3 tablespoons unsalted butter, melted']
  - [0, '', 'Vegetable', 'canola or coconut oil for the pan', 'Vegetable']
source: "Cooking.nytimes.com"
difficulty: 
photo_thumbnail: _resources/2DC57C61-5108-484B-AB4E-45F8EA21200B.jpg
image_url: https://static01.nyt.com/images/2016/06/15/dining/15PANCAKEGUIDE3-WEB/15PANCAKEGUIDE3-WEB-mediumThreeByTwo440.jpg
total_time: 
notes: |
nutritional_info: []
description: |
rating: 0
prep_time: 
created: 2020-12-19 12:26:46
directions: |
  Heat the oven to 325 degrees. Whisk flour, sugar, baking powder, baking soda and kosher salt together in a bowl. Using the whisk, make a well in the center. Pour the buttermilk into the well and crack eggs into buttermilk. Pour the melted butter into the mixture. Starting in the center, whisk everything together, moving towards the outside of the bowl, until all ingredients are incorporated. Do not overbeat (lumps are fine). Rest for 30 mins, or the batter can be refrigerated for up to one hour.
  Heat a large nonstick griddle or skillet, preferably cast-iron, over low heat for about 5 minutes. Add 1 tablespoon oil to the skillet. Turn heat up to medium–low and using a measuring cup, ladle 1/3 cup batter into the skillet. If you are using a large skillet or a griddle, repeat once or twice, taking care not to crowd the cooking surface.
  Flip pancakes after bubbles rise to surface and bottoms brown, about 2 to 4 minutes. Cook until the other sides are lightly browned. Remove pancakes to a wire rack set inside a rimmed baking sheet, and keep in heated oven until all the batter is cooked and you are ready to serve.
categories: ['Breakfast', 'J Kenji Lopez-Alt', 'USA']
source_url: https://cooking.nytimes.com/recipes/1018180-perfect-buttermilk-pancakes
cook_time: 10 minutes
servings: [4]
scale: 1
tags: 
  - recipes/breakfast
  - recipes/authors/kenji
  - recipes/world/usa
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
