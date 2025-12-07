from django.contrib import admin
from django.contrib.auth.models import Group
from .models import *



admin.site.unregister(Group)

# -----------------------------------
# LESSON ADMIN
# -----------------------------------

class LessonImageInline(admin.TabularInline):
    model = LessonImage
    extra = 1


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at")
    search_fields = ("title",)
    inlines = [LessonImageInline]


# -----------------------------------
# BOOK ADMIN
# -----------------------------------

class BookImageInline(admin.TabularInline):
    model = BookImage
    extra = 1


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "created_at")
    search_fields = ("title", "author")
    inlines = [BookImageInline]


# -----------------------------------
# SOCIAL LINKS ADMIN
# -----------------------------------

@admin.register(SocialLinks)
class SocialLinksAdmin(admin.ModelAdmin):
    list_display = ("telegram_channel", "instagram", "youtube", "facebook")


# -----------------------------------
# ANNOUNCEMENT ADMIN
# -----------------------------------

class AnnouncementImageInline(admin.TabularInline):
    model = AnnouncementImage
    extra = 1


@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ("title", "is_active", "created_at")
    list_filter = ("is_active", "created_at")
    search_fields = ("title",)
    inlines = [AnnouncementImageInline]


# -----------------------------------
# ABOUT ADMIN
# -----------------------------------

class AboutImageInline(admin.TabularInline):
    model = AboutImage
    extra = 1


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ("title", "image")
    search_fields = ("title",)
    inlines = [AboutImageInline]


# -----------------------------------
# CERTIFICATE ADMIN
# -----------------------------------

class SertificateImageInline(admin.TabularInline):
    model = SertificateImage
    extra = 1


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("title",)
    inlines = [SertificateImageInline]


# -----------------------------------
# RESULTS ADMIN
# -----------------------------------

class ResultsImageInline(admin.TabularInline):
    model = ResultsImage
    extra = 1


@admin.register(Results)
class ResultsAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("title",)
    inlines = [ResultsImageInline]
