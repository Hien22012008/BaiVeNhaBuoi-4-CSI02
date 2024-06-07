def count_word_frequency(paragraph, target_word):
    
    paragraph = paragraph.lower()
    target_word = target_word.lower()

    # Tách đoạn văn thành danh sách cá từ 
    words = paragraph.split()

    # Đếm số lần xuất hiện của từ cần tìm

    frequency = words.count(target_word)

    return frequency

paragraph_exampple = "The cat is chasing the rat in Netherlands. The dog is also chasing the rat."
word_to_find = "the"


result = count_word_frequency(paragraph_exampple, word_to_find)
print(f"Tần suất xuất hiện của từ '{word_to_find}' trong đoạn văn là {result} lần")