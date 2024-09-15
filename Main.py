from Controller import CowStrikeController
from Model import CowModel, GoatModel
from View import CowStrikeView
import json

def main():
    with open('cows_data.json', 'r') as file:
        data = json.load(file)

    cows = [CowModel(cow['cow_id'], cow['age_years'], cow['age_months'], cow['udders']) for cow in data['cows']]
    goats = [GoatModel(goat['goat_id']) for goat in data['goats']]

    view = CowStrikeView(None)  
    controller = CowStrikeController(view, cows, goats)
    view.controller = controller  
    controller.run()

if __name__ == "__main__":
    main()
