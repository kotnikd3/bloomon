import re

# Examples: 'aL', 'bS', 'bL', ...
FLOWER_REGEX = re.compile(r"^[a-z]{1}[LS]{1}$")

# Examples: 'AS2a2b3', 'BL2a2', 'AS2b3a4c5', ...
DESIGN_REGEX = re.compile(
    r"^(?P<name>[A-Z]{1})(?P<size>[SL]{1})(?P<flowers>(\d[a-z])+)(?P<capacity>\d{1})$"
)

# Examples: '2c', '2b', '3a', ...
FLOWERS_REGEX = re.compile(r"\d[a-z]")


class Parser:
    @staticmethod
    def parse(
        code,
        design_return_code,
        flower_return_code,
        invalid_return_code,
    ):
        """
        Parse the code and if the code corresponds to one of the supported
        format (design, flower), return parsed data with return code.
        """
        
        if DESIGN_REGEX.search(code):
            regex_result = DESIGN_REGEX.search(code).groupdict()

            flowers = {}
            for flower in FLOWERS_REGEX.findall(regex_result["flowers"]):
                flowers[flower[1]] = int(flower[0])
            
            return {
                'return_code': design_return_code,
                'design_code': code,
                'design_name': regex_result["name"],
                'design_size': regex_result["size"],
                'design_capacity': int(regex_result["capacity"]),
                'design_flowers': flowers
            }            
        if FLOWER_REGEX.search(code):
            return {
                'return_code': flower_return_code,
                'flower_species': code[0],
                'flower_size': code[1]
            }
        else:
            return {
                'return_code': invalid_return_code
            }
