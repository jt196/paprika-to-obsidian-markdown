# Introduction

This is a simple Python script that primarily will convert your Paprika recipes into Markdown. 

It is built for use in Obsidian using the Dataview plugin, but you can use this to convert your recipe files into markdown, with some loss in functionality.

This is not (*quite*) intended to replace Paprika as your recipe manager, but it does manage to repeat some basic functionality, including scaling and tag usage. 

# Set Up
## Requirements: 

- Python 3x 
- Paprika recipe manager (or a *.paprikarecipes* file)
## Quick Start

1. Clone the repo to a folder of your choice.
2. Export your Paprika recipes into the repo folder. You'll need to make sure this is in the format ".paprikarecipes" and NOT HTML. 
3. Open up a Terminal window in the repo folder. 
4. Run the command `python paprika_to_md.py "Archive.paprikarecipes" "my_vault/recipes" "_resources" "template_dataview.md"`. 
5. Your Paprika recipes should be exported to the folder "my_vault" in the working directory. Images will be stored in a subfolder "_resources".
# Demo Vault

I've added a demo vault with some demo recipes and a basic set up. This does include the [Cybertron theme](https://github.com/nickmilo/Cybertron) and the [dataview plugin](https://github.com/blacksmithgu/obsidian-dataview/).

You *should* just be able to open the vault and have a play around with the recipes in there. I'm not totally sure if this won't cause any issues on other systems, but it seemed like an idea to show folks what it looked like without any Paprika import files to play with.

I've included a couple of simple views (source and author) using the regular dataview table format. Please hit me if you have some more interesting stuff to add. 

# Obsidian Set Up

If you're not using the demo vault, in order to view the files properly, you'll need to install the dataview plugin and enable dataviewjs queries. 

1. Go to preferences, turn off safe mode if it's not disabled already. 
2. Go to Community Plugins, install Dataview, and enable from the menu. 
3. Go to Dataview plugin options, and Enable Javascript Queries. 

# Command Line Arguments

