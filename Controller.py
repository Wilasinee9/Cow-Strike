from Model import CowModel, GoatModel

class CowStrikeController:
    def __init__(self, view, cows, goats):
        self.view = view
        self.cows = cows
        self.goats = goats

    def process_animal(self, animal_id):
        if not animal_id.isdigit() or len(animal_id) != 8 or animal_id[0] == "0":
            self.view.show_result("รหัสต้องเป็นตัวเลข 8 หลักและไม่ขึ้นต้นด้วยเลข 0")
            return

        animal = self.find_animal_by_id(animal_id)

        if not animal:
            self.view.show_result("ไม่พบสัตว์ที่มีรหัสนี้")
            return

        if isinstance(animal, GoatModel):
            self.view.show_goat_message(f"รหัส {animal_id} เป็นแพะ ส่งกลับภูเขา")
        elif isinstance(animal, CowModel):
            if animal.udders == 4:
                milk = animal.milk()
                animal.restore_udders()
                self.view.show_result(f"รหัส {animal_id} เป็นวัว มี 4 เต้า ผลิตน้ำนมได้ {milk:.2f} ลิตร")
            elif animal.udders == 3:
                animal.restore_udders()
                self.view.show_result(f"รหัส {animal_id} เป็นวัว มี 3 เต้า ไม่สามารถผลิตนำ้นมได้แต่มีโอกาสกลับเป็นวัว 4 เต้าได้")

    def find_animal_by_id(self, animal_id):
        for cow in self.cows:
            if cow.cow_id == animal_id:
                return cow
        for goat in self.goats:
            if goat.goat_id == animal_id:
                return goat
        return None

    def run(self):
        self.view.run()
