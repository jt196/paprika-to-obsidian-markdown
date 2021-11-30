---
name: "Caramelized Onions - Low and Slow"
source: "Seriouseats.com"
ingredients: 
  - [0, '', 'Onions', '', 'Onions']
source: "Seriouseats.com"
difficulty: 
photo_thumbnail: _resources/773FA733-4614-4432-A2E3-D9C9D3AF2881.jpg
image_url: https://www.seriouseats.com/2019/05/20190510-caramelized-onions-vicky-wasik-10-1-1500x1125.jpg
total_time: 
notes: |
nutritional_info: []
description: |
rating: 0
prep_time: 
created: 2021-03-01 18:03:05
directions: |
  **Get the Onions Going**
  Add the fat of your choice to the cooking vessel, turn the heat to medium-high and add the onions. You don't need to wait for the fat or pan to heat up before adding the onions—you actually want to ease the onions into the heat and reduce any risk of the too-quick browning that can happen when food is added to a pre-heated pan.
  You're starting out over higher heat because you want to get things going, but keep in mind that as the activity in the pan ramps up, you'll have to keep turning the heat down to prevent scorching.
  **Cover**
  The first phase of the process is softening the onions so that they collapse into a tender mass while releasing a good deal of their liquid. If you cover the pan, you'll trap steam, which will speed up their softening, heat them more quickly, and help release their liquid more quickly. Lift the lid a few times during this stage to give them a stir and make sure nothing is browning yet.
  You don't have to cover the pan if you don't want to, it merely shaves some minutes off the total cooking time.
  **Uncover and Stir**
  As soon as the onions have softened, remove the lid so that the steam can escape; you won't have good browning in the presence of a lot of water, so it has to have a way to escape the pot.
  **Stir and Scrape**
  Continue stirring and scraping the onions every minute or two, keeping an eye for signs of browning on the bottom of the pot. When the browning starts speeding up, it's best to lower the heat to keep the transformation slow and even. You can, if you want, continue to work over higher heat, but you'll need to be more attentive, stirring and scraping even more frequently, and being ready with water to deglaze at a moment's notice (see the next step for more on that).
  As the brown glaze (called the fond in French) builds up under the onions, scrape it up with your wooden spoon. You want to keep scraping it up and folding it back into the onions. It's delicious.
  Do this over and over as the onions gradually more brown.
  **Deglaze If/When Necessary**
  There may come a point where you can't scrape up some of those browned bits, they're just cooked on too hard (if you're cooking over higher heat, this will definitely happen). To deal with this, pour a few tablespoons of water into the pan to deglaze it. The liquid will help you dissolve the stubborn fond and allow you to work it back into the mass of onions. The water you add will pretty quickly cook off and the bottom of the pot will start to brown again. Deglaze as often as necessary to prevent the onions from scorching.
  Deglazing the pan with water while cooking over higher heat is one of the only ways to speed up caramelized onions without sacrificing too much quality. You can deglaze as much as necessary while keeping the flame higher to brown the onions faster; the key is to add the water every time the onions threaten to burn. It should go without saying that you run the risk of ruining your onions by cooking them over higher heat, so proceed with caution.
  When they reach your desired level of caramelization, remove them from heat and season with salt. Good job, you caramelized onions, and you did it the best way—the only way.
categories: ['J Kenji Lopez-Alt', 'Vegetarian']
source_url: https://www.seriouseats.com/2019/06/how-to-caramelize-onions-classic.html
cook_time: 
servings: [1]
scale: 1
tags: 
  - recipes/authors/kenji
  - recipes/vegetarian
photos: 
 - './_resources/145E58B7-39F8-4266-8BE0-AEC5CD750ED4-29409-0005A2D3224DF434.jpg'
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
