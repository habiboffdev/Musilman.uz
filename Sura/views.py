from config.settings import TIME_ZONE
from datetime import tzinfo
from django.shortcuts import render  
from django.views.generic import TemplateView
import requests
from .models import Sura
# Create your views here.
def quran_api(sura):
                
                tafsir = 'uzb-muhammadsodikmu'
                tafsir_url = f'https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/{tafsir}/{sura}.json'
                audio_api_url = f"http://api.alquran.cloud/v1/surah/{sura}/ar.alafasy"
                
                res = requests.get(tafsir_url)
                res2 = requests.get(audio_api_url)
                audio = res2.json()['data']['ayahs']
                tafsir_data = dict()
                
                for l in range(len(res.json()['chapter'])):
                    tafsir_data[l+1]=[(res.json()['chapter'][l]['text']), audio[l]['audio']]
                context = {
                    'tafsir':tafsir_data,}
                return context
class HomePageView(TemplateView):
    template_name = 'index.html'
    def get(self, request):
        city = 'tashkent'
        if request.method == 'GET' and request.GET.get('city'):
            city = request.GET.get('city')
        
        prayer_api_url = f"https://api.pray.zone/v2/times/today.json?city={city}"
        res2 = requests.get(prayer_api_url)
        times = res2.json()['results']['datetime'][0]['times']
        result = "Hech nima topilmadi"
        dic= dict()
        ls = ["Al-Fatiha", "Al-Baqara", "Aal-Imran", "An-Nisaa'", "Al-Ma'ida", "Al-An'am", "Al-A'raf", "Al-Anfal", "Al-Tawba", "Yunus", "Hud", "Yusuf", "Ar-Ra'd", "Ibrahim", "Al-Hijr", "An-Nahl", "Al-Israa", "Al-Kahf", "Maryam", "Ta-Ha", "Al-Anbiya", "Al-Hajj", "Al-Muminun", "An-Nur", "Al-Furqan", "Ash-Shuara", "An-Naml", "Al-Qasas", "Al-Ankabut", "Ar-Rum", "Luqman", "As-Sajdah", "Al-Ahzab", "Saba", "Fatir", "Yasin", "As-Saffat", "Sad", "Az-Zumar", "Ghafir", "Fussilat", "Ash-Shura", "Az-Zukhruf", "Ad-Dukhan", "Al-Jathiya", "Al-Ahqaf", "Muhammad", "Al-Fath", "Al-Hujurat", "Qaf", "Az-Zariyat", "At-Tur", "An-Najm", "Al-Qamar", "Ar-Rahman", "Al-Waqia", "Al-Hadid", "Al-Mujadilah", "Al-Hashr", "Al-Mumtahinah", "As-Saff", "Al-Jumu'ah", "Al-Munafiqun", "At-Taghabun", "At-Talaq", "At-Tahrim", "Al-Mulk", "Al-Qalam", "Al-Haqqah", "Al-Ma'arij", "Nuh", "Al-Jinn", "Al-Muzzammil", "Al-Muddaththir", "Al-Qiyamah", "Al-Insan", "Al-Mursalat", "An-Naba", "An-Naziat", "Abasa", "At-Takwir", "Al-Infitar", "Al-Mutaffifin", "Al-Inshiqaq", "Al-Buruj", "At-Tariq", "Al-Ala", "Al-Ghashiyah", "Al-Fajr", "Al-Balad", "Ash-Shams", "Al-Lail", "Ad-Duha", "Ash-Sharh", "At-Tin", "Al-Alaq", "Al-Qadr", "Al-Bayinah", "Az-Zalzalah", "Al-Adiyat", "Al-Qariah", "Al-Takathur", "Al-Asr", "Al-Humazah", "Al-Fil", "Quraish", "Al-Ma'un", "Al-Kauthar", "Al-Kafirun", "An-Nasr", "Al-Masad", "Al-Ikhlas", "Al-Falaq", "An-Nas"]
        for l in range(114):
            dic[l+1] = ls[l]
        return render(request, self.template_name,{'q':result,
                    'saharlik':times['Imsak'],
                    'quyosh':times['Sunrise'],
                    'bomdod':times['Fajr'],
                    'peshin':times['Dhuhr'],
                    'asr':times['Asr'],
                    'q_bot':times['Sunset'],
                    'shom':times['Maghrib'],
                    'xufton':times['Isha'],
                    'json':dic,})
