# Diyabet Risk Tahmin Uygulaması
 Diyabet, günümüzde dünya çapında hızla artan bir sağlık sorunu olup, doğru tanı ve  erken müdahale ile yönetilebilir. Bu uygulama, bireylerin diyabet riski hakkında bilgi  edinmelerini sağlar. Kullanıcılar, yaş, cinsiyet, vücut kitle indeksi, kan şekeri düzeyi  gibi faktörleri girerek kişisel risklerini öğrenebilirler. 


Bu proje, diyabet hastalığının olasılığını tahmin etmek için kullanılan bir makine öğrenimi modeline dayalıdır. Uygulama, kullanıcının belirttiği sağlık verileri üzerinden diyabet riski tahmini yapar ve aynı zamanda referans dışı verileri kontrol ederek kullanıcıyı bilgilendirir.

## Özellikler

- **Makine Öğrenimi Modeli**: Diyabet tahmini yapmak için K-Nearest Neighbors (KNN) algoritması kullanılmıştır.
- **Veri Seti**: Proje, `diabetes.csv` adlı bir veri seti kullanmaktadır. Bu veri seti, diyabet riski taşıyan bireylerin çeşitli sağlık bilgilerini içermektedir.
- **Tkinter Arayüzü**: Kullanıcı dostu bir grafiksel arayüz (GUI) ile kullanıcıdan yaş, gebelik sayısı, kan şekeri, kan basıncı, cilt kalınlığı, insülin seviyesi, BMI ve diabetes pedigri fonksiyonu gibi sağlık verileri alınır.
- **Referans Değerleri Kontrolü**: Kullanıcı tarafından girilen veriler, referans değerleriyle karşılaştırılarak, anormal veriler belirlenir ve kullanıcıya önerilerde bulunulur.
- **Veri Görselleştirme**: Referans dışı değerler görselleştirilir ve kullanıcıya daha iyi bir analiz sunulur.
- **Excel Çıktısı**: Kullanıcı verileri ve referans dışı değerler, görselleştirme ve önerilerle birlikte Excel dosyasına kaydedilebilir.

## Teknolojiler

- **Python**: Programlama dili.
- **Tkinter**: GUI (grafiksel kullanıcı arayüzü) için.
- **Scikit-Learn**: Makine öğrenimi modelinin eğitiminde kullanıldı.
- **Matplotlib**: Veri görselleştirme için.
- **Pandas**: Veri işleme ve Excel dosyasına yazma işlemleri için.
- **Openpyxl**: Excel dosyası manipülasyonu için.

## Kurulum

1. Projeyi klonlayın:

```bash
git clone https://github.com/kullaniciadi/diyabet-tahmin.git

# Gerekli bağımlılıkları yükleyin:
pip install -r requirements.txt

# Uygulamayı başlatın
python Diabetica.py

# Kullanıcı arayüzü açılacaktır. Burada, aşağıdaki verileri girmeniz gerekecek:

Gebelik sayısı (Pregnancies)
Kan şekeri (Glucose)
Kan basıncı (BloodPressure)
Deri kalınlığı (SkinThickness)
İnsülin seviyesi (Insulin)
BMI (Body Mass Index)
Diabetes pedigri fonksiyonu (DiabetesPedigreeFunction)
Yaş (Age)

"Gönder" butonuna basarak diyabet riskinizi öğrenebilirsiniz.

Referans dışı verilerle ilgili görselleştirmeyi görmek ve önerileri almak için grafikler ve yazılar görüntülenecektir.


