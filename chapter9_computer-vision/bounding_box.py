from fig_config import *
from mxnet import image

set_figsize()
img = image.imread('../img/catdog.jpg').asnumpy()
plt.imshow(img)


def bbox_to_rect(bbox, color):  # 本函数已保存在d2lzh包中方便以后使用
    # 将边界框(左上x, 左上y, 右下x, 右下y)格式转换成matplotlib格式：
    # ((左上x, 左上y), 宽, 高)
    return plt.Rectangle(
        xy=(bbox[0], bbox[1]), width=bbox[2]-bbox[0], height=bbox[3]-bbox[1],
        fill=False, edgecolor=color, linewidth=2)


dog_bbox, cat_bbox = [60, 45, 378, 516], [400, 112, 655, 493]
fig = plt.imshow(img)
fig.axes.add_patch(bbox_to_rect(dog_bbox, 'blue'))##将边界框加载在图像上
fig.axes.add_patch(bbox_to_rect(cat_bbox, 'red')) ##将边界框加载在图像上
plt.show()


