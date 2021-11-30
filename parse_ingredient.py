# Source: parse-ingredients Python library
# https://github.com/MichielMag/parse-ingredients

import unicodedata
import re
from dataclasses import dataclass

@dataclass
class Ingredient:
    name : str
    quantity : int
    unit : str
    comment : str
    original_string : str

# a predefined list of unit's
units = {
    "l": ["l", "litre", "litres", "liter", "liters"],
    "ml": ["ml", "millilitre", "mL", "milli litre", "millilitres", "milli litres", "milliliter", "milli liter", "milliliters", "milli liters"],
    "g": ["g", "gram", "grams", "gr", "gm", "gm."],
    "mg": ["mg", "milligram", "milli gram", "milligrams", "milli grams"],
    "kg": ["kg", "kilogram", "kilo gram", "kilograms", "kilo grams", "kilos"],
    "oz": ["oz", "ounce", "ounces"],
    "fl": ["fl", "floz"],
    "tsp": ["tsp", "tsps", "teaspoon", "teaspoons"],
    "tbsp": ["tbsp", "tbsps", "tablespoon", "tablespoons"],
    "cup": ["cup", "cups"],
    "pint": ["pint", "pints"],
    "pinch": ["pinch"],
    "strip": ["strip", "strips"],
    "envelope": ["envelope", "envelopes", "sheet", "sheets"],
    "gal": ["gal", "gallon", "gallons"],
    "lb": ["lb", "lbs", "pound", "pounds"],
    "bunch": ["bunch", "bunches"],
    "clove": ["clove"]
}

# numbers with a simple slash fraction (1 1/3, 2 4/5, etc.)
numberAndSlashFraction = re.compile(r'(\d{1,3}?\s\d\/\d{1,3})')
# Vulgar fractions (½, ⅓, etc.)
fractionMatch = re.compile(r'[\u00BC-\u00BE\u2150-\u215E]')
# numbers (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
numberMatch = re.compile(r'(\d)')
# numbers and fractions (1⅓, 1 ⅓, etc.)
numberAndFractionMatch = re.compile(r'(\d{1,3}\s?[\u00BC-\u00BE\u2150-\u215E])')
# simple slash fractions (1/2, 1/3, 5/4, etc.)
slashFractionMatch = re.compile(r'(\d{1,3}\/\d{1,3})')
# vulgar slash which is it's own character in unicode.
# for example: 1⁄2, 4⁄3
vulgarSlashFractionMatch = re.compile(r'(\d{1,3}\u2044\d{1,3})')
# number with a vulgar slash in a fraction (1 1⁄2)
numberAndVulgarSlashFraction = re.compile(r'(\d{1,3}?\s\d\u2044\d{1,3})')
# any of the above, where the first character is not a word (to keep out "V8")
quantityMatch = re.compile(r'(?<!\w)((\d{1,3}?\s\d\/\d{1,3})|(\d{1,3}?\s?\d\u2044\d{1,3})|(\d{1,3}\u2044\d{1,3})|(\d{1,3}\s?[\u00BC-\u00BE\u2150-\u215E])|([\u00BC-\u00BE\u2150-\u215E])|(\d{1,3}\/?\d?)%?)')
# string between parantheses, for example: "this is not a match (but this is, including the parantheses)"
betweenParanthesesMatch = re.compile(r'\(([^\)]+)\)')

def isFullTypedFraction(text : str) -> bool:
    if text.find('/') >= 0 or text.find('\u2044') >= 0:
        return True
    else:
        return False

def toFloat(quantity : str) -> float:
    """ Parse a valid quantity string to a float """
    # We're using 'match', which searches only in the front of the string.
    # That way we know that if it's just a fraction (½) it can never be 1 ½, for example.
    # Then just logically look if it's anything else.
    if fractionMatch.match(quantity) is not None:
        return unicodedata.numeric(quantity)
    if slashFractionMatch.match(quantity) is not None:
        splitted = quantity.split('/')
        return int(splitted[0]) / int(splitted[1])
    if vulgarSlashFractionMatch.match(quantity) is not None:
        splitted = quantity.split('\u2044')
        return int(splitted[0]) / int(splitted[1])
    if numberAndFractionMatch.match(quantity) is not None:
        first = numberMatch.match(quantity).group()
        fraction = fractionMatch.search(quantity).group()
        return int(first) + toFloat(fraction)
    if numberAndSlashFraction.match(quantity) is not None:
        first = numberMatch.match(quantity).group()
        fraction = slashFractionMatch.search(quantity).group()
        return int(first) + toFloat(fraction)
    if numberAndVulgarSlashFraction.match(quantity) is not None:
        first = numberMatch.match(quantity).group()
        fraction = vulgarSlashFractionMatch.search(quantity).group()
        return int(first) + toFloat(fraction)
    if numberMatch.match(quantity) is not None:
        return int(quantity)

