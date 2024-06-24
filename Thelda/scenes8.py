from thumby import Sprite

class Sword:
    def __init__(self, direction, x, y):
        self.sword = True
        self.x = x
        self.y = y
        self.item_type = "sword"
        self.direction = direction
        self.item = bytearray([31, 23, 0, 23, 31])
        self.sword_up = bytearray([31, 23, 0, 23, 31])
        self.sprite = Sprite(5, 5, self.sword_up, self.x, self.y, key=1)
        self.sword_sprite = Sprite(5, 5, self.sword_up, self.x, self.y, key=1)


class Scenes8:
    def __init__(self):
        # self.nw_slope_map = bytearray([8, 22, 21, 26, 28])
        # # BITMAP: width: 5, height: 5
        # self.ne_slope_map = bytearray([30, 30, 25, 22, 4])
        # # BITMAP: width: 5, height: 5
        # self.se_slope_map = bytearray([15, 23, 7, 27, 4])
        # # BITMAP: width: 5, height: 5
        # self.sw_slope_map = bytearray([8, 22, 5, 27, 7])

        # BITMAP: width: 60, height: 7
        self.dangerous_map = bytearray(
            [127, 10, 40, 26, 127, 94, 40, 94, 127, 126, 27, 104, 30, 127, 15, 56, 58, 125, 95, 41, 94, 121, 15, 104,
             30, 121, 15, 24, 58, 121, 63, 72, 73, 123, 127, 104, 12, 105, 127, 24, 106, 24, 127, 8, 91, 40, 127, 11,
             24, 62, 127, 127, 46, 8, 46, 127, 109, 10, 109, 63])
        self.dangerous = Sprite(60, 7, self.dangerous_map, 6, 11, key=1)
        # BITMAP: width: 40, height: 7
        self.dude_1 = bytearray(
            [71, 55, 59, 57, 71, 127, 127, 127, 127, 127, 127, 127, 127, 127, 127, 127, 127, 71, 25, 34, 34, 25, 71,
             127, 127, 127, 127, 127, 127, 127, 127, 127, 127, 127, 127, 71, 55, 59, 57, 71])
        # BITMAP: width: 40, height: 7
        self.dude_2 = bytearray(
            [69, 55, 27, 58, 71, 127, 127, 127, 127, 127, 127, 127, 127, 127, 127, 127, 127, 71, 25, 34, 34, 25, 71,
             127, 127, 127, 127, 127, 127, 127, 127, 127, 127, 127, 127, 69, 55, 27, 58, 71])
        self.dude = Sprite(40, 7, self.dude_1 + self.dude_2, 16, 19, key=1)

        self.fire_1 = bytearray(
            [71, 55, 59, 57, 71, 127, 127, 127, 127, 127, 127, 127, 127, 127, 127, 127, 127, 127, 127, 127, 127, 127,
             127, 127, 127, 127, 127, 127, 127, 127, 127, 127, 127, 127, 127, 71, 55, 59, 57, 71])
        self.fire_2 = bytearray(
            [69, 55, 27, 58, 71, 127, 127, 127, 127, 127, 127, 127, 127, 127, 127, 127, 127, 127, 127, 127, 127, 127,
             127, 127, 127, 127, 127, 127, 127, 127, 127, 127, 127, 127, 127, 69, 55, 27, 58, 71])
        self.fire = Sprite(40, 7, self.fire_1 + self.fire_2, 16, 19, key=1)
        # 15 x 10
        self.dungeon_1_entrance_map = bytearray([254,249,3,252,254,22,22,29,22,22,253,254,1,191,223,
           3,1,0,1,1,0,0,0,0,0,1,1,0,1,3])
        self.dungeon_1_entrance = Sprite(15, 10, self.dungeon_1_entrance_map, 26, 15, key=1)
        
        
        self.scenes = {
            
            "scene -8,1": {
                "walls": [
                    (1, 5), (6, 5), (11, 5), (16, 5), (21, 5), (26, 5), (31, 5),
                    (36, 5), (41, 5), (46, 5), (51, 5), (56, 5), (61, 5), (66, 5),
                    (1, 10), (66, 10),
                    (1, 15), (66, 15),
                    (1, 20), (66, 20),
                    (1, 25), (66, 25),
                    (1, 30), (66, 30),
                    (1, 35), (6, 35), (11, 35), (16, 35), (21, 35), (26, 35), (41, 35),
                    (46, 35), (51, 35), (56, 35), (61, 35), (66, 35)],
                "barriers": [(6, 20), (11, 20), (16, 20), (21, 20), (26, 20), (31, 20),
                             (36, 20), (41, 20), (46, 20), (51, 20), (56, 20), (61, 20)],
                "items": [Sword("up", 33, 27)],
                "sprites": [self.dangerous, self.dude, self.fire]},
            "scene 8,0": {
                "walls": [
                    (1, 5), (6, 5), (11, 5), (16, 5), (21, 5), (26, 5), (41, 5),
                    (46, 5), (51, 5), (56, 5), (61, 5), (66, 5),
                    (1, 10), (6, 10), (11, 10), (21, 10), (41, 10), (46, 10), (51, 10),
                    (56, 10), (61, 10), (66, 10),
                    (1, 15), (6, 15), (46, 15), (51, 15), (56, 15), (61, 15), (66, 15),
                    (1, 25), (61, 25), (66, 25),
                    (1, 30), (6, 30), (61, 30), (66, 30),
                    (1, 35), (6, 35), (11, 35), (16, 35), (21, 35), (26, 35), (31, 35),
                    (36, 35), (41, 35), (46, 35), (51, 35), (56, 35), (61, 35), (66, 35)],
                "doors": [(16, 10)],
                # "slopes": [
                #     # Slope(self.nw_slope_map, 26, 10), Slope(self.nw_slope_map, 11, 15), Slope(self.ne_slope_map, 41, 15), Slope(self.sw_slope_map, 6, 25)
                # ]
                },
            "scene 8,1": {
                "walls": [
                    (1, 5), (6, 5), (11, 5), (16, 5), (21, 5), (26, 5), (31, 5),
                    (36, 5), (41, 5), (46, 5), (51, 5), (56, 5), (61, 5), (66, 5),
                    (1, 10), (41, 10), (66, 10),
                    (11, 15), (21, 15), (51, 15),
                    (11, 25), (21, 25), (51, 25),
                    (1, 30), (41, 30), (66, 30),
                    (1, 35), (6, 35), (11, 35), (16, 35), (21, 35), (26, 35), (41, 35),
                    (46, 35), (51, 35), (56, 35), (61, 35), (66, 35)],
                "enemies": {"octorok": [("S8E01"), ("S8E02"), ("S8E03")]}},
                
            "scene 8,2": {
                "bushes": [
                    (1, 5), (6, 5), (11, 5), (16, 5), (21, 5), (26, 5), (31, 5),
                    (36, 5), (41, 5), (46, 5), (51, 5), (56, 5), (61, 5), (66, 5),
                    (16, 15), (46, 15), (56, 15), (66, 15),
                    (26, 20),
                    (16, 25), (46, 25), (56, 25), (66, 25),
                    (1, 35), (6, 35), (11, 35), (16, 35), (21, 35), (26, 35), (31, 35),
                    (36, 35), (41, 35), (46, 35), (51, 35), (56, 35), (61, 35), (66, 35)],
                "enemies": {"octorok": [("S8E04"), ("S8E05")]}},
            "scene 8,3": {
                "walls": [(41, 30), (46, 30), (51, 30), (56, 30), (61, 30), (66, 30),
                          (41, 35), (46, 35), (51, 35), (56, 35), (61, 35), (66, 35)],
                "water": [(1, 5), (6, 5), (11, 5), (16, 5), (21, 5), (26, 5), (31, 5),
                          (36, 5), (41, 5), (46, 5), (51, 5), (56, 5), (61, 5), (66, 5),
                          (1, 10), (6, 10), (11, 10), (16, 10), (21, 10), (26, 10),
                          (31, 10), (36, 10), (41, 10), (46, 10), (51, 10), (56, 10),
                          (61, 10), (66, 10),
                          (1, 15), (6, 15), (11, 15), (16, 15), (21, 15), (26, 15),
                          (31, 15), (36, 15), (41, 15), (46, 15), (51, 15), (56, 15),
                          (61, 15), (66, 15)],
                "bushes": [(1, 30), (6, 30), (11, 30), (16, 30), (21, 30), (26, 30),
                           (31, 30), (36, 30), (41, 30), (46, 30), (51, 30), (56, 30),
                           (61, 30), (66, 30),
                           (1, 35), (6, 35), (11, 35), (16, 35), (21, 35), (26, 35),
                           (31, 35), (36, 35), (41, 35), (46, 35), (51, 35), (56, 35),
                           (61, 35), (66, 35)],
                "enemies": {"zora": [("S8E06")]}},

            "scene 8,4": {
                "dungeon":[], 
                "walls": [(6, 5), (11, 5), (16, 5), (21, 5), (26, 5), (31, 5), (36, 5), (41, 5), (46, 5), (51, 5), (56, 5), (61, 5), (66, 5),
                    (6, 10), (61, 10),
                    (6, 15), (61, 15),
                    (6, 20), 
                    (6, 25), (61, 25),
                    (6, 30), (61, 30),
                    (6, 35), (11, 35), (16, 35), (21, 35), (26, 35), (31, 35), (36, 35), (41, 35), (46, 35), (51, 35), (56, 35), (61, 35)], 
                "barriers": [(26, 15), (31, 15), (36, 15), (16, 15), (46, 15), (16, 20), (46, 20), (26, 20), (36, 20)], 
                "water": [(1, 5),  (66, 5), 
                    (1, 10),  (66, 10), 
                    (1, 15),  (66, 15), 
                    (1, 20),
                    (1, 25),  (66, 25), 
                    (1, 30),  (66, 30), 
                    (1, 35),  (66, 35), ],
                "bridges": [(66, 20)], 
                "doors": [(31, 20)],
                "trees": [(16, 15), (46, 15), 
                    (16, 20), (46, 20)], 
                "sprites": [self.dungeon_1_entrance],
                "enemies" : {"octorok": [("S8E07")]}
            }
        }
        
        