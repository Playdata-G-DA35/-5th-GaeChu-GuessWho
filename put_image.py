import os
import sys
from poll.models import Category, Image_path, Ans_vote
from django.utils import timezone

# 카테고리 폴더내의 이미지 객체들 생성
def main(c_id):
    path = f"./poll/static/category{c_id}"
    file_list = os.listdir(path)
    print(file_list)

    c = Category.objects.get(pk=c_id)

    for num in range(len(file_list)):
        i = Image_path(category = c, img_name = file_list[num], img_path = f"/static/category{c_id}/{file_list[num]}")
        i.save()

if __name__ == '__main__':
    main()