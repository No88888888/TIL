text = 'python'
text2 = text

print(id(text))
print(id(text2))

text += " is good ! "
print(text)
print(id(text))
print(id(text2))

# dictionary

student_dict = {
    '유재석' : 41,
    '정준하' : 42 
}

scores = [80, 89, 99, 83]

result = 0
for num in scores:
    result += num
print(result / len(scores))

