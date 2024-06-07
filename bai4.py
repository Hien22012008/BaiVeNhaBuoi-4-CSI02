def can_form_str2_from_str1(str1, str2):
    # Tạo một bảng đếm cho str1
    count_str1 = {}
    for char in str1:
        if char in count_str1:
            count_str1[char] += 1
        else:
            count_str1[char] = 1
    
    # Kiểm tra xem mỗi ký tự trong str2 có đủ số lượng trong str1 không
    for char in str2:
        if char not in count_str1 or count_str1[char] == 0:
            return False
        count_str1[char] -= 1
    
    return True

str1 = "acbdfe"
str2 = "face"
print(can_form_str2_from_str1(str1, str2))  

