from django.contrib import admin
from .models import Oyuncu, Maç, Haber, GaleriÖğesi


@admin.register(Oyuncu)
class OyuncuAdmin(admin.ModelAdmin):
    list_display = ('ad', 'pozisyon', 'numarası', 'oluşturma_tarihi')
    search_fields = ('ad', 'pozisyon')
    list_filter = ('pozisyon', 'oluşturma_tarihi')


@admin.register(Maç)
class MaçAdmin(admin.ModelAdmin):
    list_display = ('ev_sahibi', 'misafir', 'ev_sahibi_gol', 'misafir_gol', 'tarih', 'durum')
    search_fields = ('ev_sahibi', 'misafir')
    list_filter = ('durum', 'tarih', 'lig')
    date_hierarchy = 'tarih'


@admin.register(Haber)
class HaberAdmin(admin.ModelAdmin):
    list_display = ('başlık', 'yayınlama_tarihi', 'güncellenme_tarihi')
    search_fields = ('başlık', 'içerik')
    list_filter = ('yayınlama_tarihi', 'güncellenme_tarihi')
    date_hierarchy = 'yayınlama_tarihi'


@admin.register(GaleriÖğesi)
class GaleriÖğesiAdmin(admin.ModelAdmin):
    list_display = ('başlık', 'kategori', 'turu', 'sıra', 'oluşturma_tarihi')
    search_fields = ('başlık', 'açıklama')
    list_filter = ('kategori', 'turu', 'oluşturma_tarihi')
    list_editable = ('sıra',)
    fieldsets = (
        ('Temel Bilgiler', {
            'fields': ('başlık', 'açıklama', 'kategori', 'sıra')
        }),
        ('İçerik', {
            'fields': ('turu', 'resim', 'video_dosya', 'video_url')
        }),
    )
    
    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj)
        return fieldsets
