import os, re, zipfile, gzip, json, base64, ast, sys
from pathlib import Path
from string import Template
import tag_conversion as tag
from parse_ingredient import parse_ingredient
from tools import positive_filter, key_swap, filter_list, correct_path, remove_temp_files, remove_file_extension


# this function extracts a .paprikarecipes file into a .temp/ folder, unzips each gzipped recipe file and renames the contents
def extract_nested_zip(zippedFile, toFolder):
    """ Unzip a zip file and its contents, including nested zip files
        Delete the zip file(s) after extraction
    """
    if not os.path.exists(toFolder):
        os.makedirs(toFolder)
    with zipfile.ZipFile(zippedFile, 'r') as zfile:
        zfile.extractall(path=toFolder)
    # # this will delete the original .paprikarecipe file
    # os.remove(zippedFile)
    # 
    for root, dirs, files in os.walk(toFolder):
        for filename in files:
            # Look for files with the extension .paprikarecipes in the temp folder
            if re.search(r'\.paprikarecipe$', filename):
                # extract path
                p = Path(toFolder + filename)
                # create variable for opening the json document
                jsonfile = p.with_suffix('.json')
                # open json doc
                fp = open(jsonfile, 'wb')
                # unzip the gzip files in the directory
                with gzip.open(p, "rb") as f:
                    bindata = f.read()
                    fp.write(bindata)
                    fp.close()
                # remove the .paprikarecipe file
                os.remove(p)

