from import_export import resources
from .models import Review, Comment


class ReviewResource(resources.ModelResource):
    class Meta:
        model = Review
        fields = ('id', 'title_id', 'text', 'author', 'score', 'pub_date',)


class CommentResource(resources.ModelResource):
    class Meta:
        model = Comment
        fields = ('id', 'review_id', 'text', 'author', 'pub_date',)
