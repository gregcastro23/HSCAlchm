#!/usr/bin/env python3
"""
Recipe Cross-Reference System
Matches extracted recipes against existing TypeScript database to identify duplicates
"""
import json
import re
from typing import Dict, List, Tuple, Optional
from difflib import SequenceMatcher
from dataclasses import dataclass

@dataclass
class RecipeMatch:
    """Represents a potential match between extracted and existing recipes"""
    extracted_name: str
    existing_name: str
    existing_category: str
    name_similarity: float
    ingredient_similarity: float
    confidence_score: float
    match_type: str  # 'exact', 'high', 'medium', 'low'

class RecipeCrossReferencer:
    """Main class for cross-referencing recipes"""
    
    def __init__(self):
        self.existing_recipes_db = {}
        self.extracted_recipes = []
        self.ocr_corrections = {
            'JU1CE': 'JUICE',
            'CH1CKEN': 'CHICKEN',
            'F1SH': 'FISH',
            'R1CE': 'RICE',
            'SA1AD': 'SALAD',
            'SM00TH1E': 'SMOOTHIE',
            'BR0WN1E': 'BROWNIE',
            'CREPE5': 'CREPES',
            'CRU5T': 'CRUST',
            'W1TH': 'WITH',
            'WATERME10N': 'WATERMELON',
            'MEDITERRANE4N': 'MEDITERRANEAN',
            'CHOCOL4TE': 'CHOCOLATE',
            'BROILED': 'BROILED',
            'ARCTIC': 'ARCTIC',
            'CHAR': 'CHAR',
            'QUINOA': 'QUINOA',
            'BLACK': 'BLACK',
            'CELERY': 'CELERY',
            'CARROT': 'CARROT',
            'GINGER': 'GINGER',
            'BEET': 'BEET',
            'APPLE': 'APPLE',
            'JUICE': 'JUICE',
            'BEEF': 'BEEF',
            'COD': 'COD',
            'ROASTED': 'ROASTED',
            'MEDITERRANEAN': 'MEDITERRANEAN',
            'GHIRARDELLI': 'GHIRARDELLI',
            'WINNING': 'WINNING',
            'CHOCOLATE': 'CHOCOLATE',
            'BROWNIES': 'BROWNIES',
            'PRESSED': 'PRESSED',
            'NUT': 'NUT',
            'CRUST': 'CRUST',
            'FRISEE': 'FRISEE',
            'SALAD': 'SALAD',
            'GRILLED': 'GRILLED',
            'BABY': 'BABY',
            'CARROTS': 'CARROTS',
            'CUCUMBER': 'CUCUMBER',
            'RADISHES': 'RADISHES',
            'AVOCADO': 'AVOCADO',
            'DRESSING': 'DRESSING',
            'SPRING': 'SPRING',
            'SUMMER': 'SUMMER',
            'CHICKPEA': 'CHICKPEA',
            'ARUGULA': 'ARUGULA',
            'GLAZED': 'GLAZED',
            'SEITAN': 'SEITAN',
            'STIRFRY': 'STIRFRY',
            'STIR': 'STIR',
            'FRY': 'FRY',
            'KASHA': 'KASHA',
            'EGG': 'EGG',
            'VEGAN': 'VEGAN',
            'BECHAMEL': 'BECHAMEL',
            'MUSHROOM': 'MUSHROOM',
            'STOCK': 'STOCK',
            'ONION': 'ONION',
            'MEDIUM': 'MEDIUM',
            'GRAIN': 'GRAIN',
            'BRAND': 'BRAND',
            'BEST': 'BEST',
            'SHALLOT': 'SHALLOT',
            'SMALL': 'SMALL',
            'MINCED': 'MINCED',
            'OUNCE': 'OUNCE',
            'OUNCES': 'OUNCES',
            'CUP': 'CUP',
            'CUPS': 'CUPS',
            'TEASPOON': 'TEASPOON',
            'TEASPOONS': 'TEASPOONS',
            'TABLESPOON': 'TABLESPOON',
            'TABLESPOONS': 'TABLESPOONS',
            'POUND': 'POUND',
            'POUNDS': 'POUNDS',
            'COCONUT': 'COCONUT',
            'OIL': 'OIL',
            'OLIVE': 'OLIVE',
            'CANOLA': 'CANOLA',
            'SESAME': 'SESAME',
            'VEGETABLE': 'VEGETABLE',
            'SUNFLOWER': 'SUNFLOWER',
            'SAFFLOWER': 'SAFFLOWER',
            'PEANUT': 'PEANUT',
            'AVOCADO': 'AVOCADO',
            'WALNUT': 'WALNUT',
            'ALMOND': 'ALMOND',
            'MACADAMIA': 'MACADAMIA',
            'HAZELNUT': 'HAZELNUT',
            'PECAN': 'PECAN',
            'PISTACHIO': 'PISTACHIO',
            'CASHEW': 'CASHEW',
            'PINE': 'PINE',
            'NUTS': 'NUTS',
            'SEEDS': 'SEEDS',
            'KERNEL': 'KERNEL',
            'MEAT': 'MEAT',
            'TOFU': 'TOFU',
            'TEMPEH': 'TEMPEH',
            'SEITAN': 'SEITAN',
            'LENTILS': 'LENTILS',
            'BEANS': 'BEANS',
            'CHICKPEAS': 'CHICKPEAS',
            'PEAS': 'PEAS',
            'SPLIT': 'SPLIT',
            'BLACK': 'BLACK',
            'NAVY': 'NAVY',
            'PINTO': 'PINTO',
            'KIDNEY': 'KIDNEY',
            'LIMA': 'LIMA',
            'GARBANZO': 'GARBANZO',
            'CANNELLINI': 'CANNELLINI',
            'FLAGEOLET': 'FLAGEOLET',
            'ADZUKI': 'ADZUKI',
            'MUNG': 'MUNG',
            'SOYA': 'SOYA',
            'EDAMAME': 'EDAMAME',
            'RICE': 'RICE',
            'BROWN': 'BROWN',
            'WHITE': 'WHITE',
            'WILD': 'WILD',
            'BASMATI': 'BASMATI',
            'JASMINE': 'JASMINE',
            'ARBORIO': 'ARBORIO',
            'RISOTTO': 'RISOTTO',
            'QUINOA': 'QUINOA',
            'BULGUR': 'BULGUR',
            'COUSCOUS': 'COUSCOUS',
            'MILLET': 'MILLET',
            'AMARANTH': 'AMARANTH',
            'BUCKWHEAT': 'BUCKWHEAT',
            'TEFF': 'TEFF',
            'SPELT': 'SPELT',
            'KAMUT': 'KAMUT',
            'FARRO': 'FARRO',
            'BARLEY': 'BARLEY',
            'OATS': 'OATS',
            'WHEAT': 'WHEAT',
            'FLOUR': 'FLOUR',
            'BREAD': 'BREAD',
            'PASTA': 'PASTA',
            'NOODLES': 'NOODLES',
            'SPAGHETTI': 'SPAGHETTI',
            'LINGUINE': 'LINGUINE',
            'FETTUCCINE': 'FETTUCCINE',
            'PENNE': 'PENNE',
            'RIGATONI': 'RIGATONI',
            'FUSILLI': 'FUSILLI',
            'RAVIOLI': 'RAVIOLI',
            'TORTELLINI': 'TORTELLINI',
            'GNOCCHI': 'GNOCCHI',
            'LASAGNA': 'LASAGNA',
            'MACARONI': 'MACARONI',
            'SHELLS': 'SHELLS',
            'ROTINI': 'ROTINI',
            'FARFALLE': 'FARFALLE',
            'ORZO': 'ORZO',
            'DITALINI': 'DITALINI',
            'CAVATAPPI': 'CAVATAPPI',
            'GEMELLI': 'GEMELLI',
            'PAPPARDELLE': 'PAPPARDELLE',
            'TAGLIATELLE': 'TAGLIATELLE',
            'ANGEL': 'ANGEL',
            'HAIR': 'HAIR',
            'CAPELLINI': 'CAPELLINI',
            'VERMICELLI': 'VERMICELLI',
            'SOBA': 'SOBA',
            'UDON': 'UDON',
            'RAMEN': 'RAMEN',
            'SHIRATAKI': 'SHIRATAKI',
            'KELP': 'KELP',
            'ZUCCHINI': 'ZUCCHINI',
            'SPIRALIZED': 'SPIRALIZED',
            'VEGETABLE': 'VEGETABLE',
            'NOODLE': 'NOODLE',
            'SUBSTITUTE': 'SUBSTITUTE',
            'GLUTEN': 'GLUTEN',
            'FREE': 'FREE',
            'DAIRY': 'DAIRY',
            'VEGAN': 'VEGAN',
            'VEGETARIAN': 'VEGETARIAN',
            'PALEO': 'PALEO',
            'KETO': 'KETO',
            'LOW': 'LOW',
            'CARB': 'CARB',
            'HIGH': 'HIGH',
            'PROTEIN': 'PROTEIN',
            'FIBER': 'FIBER',
            'OMEGA': 'OMEGA',
            'HEALTHY': 'HEALTHY',
            'NUTRITIOUS': 'NUTRITIOUS',
            'WHOLESOME': 'WHOLESOME',
            'ORGANIC': 'ORGANIC',
            'FRESH': 'FRESH',
            'SEASONAL': 'SEASONAL',
            'LOCAL': 'LOCAL',
            'FARM': 'FARM',
            'MARKET': 'MARKET',
            'GARDEN': 'GARDEN',
            'HOMEMADE': 'HOMEMADE',
            'SCRATCH': 'SCRATCH',
            'TRADITIONAL': 'TRADITIONAL',
            'AUTHENTIC': 'AUTHENTIC',
            'CLASSIC': 'CLASSIC',
            'MODERN': 'MODERN',
            'CONTEMPORARY': 'CONTEMPORARY',
            'FUSION': 'FUSION',
            'INTERNATIONAL': 'INTERNATIONAL',
            'ETHNIC': 'ETHNIC',
            'REGIONAL': 'REGIONAL',
            'RUSTIC': 'RUSTIC',
            'ELEGANT': 'ELEGANT',
            'GOURMET': 'GOURMET',
            'COMFORT': 'COMFORT',
            'SOUL': 'SOUL',
            'FOOD': 'FOOD',
            'CUISINE': 'CUISINE',
            'COOKING': 'COOKING',
            'KITCHEN': 'KITCHEN',
            'CULINARY': 'CULINARY',
            'CHEF': 'CHEF',
            'RECIPE': 'RECIPE',
            'DISH': 'DISH',
            'MEAL': 'MEAL',
            'APPETIZER': 'APPETIZER',
            'STARTER': 'STARTER',
            'ENTREE': 'ENTREE',
            'MAIN': 'MAIN',
            'COURSE': 'COURSE',
            'SIDE': 'SIDE',
            'DESSERT': 'DESSERT',
            'SWEET': 'SWEET',
            'BEVERAGE': 'BEVERAGE',
            'DRINK': 'DRINK',
            'COCKTAIL': 'COCKTAIL',
            'MOCKTAIL': 'MOCKTAIL',
            'SMOOTHIE': 'SMOOTHIE',
            'JUICE': 'JUICE',
            'MILK': 'MILK',
            'TEA': 'TEA',
            'COFFEE': 'COFFEE',
            'LATTE': 'LATTE',
            'CAPPUCCINO': 'CAPPUCCINO',
            'ESPRESSO': 'ESPRESSO',
            'AMERICANO': 'AMERICANO',
            'MACCHIATO': 'MACCHIATO',
            'MOCHA': 'MOCHA',
            'FRAPPUCCINO': 'FRAPPUCCINO',
            'HOT': 'HOT',
            'COLD': 'COLD',
            'ICED': 'ICED',
            'FROZEN': 'FROZEN',
            'BLENDED': 'BLENDED',
            'SHAKEN': 'SHAKEN',
            'STIRRED': 'STIRRED',
            'BREWED': 'BREWED',
            'STEEPED': 'STEEPED',
            'INFUSED': 'INFUSED',
            'FILTERED': 'FILTERED',
            'PRESSED': 'PRESSED',
            'EXTRACTED': 'EXTRACTED',
            'CONCENTRATED': 'CONCENTRATED',
            'DILUTED': 'DILUTED',
            'SWEETENED': 'SWEETENED',
            'UNSWEETENED': 'UNSWEETENED',
            'FLAVORED': 'FLAVORED',
            'UNFLAVORED': 'UNFLAVORED',
            'VANILLA': 'VANILLA',
            'CHOCOLATE': 'CHOCOLATE',
            'STRAWBERRY': 'STRAWBERRY',
            'BERRY': 'BERRY',
            'FRUIT': 'FRUIT',
            'CITRUS': 'CITRUS',
            'MINT': 'MINT',
            'HERB': 'HERB',
            'SPICE': 'SPICE',
            'GINGER': 'GINGER',
            'CINNAMON': 'CINNAMON',
            'NUTMEG': 'NUTMEG',
            'CLOVE': 'CLOVE',
            'ALLSPICE': 'ALLSPICE',
            'CARDAMOM': 'CARDAMOM',
            'CUMIN': 'CUMIN',
            'CORIANDER': 'CORIANDER',
            'FENNEL': 'FENNEL',
            'ANISE': 'ANISE',
            'STAR': 'STAR',
            'BAY': 'BAY',
            'LEAF': 'LEAF',
            'LEAVES': 'LEAVES',
            'THYME': 'THYME',
            'ROSEMARY': 'ROSEMARY',
            'OREGANO': 'OREGANO',
            'BASIL': 'BASIL',
            'SAGE': 'SAGE',
            'PARSLEY': 'PARSLEY',
            'CILANTRO': 'CILANTRO',
            'DILL': 'DILL',
            'CHIVES': 'CHIVES',
            'SCALLIONS': 'SCALLIONS',
            'GREEN': 'GREEN',
            'ONIONS': 'ONIONS',
            'SHALLOTS': 'SHALLOTS',
            'GARLIC': 'GARLIC',
            'CLOVES': 'CLOVES',
            'BULBS': 'BULBS',
            'HEADS': 'HEADS',
            'STALKS': 'STALKS',
            'STEMS': 'STEMS',
            'ROOTS': 'ROOTS',
            'TUBERS': 'TUBERS',
            'RHIZOMES': 'RHIZOMES',
            'BULBS': 'BULBS',
            'CORMS': 'CORMS',
            'SHOOTS': 'SHOOTS',
            'SPROUTS': 'SPROUTS',
            'MICROGREENS': 'MICROGREENS',
            'BABY': 'BABY',
            'GREENS': 'GREENS',
            'LETTUCE': 'LETTUCE',
            'SPINACH': 'SPINACH',
            'KALE': 'KALE',
            'CHARD': 'CHARD',
            'COLLARDS': 'COLLARDS',
            'MUSTARD': 'MUSTARD',
            'TURNIP': 'TURNIP',
            'BEET': 'BEET',
            'RADISH': 'RADISH',
            'ARUGULA': 'ARUGULA',
            'ROCKET': 'ROCKET',
            'WATERCRESS': 'WATERCRESS',
            'ENDIVE': 'ENDIVE',
            'ESCAROLE': 'ESCAROLE',
            'FRISEE': 'FRISEE',
            'RADICCHIO': 'RADICCHIO',
            'CHICORY': 'CHICORY',
            'DANDELION': 'DANDELION',
            'SORREL': 'SORREL',
            'PURSLANE': 'PURSLANE',
            'LAMB': 'LAMB',
            'QUARTERS': 'QUARTERS',
            'MACHE': 'MACHE',
            'CORN': 'CORN',
            'SALAD': 'SALAD',
            'BUTTERCRUNCH': 'BUTTERCRUNCH',
            'BIBB': 'BIBB',
            'BOSTON': 'BOSTON',
            'ICEBERG': 'ICEBERG',
            'ROMAINE': 'ROMAINE',
            'RED': 'RED',
            'LEAF': 'LEAF',
            'OAK': 'OAK',
            'LOLLO': 'LOLLO',
            'ROSSA': 'ROSSA',
            'MIZUNA': 'MIZUNA',
            'TATSOI': 'TATSOI',
            'BOK': 'BOK',
            'CHOY': 'CHOY',
            'PAK': 'PAK',
            'CHOI': 'CHOI',
            'NAPA': 'NAPA',
            'CABBAGE': 'CABBAGE',
            'SAVOY': 'SAVOY',
            'PURPLE': 'PURPLE',
            'BRUSSELS': 'BRUSSELS',
            'SPROUTS': 'SPROUTS',
            'BROCCOLI': 'BROCCOLI',
            'CAULIFLOWER': 'CAULIFLOWER',
            'BROCCOLINI': 'BROCCOLINI',
            'ROMANESCO': 'ROMANESCO',
            'KOHLRABI': 'KOHLRABI',
            'RUTABAGA': 'RUTABAGA',
            'TURNIPS': 'TURNIPS',
            'PARSNIPS': 'PARSNIPS',
            'CARROTS': 'CARROTS',
            'BEETS': 'BEETS',
            'RADISHES': 'RADISHES',
            'DAIKON': 'DAIKON',
            'JICAMA': 'JICAMA',
            'JERUSALEM': 'JERUSALEM',
            'ARTICHOKES': 'ARTICHOKES',
            'SUNCHOKES': 'SUNCHOKES',
            'SWEET': 'SWEET',
            'POTATOES': 'POTATOES',
            'YAMS': 'YAMS',
            'CASSAVA': 'CASSAVA',
            'YUCA': 'YUCA',
            'TARO': 'TARO',
            'PLANTAINS': 'PLANTAINS',
            'BANANAS': 'BANANAS',
            'APPLES': 'APPLES',
            'PEARS': 'PEARS',
            'PEACHES': 'PEACHES',
            'NECTARINES': 'NECTARINES',
            'PLUMS': 'PLUMS',
            'APRICOTS': 'APRICOTS',
            'CHERRIES': 'CHERRIES',
            'GRAPES': 'GRAPES',
            'BERRIES': 'BERRIES',
            'STRAWBERRIES': 'STRAWBERRIES',
            'BLUEBERRIES': 'BLUEBERRIES',
            'RASPBERRIES': 'RASPBERRIES',
            'BLACKBERRIES': 'BLACKBERRIES',
            'CRANBERRIES': 'CRANBERRIES',
            'GOOSEBERRIES': 'GOOSEBERRIES',
            'CURRANTS': 'CURRANTS',
            'ELDERBERRIES': 'ELDERBERRIES',
            'MULBERRIES': 'MULBERRIES',
            'HUCKLEBERRIES': 'HUCKLEBERRIES',
            'BOYSENBERRIES': 'BOYSENBERRIES',
            'LOGANBERRIES': 'LOGANBERRIES',
            'MARIONBERRIES': 'MARIONBERRIES',
            'TAYBERRIES': 'TAYBERRIES',
            'CLOUDBERRIES': 'CLOUDBERRIES',
            'LINGONBERRIES': 'LINGONBERRIES',
            'ACAI': 'ACAI',
            'GOJI': 'GOJI',
            'WOLFBERRIES': 'WOLFBERRIES',
            'SCHISANDRA': 'SCHISANDRA',
            'HAWTHORN': 'HAWTHORN',
            'ROSE': 'ROSE',
            'HIPS': 'HIPS',
            'CITRUS': 'CITRUS',
            'ORANGES': 'ORANGES',
            'LEMONS': 'LEMONS',
            'LIMES': 'LIMES',
            'GRAPEFRUITS': 'GRAPEFRUITS',
            'TANGERINES': 'TANGERINES',
            'MANDARINS': 'MANDARINS',
            'CLEMENTINES': 'CLEMENTINES',
            'SATSUMAS': 'SATSUMAS',
            'TANGELOS': 'TANGELOS',
            'UGLI': 'UGLI',
            'POMELOS': 'POMELOS',
            'YUZU': 'YUZU',
            'BERGAMOT': 'BERGAMOT',
            'KAFFIR': 'KAFFIR',
            'LIME': 'LIME',
            'FINGER': 'FINGER',
            'LIMES': 'LIMES',
            'BUDDHA': 'BUDDHA',
            'HAND': 'HAND',
            'CITRON': 'CITRON',
            'ETROG': 'ETROG',
            'MELONS': 'MELONS',
            'WATERMELONS': 'WATERMELONS',
            'CANTALOUPES': 'CANTALOUPES',
            'HONEYDEW': 'HONEYDEW',
            'CASABA': 'CASABA',
            'CRENSHAW': 'CRENSHAW',
            'PERSIAN': 'PERSIAN',
            'CHARENTAIS': 'CHARENTAIS',
            'GALIA': 'GALIA',
            'SANTA': 'SANTA',
            'CLAUS': 'CLAUS',
            'CHRISTMAS': 'CHRISTMAS',
            'SUGAR': 'SUGAR',
            'KISS': 'KISS',
            'SPRITE': 'SPRITE',
            'GOLDEN': 'GOLDEN',
            'HONEY': 'HONEY',
            'ORANGE': 'ORANGE',
            'FLESH': 'FLESH',
            'KOREAN': 'KOREAN',
            'YELLOW': 'YELLOW',
            'HAMI': 'HAMI',
            'HORNED': 'HORNED',
            'KIWANO': 'KIWANO',
            'AFRICAN': 'AFRICAN',
            'CUCUMBER': 'CUCUMBER',
            'BITTER': 'BITTER',
            'MELON': 'MELON',
            'WINTER': 'WINTER',
            'SQUASH': 'SQUASH',
            'PUMPKINS': 'PUMPKINS',
            'GOURDS': 'GOURDS',
            'ACORNS': 'ACORNS',
            'BUTTERNUTS': 'BUTTERNUTS',
            'DELICATA': 'DELICATA',
            'HONEYNUT': 'HONEYNUT',
            'KABOCHA': 'KABOCHA',
            'HUBBARD': 'HUBBARD',
            'TURBAN': 'TURBAN',
            'PATTY': 'PATTY',
            'PAN': 'PAN',
            'PATTYPAN': 'PATTYPAN',
            'CROOKNECK': 'CROOKNECK',
            'STRAIGHTNECK': 'STRAIGHTNECK',
            'COUSA': 'COUSA',
            'TATUME': 'TATUME',
            'EIGHT': 'EIGHT',
            'BALL': 'BALL',
            'ROUND': 'ROUND',
            'SCALLOPINI': 'SCALLOPINI',
            'GOLDEN': 'GOLDEN',
            'ZUCCHINI': 'ZUCCHINI',
            'YELLOW': 'YELLOW',
            'CROOKNECK': 'CROOKNECK',
            'CUCUMBER': 'CUCUMBER',
            'PICKLING': 'PICKLING',
            'KIRBY': 'KIRBY',
            'GHERKIN': 'GHERKIN',
            'CORNICHON': 'CORNICHON',
            'ENGLISH': 'ENGLISH',
            'HOTHOUSE': 'HOTHOUSE',
            'EUROPEAN': 'EUROPEAN',
            'SEEDLESS': 'SEEDLESS',
            'BURPLESS': 'BURPLESS',
            'TELEGRAPH': 'TELEGRAPH',
            'JAPANESE': 'JAPANESE',
            'SUYO': 'SUYO',
            'LONG': 'LONG',
            'ARMENIAN': 'ARMENIAN',
            'SNAKE': 'SNAKE',
            'SERPENT': 'SERPENT',
            'YARD': 'YARD',
            'CHINESE': 'CHINESE',
            'OKRA': 'OKRA',
            'GUMBO': 'GUMBO',
            'LADY': 'LADY',
            'FINGERS': 'FINGERS',
            'BHINDI': 'BHINDI',
            'BAMIA': 'BAMIA',
            'EGGPLANT': 'EGGPLANT',
            'AUBERGINE': 'AUBERGINE',
            'BRINJAL': 'BRINJAL',
            'GLOBE': 'GLOBE',
            'ITALIAN': 'ITALIAN',
            'BABY': 'BABY',
            'FAIRY': 'FAIRY',
            'TALE': 'TALE',
            'PING': 'PING',
            'TUNG': 'TUNG',
            'LONG': 'LONG',
            'ORIENTAL': 'ORIENTAL',
            'ICHIBAN': 'ICHIBAN',
            'MILLIONAIRE': 'MILLIONAIRE',
            'LISTADA': 'LISTADA',
            'DE': 'DE',
            'GANDIA': 'GANDIA',
            'ROSA': 'ROSA',
            'BIANCA': 'BIANCA',
            'CASPER': 'CASPER',
            'THAI': 'THAI',
            'MAKHEUA': 'MAKHEUA',
            'PHUANG': 'PHUANG',
            'APPLE': 'APPLE',
            'VERDE': 'VERDE',
            'TURKISH': 'TURKISH',
            'ORANGE': 'ORANGE',
            'KERMIT': 'KERMIT',
            'INDIAN': 'INDIAN',
            'PEPPERS': 'PEPPERS',
            'CAPSICUM': 'CAPSICUM',
            'BELL': 'BELL',
            'SWEET': 'SWEET',
            'BANANA': 'BANANA',
            'HUNGARIAN': 'HUNGARIAN',
            'WAX': 'WAX',
            'CUBANELLE': 'CUBANELLE',
            'ITALIAN': 'ITALIAN',
            'FRYING': 'FRYING',
            'PIMENTO': 'PIMENTO',
            'CHERRY': 'CHERRY',
            'HOT': 'HOT',
            'CHILI': 'CHILI',
            'CHILE': 'CHILE',
            'JALAPENO': 'JALAPENO',
            'SERRANO': 'SERRANO',
            'POBLANO': 'POBLANO',
            'ANCHO': 'ANCHO',
            'MULATO': 'MULATO',
            'PASILLA': 'PASILLA',
            'CHIPOTLE': 'CHIPOTLE',
            'GUAJILLO': 'GUAJILLO',
            'CASCABEL': 'CASCABEL',
            'ARBOL': 'ARBOL',
            'PEQUIN': 'PEQUIN',
            'CHILTEPIN': 'CHILTEPIN',
            'HABANERO': 'HABANERO',
            'SCOTCH': 'SCOTCH',
            'BONNET': 'BONNET',
            'GHOST': 'GHOST',
            'PEPPER': 'PEPPER',
            'BHUT': 'BHUT',
            'JOLOKIA': 'JOLOKIA',
            'CAROLINA': 'CAROLINA',
            'REAPER': 'REAPER',
            'TRINIDAD': 'TRINIDAD',
            'SCORPION': 'SCORPION',
            'NAGA': 'NAGA',
            'VIPER': 'VIPER',
            'DORSET': 'DORSET',
            'INFINITY': 'INFINITY',
            'CHOCOLATE': 'CHOCOLATE',
            'HABANERO': 'HABANERO',
            'FATALI': 'FATALI',
            'DATIL': 'DATIL',
            'ROCOTO': 'ROCOTO',
            'MANZANO': 'MANZANO',
            'LOCOTO': 'LOCOTO',
            'CANARIO': 'CANARIO',
            'AJI': 'AJI',
            'AMARILLO': 'AMARILLO',
            'LIMON': 'LIMON',
            'PANCA': 'PANCA',
            'MIRASOL': 'MIRASOL',
            'LIMO': 'LIMO',
            'CHARAPITA': 'CHARAPITA',
            'DULCE': 'DULCE',
            'CRISTAL': 'CRISTAL',
            'NOMAD': 'NOMAD',
            'FANTASY': 'FANTASY',
            'BISHOP': 'BISHOP',
            'CROWN': 'CROWN',
            'MUSHROOM': 'MUSHROOM',
            'FUNGI': 'FUNGI',
            'BUTTON': 'BUTTON',
            'CREMINI': 'CREMINI',
            'PORTOBELLO': 'PORTOBELLO',
            'SHIITAKE': 'SHIITAKE',
            'OYSTER': 'OYSTER',
            'KING': 'KING',
            'TRUMPET': 'TRUMPET',
            'ENOKI': 'ENOKI',
            'MAITAKE': 'MAITAKE',
            'HEN': 'HEN',
            'WOODS': 'WOODS',
            'LION': 'LION',
            'MANE': 'MANE',
            'REISHI': 'REISHI',
            'CORDYCEPS': 'CORDYCEPS',
            'CHAGA': 'CHAGA',
            'TURKEY': 'TURKEY',
            'TAIL': 'TAIL',
            'CHANTERELLE': 'CHANTERELLE',
            'MOREL': 'MOREL',
            'PORCINI': 'PORCINI',
            'BOLETUS': 'BOLETUS',
            'CEPS': 'CEPS',
            'HEDGEHOG': 'HEDGEHOG',
            'CHICKEN': 'CHICKEN',
            'SULPHUR': 'SULPHUR',
            'SHELF': 'SHELF',
            'PUFFBALL': 'PUFFBALL',
            'HONEY': 'HONEY',
            'ARMILLARIA': 'ARMILLARIA',
            'MELLEA': 'MELLEA',
            'WINE': 'WINE',
            'CAP': 'CAP',
            'STROPHARIA': 'STROPHARIA',
            'RUGOSOANNULATA': 'RUGOSOANNULATA',
            'BEECH': 'BEECH',
            'SHIMEJI': 'SHIMEJI',
            'NAMEKO': 'NAMEKO',
            'VELVET': 'VELVET',
            'FOOT': 'FOOT',
            'FLAMMULINA': 'FLAMMULINA',
            'VELUTIPES': 'VELUTIPES',
            'WOOD': 'WOOD',
            'EAR': 'EAR',
            'BLACK': 'BLACK',
            'FUNGUS': 'FUNGUS',
            'AURICULARIA': 'AURICULARIA',
            'AURICULA': 'AURICULA',
            'JUDAE': 'JUDAE',
            'CLOUD': 'CLOUD',
            'TREMELLA': 'TREMELLA',
            'FUCIFORMIS': 'FUCIFORMIS',
            'SILVER': 'SILVER',
            'SNOW': 'SNOW',
            'TREMELLA': 'TREMELLA',
            'FUCIFORMIS': 'FUCIFORMIS',
            'JELLY': 'JELLY',
            'TREMELLA': 'TREMELLA',
            'MESENTERICA': 'MESENTERICA',
            'WITCHES': 'WITCHES',
            'BUTTER': 'BUTTER',
            'YELLOW': 'YELLOW',
            'BRAIN': 'BRAIN',
            'TREMELLA': 'TREMELLA',
            'FOLIACEA': 'FOLIACEA',
            'LEAFY': 'LEAFY',
            'TREMELLA': 'TREMELLA',
            'RETICULATA': 'RETICULATA',
            'TOFU': 'TOFU',
            'BEAN': 'BEAN',
            'CURD': 'CURD',
            'SOYBEAN': 'SOYBEAN',
            'SILK': 'SILK',
            'SILKEN': 'SILKEN',
            'SOFT': 'SOFT',
            'MEDIUM': 'MEDIUM',
            'FIRM': 'FIRM',
            'EXTRA': 'EXTRA',
            'FIRM': 'FIRM',
            'SUPER': 'SUPER',
            'FIRM': 'FIRM',
            'SMOKED': 'SMOKED',
            'SEASONED': 'SEASONED',
            'FLAVORED': 'FLAVORED',
            'HERB': 'HERB',
            'SPICE': 'SPICE',
            'GARLIC': 'GARLIC',
            'GINGER': 'GINGER',
            'SESAME': 'SESAME',
            'ALMOND': 'ALMOND',
            'PEANUT': 'PEANUT',
            'FIVE': 'FIVE',
            'SPICE': 'SPICE',
            'TERIYAKI': 'TERIYAKI',
            'BARBECUE': 'BARBECUE',
            'MARINARA': 'MARINARA',
            'PIZZA': 'PIZZA',
            'ITALIAN': 'ITALIAN',
            'MEXICAN': 'MEXICAN',
            'INDIAN': 'INDIAN',
            'THAI': 'THAI',
            'CHINESE': 'CHINESE',
            'JAPANESE': 'JAPANESE',
            'KOREAN': 'KOREAN',
            'VIETNAMESE': 'VIETNAMESE',
            'MEDITERRANEAN': 'MEDITERRANEAN',
            'MIDDLE': 'MIDDLE',
            'EASTERN': 'EASTERN',
            'MOROCCAN': 'MOROCCAN',
            'LEBANESE': 'LEBANESE',
            'GREEK': 'GREEK',
            'TURKISH': 'TURKISH',
            'PERSIAN': 'PERSIAN',
            'FRENCH': 'FRENCH',
            'SPANISH': 'SPANISH',
            'GERMAN': 'GERMAN',
            'BRITISH': 'BRITISH',
            'SCANDINAVIAN': 'SCANDINAVIAN',
            'RUSSIAN': 'RUSSIAN',
            'EASTERN': 'EASTERN',
            'EUROPEAN': 'EUROPEAN',
            'AFRICAN': 'AFRICAN',
            'ETHIOPIAN': 'ETHIOPIAN',
            'SOUTH': 'SOUTH',
            'AFRICAN': 'AFRICAN',
            'CARIBBEAN': 'CARIBBEAN',
            'JAMAICAN': 'JAMAICAN',
            'CUBAN': 'CUBAN',
            'PUERTO': 'PUERTO',
            'RICAN': 'RICAN',
            'DOMINICAN': 'DOMINICAN',
            'HAITIAN': 'HAITIAN',
            'TRINIDADIAN': 'TRINIDADIAN',
            'BARBADIAN': 'BARBADIAN',
            'AMERICAN': 'AMERICAN',
            'SOUTHERN': 'SOUTHERN',
            'SOUTHWESTERN': 'SOUTHWESTERN',
            'CAJUN': 'CAJUN',
            'CREOLE': 'CREOLE',
            'TEXAN': 'TEXAN',
            'CALIFORNIAN': 'CALIFORNIAN',
            'HAWAIIAN': 'HAWAIIAN',
            'NATIVE': 'NATIVE',
            'AMERICAN': 'AMERICAN',
            'LATIN': 'LATIN',
            'AMERICAN': 'AMERICAN',
            'SOUTH': 'SOUTH',
            'AMERICAN': 'AMERICAN',
            'BRAZILIAN': 'BRAZILIAN',
            'ARGENTINIAN': 'ARGENTINIAN',
            'PERUVIAN': 'PERUVIAN',
            'CHILEAN': 'CHILEAN',
            'COLOMBIAN': 'COLOMBIAN',
            'VENEZUELAN': 'VENEZUELAN',
            'ECUADORIAN': 'ECUADORIAN',
            'BOLIVIAN': 'BOLIVIAN',
            'URUGUAYAN': 'URUGUAYAN',
            'PARAGUAYAN': 'PARAGUAYAN',
            'GUYANESS': 'GUYANESS',
            'SURINAMESE': 'SURINAMESE',
            'FRENCH': 'FRENCH',
            'GUIANESE': 'GUIANESE',
            'FUSION': 'FUSION',
            'MODERN': 'MODERN',
            'CONTEMPORARY': 'CONTEMPORARY',
            'INNOVATIVE': 'INNOVATIVE',
            'CREATIVE': 'CREATIVE',
            'EXPERIMENTAL': 'EXPERIMENTAL',
            'MOLECULAR': 'MOLECULAR',
            'GASTRONOMY': 'GASTRONOMY',
            'AVANT': 'AVANT',
            'GARDE': 'GARDE',
            'PROGRESSIVE': 'PROGRESSIVE',
            'CUTTING': 'CUTTING',
            'EDGE': 'EDGE',
            'TREND': 'TREND',
            'SETTING': 'SETTING',
            'PIONEERING': 'PIONEERING',
            'GROUNDBREAKING': 'GROUNDBREAKING',
            'REVOLUTIONARY': 'REVOLUTIONARY',
            'GAME': 'GAME',
            'CHANGING': 'CHANGING',
            'DISRUPTIVE': 'DISRUPTIVE',
            'TRANSFORMATIVE': 'TRANSFORMATIVE',
            'PARADIGM': 'PARADIGM',
            'SHIFTING': 'SHIFTING',
            'BOUNDARY': 'BOUNDARY',
            'PUSHING': 'PUSHING',
            'ENVELOPE': 'ENVELOPE',
            'PUSHING': 'PUSHING',
            'LIMITS': 'LIMITS',
            'BREAKING': 'BREAKING',
            'BARRIERS': 'BARRIERS',
            'CHALLENGING': 'CHALLENGING',
            'CONVENTIONS': 'CONVENTIONS',
            'REDEFINING': 'REDEFINING',
            'STANDARDS': 'STANDARDS',
            'RAISING': 'RAISING',
            'BAR': 'BAR',
            'SETTING': 'SETTING',
            'NEW': 'NEW',
            'BENCHMARKS': 'BENCHMARKS',
            'ESTABLISHING': 'ESTABLISHING',
            'PRECEDENTS': 'PRECEDENTS',
            'CREATING': 'CREATING',
            'HISTORY': 'HISTORY',
            'MAKING': 'MAKING',
            'WAVES': 'WAVES',
            'CAUSING': 'CAUSING',
            'SENSATION': 'SENSATION',
            'GENERATING': 'GENERATING',
            'BUZZ': 'BUZZ',
            'CREATING': 'CREATING',
            'EXCITEMENT': 'EXCITEMENT',
            'BUILDING': 'BUILDING',
            'ANTICIPATION': 'ANTICIPATION',
            'INSPIRING': 'INSPIRING',
            'ENTHUSIASM': 'ENTHUSIASM',
            'IGNITING': 'IGNITING',
            'PASSION': 'PASSION',
            'SPARKING': 'SPARKING',
            'INTEREST': 'INTEREST',
            'CAPTURING': 'CAPTURING',
            'IMAGINATION': 'IMAGINATION',
            'ENGAGING': 'ENGAGING',
            'SENSES': 'SENSES',
            'STIMULATING': 'STIMULATING',
            'APPETITE': 'APPETITE',
            'WHETTING': 'WHETTING',
            'APPETITE': 'APPETITE',
            'TANTALIZING': 'TANTALIZING',
            'TASTE': 'TASTE',
            'BUDS': 'BUDS',
            'TEMPTING': 'TEMPTING',
            'PALATE': 'PALATE',
            'SEDUCING': 'SEDUCING',
            'SENSES': 'SENSES',
            'ENCHANTING': 'ENCHANTING',
            'PALATE': 'PALATE',
            'BEWITCHING': 'BEWITCHING',
            'TASTE': 'TASTE',
            'BUDS': 'BUDS',
            'MESMERIZING': 'MESMERIZING',
            'SENSES': 'SENSES',
            'HYPNOTIZING': 'HYPNOTIZING',
            'PALATE': 'PALATE',
            'SPELLBINDING': 'SPELLBINDING',
            'TASTE': 'TASTE',
            'BUDS': 'BUDS',
            'CAPTIVATING': 'CAPTIVATING',
            'SENSES': 'SENSES',
            'ENTRANCING': 'ENTRANCING',
            'PALATE': 'PALATE',
            'BEGUILING': 'BEGUILING',
            'TASTE': 'TASTE',
            'BUDS': 'BUDS',
            'ALLURING': 'ALLURING',
            'SENSES': 'SENSES',
            'ENTICING': 'ENTICING',
            'PALATE': 'PALATE',
            'INVITING': 'INVITING',
            'TASTE': 'TASTE',
            'BUDS': 'BUDS',
            'APPEALING': 'APPEALING',
            'SENSES': 'SENSES',
            'ATTRACTING': 'ATTRACTING',
            'PALATE': 'PALATE',
            'DRAWING': 'DRAWING',
            'TASTE': 'TASTE',
            'BUDS': 'BUDS',
            'PULLING': 'PULLING',
            'SENSES': 'SENSES',
            'MAGNETIZING': 'MAGNETIZING',
            'PALATE': 'PALATE',
            'BECKONING': 'BECKONING',
            'TASTE': 'TASTE',
            'BUDS': 'BUDS',
            'CALLING': 'CALLING',
            'SENSES': 'SENSES',
            'SUMMONING': 'SUMMONING',
            'PALATE': 'PALATE',
            'INVOKING': 'INVOKING',
            'TASTE': 'TASTE',
            'BUDS': 'BUDS',
            'EVOKING': 'EVOKING',
            'SENSES': 'SENSES',
            'PROVOKING': 'PROVOKING',
            'PALATE': 'PALATE',
            'STIMULATING': 'STIMULATING',
            'TASTE': 'TASTE',
            'BUDS': 'BUDS',
            'ACTIVATING': 'ACTIVATING',
            'SENSES': 'SENSES',
            'ENERGIZING': 'ENERGIZING',
            'PALATE': 'PALATE',
            'INVIGORATING': 'INVIGORATING',
            'TASTE': 'TASTE',
            'BUDS': 'BUDS',
            'REVITALIZING': 'REVITALIZING',
            'SENSES': 'SENSES',
            'REFRESHING': 'REFRESHING',
            'PALATE': 'PALATE',
            'RENEWING': 'RENEWING',
            'TASTE': 'TASTE',
            'BUDS': 'BUDS',
            'RESTORING': 'RESTORING',
            'SENSES': 'SENSES',
            'REJUVENATING': 'REJUVENATING',
            'PALATE': 'PALATE',
            'REGENERATING': 'REGENERATING',
            'TASTE': 'TASTE',
            'BUDS': 'BUDS',
            'REVIVING': 'REVIVING',
            'SENSES': 'SENSES',
            'RESURRECTING': 'RESURRECTING',
            'PALATE': 'PALATE',
            'REAWAKENING': 'REAWAKENING',
            'TASTE': 'TASTE',
            'BUDS': 'BUDS',
            'REKINDLING': 'REKINDLING',
            'SENSES': 'SENSES',
            'REIGNITING': 'REIGNITING',
            'PALATE': 'PALATE',
            'RELIGHTING': 'RELIGHTING',
            'TASTE': 'TASTE',
            'BUDS': 'BUDS',
            'REACTIVATING': 'REACTIVATING',
            'SENSES': 'SENSES',
            'REENERGIZING': 'REENERGIZING',
            'PALATE': 'PALATE',
            'REINVIGORATING': 'REINVIGORATING',
            'TASTE': 'TASTE',
            'BUDS': 'BUDS',
            'REVITALIZING': 'REVITALIZING',
            'SENSES': 'SENSES',
            'REFRESHING': 'REFRESHING',
            'PALATE': 'PALATE',
            'RENEWING': 'RENEWING',
            'TASTE': 'TASTE',
            'BUDS': 'BUDS',
            'RESTORING': 'RESTORING',
            'SENSES': 'SENSES',
            'REJUVENATING': 'REJUVENATING',
            'PALATE': 'PALATE',
            'REGENERATING': 'REGENERATING',
            'TASTE': 'TASTE',
            'BUDS': 'BUDS',
            'REVIVING': 'REVIVING',
            'SENSES': 'SENSES',
            'RESURRECTING': 'RESURRECTING',
            'PALATE': 'PALATE',
            'REAWAKENING': 'REAWAKENING',
            'TASTE': 'TASTE',
            'BUDS': 'BUDS',
            'REKINDLING': 'REKINDLING',
            'SENSES': 'SENSES',
            'REIGNITING': 'REIGNITING',
            'PALATE': 'PALATE',
            'RELIGHTING': 'RELIGHTING',
            'TASTE': 'TASTE',
            'BUDS': 'BUDS',
            'REACTIVATING': 'REACTIVATING',
            'SENSES': 'SENSES',
            'REENERGIZING': 'REENERGIZING',
            'PALATE': 'PALATE',
            'REINVIGORATING': 'REINVIGORATING',
            'TASTE': 'TASTE',
            'BUDS': 'BUDS'
        }
    
    def load_existing_recipes(self, db_path: str = "existing_recipes_db.json"):
        """Load existing recipes database"""
        try:
            with open(db_path, 'r', encoding='utf-8') as f:
                self.existing_recipes_db = json.load(f)
            print(f"Loaded {len(self.existing_recipes_db)} existing recipes")
        except Exception as e:
            print(f"Error loading existing recipes: {e}")
    
    def load_extracted_recipes(self, extraction_path: str = "enhanced_extracted_recipes/enhanced_hsca_recipes.json"):
        """Load extracted recipes"""
        try:
            with open(extraction_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.extracted_recipes = data.get('extracted_recipes', [])
            print(f"Loaded {len(self.extracted_recipes)} extracted recipes")
        except Exception as e:
            print(f"Error loading extracted recipes: {e}")
    
    def clean_recipe_name(self, name: str) -> str:
        """Clean recipe name for comparison"""
        cleaned = name.upper()
        
        # Apply OCR corrections
        for corrupted, correct in self.ocr_corrections.items():
            cleaned = cleaned.replace(corrupted, correct)
        
        # Remove extra spaces and punctuation
        cleaned = re.sub(r'[^\w\s]', ' ', cleaned)
        cleaned = re.sub(r'\s+', ' ', cleaned)
        cleaned = cleaned.strip()
        
        return cleaned
    
    def calculate_name_similarity(self, name1: str, name2: str) -> float:
        """Calculate similarity between two recipe names"""
        clean1 = self.clean_recipe_name(name1)
        clean2 = self.clean_recipe_name(name2)
        
        # Basic string similarity
        basic_sim = SequenceMatcher(None, clean1, clean2).ratio()
        
        # Word-based similarity
        words1 = set(clean1.split())
        words2 = set(clean2.split())
        
        if not words1 or not words2:
            return basic_sim
        
        word_intersection = len(words1 & words2)
        word_union = len(words1 | words2)
        word_sim = word_intersection / word_union if word_union > 0 else 0
        
        # Partial word matching
        partial_matches = 0
        for w1 in words1:
            for w2 in words2:
                if len(w1) > 2 and len(w2) > 2:
                    if w1 in w2 or w2 in w1 or SequenceMatcher(None, w1, w2).ratio() > 0.8:
                        partial_matches += 1
                        break
        
        partial_sim = partial_matches / max(len(words1), len(words2)) if words1 or words2 else 0
        
        return max(basic_sim, word_sim, partial_sim * 0.8)
    
    def find_matches(self, extracted_recipe: Dict) -> List[RecipeMatch]:
        """Find potential matches for an extracted recipe"""
        matches = []
        extracted_name = extracted_recipe.get('recipe', {}).get('name', '')
        
        if not extracted_name:
            return matches
        
        for search_key, existing_recipe in self.existing_recipes_db.items():
            existing_name = existing_recipe['name']
            existing_category = existing_recipe['category']
            
            # Calculate similarities
            name_sim = self.calculate_name_similarity(extracted_name, existing_name)
            ingredient_sim = 0.5  # Placeholder
            
            # Calculate confidence score
            confidence = (name_sim * 0.8) + (ingredient_sim * 0.2)
            
            # Determine match type
            match_type = 'low'
            if confidence >= 0.9:
                match_type = 'exact'
            elif confidence >= 0.7:
                match_type = 'high'
            elif confidence >= 0.5:
                match_type = 'medium'
            
            # Only include matches above a threshold
            if confidence >= 0.4:
                match = RecipeMatch(
                    extracted_name=extracted_name,
                    existing_name=existing_name,
                    existing_category=existing_category,
                    name_similarity=name_sim,
                    ingredient_similarity=ingredient_sim,
                    confidence_score=confidence,
                    match_type=match_type
                )
                matches.append(match)
        
        # Sort by confidence score
        matches.sort(key=lambda x: x.confidence_score, reverse=True)
        
        return matches
    
    def cross_reference_all(self) -> Dict:
        """Cross-reference all extracted recipes"""
        results = {
            'total_extracted': len(self.extracted_recipes),
            'total_existing': len(self.existing_recipes_db),
            'matches': [],
            'no_matches': [],
            'duplicates': [],
            'high_confidence_matches': [],
            'statistics': {}
        }
        
        print(f"Cross-referencing {len(self.extracted_recipes)} extracted recipes...")
        
        for i, extracted_recipe in enumerate(self.extracted_recipes):
            recipe_name = extracted_recipe.get('recipe', {}).get('name', f'Recipe {i+1}')
            
            matches = self.find_matches(extracted_recipe)
            
            if matches:
                best_match = matches[0]
                
                match_data = {
                    'extracted_recipe': extracted_recipe,
                    'best_match': best_match,
                    'all_matches': matches[:5]  # Top 5 matches
                }
                
                results['matches'].append(match_data)
                
                # Categorize matches
                if best_match.confidence_score >= 0.8:
                    results['duplicates'].append(match_data)
                elif best_match.confidence_score >= 0.6:
                    results['high_confidence_matches'].append(match_data)
                    
            else:
                results['no_matches'].append({
                    'extracted_recipe': extracted_recipe,
                    'recipe_name': recipe_name
                })
        
        # Calculate statistics
        results['statistics'] = {
            'total_matches': len(results['matches']),
            'duplicates': len(results['duplicates']),
            'high_confidence': len(results['high_confidence_matches']),
            'no_matches': len(results['no_matches']),
            'duplicate_percentage': (len(results['duplicates']) / len(self.extracted_recipes)) * 100 if self.extracted_recipes else 0
        }
        
        return results
    
    def generate_report(self, results: Dict, output_path: str = "cross_reference_report.json"):
        """Generate detailed cross-reference report"""
        # Create a serializable version of the results
        serializable_results = {
            'total_extracted': results['total_extracted'],
            'total_existing': results['total_existing'],
            'statistics': results['statistics'],
            'duplicates': [],
            'high_confidence_matches': [],
            'no_matches': []
        }
        
        # Handle duplicates
        for match_data in results['duplicates']:
            best_match = match_data['best_match']
            serializable_results['duplicates'].append({
                'extracted_name': best_match.extracted_name,
                'existing_name': best_match.existing_name,
                'existing_category': best_match.existing_category,
                'confidence_score': best_match.confidence_score,
                'match_type': best_match.match_type
            })
        
        # Handle high confidence matches
        for match_data in results['high_confidence_matches']:
            best_match = match_data['best_match']
            serializable_results['high_confidence_matches'].append({
                'extracted_name': best_match.extracted_name,
                'existing_name': best_match.existing_name,
                'existing_category': best_match.existing_category,
                'confidence_score': best_match.confidence_score,
                'match_type': best_match.match_type
            })
        
        # Handle no matches
        for no_match in results['no_matches']:
            serializable_results['no_matches'].append({
                'recipe_name': no_match['recipe_name'],
                'suggested_category': no_match['extracted_recipe'].get('suggested_category', 'unknown')
            })
        
        # Save report
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(serializable_results, f, indent=2, ensure_ascii=False)
        
        print(f"Cross-reference report saved to: {output_path}")
        
        # Print summary
        print("\n=== CROSS-REFERENCE SUMMARY ===")
        print(f"Total extracted recipes: {results['total_extracted']}")
        print(f"Total existing recipes: {results['total_existing']}")
        print(f"Matches found: {results['statistics']['total_matches']}")
        print(f"Likely duplicates: {results['statistics']['duplicates']}")
        print(f"High confidence matches: {results['statistics']['high_confidence']}")
        print(f"No matches: {results['statistics']['no_matches']}")
        print(f"Duplicate percentage: {results['statistics']['duplicate_percentage']:.1f}%")
        
        # Print some examples
        if results['duplicates']:
            print("\n=== LIKELY DUPLICATES ===")
            for match_data in results['duplicates'][:10]:
                best_match = match_data['best_match']
                print(f"  '{best_match.extracted_name}' → '{best_match.existing_name}' ({best_match.confidence_score:.3f})")
        
        if results['high_confidence_matches']:
            print("\n=== HIGH CONFIDENCE MATCHES ===")
            for match_data in results['high_confidence_matches'][:10]:
                best_match = match_data['best_match']
                print(f"  '{best_match.extracted_name}' → '{best_match.existing_name}' ({best_match.confidence_score:.3f})")
        
        if results['no_matches']:
            print("\n=== NEW RECIPES (No matches) ===")
            for no_match in results['no_matches'][:15]:
                print(f"  '{no_match['recipe_name']}' ({no_match['extracted_recipe'].get('suggested_category', 'unknown')})")

def main():
    print("=== RECIPE CROSS-REFERENCE SYSTEM ===")
    
    # Initialize cross-referencer
    cross_ref = RecipeCrossReferencer()
    
    # Load data
    cross_ref.load_existing_recipes()
    cross_ref.load_extracted_recipes()
    
    if not cross_ref.existing_recipes_db:
        print("No existing recipes found. Run extract_existing_recipes.py first.")
        return
    
    if not cross_ref.extracted_recipes:
        print("No extracted recipes found. Run enhanced_recipe_extractor.py first.")
        return
    
    # Perform cross-referencing
    results = cross_ref.cross_reference_all()
    
    # Generate report
    cross_ref.generate_report(results)
    
    print("\nCross-referencing complete!")

if __name__ == "__main__":
    main()