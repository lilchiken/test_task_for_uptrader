from django.db import models


class Dir(models.Model):
    title = models.CharField(max_length=100)
    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        related_name='dirs',
        null=True,
        blank=True,
        default=None
    )
    create_date = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self) -> str:
        return self.title
    
    def __repr__(self) -> str:
        return self.title
    
    # class Meta:
    #     ordering = ['-create_date']
