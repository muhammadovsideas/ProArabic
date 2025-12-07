from django.urls import path
from .views import (
    LessonListAPIView, LessonDetailAPIView,
    BookListAPIView, BookDetailAPIView,
    AnnouncementListAPIView, AnnouncementDetailAPIView,
    AboutListAPIView, AboutDetailAPIView,
    CertificateListAPIView, CertificateDetailAPIView,
    ResultsListAPIView, ResultsDetailAPIView
)

urlpatterns = [

    # LESSON
    path('lessons/', LessonListAPIView.as_view(), name='lesson-list'),
    path('lessons/<int:pk>/', LessonDetailAPIView.as_view(), name='lesson-detail'),

    # BOOK
    path('books/', BookListAPIView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailAPIView.as_view(), name='book-detail'),

    # ANNOUNCEMENT
    path('announcements/', AnnouncementListAPIView.as_view(), name='announcement-list'),
    path('announcements/<int:pk>/', AnnouncementDetailAPIView.as_view(), name='announcement-detail'),

    # ABOUT
    path('about/', AboutListAPIView.as_view(), name='about-list'),
    path('about/<int:pk>/', AboutDetailAPIView.as_view(), name='about-detail'),

    # CERTIFICATE
    path('certificates/', CertificateListAPIView.as_view(), name='certificate-list'),
    path('certificates/<int:pk>/', CertificateDetailAPIView.as_view(), name='certificate-detail'),

    # RESULTS
    path('results/', ResultsListAPIView.as_view(), name='results-list'),
    path('results/<int:pk>/', ResultsDetailAPIView.as_view(), name='results-detail'),
]
