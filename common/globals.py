'''
Created on Oct 8, 2019

@author: maor
'''
import pandas as pd
ONE_SET = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

''' taken from https://www.blackjackapprenticeship.com/blackjack-strategy-charts/
made small modifications like double on 5,5 when we should double on 10
'''
STANDARD_LOGIC = pd.DataFrame(
    {'2': {'5': 'H', '6': 'H', '7': 'H', '8': 'H', '9': 'H', '10': 'D', '11': 'D',
           '12': 'H', '13': 'S', '14': 'S', '15': 'S', '16': 'S', '17': 'S',
           '18': 'S', '19': 'S', '20': 'S', '21': 'S',
           'A,2': 'H', 'A,3': 'H', 'A,4': 'H', 'A,5': 'H', 'A,6': 'H',
           'A,7': 'D', 'A,8': 'S', 'A,9': 'S', 'A,10': 'S',
           'A,A': 'Y', '2,2': 'Y', '3,3': 'Y', '4,4': 'H', '5,5': 'D',
           '6,6': 'Y', '7,7': 'Y', '8,8': 'Y', '9,9': 'S', '10,10': 'S',
           },
     '3': {'5': 'H', '6': 'H', '7': 'H', '8': 'H', '9': 'H', '10': 'D', '11': 'D',
           '12': 'H', '13': 'S', '14': 'S', '15': 'S', '16': 'S', '17': 'S',
           '18': 'S', '19': 'S', '20': 'S', '21': 'S',
           'A,2': 'H', 'A,3': 'H', 'A,4': 'H', 'A,5': 'H', 'A,6': 'D',
           'A,7': 'D', 'A,8': 'S', 'A,9': 'S', 'A,10': 'S',
           'A,A': 'Y', '2,2': 'Y', '3,3': 'Y', '4,4': 'H', '5,5': 'D',
           '6,6': 'Y', '7,7': 'Y', '8,8': 'Y', '9,9': 'S', '10,10': 'S',
           },

     '4': {'5': 'H', '6': 'H', '7': 'H', '8': 'H', '9': 'D', '10': 'D', '11': 'D',
           '12': 'S', '13': 'S', '14': 'S', '15': 'S', '16': 'S', '17': 'S',
           '18': 'S', '19': 'S', '20': 'S', '21': 'S',
           'A,2': 'H', 'A,3': 'H', 'A,4': 'D', 'A,5': 'D', 'A,6': 'D',
           'A,7': 'D', 'A,8': 'S', 'A,9': 'S', 'A,10': 'S',
           'A,A': 'Y', '2,2': 'Y', '3,3': 'Y', '4,4': 'H', '5,5': 'D',
           '6,6': 'Y', '7,7': 'Y', '8,8': 'Y', '9,9': 'S', '10,10': 'S',
           },

     '5': {'5': 'H', '6': 'H', '7': 'H', '8': 'H', '9': 'D', '10': 'D', '11': 'D',
           '12': 'S', '13': 'S', '14': 'S', '15': 'S', '16': 'S', '17': 'S',
           '18': 'S', '19': 'S', '20': 'S', '21': 'S',
           'A,2': 'D', 'A,3': 'D', 'A,4': 'D', 'A,5': 'D', 'A,6': 'D',
           'A,7': 'D', 'A,8': 'S', 'A,9': 'S', 'A,10': 'S',
           'A,A': 'Y', '2,2': 'Y', '3,3': 'Y', '4,4': 'Y', '5,5': 'D',
           '6,6': 'Y', '7,7': 'Y', '8,8': 'Y', '9,9': 'S', '10,10': 'S',
           },

     '6': {'5': 'H', '6': 'H', '7': 'H', '8': 'H', '9': 'D', '10': 'D', '11': 'D',
           '12': 'S', '13': 'S', '14': 'S', '15': 'S', '16': 'S', '17': 'S',
           '18': 'S', '19': 'S', '20': 'S', '21': 'S',
           'A,2': 'D', 'A,3': 'D', 'A,4': 'D', 'A,5': 'D', 'A,6': 'D',
           'A,7': 'D', 'A,8': 'D', 'A,9': 'S', 'A,10': 'S',
           'A,A': 'Y', '2,2': 'Y', '3,3': 'Y', '4,4': 'Y', '5,5': 'D',
           '6,6': 'Y', '7,7': 'Y', '8,8': 'Y', '9,9': 'Y', '10,10': 'S',
           },

     '7': {'5': 'H', '6': 'H', '7': 'H', '8': 'H', '9': 'H', '10': 'D', '11': 'D',
           '12': 'H', '13': 'H', '14': 'H', '15': 'H', '16': 'H', '17': 'S', '18': 'S',
           '19': 'S', '20': 'S', '21': 'S',
           'A,2': 'H', 'A,3': 'H', 'A,4': 'H', 'A,5': 'H', 'A,6': 'H',
           'A,7': 'S', 'A,8': 'S', 'A,9': 'S', 'A,10': 'S',
           'A,A': 'Y', '2,2': 'Y', '3,3': 'Y', '4,4': 'H', '5,5': 'D',
           '6,6': 'H', '7,7': 'Y', '8,8': 'Y', '9,9': 'S', '10,10': 'S',
           },

     '8': {'5': 'H', '6': 'H', '7': 'H', '8': 'H', '9': 'H', '10': 'D', '11': 'D',
           '12': 'H', '13': 'H', '14': 'H', '15': 'H', '16': 'H', '17': 'S', '18': 'S',
           '19': 'S', '20': 'S', '21': 'S',
           'A,2': 'H', 'A,3': 'H', 'A,4': 'H', 'A,5': 'H', 'A,6': 'H',
           'A,7': 'S', 'A,8': 'S', 'A,9': 'S', 'A,10': 'S',
           'A,A': 'Y', '2,2': 'H', '3,3': 'H', '4,4': 'H', '5,5': 'H',
           '6,6': 'H', '7,7': 'H', '8,8': 'Y', '9,9': 'S', '10,10': 'S',
           },

     '9': {'5': 'H',           '6': 'H',           '7': 'H',           '8': 'H',           '9': 'H',           '10': 'D',           '11': 'D',
           '12': 'H',           '13': 'H',           '14': 'H',           '15': 'H',           '16': 'H',           '17': 'S',           '18': 'S',
           '19': 'S',           '20': 'S',           '21': 'S',
           'A,2': 'H',
           'A,3': 'H',
           'A,4': 'H',
           'A,5': 'H',
           'A,6': 'H',
           'A,7': 'H',
           'A,8': 'S',
           'A,9': 'S',
           'A,10': 'S',
           'A,A': 'Y',
           '2,2': 'H',
           '3,3': 'H',
           '4,4': 'H',
           '5,5': 'D',
           '6,6': 'H',
           '7,7': 'H',
           '8,8': 'Y',
           '9,9': 'S',
           '10,10': 'S',
           },

     '10': {'5': 'H',
            '6': 'H',
            '7': 'H',
            '8': 'H',
            '9': 'H',
            '10': 'H',
            '11': 'D',
            '12': 'H',
            '13': 'H',
            '14': 'H',
            '15': 'H',
            '16': 'H',
            '17': 'S',
            '18': 'S',
            '19': 'S',
            '20': 'S',
            '21': 'S',
            'A,2': 'H',
            'A,3': 'H',
            'A,4': 'H',
            'A,5': 'H',
            'A,6': 'H',
            'A,7': 'H',
            'A,8': 'S',
            'A,9': 'S',
            'A,10': 'S',
            'A,A': 'Y',
            '2,2': 'H',
            '3,3': 'H',
            '4,4': 'H',
            '5,5': 'H',
            '6,6': 'H',
            '7,7': 'H',
            '8,8': 'Y',
            '9,9': 'S',
            '10,10': 'S',
            },

     'A': {'5': 'H',
           '6': 'H',
           '7': 'H',
           '8': 'H',
           '9': 'H',
           '10': 'H',
           '11': 'D',
           '12': 'H',
           '13': 'H',
           '14': 'H',
           '15': 'H',
           '16': 'H',
           '17': 'S',
           '18': 'S',
           '19': 'S',
           '20': 'S',
           '21': 'S',
           'A,2': 'H',
           'A,3': 'H',
           'A,4': 'H',
           'A,5': 'H',
           'A,6': 'H',
           'A,7': 'H',
           'A,8': 'S',
           'A,9': 'S',
           'A,10': 'S',
           'A,A': 'Y',
           '2,2': 'H',
           '3,3': 'H',
           '4,4': 'H',
           '5,5': 'H',
           '6,6': 'H',
           '7,7': 'H',
           '8,8': 'Y',
           '9,9': 'S',
           '10,10': 'S',
           },
     })