- The basic commands are `python paprika_to_md.py paprika-export-file target-vault resources-folder template-file`
- `paprika-export-file` is your *.paprikarecipes* file. This should be in your working directory. 
- `target-vault` is the folder you wish to save your recipes. This is relative to the present working directory. 
- `resources-folder` is the folder where your resources will reside, it'll be a subdirectory inside the `target-vault`. 
- `template-file` is the basic format of your recipes. This resides in the templates folder. I've included a template file named `template_dataview.md` to get you started, but you can format it however you wish. You don't need to include the *templates/* filepath as the script already knows to look in the folder. 

# Template

When you parse your recipes, the script uses a Python template file to copy each one. You can choose the template file when you run the script, see the arguments section above. 

The current *template_dataview.md* file is formatted for use in Obsidian using the *dataviewjs* language. If you're not using Obsidian or dataview, it'll produce a Markdown file with frontmatter YML. I'll add some simpler templates in the future so you can choose what you want to export them as.

## DataviewJS Functionality

Using DataviewJS, I'm able to build in some functionality to the pages. 

1. Recipe Scaling. Provided the recipe ingredients are formatted properly, the recipe should be able to scale using the *scale* yml tag. It'll default at 1, and you just need to change that figure to however you wish to scale it, and the ingredients that have been correctly formatted will be adjusted. The servings will also be adjusted.
2. When the ingredients haven't been parsed properly, the whole ingredient line will be displayed. Scaling won't work, but you'll be able to see what's going on.
3. Hidden Sections. Any sections that don't have any items will be hidden. Often recipes won't have notes or a description. DataviewJS allows me to hide them if they're not there, maximising space in the note. 
4. Recipe Photos. You'll see your photos displayed - thumbnail at the top, and the remaining attached photos at the bottom of the note. Obsidian is a bit funny about rendering photos, so you may need to open and close the note if this doesn't work properly. Try entering view mode, then opening and closing. 
## Notes

- As the script is set up currently, all of the identifiers (e.g. `$recipe_name`) currently in the template file  need to be in there. If you decide to change the template, then just make sure they're currently all in there, or you'll get an error message.
- I've added a pure YML Frontmatter template *template_yml.md*, which is basically the dataview template without the dataviewjs sections. If you're using Obsidian, I'd strongly encourage you to use the dataviewjs. This is primarily for folks who aren't in Obsidian and wish to work with frontmatter YML markdown. 
- If you just want a simple note, there's also a *template_puremd.md* file, this will display your recipe and all the rest of the junk. It won't be pretty but it'll do the job. Please let me know you have any suggestions for improving this.


# Ingredients

- In order for the recipe scale functionality to work, the ingredients need to be formatted correctly. Unless you never wish to open Paprika again (or don't have a working copy), I'd suggest doing this work in Paprika. It can be quite long and laborious, (list view will help) but it'll be worth it as you'll be able to export your recipes whenever you wish to use them in a Markdown viewer.
- Once processed, the note will display the ingredients in a list, each line will look like this:
`  - [15.0, 'ml', 'Dijon mustard', '', '15ml Dijon mustard']`
- The format is `[Quantity, unit, ingredient, note, full_text]`. 

## Preparing Your Data

- I'd suggest working through your recipes in Paprika until you have all the ingredients formatted thus: 
  - `quantity unit ingredient, note` e.g. "1 tbsp black pepper, ground"
  - `quantity unit ingredient (note)` e.g. "2 litres water (filtered)"
  - `quantity ingredient, note` e.g. "1 chicken, whole
- The note bit is optional, but you don't want multiple commas or brackets after the first bracket or comma, or it won't work well.
- What DEFINITELY won't work is having the quantity towards the end or in the middle of the ingredient - e.g. "Black Pepper 1 tbsp". 
- If the ingredient parser is unable to figure out what's going on, the note will display the whole line. 

# Tags

This may be specific to me, but I wanted to preserve the tag hierarchy from my recipes. Have a look at the *tag_conversion.py* file. It's a simple Python dictionary. You can do this too if you want, but it's a bit of a manual process. It involved:

1. Copying all the tags in Paprika (as keys) - without any hierarchy.
2. Adding the hierarchy into the file (as values) - on the right hand side. 

The final file has the format:

```JSON
tag_con = {
    "African": "recipes/world/african",
    "Asian": "recipes/world/asian",
    "BBQ": "recipes/bbq"
}
```
Where the left key (e.g. "African") is the Paprika tag, and the right value (e.g. "recipes/world/african") is the tag I wish to apply in the Markdown note. 

If you're new to this type of data formatting, don't forget the commas (except the last item) and colons or it'll break. 
## Authors

Some of my Paprika tags were authors, I wanted a way to add this to another yml tag "authors". It's plural as you're able to select multiple authors and it'll still export correctly - and work with Dataview.

Any Obsidian tag containing the string "authors", e.g. "recipes/authors/adamliaw" will add the key to the authors tag. So of the pair `"Adam Liaw": "recipes/authors/adamliaw"`, if the script finds the tag "recipes/authors/adamliaw", it'll add the string "Adam Liaw" to the authors tag. 

If you wish to tailor this to your own tagging system, find the line `authors = positive_filter(tag_map, "authors")` in the script and change the "authors" after the `tag_map` to a string of your choice. This'll filter the tag list by whatever keyword you decide, and add the original Paprika tag to the "authors" section. 
# Credits

- [Dataview plugin](https://github.com/blacksmithgu/obsidian-dataview/) - used to display the recipe
- [Cybertron theme](https://github.com/nickmilo/Cybertron) - Used in the demo vault
- [Parse Ingredients](https://github.com/MichielMag/parse-ingredients) - Python library used to process the recipe ingredients.
- [Obsidian Forum Recipe Database thread](https://forum.obsidian.md/t/help-howto-build-recipe-database-in-obsidian-complex/19548/52)