# INTERSTELLAR FİLMİ: KAPSAMLI İZLEYİCİ SEGMENTASYONU VE PAZARLAMA STRATEJİSİ RAPORU

**Tarih:** 18 Ocak 2026  
**Hazırlayan:** Akademik Veri Analiz Asistanı  
**Konu:** Büyük Veri ve Makine Öğrenmesi ile İzleyici Eğilimlerinin ve Motivasyonlarının Derinlemesine Analizi

---

## 1. YÖNETİCİ ÖZETİ VE PROJE KAPSAMI

### 1.1. Projenin Amacı
Bu çalışmanın temel amacı, *Interstellar* gibi kültleşmiş bir bilim kurgu eserinin izleyici üzerindeki etkisini **"Büyük Veri" (Big Data)** perspektifiyle incelemek ve bu verilerden yola çıkarak uygulanabilir, veri odaklı bir **dijital film pazarlama stratejisi** geliştirmektir. Akademik bir yaklaşımla, izleyicilerin sadece ne izlediği değil, *neden* ve *nasıl* etkilendiği (motivasyon analizi) ortaya konmuştur.

### 1.2. Veri Seti ve Çalışma Büyüklüğü
Analiz, toplamda **24.145 adet bağımsız kullanıcı geri bildirimine** dayanmaktadır. Bu hacim, geleneksel anket yöntemlerinin çok ötesinde, istatistiksel olarak anlamlı ve güvenilir sonuçlar sunar.

*   **YouTube Verisi:** 24.123 adet yorum (Genel izleyici, kısa ve anlık tepkiler).
*   **IMDb Verisi:** 22 adet detaylı inceleme (Sinefil kitlesi, uzun ve teknik eleştiriler).
*   **Kullanılan Teknoloji:** Veriler, Python tabanlı yapay zeka algoritmaları (NLP, K-Means Clustering) ile işlenerek 4 farklı izleyici profili modellenmiştir.

### 1.3. Yönetici Özeti (Sonuç)
Analiz sonuçları, görsel efektlerin ötesinde **hikaye derinliği** ve **duygusal bağın** izleyici sadakatinin temel taşları olduğunu ortaya koymaktadır. Rapor, pazarlama stratejilerine yön verecek kritik görsellerin detaylı yorumlanması üzerine kurgulanmıştır.

---

## 2. METODOLOJİ VE VERİ

*   **Veri Kaynağı:** YouTube (Fragmanlar, İncelemeler, "Ending Explained" videoları).
*   **Analiz Yöntemi:**
    *   **K-Means Kümeleme:** İzleyici tiplerini belirlemek için.
    *   **Aspect-Based Sentiment Analysis (ABSA):** Belirli film unsurlarına (müzik, senaryo, bilim) yönelik duyguyu ölçmek için.
    *   **Vektörleştirme:** Kullanıcı yorumlarının anlamsal (semantic) derinliğini yakalamak için.

### 2.1. Veri Kaynakları (YouTube)

Analiz edilen ana veri seti, aşağıdaki yüksek etkileşimli YouTube videolarından derlenmiştir:

| Video Başlığı / Konusu | Video ID | Link |
| :--- | :--- | :--- |
| **Interstellar - Docking Scene (No Time for Caution)** | `j3DuONZb3Ik` | [İzle](https://www.youtube.com/watch?v=j3DuONZb3Ik) |
| **Interstellar - Ending Explained** | `zSWdZVtXT7E` | [İzle](https://www.youtube.com/watch?v=zSWdZVtXT7E) |
| **Interstellar Main Theme - Hans Zimmer** | `BHsFzDON6pA` | [İzle](https://www.youtube.com/watch?v=BHsFzDON6pA) |
| **Interstellar Review (Deep Dive)** | `qhW1HfSuPVQ` | [İzle](https://www.youtube.com/watch?v=qhW1HfSuPVQ) |

---

## 3. İZLEYİCİ SEGMENTASYONU VE KÜME YAPISI

İzleyici kitlesinin homojen olmadığı, belirgin motivasyonlarla ayrıştığı tespit edilmiştir. Bu bölüm, kitlenin genel yapısını ve büyüklüklerini incelemektedir.

### 3.1. İzleyici Segmentlerinin Dağılımı (Pie Chart)

Aşağıdaki pasta grafiği, izleyici kitlesinin oransal dağılımını göstermektedir. Bu görsel, hedef kitlenin ağırlık merkezini belirlemek adına kritiktir.

**(Şekil 3.1: Küme Segmentlerinin Oransal Dağılımı)**
![Küme Dağılımı Pasta Grafiği](outputs/cluster_distribution_pie.png)

**Görsel Analizi ve Yorumu:**
*   **Hakim Grup (%39.1 - Fanlar / Duygusal İzleyiciler):** Grafiğin en büyük dilimi olan bu grup, filmin "sadık müşterileri"dir. Pazarlama bütçesinin korunması ve yeniden pazarlama (remarketing) çalışmaları için ana hedeftir.
*   **Potansiyel Grup (%27.9 - Anlamak İsteyenler):** İkinci büyük dilim, filmi beğenen ancak "kafa karışıklığı" yaşayan kitleyi temsil eder. Bu gruba yönelik açıklayıcı içerikler üretilmesi, onları sadık kitleye dönüştürebilir.
*   **Niş Grup (%22.9 - Bilim Meraklıları):** Filmin "Hard Sci-Fi" yönüne odaklanan entelektüel kesimdir.
*   **Geçici İzleyici (%10.1 - Video Tüketicileri):** En küçük dilim, filme derinlemesine bağlı olmayan, sadece popüler kültür tüketimi yapan kitledir.

---

### 3.2. İzleyici Kitlelerinin Ayrışması (Scatter Plot Analysis)

PCA (Principal Component Analysis) yöntemiyle 4 ana kümenin 2 boyutlu uzayda nasıl ayrıştığı görselleştirilmiştir.

**(Şekil 3.2: Kümelerin PCA Saçılım Grafiği)**
![Küme Saçılım Grafiği](outputs/cluster_scatter.png)

**Görsel Analizi:**
*   **Kümelerin Ayrışması:** Grafikte kümelerin birbirine çok fazla geçmediği, belirgin sınırlarla ayrıldığı görülmektedir. Bu, izleyicilerin "kararsız" olmadığını, herkesin filme çok net bir bakış açısıyla yaklaştığını kanıtlar.
*   **Merkezlerin Konumu:** "Fanlar" (Kırmızı/En Büyük Küme) merkezde ve yoğun bir dağılım gösterirken, "Video Tüketicileri" daha dağınık bir yapıdadır.

---

### 3.3. Küme Büyüklüklerinin Karşılaştırılması (Bar Chart)

Pasta grafiğinin sayısal karşılığı olan bu grafik, her bir segmentin hacmini net bir şekilde ortaya koymaktadır.

**(Şekil 3.3: Segment Büyüklükleri ve Yorum Sayıları)**
![Küme Dağılım Çubuk Grafiği](outputs/cluster_distribution.png)

**Görsel Analizi:**
*   **Fanlar (Cluster 1)**, 9000'i aşkın yorumla tartışmasız liderdir. Bu, filmin kulaktan kulağa (word-of-mouth) yayılma gücünün bu kitle tarafından sağlandığını gösterir.
*   **Bilim Meraklıları (Cluster 2)** ve **Anlamak İsteyenler (Cluster 0)** toplamda kitlenin %50'sinden fazlasını oluşturur. Bu da filmin sadece "izle-geç" değil, "izle-ve-tartış" türünde bir yapım olduğunu kanıtlar.

---

## 4. KÜMELERİN KARAKTERİSTİK ANALİZİ (HEATMAP & DETAY)

Bu bölüm, "Neden bu isimleri verdik?" sorusunun cevabını vererek, her kümenin DNA'sını incelemektedir.

### 4.1. Kümelerin İlgi Alanı Yoğunluk Haritası (Heatmap)

Bu ısı haritası, hangi kümenin hangi konuyu daha yoğun konuştuğunu görselleştirir. Renk koyuluğu, o konunun o küme için ne kadar önemli olduğunu gösterir.

**(Şekil 4.1: Küme-Özellik İlişkisi Isı Haritası)**
![Küme İlişki Isı Haritası](outputs/cluster_aspect_heatmap.png)

**Görsel Analizi ve Stratejik Çıkarımlar:**
*   **Cluster 2 (Bilim Meraklıları) ve "Science/Physics":** Haritada bu kesişimin koyu renkli olması, bu grubun filmi bir "fizik dersi" gibi izlediğini doğrular. Pazarlamada *Kip Thorne* referansları bu gruba yöneliktir.
*   **Cluster 1 (Fanlar) ve "Emotional Impact":** Fan grubunda "Music" ve "Emotional Impact" sütunlarının yoğunluğu, Hans Zimmer'in müziklerinin ve baba-kız dramının bu kitleyi bir arada tutan tutkal olduğunu gösterir.
*   **Cluster 0 (Anlamak İsteyenler) ve "Plot/Story":** Bu grupta hikaye kurgusuna odaklanma yüksektir, çünkü ana problemleri hikayeyi çözmektir.

---

### 4.2. Kümelerin Beğeni ve Eleştiri Dağılımı

Her grubun filme yaklaşımı pozitif veya negatif olarak değişmektedir. Bu görsel, hangi grubun neyi övdüğünü veya yerdiğini detaylandırır.

**(Şekil 4.2: Kümeler Bazında Pozitif/Negatif Özellik Ayrımı)**
![Küme Bazlı Pozitif Negatif Dağılım](outputs/cluster_positive_negative_aspects.png)

**Görsel Analizi:**
*   **Fanlar (Duygusal İzleyiciler):** Görselde pozitif barların (özellikle Müzik ve Görsellik) en yüksek olduğu gruptur. Negatif yorumları neredeyse yok denecek kadar azdır.
*   **Anlamak İsteyenler:** "Clarity (Anlaşılırlık)" ve "Ending (Son)" kategorilerinde negatif barların en uzun olduğu gruptur. Bu görsel, filmin sonunun bu kitle için bir hayal kırıklığı veya kafa karışıklığı kaynağı olduğunu net bir şekilde gösterir.
*   **Bilim Meraklıları:** "Science" kategorisinde pozitif ve negatifin dengeli olduğu görülür (çünkü kendi aralarında bilimsel doğruluğu tartışmaktadırlar).

---

## 5. GENEL DUYGU VE FİLM UNSURLARININ ANALİZİ

İzleyici kitlesinden bağımsız olarak, filmin genel algısını oluşturan güçlü ve zayıf yönler bu bölümde incelenmiştir.

### 5.1. Özellik Bazlı Genel Duygu Analizi

Tüm yorumlar havuzunda, filmin temel bileşenlerine (Senaryo, Oyunculuk, Müzik vb.) yönelik genel sentiment durumu.

**(Şekil 5.1: Film Özelliklerinin Genel Duygu Puanları)**
![Özellik Bazlı Genel Duygu](outputs/aspect_sentiment.png)

**Görsel Analizi:**
*   **En Yüksek Skorlar:** "Music" ve "Visual Effects" barları en sağda (pozitif uçta) yer almaktadır. Bu, filmin teknik başarısının tartışılamaz olduğunu gösterir.
*   **En Düşük Skorlar:** "Clarity" (Anlaşılırlık) barı negatife en yakın olandır. Filmin en zayıf karnı, karmaşık kurgusunun genel izleyici tarafından zor anlaşılmasıdır.

---

### 5.2. En Çok Beğenilen Unsurlar (Pozitif Yönler)

**(Şekil 5.2: Pozitif Özelliklerin Kelime Frekansı ve Ağırlığı)**
![Pozitif Yönler](outputs/positive_aspects.png)

**Görsel Yorumu:**
*   Görselde **"Visuals", "Soundtrack", "Masterpiece"** kelimelerinin baskınlığı görülmektedir.
*   İzleyiciler filmi sadece bir film değil, bir "deneyim" (Experience) olarak tanımlamaktadır. "Emotional" kelimesinin pozitif tarafta yer alması, dramatik yapının başarısını kanıtlar.

### 5.3. En Çok Eleştirilen Unsurlar (Negatif Yönler)

**(Şekil 5.3: Negatif Özelliklerin Kelime Frekansı ve Ağırlığı)**
![Negatif Yönler](outputs/negative_aspects.png)

**Görsel Yorumu:**
*   Görselde **"Confusing", "Long", "Ending"** kelimeleri öne çıkmaktadır.
*   "Boring" (Sıkıcı) ifadesinin varlığı, filmin yavaş temposunun aksiyon odaklı izleyiciler (muhtemelen Video Tüketicileri segmenti) için bir bariyer olduğunu gösterir.
*   "Loud" (Gürültülü) ifadesi, müzik miksajına yönelik spesifik bir teknik eleştiriyi ortaya koymaktadır.

---

## 6. PAZARLAMA İÇİN İZLEYİCİ MOTİVASYONU ANALİZİ

"Senaryo 5" sorularının kalbi olan bu bölüm, izleyicinin filmi **neden** izlediğini ve pazarlamada neyin öne çıkarılması gerektiğini veriye dayalı olarak cevaplar.

**(Şekil 6.1: İzleyici Motivasyon Analizi)**
![İzleyici Motivasyon Analizi](outputs/viewer_motivation_analysis.png)

**Görsel Analizi ve Kritik Bulgular:**
1.  **Hikaye Kraldır (%36.8):** Görsel Efektler (%33) çok güçlü olsa da, izleyicinin ana motivasyonu **Story & Narrative** (Hikaye ve Anlatı) olmuştur.
    *   *Pazarlama Çıkarımı:* Fragmanlarda sadece uzay görüntüleri değil, karakterlerin içsel yolculuğu ve hikayenin gizemi ön planda tutulmalıdır.
2.  **Müzik Bir Çekim Gücüdür (%15.5):** Müzik, bir filmin yan unsuru olmaktan çıkıp, izleyicilerin %15'i için ana izleme veya beğenme sebebi haline gelmiştir. Hans Zimmer markası pazarlamada aktif kullanılmalıdır.
3.  **Bilim ve Felsefe (%9.2):** Azımsanmayacak bir kitle, filmi entelektüel tatmin için izlemektedir.

---

## 7. EK ANALİZ: PLATFORM KARŞILAŞTIRMASI (YOUTUBE vs IMDB)

Analiz kapsamı genişletilerek, YouTube'daki "genel izleyici" ile IMDb'deki "sinefil/eleştirmen" kitlesi arasındaki farklar incelenmiştir. **22 adet detaylı IMDb incelemesi** (uzun formatlı ve yüksek puanlı) ile YouTube yorumları aynı kümeleme algoritması (K-Means) üzerinden karşılaştırılmıştır.

**(Şekil 7.1: YouTube ve IMDb İzleyici Segment Dağılımı)**
![Platform Karşılaştırması](outputs/platform_comparison.png)

**Kritik Bulgular:**

*   **Fan Kümesinin ve Duygusallığın Hakimiyeti:** IMDb incelemelerinde **"Fanlar / Duygusal İzleyiciler" (Cluster 1)** segmenti belirgin bir ağırlığa sahiptir. Kullanıcılar, *Interstellar*'ı sadece bir film olarak değil, hayatlarını değiştiren bir "deneyim" olarak tanımlamakta; "7 yıl sonra bile...", "Hayatımda gördüğüm en iyi film" gibi ifadelerle derin bir sadakat sergilemektedirler.
*   **Teknik ve Bilimsel Takdir:** YouTube'da bilimsel tartışmalar bazen yüzeysel kalırken, IMDb'deki **"Bilim Meraklıları" (Cluster 2)** grubu, *Hans Zimmer*'in müziklerini ve *Hoyte van Hoytema*'nın sinematografisini detaylandırarak filmin teknik başarısını "şaheser" (masterpiece) seviyesinde övmektedir.
*   **Nitelikli İçerik:** IMDb verisetinde kısa veya anlamsız yorumlara (Cluster 3) neredeyse hiç rastlanmamıştır. Bu platformdaki izleyiciler, YouTube'daki "hızlı tüketim" (snack content) alışkanlığının aksine, filme zaman ayıran ve üzerine düşünen (contemplative) bir profildir.

---

## 8. SONUÇ VE STRATEJİK ÖNERİLER

Görsel destekli bu kapsamlı analiz, *Interstellar*'ın başarısının tek bir faktöre indirgenemeyeceğini, aksine **çok katmanlı bir izleyici deneyimi** sunduğunu kanıtlamıştır. Elde edilen veriler ışığında, gelecekteki iletişim ve pazarlama çalışmaları için aşağıdaki **5 maddelik stratejik yol haritası** önerilmektedir:

### 8.1. Platforma Özgü İletişim Stratejisi (Differentiation)
*   **IMDb ve Sinefil Kanalları:** Bu mecrada **"Sanat ve Duygu"** ön plana çıkarılmalıdır. İletişim dili, filmin görsel ihtişamını, Hans Zimmer'in müziklerini ve baba-kız ilişkisinin dramatik derinliğini vurgulamalıdır. ("Bir filmden fazlası", "Sinematik bir şaheser" temaları).
*   **YouTube ve Sosyal Medya:** Bu mecrada **"Merak ve Bilim"** tetiklenmelidir. "Kip Thorne'un kara delik teorisi", "Sonunda ne oldu?" veya "Zaman genişlemesi gerçek mi?" gibi tartışma yaratan içerikler, etkileşimi (yorum ve paylaşım) maksimize edecektir.

### 8.2. "Hans Zimmer Etkisi"nin Kaldıraç Olarak Kullanımı
Veriler göstermektedir ki, **Müzik (Score)**, izleyiciler için sadece bir fon değil, filmin *ruhunu* oluşturan ana elementtir.
*   **Öneri:** Film pazarlamasında soundtrack'in gücü kullanılmaya devam edilmelidir. Konser kayıtları, "kamera arkası müzik yapımı" videoları ve besteci odaklı içerikler, sadık fan kitlesinin (Cluster 1) ilgisini sürekli canlı tutacaktır.

### 8.3. "Karmaşıklığı" Bir Pazarlama Ürününe Dönüştürmek
"Anlaşılırlık" (Clarity) konusundaki negatif skorlar bir dezavantaj değil, fırsattır.
*   **Öneri:** Filmin zor anlaşılması, bir **"Zeka Meydan Okuması" (Intellectual Challenge)** olarak konumlandırılmalıdır. "Sadece dikkatli izleyicilerin fark ettiği detaylar" veya "Filmi anlamak için rehber" tarzı içerikler, hem Cluster 0 (Kafası Karışıklar) grubunu eğitir hem de Cluster 2 (Bilim Meraklıları) grubunun egosunu tatmin eder.

### 8.4. Duygusal Bağı Derinleştirmek (Community Management)
Fan kitlesi (Cluster 1), filme rasyonel değil, duygusal nedenlerle bağlıdır.
*   **Öneri:** "Babanızla izlediğinizde ne hissettiniz?" veya "Murph'ün vedası size ne hatırlatıyor?" gibi duygusal tetikleyiciler içeren topluluk soruları, bu kitlenin etkileşimini artıracaktır.

### 8.5. Uzun Vadeli Marka Sadakati
*Interstellar*, izleyiciler tarafından bir "Kült Klasik" olarak tanımlanmaktadır.
*   **Öneri:** Filmin yıldönümlerinde yapılacak özel gösterimler veya dijital etkinlikler, bu sadık kitlenin ("7 yıl sonra bile izliyorum" diyenlerin) potansiyelini ticari faydaya dönüştürecektir. IMDb'deki yüksek puanlı ve uzun yorumlar, bu markanın "Premium/Prestij" algısını koruduğunun en büyük kanıtıdır.

---

## 9. GENEL DEĞERLENDİRME VE SON SÖZ

**Interstellar**, sadece bir bilim kurgu filmi değil, izleyicilerini hem duygusal hem de entelektüel düzeyde yakalayan nadir bir sinema olayıdır. Büyük veri analiziyle ortaya çıkan "Fan" ve "Bilim Meraklısı" kümeleri, filmin iki kutuplu başarısını kanıtlamaktadır: Bir yanda kalplere dokunan **baba-kız dramı**, diğer yanda zihinleri zorlayan **astrofizik teorileri**.

Bu raporun ortaya koyduğu en net sonuç şudur: **Interstellar doğru bir pazarlama stratejisiyle, sadece "izlenip geçilen" bir film olmaktan çıkıp, yıllarca konuşulan ve tekrar tüketilen bir "kültür ürününe" dönüşme potansiyeline sahiptir.**
