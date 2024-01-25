# IhaKiralama
### İnsansız Hava Aracı Kiralama Uygulaması 

## Kod için gereksinimler
Python <br>
Django <br>
PostgreSQL <br>
Postman
### Tanım
İlk olarak projemde bir yetkilendirme işlemi yaptım. Buradaki amacım ihaların olduğu sayfayı uygulamayı kullanan kullanıcılaarın görmesini engellemekti. Bunu yapma sebebim ise güvenlikten dolayıdır.
<br><br>
<img src="https://github.com/IremDAL/IhaKiralama/blob/main/fotograflar/Ekran%20g%C3%B6r%C3%BCnt%C3%BCs%C3%BC%202024-01-25%20214744.png" alt="alt text" width="1000" height="500">
<br><br>
Burada username ve password bilgisini doğru giirdiği için sisteme giriş yapabiliyor.
<br><br>
<img src="https://github.com/IremDAL/IhaKiralama/blob/main/fotograflar/Ekran%20g%C3%B6r%C3%BCnt%C3%BCs%C3%BC%202024-01-25%20214822.png" alt="alt text" width="1000" height="500">
<br><br>
Hatalı giriş yaptığı için tüm iha bilgilerini içeren sayfaya giriş yapamıyor.
<br><br>
<img src="https://github.com/IremDAL/IhaKiralama/blob/main/fotograflar/Ekran%20g%C3%B6r%C3%BCnt%C3%BCs%C3%BC%202024-01-25%20220328.png" alt="alt text" width="1000" height="500">
<br><br>
Admin olup olamdığı bilgileri girilen kullanıcı bilgilerim.
<br><br>
<img src="https://github.com/IremDAL/IhaKiralama/blob/main/fotograflar/Ekran%20g%C3%B6r%C3%BCnt%C3%BCs%C3%BC%202024-01-25%20215202.png" alt="alt text"  width="1000" height="500">
<br><br>
Bu kısımda ise ihaall tabloma yeni veri ekleme  işlemi gerçekleştiriyorum.Veri ekleme işlemi yaparken tablomdaki bazı değerler default olarak kendiliğinden geldiği için sadece işime yarayacak verileri post methodum ile alıyorum.
<br><br>
<img src="https://github.com/IremDAL/IhaKiralama/blob/main/fotograflar/Ekran%20g%C3%B6r%C3%BCnt%C3%BCs%C3%BC%202024-01-25%20215225.png" alt="alt text" width="1000" height="500">
<br><br>
Bu kısımda ise ihaall tablomdan id ye göre silme işlemi yapmaktayım.
<br><br>
<img src="https://github.com/IremDAL/IhaKiralama/blob/main/fotograflar/Ekran%20g%C3%B6r%C3%BCnt%C3%BCs%C3%BC%202024-01-25%20215102.png" alt="alt text" width="1000" height="500">
<br><br>
Burada bütün iha bilgilerimi get methodum ile alıyorum.
<br><br>
<img src="https://github.com/IremDAL/IhaKiralama/blob/main/fotograflar/Ekran%20g%C3%B6r%C3%BCnt%C3%BCs%C3%BC%202024-01-25%20220256.png" alt="alt text"  width="1000" height="500">
<br><br>
ihaall tablom.
<br><br>
<img src="https://github.com/IremDAL/IhaKiralama/blob/main/fotograflar/Ekran%20g%C3%B6r%C3%BCnt%C3%BCs%C3%BC%202024-01-25%20215401.png" alt="alt text" width="1000" height="500">
<br><br>
Kullanıcılar bu tablodan isteklerine uygun bilgileri girmekteler. Her bilgiyi eklemelerine gerek yok çünkü amount bilgsi alınan verilerden otomatik olarak hesaplanıp alınmakta diğer veriler ise default olarak gelmektedir.
<br><br>
<img src="https://github.com/IremDAL/IhaKiralama/blob/main/fotograflar/Ekran%20g%C3%B6r%C3%BCnt%C3%BCs%C3%BC%202024-01-25%20215330.png" alt="alt text" width="1000" height="500">
<br><br>
Burada girilen id silinmiş olup isDeleted =0 olduğu için ve numbers bilgisi de (yani kaç adet olduğu) =0 olduğu için ekleme yaparken başarılı olmamaktadır.
<br><br>
<img src="https://github.com/IremDAL/IhaKiralama/blob/main/fotograflar/Ekran%20g%C3%B6r%C3%BCnt%C3%BCs%C3%BC%202024-01-25%20215603.png" alt="alt text" width="1000" height="500">
<br><br>
Burada ise para hesabı yapılıp amount olarak kaydedilmektedir. Kullanıcı işlem yapacağı para birimini seçmesine rağmen spnuç olarak toplam tutar tl cinsinden hesaplanmaktadır.
<br><br>
<img src="https://github.com/IremDAL/IhaKiralama/blob/main/fotograflar/Ekran%20g%C3%B6r%C3%BCnt%C3%BCs%C3%BC%202024-01-25%20220312.png" alt="alt text" width="1000" height="500">
<br><br>
ihainformation tablom.
