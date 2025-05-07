class Solution:
    def countPoints(self, rings: str) -> int:
        rods = {}
        current_ring = rings[0]

        for i in range(1, len(rings)):
            if i % 2 != 0:
                if rings[i] not in rods:
                    rods[rings[i]] = [current_ring]
                else:
                    rods[rings[i]].append(current_ring)
            else:
                current_ring = rings[i]
        
        rings_color = ['R', 'B', 'G']
        result_rods = 0

        for val in rods.values():
            if all(r_c in val for r_c in rings_color):
                result_rods += 1
        
        return result_rods