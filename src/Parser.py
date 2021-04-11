"""
Author: Denis Kotnik, april 2021
"""

import re

# Examples: 'aL', 'bS', 'bL', ...
FLOWER_REGEX = re.compile(r"^[a-z]{1}[LS]{1}$")

# Examples: 'AS2a2b3', 'BL2a2', 'AS2b3a4c5', ...
DESIGN_REGEX = re.compile(r"^(?P<name>[A-Z]{1})(?P<size>[SL]{1})(?P<flowers>(\d[a-z])+)(?P<capacity>\d{1})$")

# Examples: '2c', '2b', '3a', ...
FLOWERS_REGEX = re.compile(r"\d[a-z]")

class Parser():
    def parse(code, designReturnCode, flowerReturnCode, invalidReturnCode):
        """
        Parse the code and if the code corresponds to one of the supported format (design, flower),
        return parsed data with appropiate return code.
        """
        
        if DESIGN_REGEX.search(code):
            regexResult = DESIGN_REGEX.search(code).groupdict()

            flowers = {}
            for flower in FLOWERS_REGEX.findall(regexResult["flowers"]):
                flowers[flower[1]] = int(flower[0])
            
            return {
                'returnCode': designReturnCode,
                'designCode': code,
                'designName': regexResult["name"],
                'designSize': regexResult["size"],
                'designCapacity': int(regexResult["capacity"]),
                'designFlowers': flowers
            }            
        if FLOWER_REGEX.search(code):
            return {
                'returnCode': flowerReturnCode,
                'flowerSpecies': code[0],
                'flowerSize': code[1]
            }
        else:
            return {
                'returnCode': invalidReturnCode
            }