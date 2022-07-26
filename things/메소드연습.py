text = 'aa.bb.cc.dd.ee.ff'

print(f'text : {text}')

#split()
s =text.split()
s1 = text.split('.')
s2 = text.split(sep='.')

print(f'text.split() : {s}')
print(f"text.split('.') : {s1}")
print(f"text.split(sep='.') : {s2}")

txt = ',,,,,ssafy????'

print(txt.lstrip(','))
print(txt.strip(',?'))
print(txt.rstrip('?'))