---
name: "Chocolate Chip Cookies (Kenji)"
source: "Seriouseats.com"
ingredients: 
  - [8.0, 'oz', 'unsalted butter', '(2 sticks; 225g)', '8 ounces unsalted butter (2 sticks; 225g)']
  - [1.0, '', 'standard ice cube', '(about 2 tablespoons; 30mL frozen water)', '1 standard ice cube (about 2 tablespoons; 30mL frozen water)']
  - [10.0, 'oz', 'all-purpose flour', '(about 2 cups; 280g)', '10 ounces all-purpose flour (about 2 cups; 280g)']
  - [0.75, 'tsp', 'baking soda', '(3g)', '3/4 teaspoon (3g) baking soda']
  - [1.5, 'tsp', 'table salt', '(4g)', '2 teaspoons Diamond Crystal kosher salt or 1 teaspoon table salt (4g)']
  - [5.0, 'oz', 'granulated sugar', '(about 3/4 cup; 140g)', '5 ounces granulated sugar (about 3/4 cup; 140g)']
  - [2.0, '', 'large eggs', '(100g)', '2 large eggs (100g)']
  - [2.0, 'tsp', 'vanilla extract', '(10mL)', '2 teaspoons (10mL) vanilla extract']
  - [5.0, 'oz', 'dark brown sugar', '(about 1/2 tightly packed cup plus 2 tablespoons; 140g)', '5 ounces dark brown sugar (about 1/2 tightly packed cup plus 2 tablespoons; 140g)']
  - [8.0, 'oz', 'semisweet chocolate', '(225g)  roughly chopped with a knife into 1/2- to 1/4-inch chunks', '8 ounces (225g) semisweet chocolate, roughly chopped with a knife into 1/2- to 1/4-inch chunks']
  - [0, '', 'Coarse sea salt', 'for garnish', 'Coarse sea salt, for garnish']
source: "Seriouseats.com"
difficulty: 
photo_thumbnail: _resources/A8AE9063-1716-4E4A-9B2E-A83A0A004481.jpg
image_url: https://www.seriouseats.com/recipes/images/2015/12/20131213-chocolate-chip-cookies-food-lab-55-edit.jpg
total_time: 
notes: |
nutritional_info: []
description: |
rating: 5
prep_time: 30 minutes
created: 2020-11-19 14:24:43
directions: |
  1. Melt butter in a medium saucepan over medium-high heat. Cook, gently swirling pan constantly, until particles begin to turn golden brown and butter smells nutty, about 5 minutes. Remove from heat and continue swirling the pan until the butter is a rich brown, about 15 seconds longer. Transfer to a medium bowl, whisk in ice cube, transfer to refrigerator, and allow to cool completely, about 20 minutes, whisking occasionally. (Alternatively, whisk over an ice bath to hasten the process.)
  2. Meanwhile, whisk together flour, baking soda, and salt in a large bowl. Place granulated sugar, eggs, and vanilla extract in the bowl of a stand mixer fitted with the whisk attachment. Whisk on medium-high speed until mixture is pale brownish-yellow and falls off the whisk in thick ribbons when lifted, about 5 minutes.
  3. Fit paddle attachment onto mixer. When brown butter mixture has cooled (it should be just starting to turn opaque again and firm around the edges), add brown sugar and cooled brown butter to egg mixture in stand mixer. Mix on medium speed to combine, about 15 seconds. Add flour mixture and mix on low speed until just barely combined, with some dry flour still remaining, about 15 seconds. Add chocolate and mix on low speed until dough comes together, about 15 seconds longer. Transfer to an airtight container and refrigerate dough at least overnight and up to 3 days.
  4. When ready to bake, adjust oven racks to upper- and lower-middle positions and preheat oven to 325°F. Using a 1-ounce ice cream scoop or a spoon, place scoops of cookie dough onto a nonstick or parchment-lined baking sheet. Each ball should measure approximately 3 tablespoons in volume, and you should be able to fit 6 to 8 balls on each sheet. Tear each ball in half to reveal a rougher surface, then stick them back together with the rough sides facing outward. Transfer to oven and bake until golden brown around edges but still soft, 13 to 16 minutes, rotating pans back to front and top to bottom halfway through baking.
  5. Remove baking sheets from oven. While cookies are still hot, sprinkle very lightly with coarse salt and gently press salt down to embed. Let cool for 2 minutes, then transfer cookies to a wire rack to cool completely.
  6. Repeat steps 3 through 5 for remaining cookie dough. Allow cookies to cool completely before storing in an airtight container, plastic bag, or cookie jar at room temperature for up to 5 days.
categories: ['Baking', 'Dessert', 'J Kenji Lopez-Alt']
source_url: https://www.seriouseats.com/recipes/2013/12/the-food-lab-best-chocolate-chip-cookie-recipe.html
cook_time: 1 day
servings: [28]
scale: 1
tags: 
  - recipes/baking
  - recipes/dessert
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
