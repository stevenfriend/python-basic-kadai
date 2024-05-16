import random

class Human:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def check_adult(self):
    if self.age >= 20:
      print(f'{self.age}歳の{self.name}は大人です。')
    else:
      print(f'{self.age}歳の{self.name}は大人ではありません。')

humans = [
  Human('侍太郎', random.randint(0, 100)),
  Human('鈴木一郎', random.randint(0, 100)),
  Human('佐藤花子', random.randint(0, 100)),
  Human('田中美咲', random.randint(0, 100)),
  Human('伊藤勇気', random.randint(0, 100))
]

for human in humans:
  human.check_adult()