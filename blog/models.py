from django.db import models
from django.conf import settings
from django.utils import timezone



class Post(models.Model): # models.Model은 Post가 장고 모델임을 의미한다. 이 코드가 있음으로 장고는 Post가 데이터 베이스에 저장되어야 한다고 알게 된다.
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200) # CharField는 글자 수에 제한이 있는 텍스트를 정의할 때 사용
    text = models.TextField() # TextField는 글자 수에 제한이 없는 긴 텍스트를 위한 속성
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title