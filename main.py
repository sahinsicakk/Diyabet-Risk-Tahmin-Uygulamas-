import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
from sklearn.metrics import classification_report, confusion_matrix

# Diyabet verilerini okuma
diabetes = pd.read_csv('diabetes.csv')

# Veri kümesindeki korelasyonları görselleştirme
plt.figure(figsize=(12, 10))
sns.heatmap(diabetes.corr(), annot=True, cmap='RdYlGn')  # Isı haritası
plt.show()

# Veri hakkında genel bilgi
diabetes.info(verbose=True)  # Veri türleri, boş değerler vb. hakkında bilgi
print(diabetes.describe())  # Verinin istatistiksel özeti
print(diabetes.shape)  # Verinin satır ve sütun sayısı

# Outcome sütununa göre dağılım
print(diabetes.groupby('Outcome').size())  # Diyabetli ve sağlıklı kişilerin sayısı
p = diabetes.Outcome.value_counts().plot(kind="bar")  # Bar grafiği ile gösterim
plt.show()

# Veriyi eğitim ve test olarak ayırma
X_train, X_test, y_train, y_test = train_test_split(
    diabetes.loc[:, diabetes.columns != 'Outcome'],  # Özellikler
    diabetes['Outcome'],  # Etiketler
    stratify=diabetes['Outcome'],  # Çıkışa göre dengeli bir şekilde ayırma
    random_state=66  # Rastgele durum için sabit değer
)

# KNN algoritmasının başarı analizi için doğruluk oranları
training_accuracy = []  # Eğitim doğruluk oranları
test_accuracy = []  # Test doğruluk oranları
knneighbors_settings = range(1, 11)  # 1 ile 10 arasında komşu sayısı

# Farklı komşu sayıları ile doğruluk oranlarını hesaplama
for n_neighbors in knneighbors_settings:
    knn = KNeighborsClassifier(n_neighbors=n_neighbors)  # KNN modelini oluşturma
    knn.fit(X_train, y_train)  # Modeli eğitim verisiyle eğitme
    training_accuracy.append(knn.score(X_train, y_train))  # Eğitim doğruluğu
    test_accuracy.append(knn.score(X_test, y_test))  # Test doğruluğu

# Doğruluk oranlarını görselleştirme
plt.title("Başarı Analizi")
plt.plot(knneighbors_settings, training_accuracy, label="Eğitim Seti")
plt.plot(knneighbors_settings, test_accuracy, label="Test Seti")
plt.ylabel("Doğruluk Yüzdesi")
plt.xlabel("Komşu Sayısı")
plt.legend()
plt.show()

# En iyi doğruluk oranı için komşu sayısını seçme
knn = KNeighborsClassifier(n_neighbors=9)  # Komşu sayısı 9 seçildi
knn.fit(X_train, y_train)

# Eğitim ve test doğruluk oranları
print(f'Eğitim setinde K-NN doğruluk oranı: {knn.score(X_train, y_train):.2f}')
print(f'Test setinde K-NN doğruluk oranı: {knn.score(X_test, y_test):.2f}')

# Performans değerlendirmesi için karışıklık matrisi
y_pred = knn.predict(X_test)  # Test verisi için tahmin yapma
conf_matrix = confusion_matrix(y_test, y_pred)  # Karışıklık matrisi

# Karışıklık matrisini görselleştirme
sns.heatmap(pd.DataFrame(conf_matrix), annot=True, cmap="YlGnBu", fmt='g')
plt.title('Karışıklık Matrisi', y=1.1)
plt.ylabel('Gerçek Değerler')
plt.xlabel('Tahmin Edilen Değerler')
plt.show()

# Karışıklık matrisi ile birlikte sınıflandırma raporunu gösterme
print(pd.crosstab(y_test, y_pred, rownames=['Gerçek'], colnames=['Tahmin'], margins=True))  # Karışıklık tablosu
print(classification_report(y_test, y_pred))  # F1, precision, recall gibi metrikleri raporlama