# Manipulate json files extracted to temp folder
def json_manipulate(sourceFolder, targetFolder, resourceFolder, template):
    # Create target folders if they don't exist
    if not os.path.exists(targetFolder):
        os.makedirs(targetFolder)
    if not os.path.exists(targetFolder + resourceFolder):
        os.makedirs(targetFolder + resourceFolder)
    # Checking source folder and template exist
    if not os.path.exists(sourceFolder):
        sys.exit("Source folder path incorrect, please re-enter")
    template_file = "templates/" + template
    if not os.path.exists(template_file):
        sys.exit("Template file path incorrect, please re-enter")
    tag_map = tag.tag_con
    # filter the tag list removing all but value matches for authors
    authors = positive_filter(tag_map, "authors")
    # swap key/values around
    authors = key_swap(authors)
    # create a regex based on the keys in the tag_map dict
    pattern = re.compile(r'\b(' + '|'.join(tag_map.keys()) + r')\b')
    # create regex pattern for authors
    auth_pattern = re.compile(r'\b(' + '|'.join(authors.keys()) + r')\b')
    for root, dirs, files in os.walk(sourceFolder):
        for filename in files:
            if re.search(r'\.json$', filename):
                p = Path(sourceFolder + filename)
                with open(p, encoding="utf-8") as json_file:
                    d = {}
                    recipe_data = json.load(json_file)
                    bare_filename = remove_file_extension(filename)
                    # assign variable, split according to line breaks, remove any empty entries
                    recipe_ingredients = recipe_data["ingredients"]
                    recipe_ingredients = recipe_ingredients.splitlines()
                    recipe_ingredients = [i for i in recipe_ingredients if i]
                    ingredients = ""
                    for ingredient in recipe_ingredients:
                        try:
                            result = parse_ingredient(ingredient)
                        except:
                            print("Error parsing ingredients for: " + recipe_name)    
                        ingredients += "\n  - " + str(result)
                    recipe_source = recipe_data["source"]
                    recipe_source = re.sub(r'"', '\'', recipe_source)
                    recipe_source = '"' + recipe_source + '"'
                    recipe_hash = recipe_data["hash"]
                    recipe_difficulty = recipe_data["difficulty"]
                    recipe_photo = recipe_data["photo"]
                    recipe_image_url = recipe_data["image_url"]
                    recipe_total_time = recipe_data["total_time"]
                    recipe_notes = recipe_data["notes"]
                    recipe_notes = recipe_notes.splitlines()
                    recipe_notes = [i for i in recipe_notes if i]
                    notes = ""
                    for note in recipe_notes:
                        notes += "\n  " + str(note)
                    recipe_name = recipe_data["name"]
                    # replace any "/" characters in the name - screws the file naming up
                    recipe_name = re.sub(r'\/', '-', recipe_name)
                    # replace any quotation marks in the recipe name " with '
                    recipe_name = re.sub(r'"', '\'', recipe_name)
                    recipe_name_tag = '"' + recipe_name + '"'
                    recipe_photo_hash = recipe_data["photo_hash"]
                    recipe_nutritional_info = recipe_data["nutritional_info"]
                    recipe_nutritional_info = recipe_nutritional_info.splitlines() 
                    recipe_description = recipe_data["description"]
                    recipe_description = recipe_description.splitlines()
                    recipe_description = [i for i in recipe_description if i]
                    descriptions = ""
                    for description in recipe_description:
                        descriptions += "\n  " + str(description)
                    recipe_rating = recipe_data["rating"]
                    recipe_prep_time = recipe_data["prep_time"]
                    recipe_photos = recipe_data["photos"]
                    recipe_uid = recipe_data["uid"]
                    recipe_created = recipe_data["created"]
                    recipe_directions = recipe_data["directions"]
                    # split the text into a list every new line
                    recipe_directions = recipe_directions.splitlines()
                    # remove empty list entries
                    recipe_directions = [i for i in recipe_directions if i]
                    directions = ""
                    if recipe_directions:
                        for direction in recipe_directions:
                            directions += "\n  " + str(direction)
                    recipe_categories = recipe_data["categories"]
                    recipe_tags = recipe_categories
                    # find and replace for the tags - based on dictionary file that I'm importing at the top
                    recipe_tags = pattern.sub(lambda x: tag_map[x.group()], str(recipe_categories))
                    # converts this from a string to a proper dictionary
                    recipe_tags = ast.literal_eval(recipe_tags)
                    tags = "\n  - " + "\n  - ".join(recipe_tags)
                    # PROCESS TAGS INTO AUTHORS IF EXISTS
                    # filter recipe tags, removing all but author tags
                    recipe_tags_filtered = filter_list("authors", recipe_tags)
                    # substitute those tags for the author names
                    recipe_authors = auth_pattern.sub(lambda x: authors[x.group()], str(recipe_tags_filtered))
                    recipe_authors = ast.literal_eval(recipe_authors)
                    my_authors = ""
                    if recipe_authors:
                        for author in recipe_authors:
                            my_authors += "\n  " + str(author)
                    recipe_photo_data = recipe_data.get("photo_data")
                    recipe_source_url = recipe_data["source_url"]
                    recipe_cook_time = recipe_data["cook_time"]
                    recipe_photo_large = recipe_data["photo_large"]
                    recipe_scale = 1
                    recipe_servings_raw = recipe_data["servings"].lower()
                    # find any digits in the recipe_servings data
                    temp = re.findall(r'\d+', recipe_servings_raw)
                    # convert the list to integers
                    res = list(map(int, temp))
                    # append to recipe_servings list
                    recipe_servings = []
                    if len(res) > 1:
                        # if min and max portion
                        recipe_servings.append(res[0])
                        recipe_servings.append(res[1])
                    elif len(res) > 0:
                        # if no max portion
                        recipe_servings.append(res[0])
                    else: 
                        # if no entry for servings, make it 1
                        recipe_servings = [1]
                    # save the recipe thumbnail to file
                    if recipe_photo_data:
                        # decode photo data
                        recipe_jpg = base64.b64decode(recipe_photo_data)
                        # write to folder
                        g = open(targetFolder + resourceFolder + recipe_photo, "wb")
                        g.write(recipe_jpg)
                        g.close()
                    photo_list = []
                    # save recipe photos to file and add to photo_list
                    if recipe_photos:
                        # print(recipe_photos)
                        for photo in recipe_photos:
                            # Add filename to list
                            file = photo['filename']
                            photo_list.append(("\n - './" + resourceFolder + file + "'"))
                            # decode the photo data
                            # print(file)
                            recipe_jpg = base64.b64decode(photo['data'])
                            # write to folder
                            g = open(targetFolder + resourceFolder + file, "wb")
                            g.write(recipe_jpg)
                            g.close()
                    # parse the photo list to make them yml format
                    photo_list = "".join(photo_list)
                    # add relative path to recipe_photo if exists
                    if recipe_photo:
                        recipe_photo = resourceFolder + recipe_photo
                    d = {
                        'recipe_name': recipe_name_tag,
                        'recipe_source': recipe_source,
                        'recipe_ingredients': ingredients,
                        'recipe_source': recipe_source,
                        'recipe_difficulty': recipe_difficulty,
                        'recipe_photo': recipe_photo,
                        'recipe_image_url': recipe_image_url,
                        'recipe_total_time': recipe_total_time,
                        'recipe_notes': notes,
                        'recipe_nutritional_info': recipe_nutritional_info,
                        'recipe_description': descriptions,
                        'recipe_rating': recipe_rating,
                        'recipe_prep_time': recipe_prep_time,
                        'recipe_created': recipe_created,
                        'recipe_directions': directions,
                        'recipe_categories': recipe_categories,
                        'recipe_tags': tags,
                        'recipe_source_url': recipe_source_url,
                        'recipe_cook_time': recipe_cook_time,
                        'recipe_servings': recipe_servings,
                        'recipe_scale': recipe_scale,
                        'photo_list': photo_list,
                        'my_authors': my_authors
                        }
                    with open(template_file, "r") as f:
                        src = Template(f.read())
                        result = src.substitute(d)
                        g = open(targetFolder + bare_filename + ".md", "w", encoding="utf-8")
                        g.write(result)
                        g.close()

# Run full conversion
def convert_paprika(paprika_file, target_vault, resource_folder, template_file):
    extract_nested_zip(paprika_file, ".temp/")
    target = correct_path(target_vault)
    resource = correct_path(resource_folder)
    json_manipulate(".temp/", target, resource, template_file)
    remove_temp_files(".temp/")

convert_paprika(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
