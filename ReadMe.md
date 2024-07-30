# File Manager Organizer

## 개요
`File Manager Organizer`는 데스크탑의 `AUTO_FILEMANAGER` 폴더 내의 파일들을 파일 유형별로 정리하고, 불필요한 비어있는 폴더를 삭제하거나 기타 폴더로 이동하는 Python 스크립트입니다.

## 기능
- **파일 분류**: `AUTO_FILEMANAGER` 폴더 내의 파일들을 이미지, 문서, 오디오, 비디오, 압축 파일, 스크립트, 기타 파일 등으로 분류합니다.
- **폴더 정리**: `AUTO_FILEMANAGER` 폴더 내의 폴더들은 "others" 폴더로 이동합니다.
- **폴더 예외 처리**: 이미 존재하는 타입별 폴더 및 "others" 폴더는 이동하지 않습니다.
- **이름 충돌 해결**: 동일한 이름의 파일이나 폴더가 있을 경우 이름을 변경하여 이동합니다.

## 설치
1. Python 3.x가 설치되어 있는지 확인합니다.
2. 이 리포지토리를 클론합니다:

    ```bash
    git clone https://github.com/username/file_manager_organizer.git
    cd file_manager_organizer
    ```

3. 필요한 패키지가 있다면 설치합니다:

    ```bash
    pip install -r requirements.txt
    ```

## 사용 방법
1. 스크립트를 실행하기 전에, 데스크탑에 `AUTO_FILEMANAGER` 폴더가 있는지 확인합니다. 없으면 스크립트가 폴더를 생성합니다.
2. 터미널이나 명령 프롬프트를 열고, 스크립트가 있는 디렉토리로 이동합니다:

    ```bash
    cd path/to/file_manager_organizer
    ```

3. 스크립트를 실행합니다:

    ```bash
    python file_manager_organizer.py
    ```

4. 스크립트가 실행되면, `AUTO_FILEMANAGER` 폴더 내의 파일과 폴더가 정리됩니다.

## 디렉토리 구조
이 프로젝트의 디렉토리 구조는 다음과 같습니다:

```plaintext
file_manager_organizer/
│
├── file_manager_organizer.py  # 메인 스크립트 파일
├── README.md                   # 프로젝트 설명서
└── requirements.txt            # 필요 패키지 목록 (선택 사항)
