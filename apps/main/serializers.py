from rest_framework import serializers

from apps.main.models import Problem, CodeImage, Reply, Comment


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CodeImage
        fields = ('image',)


class ProblemCreateSerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField(format='%d %B %Y %H:%M', read_only=True)
    updated = serializers.DateTimeField(format='%d %B %Y %H:%M', read_only=True)
    images = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = Problem
        fields = ['id', 'title_ru', 'title_en', 'title_ky', 'description_ru', 'description_en', 'description_ky', 'images', 'created', 'updated']

    def get_fields(self):
        action = self.context.get('action')
        fields = super().get_fields()
        if action == 'list':
            fields.pop('images')
            fields.pop('description_en')
            fields.pop('description_ky')
            fields.pop('created')
        return fields


    def create(self, validated_data):
        request = self.context.get('request')
        images_data = request.FILES
        author = request.user
        problem = Problem.objects.create(author=author, **validated_data)
        for image in images_data.getlist('images'):
            CodeImage.objects.create(problem=problem, image=image)

        return problem


class ReplySerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Reply
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get('request')
        author = request.user
        reply = Reply.objects.create(autho=author, **validated_data)
        return reply

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['images'] = ImageSerializer(instance.images.all(), many=True).data
        representation['replies'] = ReplySerializer(instance.replies.all(), many=True).data
        return representation


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Comment
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get('request')
        author = request.user
        comment = Comment.objects.create(autho=author, **validated_data)
        return comment























#
# class ProblemListSerializer(serializers.ModelSerializer):
#     created = serializers.DateTimeField(format='%d %B %Y %H:%M', read_only=True)
#     author = serializers.ReadOnlyField(source='author.username')
#
#     class Meta:
#         model = Problem
#         fields = ['id', 'title', 'created', 'author']



#
# class ProblemDetailSerializer(serializers.ModelSerializer):
#     created = serializers.DateTimeField(format='%d %B %Y %H:%M', read_only=True)
#     author = serializers.ReadOnlyField(source='author.username')
#
#     class Meta:
#         model = Problem
#         fields = ('id', 'title', 'description', 'author', 'created', 'images')
#
#     def to_representation(self, instance):
#         representation = super().to_representation(instance)
#         representation['images'] = ImageSerializer(instance.images.all(), many=True).data
#         representation['replies'] = ReplySerializer(instance.replies.all(), many=True).data
#         return representation
#
#
# class ProblemUpdateSerializer(serializers.ModelSerializer):
#     images = ImageSerializer(many=True, write_only=True)
#
#     class Meta:
#         model = Problem
#         fields = ['title', 'description', 'images']
#
#     def update(self, instance, validated_data):
#         request = self.context.get('request')
#         title = validated_data.get('title')
#         description = validated_data.get('description')
#         if title:
#             instance.title = title
#         if description:
#             instance.description = description
#         instance.save()
#         instance.title = title
#         instance.description = description
#         images_data = request.FILES
#         for image in images_data.getlist('images'):
#             CodeImage.objects.get_or_create(problem=instance, image=image)
#         return instance