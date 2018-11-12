from __future__ import print_function

import os

from PIL import Image



files = [
  'part1-0001.jpg',
  'part2-0001.jpg',
  'part2-0001.jpg',
]

result = Image.new("RGB", (800, 800))

for index, file in enumerate(files):

  path = os.path.expanduser(file)

  img = Image.open(path)

  img.thumbnail((400, 400), Image.ANTIALIAS)

  x = index // 1 * 400

  y = index % 1 * 400

  w, h = img.size

  print('pos {0},{1} size {2},{3}'.format(x, y, w, h))

  result.paste(img, (x, y, x + w, y + h))


result.save(os.path.expanduser('image.jpg'))