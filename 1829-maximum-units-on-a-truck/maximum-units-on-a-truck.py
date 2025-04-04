class Solution:
    def maximumUnits(self, boxTypes: list[list[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: -x[1])
        total_units = 0

        for boxes, units in boxTypes:
            if truckSize == 0:
                break
            take = min(truckSize, boxes)
            total_units += take * units
            truckSize -= take

        return total_units
