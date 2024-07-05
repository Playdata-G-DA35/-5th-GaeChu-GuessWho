import os
import sys
from poll.models import Category, Image_path, Ans_vote
from django.utils import timezone

def main(c_id):
    path = f"./poll/static/category{c_id}"
    file_list = os.listdir(path)
    print(file_list)

    c = Category.objects.get(pk=c_id)

    for num in range(len(file_list)):
        i = Image_path(category = c, img_name = file_list[num], img_path = f"/static/category{c_id}/{file_list[num]}")
        i.save()

    #for name in file_list:
    #    img_obj = Image_path(img_path=f'{name}.jpg', pub_date= timezone.now(), category= )
    #    img_obj.save()

if __name__ == '__main__':
    main()