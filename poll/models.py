from django.db import models

class Category(models.Model):
    cat_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.id}. {self.cat_name}"
    
class Image_path(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    img_name = models.CharField(max_length=100)
    img_path = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.id}. {self.img_path}"
    
class Ans_vote(models.Model):
    ans_text = models.CharField(max_length= 100)
    votes = models.IntegerField(default= 0)
    img_path = models.ForeignKey(Image_path, on_delete=models.CASCADE)

    # def __str__(self):
    #     return f"{self.id}. {self.ans_text}"