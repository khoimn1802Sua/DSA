import math
def minimize_max_distance(x: list[int], k: int) -> float:
    def can_achieve(d: float) -> bool:
        new_stations = 0
        for i in range(len(x) - 1):
            segment_len = x[i+1] - x[i]
            if segment_len > d:
                new_stations += math.ceil(segment_len / d - 1e-9) - 1
                if new_stations > k:
                    return False
        return new_stations <= k
    low = 0.0
    high = float(x[-1] - x[0])
    for _ in range(80):
        mid = (low + high) / 2
        if can_achieve(mid):
            high = mid  
        else:
            low = mid           
    return low
