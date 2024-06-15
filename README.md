# Proyek Kedua: Menyelesaikan Permasalahan Jaya Jaya Institut

## Business Understanding
Jaya Jaya Institut merupakan salah satu institusi pendidikan perguruan yang telah berdiri sejak tahun 2000. Hingga saat ini ia telah mencetak banyak lulusan dengan reputasi yang sangat baik. 

### Permasalahan Bisnis
Akan tetapi, terdapat banyak juga siswa yang tidak menyelesaikan pendidikannya alias dropout. Jumlah dropout yang tinggi ini tentunya menjadi salah satu masalah yang besar untuk sebuah institusi pendidikan. Oleh karena itu, Jaya Jaya Institut ingin mendeteksi secepat mungkin siswa yang mungkin akan melakukan dropout sehingga dapat diberi bimbingan khusus.

### Cakupan Proyek
- Mengidentifikasi penyebab tingginya jumlah mahasiswa Jaya Jaya Institut yang melakukan dropout.
- Membuat business dashboard.
- Membuat model machine learning berdasarkan dataset mahasiswa Jaya Jaya Institut untuk memprediksi kemungkinan mahasiswa melakukan dropout.

### Persiapan

Sumber data: Jaya Jaya Institut (https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/main/students_performance/data.csv)

Setup environment Dashboard:

```
docker pull metabase/metabase:v0.46.4
docker run -p 3000:3000 --name metabase metabase/metabase
```

Login Metabase:
```
Username: root@mail.com
Password: root123
```

Setup environment Python - Anaconda:
```
conda create --name students-performance python=3.9
conda activate students-performance
pip install -r requirements.txt
```

Setup environment Python - Terminal:
```
mkdir students_performance
cd students_performance
pipenv install
pipenv shell
pip install -r requirements.txt
```

## Business Dashboard

![image](https://github.com/humamfa/JayaJayaInstitut/assets/152384891/08f5bba3-680f-4713-b103-d866915e04d7)

Business dashboard dapat di-filter berdasarkan status enrollment mahasiswa (Enrolled, Graduate, Dropout).


## Menjalankan Sistem Machine Learning
Jalankan 'run app.bat' untuk membuka prototype machine learning. Dapat juga dijalankan secara manual:
```
python data_preprocessing.py
python prediction.py
streamlit run students_performance_app.py
```

## Conclusion
- Mahasiswa yang dropout memiliki rata-rata nilai yang jauh lebih rendah dibandingkan dengan mahasiswa yang graduate, baik di semester 1 maupun semester 2.
- Jumlah mahasiswa dropout dengan tuition fees yang belum lunas jauh lebih tinggi dibandingkan dengan mahasiswa graduate.

### Rekomendasi Action Items
Berikan beberapa rekomendasi action items yang harus dilakukan Jaya Jaya institut guna menyelesaikan permasalahan atau mencapai target mereka.
- Jaya Jaya Institut perlu mengawasi nilai mahasiswa agar tetap di atas standar.
- Jaya Jaya Institut perlu memastikan agar seluruh mahasiswa mampu untuk membayar tuition fees yang ditetapkan. Institut juga dapat menyediakan program bantuan dana/beasiswa bagi mahasiswa berprestasi yang kurang mampu secara finansial.