class ResultViewPage(TemplateView):
    template_name = 'natija.html'
    model = Sura
    def get(self, request):
        sura = request.GET.get('q','')
        if request.GET.get('q'):
            if request.GET.get('q').isdigit():
                context = quran_api(sura)
                natija = self.model.objects.filter(surah_number=sura).all()
                context['data'] = natija[0]
                return render(request, self.template_name,context)
                
            else:
                ls = ["Al-Fatiha", "Al-Baqara", "Aal-Imran", "An-Nisaa'", "Al-Ma'ida", "Al-An'am", "Al-A'raf", "Al-Anfal", "Al-Tawba", "Yunus", "Hud", "Yusuf", "Ar-Ra'd", "Ibrahim", "Al-Hijr", "An-Nahl", "Al-Israa", "Al-Kahf", "Maryam", "Ta-Ha", "Al-Anbiya", "Al-Hajj", "Al-Muminun", "An-Nur", "Al-Furqan", "Ash-Shuara", "An-Naml", "Al-Qasas", "Al-Ankabut", "Ar-Rum", "Luqman", "As-Sajdah", "Al-Ahzab", "Saba", "Fatir", "Yasin", "As-Saffat", "Sad", "Az-Zumar", "Ghafir", "Fussilat", "Ash-Shura", "Az-Zukhruf", "Ad-Dukhan", "Al-Jathiya", "Al-Ahqaf", "Muhammad", "Al-Fath", "Al-Hujurat", "Qaf", "Az-Zariyat", "At-Tur", "An-Najm", "Al-Qamar", "Ar-Rahman", "Al-Waqia", "Al-Hadid", "Al-Mujadilah", "Al-Hashr", "Al-Mumtahinah", "As-Saff", "Al-Jumu'ah", "Al-Munafiqun", "At-Taghabun", "At-Talaq", "At-Tahrim", "Al-Mulk", "Al-Qalam", "Al-Haqqah", "Al-Ma'arij", "Nuh", "Al-Jinn", "Al-Muzzammil", "Al-Muddaththir", "Al-Qiyamah", "Al-Insan", "Al-Mursalat", "An-Naba", "An-Naziat", "Abasa", "At-Takwir", "Al-Infitar", "Al-Mutaffifin", "Al-Inshiqaq", "Al-Buruj", "At-Tariq", "Al-Ala", "Al-Ghashiyah", "Al-Fajr", "Al-Balad", "Ash-Shams", "Al-Lail", "Ad-Duha", "Ash-Sharh", "At-Tin", "Al-Alaq", "Al-Qadr", "Al-Bayinah", "Az-Zalzalah", "Al-Adiyat", "Al-Qariah", "Al-Takathur", "Al-Asr", "Al-Humazah", "Al-Fil", "Quraish", "Al-Ma'un", "Al-Kauthar", "Al-Kafirun", "An-Nasr", "Al-Masad", "Al-Ikhlas", "Al-Falaq", "An-Nas"]
                n = ls.index(sura)
                sura = n+1
                context = quran_api(sura)
                natija = self.model.objects.filter(surah_number=sura).all()
                context['data'] = natija[0]
                return render(request, self.template_name,context)
        else:
            return render(request, self.template_name,{'natija':'hech nima topilmadi'})

def get_qazo(request):
    template_name='qazo.html'
    if request.method == 'POST':
        qazo = request.POST.getlist('xuftonqazo')
        print(qazo)  
    return render(request, template_name,{'qazo':qazo})