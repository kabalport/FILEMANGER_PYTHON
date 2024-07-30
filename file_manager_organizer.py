import os
import shutil

# 현재 사용자의 데스크탑 경로 가져오기
desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
auto_filemanager_path = os.path.join(desktop_path, "AUTO_FILEMANAGER")

# AUTO_FILEMANAGER 폴더가 없으면 생성
if not os.path.exists(auto_filemanager_path):
    os.makedirs(auto_filemanager_path)
    print(f"폴더 생성됨: {auto_filemanager_path}")
else:
    print(f"폴더 존재함: {auto_filemanager_path}")

# 파일 타입별 폴더 이름 설정
folders = {
    "images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"],
    "documents": [".pdf", ".doc", ".docx", ".txt", ".xls", ".xlsx", ".ppt", ".pptx"],
    "audio": [".mp3", ".wav", ".aac", ".flac", ".ogg"],
    "video": [".mp4", ".mkv", ".avi", ".mov", ".wmv"],
    "archives": [".zip", ".rar", ".tar", ".gz", ".bz2"],
    "scripts": [".py", ".js", ".sh", ".bat", ".php", ".html", ".css"],
    "others": []
}

# 서브 폴더 생성 함수
def create_subfolders(base_path, folder_dict):
    for folder in folder_dict.keys():
        folder_path = os.path.join(base_path, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            print(f"서브 폴더 생성됨: {folder_path}")

# 동일한 이름의 폴더가 있는 경우 이름을 변경하는 함수
def get_unique_path(path):
    base, name = os.path.split(path)
    counter = 1
    new_path = path
    while os.path.exists(new_path):
        new_path = os.path.join(base, f"{name}_{counter}")
        counter += 1
    return new_path

# 파일 이동 함수
def move_files(base_path, folder_dict):
    others_folder_path = os.path.join(base_path, "others")
    if not os.path.exists(others_folder_path):
        os.makedirs(others_folder_path)
        print(f"서브 폴더 생성됨: {others_folder_path}")

    for item in os.listdir(base_path):
        item_path = os.path.join(base_path, item)

        # "others" 폴더 및 타입별 폴더는 건너뛰기
        if item == "others" or item in folder_dict.keys():
            continue

        # 폴더는 others 폴더로 이동
        if os.path.isdir(item_path):
            target_folder_path = os.path.join(others_folder_path, item)
            unique_target_folder_path = get_unique_path(target_folder_path)
            shutil.move(item_path, unique_target_folder_path)
            print(f"폴더 이동됨: {item_path} -> {unique_target_folder_path}")
            continue

        # 파일 확장자 가져오기
        _, ext = os.path.splitext(item)
        ext = ext.lower()

        # 파일을 적절한 서브폴더로 이동
        moved = False
        for folder, extensions in folder_dict.items():
            if ext in extensions:
                target_folder_path = os.path.join(base_path, folder)
                if not os.path.exists(target_folder_path):
                    os.makedirs(target_folder_path)
                    print(f"서브 폴더 생성됨: {target_folder_path}")

                shutil.move(item_path, os.path.join(target_folder_path, item))
                print(f"파일 이동됨: {item_path} -> {os.path.join(target_folder_path, item)}")
                moved = True
                break

        # 기타 파일은 others 폴더로 이동
        if not moved:
            target_folder_path = os.path.join(others_folder_path, item)
            unique_target_path = get_unique_path(target_folder_path)
            shutil.move(item_path, unique_target_path)
            print(f"파일 이동됨: {item_path} -> {unique_target_path}")

# 서브 폴더 생성
create_subfolders(auto_filemanager_path, folders)

# 파일 이동
move_files(auto_filemanager_path, folders)

print("파일 정리 완료!")
