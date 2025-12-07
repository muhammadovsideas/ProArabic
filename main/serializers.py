from rest_framework import serializers
from .models import (
    Lesson, LessonImage,
    Book, BookImage,
    SocialLinks,
    Announcement, AnnouncementImage,
    About, AboutImage,
    Certificate, SertificateImage,
    Results, ResultsImage
)

# =============================
# LESSON SERIALIZERS
# =============================

class LessonImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonImage
        fields = ["id", "image"]


class LessonSerializer(serializers.ModelSerializer):
    images = LessonImageSerializer(many=True, read_only=True)

    class Meta:
        model = Lesson
        fields = [
            "id",
            "title",
            "description",
            "video",
            "image",
            "file",
            "created_at",
            "images",
        ]


# =============================
# BOOK SERIALIZERS
# =============================

class BookImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookImage
        fields = ["id", "image"]


class BookSerializer(serializers.ModelSerializer):
    images = BookImageSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = [
            "id",
            "title",
            "description",
            "author",
            "pdf",
            "image",
            "created_at",
            "images",
        ]


# =============================
# SOCIAL LINKS SERIALIZER
# =============================

class SocialLinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialLinks
        fields = "__all__"


# =============================
# ANNOUNCEMENT SERIALIZERS
# =============================

class AnnouncementImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnnouncementImage
        fields = ["id", "image"]


class AnnouncementSerializer(serializers.ModelSerializer):
    images = AnnouncementImageSerializer(many=True, read_only=True)

    class Meta:
        model = Announcement
        fields = [
            "id",
            "title",
            "description",
            "image",
            "created_at",
            "updated_at",
            "is_active",
            "images",
        ]


# =============================
# ABOUT SERIALIZERS
# =============================

class AboutImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutImage
        fields = ["id", "image"]


class AboutSerializer(serializers.ModelSerializer):
    images = AboutImageSerializer(many=True, read_only=True)

    class Meta:
        model = About
        fields = [
            "id",
            "title",
            "description",
            "image",
            "images",
        ]


# =============================
# CERTIFICATE SERIALIZERS
# =============================

class SertificateImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SertificateImage
        fields = ["id", "image"]


class CertificateSerializer(serializers.ModelSerializer):
    images = SertificateImageSerializer(many=True, read_only=True)

    class Meta:
        model = Certificate
        fields = [
            "id",
            "name",
            "description",
            "image",
            "images",
        ]


# =============================
# RESULTS SERIALIZERS
# =============================

class ResultsImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResultsImage
        fields = ["id", "image"]


class ResultsSerializer(serializers.ModelSerializer):
    images = ResultsImageSerializer(many=True, read_only=True)

    class Meta:
        model = Results
        fields = [
            "id",
            "name",
            "description",
            "image",
            "images",
        ]
