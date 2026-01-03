import math

def read_points():
    points = input("x1, y1 , x2, y2 , x3, y3 ")
    L = [float(t.strip()) for t in points.split(",")]
    A = (L[0], L[1])
    B = (L[2] , L[3])
    C = (L[4] , L[5])
    return A , B , C

def distance(p,q):
     return math.hypot(q[0] - p[0], q[1] - p[1])

def is_valid_triangle(a , b , c):
    return a + b > c and b + c > a and a + c > b

def perimeter(a,b,c):
    per = a + b + c
    return per

def area(a,b,c):
    s = perimeter(a,b,c) / 2.0
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

def type_by_sides(a, b, c):
    if a == b == c:
        return "ισόπλευρο"
    if a == b or b == c or c == a:
        return "ισοσκελές"
    return "σκαληνό"

def type_by_angles(a, b, c):
    a, b, c = sorted([a, b, c])  # a ≤ b ≤ c

    # στρογγυλοποίηση για να αποφύγουμε σφάλματα κινητής υποδιαστολής
    left = round(a*a + b*b, 4)
    right = round(c*c, 4)

    if left == right:
        return "ορθογώνιο"
    return "οξυγώνιο" if left > right else "αμβλυγώνιο"

# --- main ---
print("=== Triangle Inspector (με συναρτήσεις) ===")
A, B, C = read_points() 
ab = distance(A,B) 
bc = distance(B,C) 
ca = distance(C,A) 

print(f"AB={ab:.4f}, BC={bc:.4f}, CA={ca:.4f}")

if not is_valid_triangle(ab, bc, ca):
    print("Τα σημεία δεν σχηματίζουν έγκυρο τρίγωνο.")
else:
    per = perimeter(ab , bc , ca)             
    area_val = area(ab , bc , ca)            
    sides_t = type_by_sides(ab , bc , ca)     
    angles_t = type_by_angles(ab , bc , ca)   

    print("Έγκυρο τρίγωνο.")
    print(f"Περίμετρος = {per:.4f}")
    print(f"Εμβαδόν = {area_val:.4f}")
    print(f"Τύπος κατά πλευρές: {sides_t}")
    print(f"Τύπος κατά γωνίες: {angles_t}")