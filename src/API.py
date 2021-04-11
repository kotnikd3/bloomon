"""
Author: Denis Kotnik, april 2021
"""

from Parser import Parser
from BusinessLogic import BusinessLogic


DESIGN_RETURN_CODE = "DESIGN"
FLOWER_RETURN_CODE = "FLOWER"
INVALID_RETURN_CODE = "INVALID"

businessLogic = BusinessLogic()

while(True):
    data = Parser.parse(input(), DESIGN_RETURN_CODE, FLOWER_RETURN_CODE, INVALID_RETURN_CODE)

    if data['returnCode'] == DESIGN_RETURN_CODE:
        businessLogic.addDesign(data)
    elif data['returnCode'] == FLOWER_RETURN_CODE:
        businessLogic.addFlower(data)
        bouquetName = businessLogic.processFlower()
        if (bouquetName is not None):
            print(bouquetName)
    else:
        continue