#There are three rectangles in a plane each of which's sides are horizontal and vertical. The goal is to count the area's area where is at least one of the given rectangles. 

#A function returns the asked area. 


#I utilized this code in my solution: https://www.geeksforgeeks.org/total-area-two-overlapping-rectangles/
def area(rec1, rec2, rec3):
    area1 = abs(rec1[2]-rec1[0])*abs(rec1[1]-rec1[3])
    area2 = abs(rec2[2]-rec2[0])*abs(rec2[1]-rec2[3])
    area3 = abs(rec3[2]-rec3[0])*abs(rec3[1]-rec3[3])

   

    total_area = area1+area2+area3
    #count overlapping areas and subtract from total area
    return total_area-overlap_area(rec1, rec2)-overlap_area(rec1, rec3)-overlap_area(rec2, rec3)+overlap(rec1, rec2, rec3)

def overlap(r1, r2, r3):
    intersect = False
    x_dist = (min(r1[2], r2[2])-max(r1[0], r2[0]))
    y_dist = (min(r1[1], r2[1])-max(r1[3], r2[3]))
    overlap_rec = (max(r1[0], r2[0]), min(r1[1], r2[1]), min(r1[2], r2[2]), max(r1[3], r2[3]))

    if x_dist > 0 and y_dist > 0:
        intersect = True
    if intersect:
        intersect_area = overlap_area(overlap_rec, r3)
        return intersect_area
    else:
        return 0

def overlap_area(r1, r2):
    x_dist = (min(r1[2], r2[2])-max(r1[0], r2[0]))
    y_dist = (min(r1[1], r2[1])-max(r1[3], r2[3]))

    common = 0
    if x_dist > 0 and y_dist > 0:
        common = x_dist * y_dist
    return common


    

if __name__ == "__main__":
    rec1 = (-1,1,1,-1)
    rec2 = (0,3,2,0)
    rec3 = (0,2,3,-2)
    print(area(rec1,rec2,rec3)) # 16
