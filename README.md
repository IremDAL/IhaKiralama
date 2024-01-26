# IhaKiralama
### İnsansız Hava Aracı Kiralama Uygulaması 
## AYSEL İREM NUR DAL
## Kod için gereksinimler
Python <br>
Django <br>
PostgreSQL <br>
Postman
### Tanım
İlk olarak projemde bir yetkilendirme işlemi yaptım. Buradaki amacım ihaların olduğu sayfayı uygulamayı kullanan kullanıcıların görmesini engellemekti. Bunu yapma sebebim ise güvenlikten dolayıdır.
<br><br>
<img src="https://github.com/IremDAL/IhaKiralama/blob/main/fotograflar/Ekran%20g%C3%B6r%C3%BCnt%C3%BCs%C3%BC%202024-01-25%20214744.png" alt="alt text" width="900" height="600">
<br><br>
Burada username ve password bilgisini doğru girdiği için kullanıcı sisteme giriş yapabiliyor.
<br><br>
<img src="https://github.com/IremDAL/IhaKiralama/blob/main/fotograflar/Ekran%20g%C3%B6r%C3%BCnt%C3%BCs%C3%BC%202024-01-25%20214822.png" alt="alt text" width="900" height="600">
<br><br>
Hatalı giriş yaptığı için tüm iha bilgilerini içeren sayfaya kullanıcı giriş yapamıyor.
<br><br>
<img src="https://github.com/IremDAL/IhaKiralama/blob/main/fotograflar/Ekran%20g%C3%B6r%C3%BCnt%C3%BCs%C3%BC%202024-01-25%20220328.png" alt="alt text" width="900" height="600">
<br><br>
Admin olup olamdığı bilgileri içeren UserLogin tablom.
<br><br>
<img src="https://github.com/IremDAL/IhaKiralama/blob/main/fotograflar/Ekran%20g%C3%B6r%C3%BCnt%C3%BCs%C3%BC%202024-01-25%20215202.png" alt="alt text"  width="900" height="600">
<br><br>
Bu kısımda ise ihaall tabloma veri ekleme işlemi gerçekleştiriyorum.Veri ekleme işlemi yaparken tablomdaki curency,rentalActive ve isDeleted değerlerim default olarak kendiliğinden gelmektedir.Currency (para birimi) alanı otomatik olarak "TL" olarak gelirken, rentalActive (kiralık mı) ve numbers (iha sayısı) alanlarına ilişkin değerler belirli koşullara bağlı olarak otomatik olarak atanmaktadır. Eğer numbers değeri 0 ise rentalActive değeri 0 olarak gelirken, numbers değeri 0'dan farklı bir değer ise rentalActive değeri 1 olarak atanmaktadır. Ayrıca, isDeleted alanı ise silme işlemi yapılmadığı durumda otomatik olarak 0 değeri ile gelmektedir.
<br><br>
<img src="https://github.com/IremDAL/IhaKiralama/blob/main/fotograflar/Ekran%20g%C3%B6r%C3%BCnt%C3%BCs%C3%BC%202024-01-25%20215225.png" alt="alt text" width="900" height="600">
<br><br>
Bu kısımda ise ihaall tablomdan Id'ye göre silme işlemi yapmaktayım.Bu işlem yapıldıktan sonra verilerim kaybolmuyor ve isDeleted =1 oluyor.
<br><br>
<img src="https://github.com/IremDAL/IhaKiralama/blob/main/fotograflar/Ekran%20g%C3%B6r%C3%BCnt%C3%BCs%C3%BC%202024-01-25%20215102.png" alt="alt text" width="900" height="600">
<br><br>
Burada bütün iha bilgilerimi GET methodu ile alıyorum.
<br><br>
<img src="https://github.com/IremDAL/IhaKiralama/blob/main/fotograflar/Ekran%20g%C3%B6r%C3%BCnt%C3%BCs%C3%BC%202024-01-25%20220256.png" alt="alt text"  width="900" height="600">
<br><br>
ihaall tablom.
<br><br>
<img src="https://github.com/IremDAL/IhaKiralama/blob/main/fotograflar/Ekran%20g%C3%B6r%C3%BCnt%C3%BCs%C3%BC%202024-01-25%20215401.png" alt="alt text" width="900" height="600">
<br><br>
Kullanıcılar bu tablodan isteklerine uygun bilgileri girmektedirler. Amount,currency ve rentalPeriodOver otomatik olarak default gelmektedir.Currency otomatik olarak TL gelmektedir. RentalPeriodOver(kiralama bitti mi) ilk olarak False geliyor.Amount değeri, kullanıcının istediği İnsansız Hava Aracının aylık maliyeti, aylık kiralama süresi,alınacak adet ve TL para birimi çevrim değeri ile çarpılarak otomatik olarak Amount sütununa eklenir. Buradaki item(kaç adet iha istediği) değeri girildikten sonra ihaall da bulunan numbers(toplam iha) değeri otomatik olarak azalmaktadır.
<br><br>
<img src="https://github.com/IremDAL/IhaKiralama/blob/main/fotograflar/Ekran%20g%C3%B6r%C3%BCnt%C3%BCs%C3%BC%202024-01-25%20215330.png" alt="alt text" width="900" height="600">
<br><br>
Burada girilen id silinmiş olup isDeleted =1 olduğu için ve numbers bilgisi de (yani kaç adet olduğu) =0 olduğu için ekleme yaparken başarılı olmamaktadır.
<br><br>
<img src="https://github.com/IremDAL/IhaKiralama/blob/main/fotograflar/Ekran%20g%C3%B6r%C3%BCnt%C3%BCs%C3%BC%202024-01-25%20215603.png" alt="alt text" width="900" height="600">
<br><br>
Burada ise para hesabı yapılıp amount olarak kaydedilmektedir. Kullanıcı işlem yapacağı para birimini seçmesine rağmen sonuç olarak toplam tutar tl cinsinden hesaplanmaktadır.
<br><br>
<img src="https://github.com/IremDAL/IhaKiralama/blob/main/fotograflar/Ekran%20g%C3%B6r%C3%BCnt%C3%BCs%C3%BC%202024-01-25%20220312.png" alt="alt text" width="900" height="600">
<br><br>
ihainformation tablom.
