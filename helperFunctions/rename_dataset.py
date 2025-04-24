import os

def rename_dataset(image_dir, label_dir, image_ext='.jpg', label_ext='.txt', start_index=1):
    """
    统一修改数据集图片和标签的名字。
    
    :param image_dir: 图片文件夹路径
    :param label_dir: 标签文件夹路径
    :param image_ext: 图片文件扩展名（如 .jpg）
    :param label_ext: 标签文件扩展名（如 .txt）
    :param start_index: 起始编号
    """
    # 获取图片和标签文件列表
    image_files = sorted([f for f in os.listdir(image_dir) if f.endswith(image_ext)])
    label_files = sorted([f for f in os.listdir(label_dir) if f.endswith(label_ext)])
    
    # 确保图片和标签文件数量一致
    if len(image_files) != len(label_files):
        raise ValueError("图片文件和标签文件数量不一致，请检查数据集！")
    
    # 遍历图片和标签文件，按新命名规则重命名
    for idx, (img_file, lbl_file) in enumerate(zip(image_files, label_files), start=start_index):
        new_name = f"CRYTOT{idx}"  # 生成统一编号
        new_img_name = f"{new_name}{image_ext}"
        new_lbl_name = f"{new_name}{label_ext}"
        
        # 重命名图片文件
        os.rename(os.path.join(image_dir, img_file), os.path.join(image_dir, new_img_name))
        # 重命名标签文件
        os.rename(os.path.join(label_dir, lbl_file), os.path.join(label_dir, new_lbl_name))
    
    print(f"数据集重命名完成！共重命名 {len(image_files)} 对图片和标签文件。")

# 使用示例
if __name__ == '__main__':
    image_dir = r'C:\Users\86153\ultralytics\data\CRYTOT\images'  # 图片文件夹路径
    label_dir = r'C:\Users\86153\ultralytics\data\CRYTOT\lables'  # 标签文件夹路径
    rename_dataset(image_dir, label_dir)
