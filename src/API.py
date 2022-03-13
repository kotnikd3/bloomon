from Parser import Parser
from BusinessLogic import BusinessLogic


DESIGN_RETURN_CODE = "DESIGN"
FLOWER_RETURN_CODE = "FLOWER"
INVALID_RETURN_CODE = "INVALID"

business_logic = BusinessLogic()


while True:
    data = Parser.parse(
        input(),
        DESIGN_RETURN_CODE,
        FLOWER_RETURN_CODE,
        INVALID_RETURN_CODE,
    )

    if data['return_code'] == DESIGN_RETURN_CODE:
        business_logic.add_design(data)
    elif data['return_code'] == FLOWER_RETURN_CODE:
        business_logic.add_flower(data)
        bouquet_name = business_logic.process_flower()
        if bouquet_name is not None:
            print(bouquet_name)
    else:
        continue
