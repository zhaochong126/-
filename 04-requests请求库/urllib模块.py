import urllib.request



url = 'https://tse1-mm.cn.bing.net/th/id/OIP-C.g9UbVfyVZX-SfD09JcYr5QHaEK?rs=1&pid=ImgDetMain'

# 保存图片urlretrieve
urllib.request.urlretrieve(url, '图片.jpg')