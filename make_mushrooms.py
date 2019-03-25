import numpy as np
import pandas as pd

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/mushroom/agaricus-lepiota.data'
codes = {
    'edible': {'e': 'edible',
               'p': 'poisonous'},

     'cap_shape': {'b': 'bell',
               'c': 'conical',
               'x': 'convex',
               'f': 'flat',
               'k': 'knobbed',
               's': 'sunken'},

    'cap_surface': {'f':
                    'fibrous',
                    'g': 'grooves',
                    'y': 'scaly',
                    's': 'smooth'},

    'cap_color': {'n': 'brown',
        'b': 'buff',
        'c': 'cinnamon',
        'g': 'gray',
        'r': 'green',
        'p': 'pink',
        'u': 'purple',
        'e': 'red',
        'w': 'white',
        'y': 'yellow'},

    'bruises': {'t': 'bruises',
                'f': 'no'},
    'odor': {'a': 'almond',
        'l': 'anise',
        'c': 'creosote',
        'y': 'fishy',
        'f': 'foul',
        'm': 'musty',
        'n': 'none',
        'p': 'pungent',
        's': 'spicy'},

    'gill_attachment': {'a': 'attached', 'd': 'descending', 'f': 'free', 'n':
            'notched'},
    'gill_spacing': {'c': 'close', 'w': 'crowded', 'd': 'distant'},

    'gill_size': {'b': 'broad', 'n': 'narrow'},

    'gill_color': {'k': 'black',
        'n': 'brown',
        'b': 'buff',
        'h': 'chocolate',
        'g': 'gray',
        'r': 'green',
        'o': 'orange',
        'p': 'pink',
        'u': 'purple',
        'e': 'red',
        'w': 'white',
        'y': 'yellow'},

    'stalk_shape': {'e': 'enlarging',
            't': 'tapering'},

    'stalk_root': {'b': 'bulbous',
            'c': 'club',
            'u': 'cup',
            'e': 'equal',
            'z': 'rhizomorphs',
            'r': 'rooted',
            '?': np.NaN},

    'stalk_surface_above_ring': {'f': 'fibrous',
            'y': 'scaly',
            'k': 'silky',
            's': 'smooth'},

    'stalk_surface_below_ring':{'f': 'fibrous',
            'y': 'scaly',
            'k': 'silky',
            's': 'smooth'},

    'stalk_color_above_ring': {'n': 'brown',
            'b': 'buff',
            'c': 'cinnamon',
            'g': 'gray',
            'o': 'orange',
            'p': 'pink',
            'e': 'red',
            'w': 'white', 'y': 'yellow'},

    'stalk_color_below_ring': {'n': 'brown',
            'b': 'buff',
            'c': 'cinnamon',
            'g': 'gray',
            'o': 'orange',
            'p': 'pink',
            'e': 'red',
            'w': 'white',
            'y': 'yellow'},

    'veil_type': {'p': 'partial',
                  'u': 'universal'},

    'veil_color': {'n': 'brown',
                   'o': 'orange',
                   'w': 'white',
                   'y': 'yellow'},

    'ring_number': {'n': 'none',
            'o': 'one',
            't': 'two'},

    'ring_type': {'c': 'cobwebby',
            'e': 'evanescent',
            'f': 'flaring',
            'l': 'large',
            'n': 'none',
            'p': 'pendant',
            's': 'sheathing',
            'z': 'zone'},

    'spore_print_color': {'k': 'black',
            'n': 'brown',
            'b': 'buff',
            'h': 'chocolate',
            'r': 'green',
            'o': 'orange',
            'u': 'purple',
            'w': 'white',
            'y': 'yellow'},

    'population': {'a': 'abundant',
            'c': 'clustered',
            'n': 'numerous',
            's': 'scattered',
            'v': 'several',
            'y': 'solitary'},

    'habitat': {'g': 'grasses',
            'l': 'leaves',
            'm': 'meadows',
            'p': 'paths',
            'u': 'urban',
            'w': 'waste',
            'd': 'woods'},
}

df = pd.read_csv(url, header=None, index_col=False)
df.columns = codes.keys()
for column in df.columns:
    df[column] = df[column].map(codes[column])
