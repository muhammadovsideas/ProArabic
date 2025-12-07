from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .serializers import *


# ============================================================
# LESSON (LIST + DETAIL)
# ============================================================

class LessonListAPIView(ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="List lessons with search and ordering",
        manual_parameters=[
            openapi.Parameter("search", openapi.IN_QUERY, type=openapi.TYPE_STRING),
            openapi.Parameter("ordering", openapi.IN_QUERY, type=openapi.TYPE_STRING,
                              enum=["title", "-title", "created_at", "-created_at"]),
        ]
    )
    def get(self, request):
        items = Lesson.objects.all()

        search = request.GET.get("search")
        if search:
            items = items.filter(title__icontains=search)

        ordering = request.GET.get("ordering")
        if ordering in ["title", "-title", "created_at", "-created_at"]:
            items = items.order_by(ordering)

        return Response(LessonSerializer(items, many=True).data)


class LessonDetailAPIView(RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [AllowAny]


# ============================================================
# BOOK (LIST + DETAIL)
# ============================================================

class BookListAPIView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="List books with search and ordering",
        manual_parameters=[
            openapi.Parameter("search", openapi.IN_QUERY, type=openapi.TYPE_STRING),
            openapi.Parameter("ordering", openapi.IN_QUERY, type=openapi.TYPE_STRING,
                              enum=["title", "-title", "created_at", "-created_at"]),
        ]
    )
    def get(self, request):
        items = Book.objects.all()

        search = request.GET.get("search")
        if search:
            items = items.filter(title__icontains=search) | items.filter(author__icontains=search)

        ordering = request.GET.get("ordering")
        if ordering in ["title", "-title", "created_at", "-created_at"]:
            items = items.order_by(ordering)

        return Response(BookSerializer(items, many=True).data)


class BookDetailAPIView(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]


# ============================================================
# ANNOUNCEMENT (LIST + DETAIL)
# ============================================================

class AnnouncementListAPIView(ListAPIView):
    queryset = Announcement.objects.filter(is_active=True)
    serializer_class = AnnouncementSerializer
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="List announcements with search and ordering",
        manual_parameters=[
            openapi.Parameter("search", openapi.IN_QUERY, type=openapi.TYPE_STRING),
            openapi.Parameter("ordering", openapi.IN_QUERY, type=openapi.TYPE_STRING,
                              enum=["created_at", "-created_at"]),
        ]
    )
    def get(self, request):
        items = Announcement.objects.filter(is_active=True)

        search = request.GET.get("search")
        if search:
            items = items.filter(title__icontains=search) | items.filter(description__icontains=search)

        ordering = request.GET.get("ordering")
        if ordering in ["created_at", "-created_at"]:
            items = items.order_by(ordering)

        return Response(AnnouncementSerializer(items, many=True).data)


class AnnouncementDetailAPIView(RetrieveAPIView):
    queryset = Announcement.objects.filter(is_active=True)
    serializer_class = AnnouncementSerializer
    permission_classes = [AllowAny]


# ============================================================
# ABOUT (LIST + DETAIL)
# ============================================================

class AboutListAPIView(ListAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="List about records with search",
        manual_parameters=[
            openapi.Parameter("search", openapi.IN_QUERY, type=openapi.TYPE_STRING),
        ]
    )
    def get(self, request):
        items = About.objects.all()

        search = request.GET.get("search")
        if search:
            items = items.filter(title__icontains=search)

        return Response(AboutSerializer(items, many=True).data)


class AboutDetailAPIView(RetrieveAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer
    permission_classes = [AllowAny]


# ============================================================
# CERTIFICATE (LIST + DETAIL)
# ============================================================

class CertificateListAPIView(ListAPIView):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="List certificates with search",
        manual_parameters=[
            openapi.Parameter("search", openapi.IN_QUERY, type=openapi.TYPE_STRING),
        ]
    )
    def get(self, request):
        items = Certificate.objects.all()

        search = request.GET.get("search")
        if search:
            items = items.filter(name__icontains=search)

        return Response(CertificateSerializer(items, many=True).data)


class CertificateDetailAPIView(RetrieveAPIView):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer
    permission_classes = [AllowAny]


# ============================================================
# RESULTS (LIST + DETAIL)
# ============================================================

class ResultsListAPIView(ListAPIView):
    queryset = Results.objects.all()
    serializer_class = ResultsSerializer
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="List results with search",
        manual_parameters=[
            openapi.Parameter("search", openapi.IN_QUERY, type=openapi.TYPE_STRING),
        ]
    )
    def get(self, request):
        items = Results.objects.all()

        search = request.GET.get("search")
        if search:
            items = items.filter(name__icontains=search) | items.filter(description__icontains=search)

        return Response(ResultsSerializer(items, many=True).data)


class ResultsDetailAPIView(RetrieveAPIView):
    queryset = Results.objects.all()
    serializer_class = ResultsSerializer
    permission_classes = [AllowAny]
