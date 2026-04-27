from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.http import JsonResponse
from .models import Oyuncu, Maç, Haber, GaleriÖğesi


def index(request):
    """Ana sayfa"""
    haberler = Haber.objects.all()[:5]
    context = {
        'haberler': haberler,
        'page': 'ana'
    }
    return render(request, 'index.html', context)


def galeri(request):
    """Galeri sayfası"""
    galeri_öğeleri = GaleriÖğesi.objects.all()
    context = {
        'galeri_öğeleri': galeri_öğeleri,
        'page': 'galeri'
    }
    return render(request, 'galeri.html', context)


def takim(request):
    """Takım sayfası"""
    oyuncular = Oyuncu.objects.all()
    context = {
        'oyuncular': oyuncular,
        'page': 'takim',
        'toplam_oyuncu': oyuncular.count(),
        'yabancı_oyuncu': oyuncular.filter(pozisyon__icontains='Yabancı').count(),
    }
    return render(request, 'takim.html', context)


def maclar(request):
    """Maçlar sayfası"""
    tüm_maçlar = Maç.objects.all().order_by('-tarih')
    geçmiş_maçlar = tüm_maçlar.filter(durum__in=['kazanıldı', 'kaybedildi', 'berabere'])
    gelecek_maçlar = tüm_maçlar.filter(durum='gelecek')
    
    context = {
        'tüm_maçlar': tüm_maçlar,
        'geçmiş_maçlar': geçmiş_maçlar,
        'gelecek_maçlar': gelecek_maçlar,
        'page': 'maclar',
        'toplam_maç': geçmiş_maçlar.count(),
        'kazanılan': geçmiş_maçlar.filter(durum='kazanıldı').count(),
        'berabere': geçmiş_maçlar.filter(durum='berabere').count(),
        'kaybedilen': geçmiş_maçlar.filter(durum='kaybedildi').count(),
    }
    return render(request, 'maclar.html', context)


def iletisim(request):
    """İletişim sayfası"""
    context = {'page': 'iletisim'}
    
    if request.method == 'POST':
        # Form işleme - gerçek implementasyonda email gönderme işlemi yapılacak
        ad = request.POST.get('ad')
        email = request.POST.get('email')
        konu = request.POST.get('konu')
        mesaj = request.POST.get('mesaj')
        
        # Email gönderme örneği (activate etmek için settings'de EMAIL_* ayarlarını yapmanız gerekir)
        # from django.core.mail import send_mail
        # send_mail(
        #     subject=f"Yeni İletişim: {konu}",
        #     message=f"Ad: {ad}\nEmail: {email}\n\n{mesaj}",
        #     from_email=settings.DEFAULT_FROM_EMAIL,
        #     recipient_list=['info@karabaglarfk.com']
        # )
        
        context['mesaj_gönderildi'] = True
    
    return render(request, 'iletisim.html', context)


class IndexView(TemplateView):
    """Ana sayfa - class-based view alternatifi"""
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['haberler'] = Haber.objects.all()[:5]
        context['page'] = 'ana'
        return context
import random

def home(request):
    rand = random.randint(1, 10000)
    return render(request, "index.html", {"rand": rand})