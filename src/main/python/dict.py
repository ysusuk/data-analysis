#dictionary - class?
alien = {'color': 'green', 'points': 5}
print(alien['color'])
print(alien['points'])

alien['color'] = 'blue'
print(alien['color'])

alien['x'] = 0
alien['y'] = 25
print(alien)

del alien['points']
print(alien)

user = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
    'cars': ['bmw 1', 'bmw x5']
}

for key, value in user.items():
    print("key: " + key + ", value: " + str(value))

users = [user, user]

furniture = {
  'couch': {
      'color': 'blue',
      'weight': '1kg'
  }
}

print(furniture)
