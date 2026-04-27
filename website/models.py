from django.db import models


# Create your models here.
# Model örnekleri eklenebilir - örneğin: Oyuncu, Maç, Haber vb.


class Oyuncu(models.Model):
    """Takım oyuncuları için model"""
    ad = models.CharField(max_length=100)
    pozisyon = models.CharField(max_length=50)
    numarası = models.IntegerField()
    oluşturma_tarihi = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Oyuncu"
        verbose_name_plural = "Oyuncular"
    
    def __str__(self):
        return f"{self.ad} - #{self.numarası}"


class Maç(models.Model):
    """Maç sonuçları ve bilgileri"""
    STATUS_CHOICES = [
        ('kazanıldı', 'Kazanıldı'),
        ('berabere', 'Berabere'),
        ('kaybedildi', 'Kaybedildi'),
        ('gelecek', 'Gelecek'),
    ]
    
    tarih = models.DateTimeField()
    ev_sahibi = models.CharField(max_length=100)
    misafir = models.CharField(max_length=100)
    ev_sahibi_gol = models.IntegerField(default=0)
    misafir_gol = models.IntegerField(default=0)
    lig = models.CharField(max_length=100)
    durum = models.CharField(max_length=20, choices=STATUS_CHOICES, default='gelecek')
    oluşturma_tarihi = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Maç"
        verbose_name_plural = "Maçlar"
    
    def __str__(self):
        return f"{self.ev_sahibi} vs {self.misafir} - {self.tarih.strftime('%d.%m.%Y')}"


class Haber(models.Model):
    """Haber ve duyurular"""
    başlık = models.CharField(max_length=200)
    içerik = models.TextField()
    görsel = models.ImageField(upload_to='haberler/', blank=True, null=True)
    yayınlama_tarihi = models.DateTimeField(auto_now_add=True)
    güncellenme_tarihi = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Haber"
        verbose_name_plural = "Haberler"
        ordering = ['-yayınlama_tarihi']
    
    def __str__(self):
        return self.başlık


class GaleriÖğesi(models.Model):
    """Galeri için resim ve videolar"""
    KATEGORI_CHOICES = [
        ('maçlar', 'Maçlar'),
        ('antrenman', 'Antrenman'),
        ('etkinlik', 'Etkinlikler'),
    ]
    
    TURU_CHOICES = [
        ('resim', 'Resim'),
        ('video', 'Video'),
    ]
    
    başlık = models.CharField(max_length=200)
    açıklama = models.TextField(blank=True)
    kategori = models.CharField(max_length=50, choices=KATEGORI_CHOICES, default='maçlar')
    turu = models.CharField(max_length=10, choices=TURU_CHOICES, default='resim')
    resim = models.ImageField(upload_to='galeri/', blank=True, null=True)
    video_url = models.URLField(blank=True, null=True, help_text="YouTube video URL'sini girin (isteğe bağlı)")
    video_dosya = models.FileField(upload_to='galeri/videos/', blank=True, null=True, help_text="Yerel video dosyası yükleyin (mp4, webm, vb.)")
    oluşturma_tarihi = models.DateTimeField(auto_now_add=True)
    sıra = models.IntegerField(default=0)
    
    class Meta:
        verbose_name = "Galeri Öğesi"
        verbose_name_plural = "Galeri Öğeleri"
        ordering = ['-sıra', '-oluşturma_tarihi']
    
    def __str__(self):
        return f"{self.başlık} ({self.get_turu_display()})"
    
    def is_video(self):
        return self.turu == 'video'
    
    def has_local_video(self):
        """Yerel video dosyası var mı kontrol et"""
        return bool(self.video_dosya)
    
    def has_youtube_video(self):
        """YouTube URL'si var mı kontrol et"""
        return bool(self.video_url)
    
    def get_youtube_id(self):
        """YouTube URL'sinden video ID'sini çıkart - çeşitli URL formatlarını destekler"""
        if not self.video_url:
            return None
        
        import re
        
        # Regex patterns for different YouTube URL formats
        patterns = [
            r'(?:youtube\.com\/watch\?v=|youtube\.com\/\?v=)([a-zA-Z0-9_-]{11})',
            r'(?:youtu\.be\/)([a-zA-Z0-9_-]{11})',
            r'(?:youtube\.com\/embed\/)([a-zA-Z0-9_-]{11})',
            r'(?:youtube\.com\/v\/)([a-zA-Z0-9_-]{11})',
            r'^([a-zA-Z0-9_-]{11})$'
        ]
        
        for pattern in patterns:
            match = re.search(pattern, self.video_url)
            if match:
                return match.group(1)
        
        return None
