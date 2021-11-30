---
name: "Fried Rice"
source: "Seriouseats.com"
ingredients: 
  - [350.0, 'g', 'cooked white rice', 'see note)', '350g cooked white rice - see note)']
  - [30.0, 'ml', 'vegetable or canola oil', 'divided', '30ml vegetable or canola oil, divided']
  - [1.0, '', 'small onion', '(finely chopped - 4 ounces; 115g)', '1 small onion (finely chopped - 4 ounces; 115g)']
  - [1.0, '', 'medium carrot', '(peeled and cut into small dice - 3 ounces; 85g)', '1 medium carrot (peeled and cut into small dice - 3 ounces; 85g)']
  - [2.0, '', 'scallions', '(thinly sliced - 1 ounce; 30g)', '2 scallions (thinly sliced - 1 ounce; 30g)']
  - [2.0, '', 'cloves garlic', '(medium, minced - about 2 teaspoons; 5g)', '2 cloves garlic, (medium, minced - about 2 teaspoons; 5g)']
  - [1.0, 'tsp', 'soy sauce', '', '1 teaspoon soy sauce']
  - [1.0, 'tsp', 'toasted sesame oil', '', '1 teaspoon toasted sesame oil']
  - [0, '', 'Kosher salt and ground white pepper', '', 'Kosher salt and ground white pepper']
  - [1.0, '', 'large egg', '', '1 large egg']
  - [115.0, 'g', 'frozen peas', '', '115g frozen peas']
source: "Seriouseats.com"
difficulty: 
photo_thumbnail: _resources/4B27A57A-1261-4D9F-A027-BADFF241BB06.jpg
image_url: https://www.seriouseats.com/recipes/images/2016/01/20160206-fried-rice-food-lab-68-750x563.jpg
total_time: 
notes: |
nutritional_info: []
description: |
rating: 0
prep_time: 10 minutes
created: 2020-09-02 20:21:42
directions: |
  1. If using day-old rice (see note), transfer to a medium bowl and break the rice up with your hands into individual grains before proceeding. Heat 1/2 tablespoon (7ml) vegetable oil in a wok over high heat until smoking. Add half of rice and cook, stirring and tossing, until the rice is pale brown and toasted and has a lightly chewy texture, about 3 minutes. Transfer to a medium bowl. Repeat with another 1/2 tablespoon oil and remaining rice.
  2. Return all the rice to the wok and press it up the sides, leaving a space in the middle. Add 1/2 tablespoon (7ml) oil to the space. Add onion, carrot, scallions, and garlic and cook, stirring gently, until lightly softened and fragrant, about 1 minute. Toss with rice to combine. Add soy sauce and sesame oil and toss to coat. Season to taste with salt and white pepper.
  3. Push rice to the side of the wok and add remaining 1/2 tablespoon (7ml) oil. Break the egg into the oil and season with a little salt. Use a spatula to scramble the egg, breaking it up into small bits. Toss the egg and the rice together.
  4. Add frozen peas and continue to toss and stir until peas are thawed and every grain of rice is separate. Serve immediately.
categories: ['Asian', 'J Kenji Lopez-Alt', 'Rice']
source_url: https://www.seriouseats.com/recipes/2016/02/easy-vegetable-fried-rice-recipe.html
cook_time: 10 minutes
servings: [2, 3]
scale: 1
tags: 
  - recipes/world/asian
  - recipes/authors/kenji
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
