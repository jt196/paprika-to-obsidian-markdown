---
name: "Spaetzle (Austrian Pasta - Dumplings)"
source: ""
ingredients: 
  - [70.0, 'g', 'flour', '', '70g flour']
  - [1.0, '', 'large egg', '', '1 large egg']
  - [40.0, 'ml', 'milk', '', '40ml milk']
  - [0, '', 'Pinch salt + pepper', '', 'Pinch salt + pepper']
  - [0, '', 'Some herbs', '', 'Some herbs ']
source: ""
difficulty: Easy
photo_thumbnail: _resources/8F362908-23D0-43F8-9713-A78DEB760E43-485-00029DC1D423C03E.jpg
image_url: None
total_time: 
notes: |
  You can also make the recipe with the same volume of water instead of milk. I like the texture and richness milk adds to it. It's very forgiving, so go with whatever you'd like.
  At the restaurant, we make large batches of batter, mix it a little longer, and let it rest overnight before boiling. You can do this at home too, if you prefer. Longer mixing makes them a little chewier and puffier, while resting the batter overnight improves flavor (similar to how resting cookie dough or Yorkshire pudding batter can help flavor: https://sweets.seriouseats.com/2013/1...).
nutritional_info: []
description: |
rating: 5
prep_time: 
created: 2020-11-19 13:14:31
directions: |
  Combine flour, egg, milk, a pinch of salt and pepper, and if desired, some finely minced herbs like parsley or chives. A pinch of ground nutmeg is also excellent and common with it. Whisk well and adjust texture with milk. It should flow like lava.
  Drop the batter into a pot of salted boiling water using a spaetzle-maker or by pressing it through the holes of a colander using a spatula. Boil for a minute, then remove from water. You can then toss in oil and chill it at this point.
  Finish it by sauteing in a pan with brown butter, or however else you want. This version uses cabbage and onion, similar to, say, Hungarian Halusky. Just plain onions and bacon is also great. So is mixing it with a good melting cheese like gruyere. Or if you want to go crazy, fry some kimchi and bacon, add the spaetzle, add some gochujang and water (or dashi), then cook it down until glazed and spicy and delicious. Apologize to your German friends.
categories: ['J Kenji Lopez-Alt']
source_url: 
cook_time: 
servings: [1]
scale: 1
tags: 
  - recipes/authors/kenji
photos: 
 - './_resources/7295A7F8-E920-4A45-A683-A221058B9678-485-00029DB7655D7A4B.jpg'
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
