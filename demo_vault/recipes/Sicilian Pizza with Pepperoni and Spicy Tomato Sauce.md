---
name: "Sicilian Pizza with Pepperoni and Spicy Tomato Sauce"
source: "Seriouseats.com"
ingredients: 
  - [0, '', '**For the Dough :**', '(see note)', '**For the Dough (see note):**']
  - [500.0, 'g', 'bread flour', '', '500g bread flour']
  - [14.0, 'g', 'salt', '', '14g salt']
  - [6.0, 'g', 'instant yeast', '', '6g instant yeast']
  - [20.0, 'g', 'extra-virgin olive oil', '', '20g extra-virgin olive oil']
  - [40.0, 'g', 'olive oil for the pan', '', '40g olive oil for the pan']
  - [325.0, 'g', 'water', 'room-temperature', '325g water, room-temperature']
  - [0, '', '**For the Sauce:**', '', '**For the Sauce:**']
  - [30.0, 'ml', 'extra-virgin olive oil', '', '30ml extra-virgin olive oil']
  - [9.0, '', 'cloves garlic', 'medium roughly chopped', '9 cloves garlic, medium roughly chopped']
  - [1.0, 'tbsp', 'dried oregano', '', '1 tablespoon dried oregano']
  - [2.0, 'tsp', 'dried red pepper flakes', '', '2 teaspoons dried red pepper flakes']
  - [800.0, 'g', 'can whole peeled tomatoes', '', '800g can whole peeled tomatoes']
  - [1.0, 'tsp', 'sugar', '', '1 teaspoon sugar']
  - [0, '', 'Kosher salt', '', 'Kosher salt']
  - [0, '', '**To Assemble and Bake:**', '', '**To Assemble and Bake:**']
  - [450.0, 'g', 'mozzarella cheese', 'sliced', '450g mozzarella cheese, sliced']
  - [325.0, 'g', 'pepperoni', 'cut into 1/8-inch slices', '325g pepperoni, cut into 1/8-inch slices']
  - [115.0, 'g', 'Pecorino Romano cheese', 'ground', '115g Pecorino Romano cheese, ground']
source: "Seriouseats.com"
difficulty: 
photo_thumbnail: _resources/7744F624-C160-4C62-A368-FF05C294A181.jpg
image_url: https://www.seriouseats.com/recipes/images/2016/05/20160503-spicy-spring-pizza-recipe-37.jpg
total_time: 
notes: |
nutritional_info: []
description: |
rating: 0
prep_time: 30 minutes
created: 2020-06-28 18:43:49
directions: |
  1. To Make the Dough in a Food Processor (recommended): Combine flour, salt, yeast, 0.35 ounce olive oil, and water in the bowl of a food processor fitted with the blade or dough blade attachment. Process until a dough that rides around the blade forms, then continue processing for 30 seconds. Continue with Step 4 below.
  2. To Make the Dough in a Stand Mixer: Combine flour, salt, yeast, and 0.35 ounce olive oil in the bowl of a stand mixer (see below for mixer-free version). Whisk to combine. Fit mixer with dough hook attachment. Add water to mixer and mix on medium speed until dough comes together and no dry flour remains. Increase speed to medium-high and mix until dough is stretchy and smooth, about 6 minutes. The dough should stick to the bottom of bowl, but pull away from the sides. Continue with Step 4 below.
  3. To Make the Dough Using the No-Knead Method: Combine flour, salt, and yeast in a large bowl. Whisk to combine. Add 0.35 ounce olive oil and water and stir by hand until dough comes together and no dry flour remains. Cover bowl tightly with plastic wrap and let rest at room temperature for 12 to 24 hours. Continue with Step 4 below.
  4. Pour remaining 1/4 cup olive oil into a 13- by 18-inch rimmed baking sheet and spread over entire inner surface with your hands. Transfer dough to baking sheet and turn in oil until thoroughly coated. Spread gently with your hands. (It will not stretch to fill the pan; this is fine.) Cover baking sheet with plastic wrap and allow to rise at room temperature until dough has slackened and started to spread out toward the edges of the pan, 2 to 3 hours. Carefully remove plastic wrap from pizza dough. Using oiled hands, and working as gently as possible to maintain air bubbles, push and stretch dough into the corners of the pan by pressing out from the center, lifting each corner, and stretching it beyond the edge of the pan. It should pull back until pan is just filled with dough. Set aside for 20 to 30 minutes while you make the sauce.
  5. For the Sauce: Heat olive oil in a large saucepan over medium heat until shimmering. Add garlic, oregano, and red pepper flakes and cook, stirring, until softened and aromatic, about 1 minute. Add tomatoes. Using a pastry cutter or a potato masher, break up tomatoes into fine chunks. Stir in sugar. Bring to a bare simmer and allow to cook for about 15 minutes to let flavors meld. Season to taste with salt. Set aside and allow to cool slightly.
  6. Thirty minutes before baking, adjust oven rack to lower position and preheat oven to 550°F.
  7. To Assemble and Bake: Spread slices of mozzarella cheese evenly over surface of pizza. Spoon sauce on top of cheese and spread with the back of a spoon. (You will not need all the sauce; use as much as you like, but be sparing.) Spread pepperoni slices evenly over surface. Sprinkle with half of Romano cheese. Transfer to oven and bake until pepperoni is crisp and curled and bottom of pizza is golden brown when you peek by lifting the corner with a thin spatula, about 10 minutes. With some ovens, you may need to loosely tent the top of the pizza with aluminum foil and continue baking until the bottom is golden and crisp.
  8. Remove pizza from oven. Sprinkle with remaining half of Romano cheese, use a pizza wheel to cut it into slices, and serve immediately.
categories: ['Italian', 'J Kenji Lopez-Alt', 'Pizza']
source_url: https://www.seriouseats.com/recipes/2016/05/spicy-spring-sicilian-pizza-recipe.html
cook_time: about 4 hours (or 16 to 28 hours if using no-knead hand method)
servings: [13, 18]
scale: 1
tags: 
  - recipes/world/european/italian
  - recipes/authors/kenji
  - recipes/pizza
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
