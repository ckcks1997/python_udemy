import shutil

# files 디렉토리의 파일을 zip파일로 output이라는 이름으로 생성
shutil.make_archive("output", "zip", "files")