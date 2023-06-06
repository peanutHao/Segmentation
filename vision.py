import matplotlib.pyplot as plt
from PIL import Image

original = ['/data/qianhao/Endoscope-WL/TestDataset/Kvasir/images/cju7bd1qu1mx409877xjxibox.png', '/data/qianhao/Endoscope-WL/TestDataset/Kvasir/images/cju7bgnvb1sf808717qa799ir.png', '/data/qianhao/Endoscope-WL/TestDataset/CVC-ClinicDB/images/25.png']  # 原图像列表
gt = ['/data/qianhao/Endoscope-WL/TestDataset/Kvasir/masks/cju7bd1qu1mx409877xjxibox.png', '/data/qianhao/Endoscope-WL/TestDataset/Kvasir/masks/cju7bgnvb1sf808717qa799ir.png', '/data/qianhao/Endoscope-WL/TestDataset/CVC-ClinicDB/masks/25.png']    # GT图像列表
predict = ['/data/qianhao/Polyp-PVT-main/result_map/output/Kvasircju7bd1qu1mx409877xjxibox.png', '/data/qianhao/Polyp-PVT-main/result_map/output/Kvasircju7bgnvb1sf808717qa799ir.png', '/data/qianhao/Polyp-PVT-main/result_map/output/CVC-ClinicDB25.png']
# 定义图像的标题
original_images = []
for file in original:
    image = Image.open(file)
    original_images.append(image)
gt_images = []
for file in gt:
    image = Image.open(file)
    gt_images.append(image)
predict_images = []
for file in predict:
    image = Image.open(file)
    predict_images.append(image)
column_titles = ['Original', 'GT', 'Predict']

# 定义行数和列数
num_rows = len(original_images)
num_cols = len(column_titles)

# 创建子图并显示图像
fig, axes = plt.subplots(num_rows, num_cols, figsize=(10, 10))

for i, (original, gt, pre) in enumerate(zip(original_images, gt_images, predict_images)):
    # 显示原图
    axes[i, 0].imshow(original)
    axes[i, 0].set_title(column_titles[0])
    axes[i, 0].axis('off')

    # 显示GT图像
    axes[i, 1].imshow(gt, cmap='gray')
    axes[i, 1].set_title(column_titles[1])
    axes[i, 1].axis('off')

    axes[i, 2].imshow(pre, cmap='gray')
    axes[i, 2].set_title(column_titles[2])
    axes[i, 2].axis('off')

plt.tight_layout()
plt.show()
plt.savefig('vision.png')