def average(quantities):
    """ In the case we have multiple numbers in an ingredient string
        '1 - 2 eggs', we can use this function to just average that out.
    """
    # if there is no quantity in the string, there is a good chance the string was
    # just "onion", in which case the quantity should be 1
    if quantities is None or len(quantities) == 0:
        return 1
    total = 0
    n = len(quantities)
    for q in quantities:
        total += toFloat(q.strip(' '))
    return total / n

def cleanhtml(raw_html):
    """ In some recipe websites, the ingredient can contain an HTML tag, mostly an anchor
        to link to some other recipe. Let's remove those.
    """
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext

def parse_ingredient(raw_ingredient : str) -> Ingredient:
    """ Tries to extract the quantity, the unit and the ingredient itself from a string """

    # We're doing a VERY simple parse. This could probably be better with some NLP
    # but we have nowhere near time enough for that during this assignment.

    ingredient = cleanhtml(raw_ingredient)
    quantity = 0
    unit = ''
    name = ''
    comment = ''

    # Recipe websites tend to put a comment between parantheses. 
    # for example: 1 (fresh) egg. Let's see if we can find any and extract it
    betweenMatch = betweenParanthesesMatch.search(ingredient)
    if betweenMatch is not None:
        betweenParentheses = betweenMatch.group()
        comment = comment + (', ' if len(comment) > 0 else '') + betweenParentheses
        ingredient = ingredient.replace(betweenParentheses, '')
        if ingredient[0] == ' ':
            ingredient = ingredient[1:]

    # Some recipe websites tend to put a comment in the end of the line
    # seperated by a comma. Let's see if we can find any and extract it
    # We do this here, pretty early, because there might be numbers in there
    # we don't want to take in account for quantities.
    commaSplitted = ingredient.split(',')
    if len(commaSplitted) > 1:
        comment = comment + ' ' + ', '.join(commaSplitted[1:])
        comment = comment.strip(' ')
        ingredient = commaSplitted[0]

    dashSplitted = ingredient.split(' - ')
    if len(dashSplitted) > 1:
        comment = comment + ' ' + ' - '.join(dashSplitted[1:])
        comment = comment.strip(' ')
        ingredient = dashSplitted[0]

    rest = ingredient

    last_quantity_character = 0

    # First, let's see if we can find any quantity in the forms of:
    # type                              -   example
    # a vulgar fraction                 -   ½ or \u00BC
    # a vulgar slash between numbers    -   1⁄2
    # a normal slash between numbers    -   1/2
    # a number                          -   1 or 2 etc.
    # a number and a vulgar fraction    -   1 ½ or 1½
    match = quantityMatch.findall(ingredient)
    if match is not None and len(match) > 0:
        # Take all found regex matches and take them from their groups into a flat array
        quantity_groups = list(map(lambda x: next(filter(lambda y: y != '', x)), match))

        # We don't want percentages, but we couldn't match them with regex.
        quantity_groups = [i for i in quantity_groups if '%' not in i]
        q_n = len(quantity_groups)
        
        # Find the last character index that matched a quantity
        last_quantity_character = ingredient.rfind(quantity_groups[q_n-1]) + len(quantity_groups[q_n-1])

        # If the last character happens to be in the end of the string...
        # Someone probably said 'see note 1' in the end of his ingredient.
        if last_quantity_character == len(ingredient) or last_quantity_character == len(ingredient) - 1:
            if q_n > 1:
                last_quantity_character = ingredient.rfind(quantity_groups[q_n-2]) + len(quantity_groups[q_n-2])
            else:
                last_quantity_character = 0
            quantity_groups.pop()
    
        quantity = average(quantity_groups)
    
    if last_quantity_character > 0:
        if ingredient[last_quantity_character] == ' ':
            last_quantity_character = last_quantity_character + 1
        rest = ingredient[last_quantity_character:]

    # Now split the rest of the string.
    splitted = rest.split(' ')

    # If the string is just one more word, it's probably safe to assume
    # that there is no unit string available, but we're dealing with, 
    # for example: 1 egg, where egg is both the ingredient and unit.
    if len(splitted) == 1:
        return [quantity, '', rest, comment, ingredient]
    
    # let's see if we can find something in the string that matches any
    # of my defined units. The list isn't finished and will probably miss
    # lot's of them. But by using a predefined list we avoid a situation where
    # "1 fresh egg" gives us a unit "fresh". Here the unit will be undefined 
    # and 'fresh egg' will be the ingredient. This should probably later be 
    # filtered again.
    wouldBeUnit = splitted[0]
    for key in units:
        value = units[key]
        if wouldBeUnit in value:
            unit = key
    
    # If we did have a unit, join the rest of the string
    # if we didn't, join the entire string
    if unit != '':
        name = ' '.join(splitted[1:])
    else:
        name = ' '.join(splitted)

    # and voila! The most basic ingredient parser ever.
    # as I said, I'm not too happy with it and NLP would probably
    # be a better fit, but this brings more complexity
    # return Ingredient(name.strip(' '), quantity, unit, comment, raw_ingredient)
    return [quantity, unit, name.strip(' '), comment, raw_ingredient]