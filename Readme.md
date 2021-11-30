# Introduction

This is a simple Python script that primarily will convert your Paprika recipes into Markdown. 

It is built for use in Obsidian using the Dataview plugin, but you can use this to convert your recipe files into markdown, with some loss in functionality. 

# Set Up
## Requirements: 

- Python 3x 
- Paprika recipe manager
## Quick Start

1. Clone the repo to a folder of your choice.
2. Export your Paprika recipes into the repo folder. You'll need to make sure this is in the format ".paprikarecipes" and NOT HTML. 
3. Open up a Terminal window in the repo folder. 
4. Run the command `python paprika_to_md.py "Archive.paprikarecipes" "my_vault" "_resources" "template.md"`. 
5. Your Paprika recipes should be exported to the folder "my_vault" in the working directory. Images will be stored in a subfolder "_resources".
# Demo Vault

I've added a demo vault with some demo recipes and a basic set up. This does include the [Cybertron theme](https://github.com/nickmilo/Cybertron) and the [dataview plugin](https://github.com/blacksmithgu/obsidian-dataview/).

You *should* just be able to open the vault and have a play around with the recipes in there. I'm not totally sure if this won't cause any issues on other systems, but it seemed like an idea to show folks what it looked like without any Paprika import files to play with.

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
- `template-file` is the basic format of your recipes. I've included a template file named `template.md` to get you started, but you can format it however you wish.

# Template

The current *template.md* file is formatted for use in Obsidian using the *dataviewjs* language. If you're not using Obsidian or dataview, it'll produce a Markdown file with frontmatter YML. I'll add some simpler templates in the future so you can choose what you want to export them as.

As the script is set up currently, all of the identifiers (e.g. `$recipe_name`) currently in the template file  need to be in there. If you decide to change the template, then just make sure they're currently all in there, or you'll get an error message. 






