# streamlit_app.py
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Load data
mydata = pd.read_csv("data.csv")

mydata.rename(columns={
    'age': 'usia',
    'gender': 'jenis_kelamin',
    'study_hours_per_day': 'jam_belajar_per_hari',
    'social_media_hours': 'jam_sosmed',
    'netflix_hours': 'jam_netflix',
    'part_time_job': 'kerja_paruh_waktu',
    'attendance_percentage': 'persentase_kehadiran',
    'sleep_hours': 'jam_tidur',
    'diet_quality': 'kualitas_diet',
    'exercise_frequency': 'frekuensi_olahraga',
    'parental_education_level': 'pendidikan_orangtua',
    'internet_quality': 'kualitas_internet',
    'mental_health_rating': 'skor_kesehatan_mental',
    'extracurricular_participation': 'ikut_ekstrakurikuler',
    'exam_score': 'nilai_ujian'
}, inplace=True)



# Buat kategori untuk keperluan visualisasi
mydata['kategori_kehadiran'] = pd.cut(mydata['persentase_kehadiran'], bins=[0, 60, 70, 80, 90, 100], labels=['<60%', '60-70%', '70-80%', '80-90%', '90-100%'])
mydata['kategori_jam_sosmed'] = pd.cut(mydata['jam_sosmed'], bins=[0, 1, 2, 3, 4, 5, 24], labels=['<1 Jam', '1-2 Jam', '2-3 Jam', '3-4 Jam', '4-5 Jam', '>5 Jam'])
mydata['kategori_tidur'] = pd.cut(mydata['jam_tidur'], bins=[0, 4, 5, 6, 7, 8, 24], labels=['<4', '4-5', '5-6', '6-7', '7-8', '>8'])

# Sidebar navigasi
st.sidebar.title("📊 Let's See The Result!")
menu = st.sidebar.radio("Pilih Halaman:", [
    "Main Page",
    "Heatmap",
    "Visualisasi Bar Chart",
    "Visualisasi Boxplot",
    "Visualisasi Diagram Venn",
    "Visualisasi Scatter Plot",
    "Top Pengaruh Akademik"
])

show_code = st.sidebar.checkbox("🧾 Tampilkan Kode")

# Header
st.markdown("""
    <style>
        .main-header {
            background-color: #eee;
            padding: 20px;
            border-radius: 5px;
            text-align: center;
            font-size: 26px;
            font-weight: bold;
            color: #333;
        }
    </style>
    <div class='main-header'>Visualisasi Data Gaya Hidup Mahasiswa dan Kaitannya dengan Performa Akademik</div>
""", unsafe_allow_html=True)

# MAIN PAGE
if menu == "Main Page":
    st.markdown("""
    ---
    **Project Chartastic**  
    ---
    Performa akademik mahasiswa tidak hanya dipengaruhi oleh kemampuan intelektual, tetapi juga oleh kebiasaan hidup sehari-hari.
    Faktor seperti jam tidur, durasi penggunaan media sosial, frekuensi olahraga, dan kondisi kesehatan mental sangat memengaruhi hasil belajar mereka.

    Proyek ini bertujuan untuk memberikan gambaran komprehensif mengenai bagaimana kebiasaan sehari-hari siswa berkorelasi dengan performa akademik mereka. Melalui analisis data yang divisualisasikan dengan baik, diharapkan hasil dari proyek ini tidak hanya menjadi informasi, tetapi juga menjadi bahan refleksi yang kuat bagi siswa, guru, maupun orang tua. Dengan begitu, semua orang dapat lebih memahami bahwa keberhasilan akademik bukan hanya hasil dari belajar keras, tetapi juga dari cara menjalani kehidupan sehari-hari secara seimbang dan sehat.

    ---
    **Sumber Data:** [Student Habits and Performance – Kaggle](https://www.kaggle.com/datasets/jayaantanaath/student-habits-vs-academic-performance)
    """)

    st.markdown("---")
    st.subheader("🗂️ Data Overview")
    st.write("Berikut adalah dataset yang digunakan:")
    st.dataframe(mydata)

    st.markdown("---")
    st.subheader("📑 Penjelasan Kolom")
    st.markdown("""
    - **usia**: Umur mahasiswa
    - **jenis_kelamin**: Laki-laki / Perempuan
    - **jam_belajar_per_hari**: Durasi belajar harian dalam jam
    - **jam_sosmed**: Waktu harian menggunakan media sosial (jam)
    - **jam_netflix**: Waktu menonton hiburan (Netflix, dll)
    - **kerja_paruh_waktu**: Apakah mahasiswa bekerja paruh waktu (Yes/No)
    - **persentase_kehadiran**: Persentase kehadiran kelas
    - **jam_tidur**: Rata-rata jam tidur per hari
    - **kualitas_diet**: Penilaian subjektif kualitas pola makan
    - **frekuensi_olahraga**: Berapa kali olahraga dalam seminggu
    - **pendidikan_orangtua**: Tingkat pendidikan orang tua
    - **kualitas_internet**: Penilaian kualitas koneksi internet
    - **skor_kesehatan_mental**: Penilaian terhadap kesehatan mental (0–100)
    - **ikut_ekstrakurikuler**: Keikutsertaan dalam kegiatan non-akademik
    - **nilai_ujian**: Nilai ujian akhir mahasiswa
    """)
    st.markdown("---")
    st.subheader("**Anggota Kelompok Chartastic**")
    st.markdown(""" 
    - Diah Ayu Puspasari (0110223052)  
    - Eka Kartini (0110223054)  
    - Nurhayati (0110223081)
                """)

# HEATMAP PAGE
elif menu == "Heatmap":
    st.markdown("""
    ---""")
    st.subheader("🔺 Korelasi Antar Variabel Numerik")

    # Hitung korelasi
    num_cols = ['usia', 'jam_belajar_per_hari', 'jam_sosmed', 'jam_netflix',
                'persentase_kehadiran', 'jam_tidur', 'frekuensi_olahraga',
                'skor_kesehatan_mental', 'nilai_ujian']
    corr = mydata[num_cols].corr()

    # Plot heatmap
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f", ax=ax)
    plt.title('Korelasi Antar Variabel Numerik')
    st.pyplot(fig)

    st.markdown("""
    ---
    Dari visualisasi ini menunjukkan hubungan antar berbagai kebiasaan harian dengan nilai ujian. Terlihat jelas bahwa **waktu belajar per hari** punya pengaruh paling besar terhadap nilai ujian, ditunjukkan oleh korelasi yang sangat kuat (**0.83**). Artinya, makin rajin belajar, biasanya nilai ujiannya juga makin bagus.  
    Selain itu, **skor kesehatan mental** juga cukup berpengaruh (**0.32**), jadi kondisi mental yang baik ternyata bisa bantu kita lebih fokus dan perform lebih baik secara akademik. Sementara itu, hal-hal seperti main sosmed, nonton Netflix, atau usia, tidak terlalu banyak pengaruhnya ke nilai. Dari sini bisa disimpulkan bila menjaga waktu belajar dan kondisi mental itu penting untuk hasil belajar yang optimal.
    """)

    if show_code:
        with st.expander("📄 Lihat kode Heatmap"):
            st.code("""
import seaborn as sns
import matplotlib.pyplot as plt

# Pilih kolom numerik
num_cols = ['usia', 'jam_belajar_per_hari', 'jam_sosmed', 'jam_netflix',
            'persentase_kehadiran', 'jam_tidur', 'frekuensi_olahraga',
            'skor_kesehatan_mental', 'nilai_ujian']

# Hitung korelasi
corr = mydata[num_cols].corr()

# Plot heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Korelasi Antar Variabel Numerik')
plt.show()
""")

# BAR CHART PAGE
elif menu == "Visualisasi Bar Chart":
    st.markdown("""
    ---""")
    st.subheader("📊 Bar Chart - Rata-rata Nilai")
    st.markdown("""
    Bar chart adalah salah satu jenis grafik yang paling efektif untuk memperlihatkan **rata-rata atau perbandingan antar kategori**. 
    Dalam konteks proyek ini, visualisasi bar chart digunakan untuk memperlihatkan bagaimana **berbagai kebiasaan mahasiswa**, seperti durasi belajar, tidur, penggunaan media sosial, hingga kehadiran dan pekerjaan paruh waktu, dapat **berkorelasi dengan nilai ujian mereka**.
    """)
    opsi = st.selectbox("Pilih salah satu variabel di bawah ini untuk melihat dampaknya terhadap rata-rata nilai ujian:", [
        "Jam Belajar",
        "Jam Tidur",
        "Jam Sosial Media",
        "Kerja Paruh Waktu",
        "Frekuensi Olahraga",
        "Kehadiran"
    ])
    st.markdown("""
    ---""")
    if opsi == "Jam Belajar":
        mydata['kategori_belajar'] = pd.cut(
            mydata['jam_belajar_per_hari'],
            bins=[0, 1, 2, 3, 4, 5, 24],
            labels=['<1 Jam', '1-2 Jam', '2-3 Jam', '3-4 Jam', '4-5 Jam', '>5 Jam']
        )
        fig = plt.figure(figsize=(10, 6))
        sns.barplot(data=mydata, x='kategori_belajar', y='nilai_ujian', estimator=np.mean, palette='plasma')
        plt.title('Rata-rata Nilai Ujian Berdasarkan Jam Belajar per Hari')
        plt.xlabel('Kategori Jam Belajar')
        plt.ylabel('Rata-rata Nilai Ujian')
        plt.ylim(0, 100)
        plt.grid(True)
        st.pyplot(fig)
        st.markdown("""
        ---
        Visualisasi ini menampilkan rata-rata nilai ujian berdasarkan kategori jam belajar per hari. Terlihat adanya pola yang konsisten: makin lama seseorang belajar, makin tinggi pula rata-rata nilainya. Misalnya, mereka yang belajar lebih dari 5 jam per hari memiliki rata-rata nilai mendekati 90, jauh lebih tinggi dibandingkan dengan kelompok yang belajar kurang dari 1 jam yang rata-ratanya hanya sekitar 40. Grafik ini memperkuat pesan bahwa durasi belajar benar-benar berpengaruh terhadap performa akademik. Dengan kata lain, investasi waktu dalam belajar setiap harinya sangat layak untuk diperjuangkan demi hasil yang lebih baik.
        """)
        if show_code:
            with st.expander("Lihat kode Jam Belajar"):
                st.code("""
mydata['kategori_belajar'] = pd.cut(
    mydata['jam_belajar_per_hari'],
    bins=[0, 1, 2, 3, 4, 5, 24],
    labels=['<1 Jam', '1-2 Jam', '2-3 Jam', '3-4 Jam', '4-5 Jam', '>5 Jam']
)

# Barplot rata-rata nilai per kategori jam belajar
plt.figure(figsize=(10, 6))
sns.barplot(data=mydata, x='kategori_belajar', y='nilai_ujian', estimator='mean', palette='plasma')
plt.title('Rata-rata Nilai Ujian Berdasarkan Jam Belajar per Hari')
plt.xlabel('Kategori Jam Belajar')
plt.ylabel('Rata-rata Nilai Ujian')
plt.ylim(0, 100)
plt.grid(True)
plt.tight_layout()
plt.show()
""")

    elif opsi == "Jam Tidur":
        fig = plt.figure(figsize=(10, 6))
        sns.barplot(data=mydata, x='kategori_tidur', y='nilai_ujian', estimator=np.mean, palette='YlOrRd')
        plt.title('Rata-rata Nilai Ujian Berdasarkan Jam Tidur per Hari')
        plt.xlabel('Kategori Jam Tidur')
        plt.ylabel('Rata-rata Nilai Ujian')
        st.pyplot(fig)
        st.markdown("""
        Visualisasi ini memperlihatkan rata-rata nilai ujian berdasarkan durasi tidur per hari. Terlihat bahwa nilai ujian cenderung meningkat seiring dengan durasi tidur yang cukup, terutama di rentang 6–8 jam per hari. Kelompok yang tidur kurang dari 4 jam memiliki rata-rata nilai paling rendah, sedangkan kelompok yang tidur 7–8 jam memiliki nilai rata-rata tertinggi. Hal ini menunjukkan bahwa kualitas dan kecukupan tidur berperan penting dalam mendukung performa belajar. Tidur yang cukup membantu tubuh dan otak untuk memulihkan energi, sehingga kita bisa belajar dan berpikir lebih efektif saat menghadapi ujian.
        """)
        if show_code:
            with st.expander("Lihat kode Jam Tidur"):
                st.code("""
plt.figure(figsize=(10, 6))
sns.barplot(data=mydata, x='kategori_tidur', y='nilai_ujian', estimator='mean', palette='YlOrRd')
plt.title('Rata-rata Nilai Ujian Berdasarkan Jam Tidur per Hari')
plt.xlabel('Kategori Jam Tidur')
plt.ylabel('Rata-rata Nilai Ujian')
plt.tight_layout()
plt.show()
""")

    elif opsi == "Jam Sosial Media":
        fig = plt.figure()
        sns.barplot(data=mydata, x='kategori_jam_sosmed', y='nilai_ujian', estimator=np.mean, palette='mako')
        plt.title('Rata-rata Nilai Ujian Berdasarkan Jam Sosial Media')
        plt.xlabel('Kategori Jam Sosial Media')
        plt.ylabel('Rata-rata Nilai')
        st.pyplot(fig)
        st.markdown("""
        Rata-rata nilai ujian menurun seiring dengan bertambahnya waktu penggunaan media sosial. Pengguna media sosial kurang dari 1 jam per hari memiliki rata-rata nilai tertinggi, sementara nilai cenderung menurun pada kategori durasi yang lebih tinggi. Meskipun begitu, pada kategori ">5 Jam" terlihat sedikit kenaikan, namun dengan error bar yang lebar, menunjukkan variasi yang besar dalam kelompok ini.
        """)
        if show_code:
            with st.expander("Lihat kode Jam Sosmed"):
                st.code("""
mydata['kategori_jam_sosmed'] = pd.cut(
    mydata['jam_sosmed'],
    bins=[0, 1, 2, 3, 4, 5, 24],
    labels=['<1 Jam', '1-2 Jam', '2-3 Jam', '3-4 Jam', '4-5 Jam', '>5 Jam']
)

# Barplot
sns.barplot(data=mydata, x='kategori_jam_sosmed', y='nilai_ujian', estimator=np.mean, palette='mako')
plt.title('Rata-rata Nilai Ujian Berdasarkan Jam Sosial Media')
plt.xlabel('Kategori Jam Sosial Media')
plt.ylabel('Rata-rata Nilai')
plt.tight_layout()
plt.show()
""")

    elif opsi == "Kerja Paruh Waktu":
        fig = plt.figure()
        sns.barplot(data=mydata, x='kerja_paruh_waktu', y='nilai_ujian', estimator=np.mean, palette='Set2')
        plt.title('Rata-rata Nilai: Mahasiswa Kerja vs Tidak')
        plt.xlabel('Kerja Paruh Waktu')
        plt.ylabel('Rata-rata Nilai')
        st.pyplot(fig)
        st.markdown("""
        Mahasiswa yang tidak bekerja paruh waktu cenderung memiliki nilai ujian sedikit lebih tinggi dibandingkan yang bekerja. Ini mengindikasikan bahwa pekerjaan paruh waktu bisa sedikit mengganggu fokus atau waktu belajar mahasiswa, meskipun perbedaannya relatif kecil.
        """)
        if show_code:
            with st.expander("Lihat kode Kerja Paruh Waktu"):
                st.code("""
sns.barplot(data=mydata, x='kerja_paruh_waktu', y='nilai_ujian', estimator=np.mean, palette='Set2')
plt.title('Rata-rata Nilai: Mahasiswa Kerja vs Tidak')
plt.xlabel('Kerja Paruh Waktu')
plt.ylabel('Rata-rata Nilai')
plt.tight_layout()
plt.show()
""")

    elif opsi == "Frekuensi Olahraga":
        fig = plt.figure()
        sns.barplot(data=mydata, x='frekuensi_olahraga', y='nilai_ujian', estimator=np.mean, palette='YlGnBu')
        plt.title('Rata-rata Nilai Ujian Berdasarkan Frekuensi Olahraga')
        plt.xlabel('Hari Olahraga per Minggu')
        plt.ylabel('Rata-rata Nilai')
        st.pyplot(fig)
        st.markdown("""
        Frekuensi olahraga yang lebih tinggi berkorelasi positif dengan rata-rata nilai ujian. Mahasiswa yang berolahraga 5–6 kali seminggu menunjukkan performa akademik tertinggi. Ini menyiratkan bahwa kebiasaan hidup sehat, khususnya olahraga teratur, mungkin mendukung kinerja belajar dan konsentrasi.
        """)
        if show_code:
            with st.expander("Lihat kode Olahraga"):
                st.code("""
sns.barplot(data=mydata, x='frekuensi_olahraga', y='nilai_ujian', estimator=np.mean, palette='YlGnBu')
plt.title('Rata-rata Nilai Ujian Berdasarkan Frekuensi Olahraga')
plt.xlabel('Hari Olahraga per Minggu')
plt.ylabel('Rata-rata Nilai')
plt.tight_layout()
plt.show()
""")

    elif opsi == "Kehadiran":
        fig = plt.figure()
        sns.barplot(data=mydata, x='kategori_kehadiran', y='nilai_ujian', estimator=np.mean, palette='rocket')
        plt.title('Rata-rata Nilai Ujian Berdasarkan Kategori Kehadiran')
        plt.xlabel('Kategori Kehadiran')
        plt.ylabel('Rata-rata Nilai')
        st.pyplot(fig)
        st.markdown("""
        Terdapat hubungan positif antara tingkat kehadiran dan rata-rata nilai ujian. Semakin tinggi persentase kehadiran, semakin tinggi pula rata-rata nilai yang diperoleh mahasiswa. Kelompok dengan kehadiran 90–100% memiliki rata-rata nilai tertinggi, sedangkan kelompok dengan kehadiran di bawah 60% memiliki nilai terendah. Hal ini menunjukkan bahwa partisipasi aktif dalam perkuliahan berkontribusi signifikan terhadap pencapaian akademik yang lebih baik.
        """)
        if show_code:
            with st.expander("Lihat kode Kehadiran"):
                st.code("""
mydata['kategori_kehadiran'] = pd.cut(
    mydata['persentase_kehadiran'],
    bins=[0, 60, 70, 80, 90, 100],
    labels=['<60%', '60-70%', '70-80%', '80-90%', '90-100%']
)

sns.barplot(data=mydata, x='kategori_kehadiran', y='nilai_ujian', estimator=np.mean, palette='rocket')
plt.title('Rata-rata Nilai Ujian Berdasarkan Kategori Kehadiran')
plt.xlabel('Kategori Kehadiran')
plt.ylabel('Rata-rata Nilai')
plt.tight_layout()
plt.show()
""")

# BOX PLOT PAGE
elif menu == "Visualisasi Boxplot":
    st.markdown("""
    ---""")
    st.subheader("📦 Boxplot - Distribusi Nilai Ujian")
    st.markdown("""
    Boxplot digunakan untuk memperlihatkan **distribusi nilai** dari suatu variabel berdasarkan kategori tertentu. 
    Dalam konteks proyek ini, visualisasi boxplot membantu melihat **keragaman, median, dan potensi outlier** pada nilai ujian mahasiswa berdasarkan faktor-faktor seperti jam belajar, tidur, penggunaan media sosial, dan pekerjaan.
    """)
    opsi = st.selectbox("Pilih Variabel:", [
        "Jam Belajar",
        "Jam Tidur",
        "Jam Sosial Media",
        "Kerja Paruh Waktu"
    ])
    st.markdown("""
    ---""")
    if opsi == "Jam Belajar":
        mydata['kategori_belajar'] = pd.cut(mydata['jam_belajar_per_hari'],
            bins=[0, 1, 2, 3, 4, 5, 24],
            labels=['<1 Jam', '1-2 Jam', '2-3 Jam', '3-4 Jam', '4-5 Jam', '>5 Jam'])
        fig = plt.figure(figsize=(10, 6))
        sns.boxplot(data=mydata, x='kategori_belajar', y='nilai_ujian', palette='coolwarm')
        plt.title('Distribusi Nilai Ujian Berdasarkan Kategori Jam Belajar')
        plt.xlabel('Jam Belajar per Hari')
        plt.ylabel('Nilai Ujian')
        plt.grid(True)
        st.pyplot(fig)
        st.markdown("""
        Visualisasi ini menunjukkan distribusi nilai ujian berdasarkan durasi jam belajar per hari. Terlihat jelas bahwa semakin lama seseorang belajar, nilai ujiannya cenderung semakin tinggi. Misalnya, mereka yang belajar lebih dari 5 jam per hari memiliki nilai median yang sangat tinggi dan stabil, dibandingkan dengan kelompok yang belajar kurang dari 1 jam yang nilai ujiannya cenderung rendah dan lebih tersebar. Pola ini memperkuat pesan bahwa waktu belajar memang punya pengaruh besar terhadap hasil ujian. Jadi, makin konsisten kita meluangkan waktu untuk belajar, makin besar juga peluang kita untuk meraih nilai yang lebih baik.
        """)
        if show_code:
            with st.expander("Lihat kode Boxplot Jam Belajar"):
                st.code("""
# Kelompokkan jam belajar ke dalam kategori
mydata['kategori_belajar'] = pd.cut(mydata['jam_belajar_per_hari'],
    bins=[0, 1, 2, 3, 4, 5, 24], labels=['<1 Jam', '1-2 Jam', '2-3 Jam', '3-4 Jam', '4-5 Jam', '>5 Jam'])

plt.figure(figsize=(10, 6))
sns.boxplot(data=mydata, x='kategori_belajar', y='nilai_ujian', palette='coolwarm')
plt.title('Distribusi Nilai Ujian Berdasarkan Kategori Jam Belajar')
plt.xlabel('Jam Belajar per Hari')
plt.ylabel('Nilai Ujian')
plt.grid(True)
plt.show()
""")

    elif opsi == "Jam Tidur":
        mydata['kategori_tidur'] = pd.cut(
            mydata['jam_tidur'],
            bins=[0, 4, 5, 6, 7, 8, 24],
            labels=['<4 Jam', '4-5 Jam', '5-6 Jam', '6-7 Jam', '7-8 Jam', '>8 Jam']
        )
        fig = plt.figure(figsize=(10, 6))
        sns.boxplot(data=mydata, x='kategori_tidur', y='nilai_ujian', palette='BuGn')
        plt.title('Distribusi Nilai Ujian Berdasarkan Kategori Jam Tidur')
        plt.xlabel('Jam Tidur per Hari')
        plt.ylabel('Nilai Ujian')
        st.pyplot(fig)
        st.markdown("""
        Visualisasi ini menunjukkan distribusi nilai ujian berdasarkan kategori durasi tidur per hari. Secara umum, terlihat bahwa semakin cukup durasi tidurnya—terutama di rentang 6 hingga 8 jam atau lebih—nilai ujian cenderung lebih tinggi dan stabil. Sementara itu, mereka yang tidur kurang dari 4 jam memiliki nilai median yang lebih rendah, dengan sebaran yang lebih sempit. Artinya, kekurangan tidur bisa berdampak negatif terhadap performa akademik. Jadi, selain belajar yang cukup, menjaga waktu tidur juga penting agar tubuh dan pikiran tetap optimal dalam menghadapi ujian.
        """)
        if show_code:
            with st.expander("Lihat kode Boxplot Jam Tidur"):
                st.code("""
mydata['kategori_tidur'] = pd.cut(
    mydata['jam_tidur'],
    bins=[0, 4, 5, 6, 7, 8, 24],
    labels=['<4 Jam', '4-5 Jam', '5-6 Jam', '6-7 Jam', '7-8 Jam', '>8 Jam']
)

plt.figure(figsize=(10, 6))
sns.boxplot(data=mydata, x='kategori_tidur', y='nilai_ujian', palette='BuGn')
plt.title('Distribusi Nilai Ujian Berdasarkan Kategori Jam Tidur')
plt.xlabel('Jam Tidur per Hari')
plt.ylabel('Nilai Ujian')
plt.tight_layout()
plt.show()
""")

    elif opsi == "Jam Sosial Media":
        fig = plt.figure(figsize=(10, 6))
        sns.boxplot(data=mydata, x='kategori_jam_sosmed', y='nilai_ujian', palette='crest')
        plt.title('Distribusi Nilai Ujian Berdasarkan Jam Sosial Media')
        plt.xlabel('Kategori Jam Sosial Media')
        plt.ylabel('Nilai Ujian')
        st.pyplot(fig)
        st.markdown("""
        Dari visualisasi distribusi nilai ujian ini terlihat, distribusi nilai ujian semakin menyebar dan tidak stabil seiring bertambahnya waktu di media sosial. Kategori dengan durasi lebih pendek (<1 jam dan 1–2 jam) cenderung memiliki median nilai lebih tinggi dan distribusi yang lebih rapat. Sementara pada kategori durasi lebih lama (3 jam ke atas), nilai ujian lebih bervariasi dengan banyak outlier dan penyebaran yang lebar, mengindikasikan performa akademik yang tidak konsisten.
        """)
        if show_code:
            with st.expander("Lihat kode Boxplot Sosmed"):
                st.code("""
sns.boxplot(data=mydata, x='kategori_jam_sosmed', y='nilai_ujian', palette='crest')
plt.title('Distribusi Nilai Ujian Berdasarkan Jam Sosial Media')
plt.xlabel('Kategori Jam Sosial Media')
plt.ylabel('Nilai Ujian')
plt.tight_layout()
plt.show()
""")

    elif opsi == "Kerja Paruh Waktu":
        fig = plt.figure(figsize=(10, 6))
        sns.boxplot(data=mydata, x='kerja_paruh_waktu', y='nilai_ujian', palette='Set3')
        plt.title('Distribusi Nilai: Mahasiswa Kerja vs Tidak')
        plt.xlabel('Kerja Paruh Waktu')
        plt.ylabel('Nilai Ujian')
        st.pyplot(fig)
        st.markdown("""
        Distribusi nilai mahasiswa yang tidak bekerja menunjukkan lebih banyak variasi dan beberapa nilai ekstrem (outlier rendah), sementara mahasiswa yang bekerja memiliki distribusi yang lebih stabil. Ini bisa berarti bahwa meskipun bekerja tidak terlalu menurunkan rata-rata nilai, mahasiswa yang tidak bekerja memiliki kemungkinan nilai sangat rendah atau sangat tinggi yang lebih besar.
        """)
        if show_code:
            with st.expander("Lihat kode Boxplot Kerja"):
                st.code("""
sns.boxplot(data=mydata, x='kerja_paruh_waktu', y='nilai_ujian', palette='Set3')
plt.title('Distribusi Nilai: Mahasiswa Kerja vs Tidak')
plt.xlabel('Kerja Paruh Waktu')
plt.ylabel('Nilai Ujian')
plt.tight_layout()
plt.show()
""")

# DIAGRAM LINGKARAN PAGE
elif menu == "Visualisasi Diagram Venn":
    st.markdown("""
    ---
    """)
    st.subheader("🟣 Diagram Pie - Distribusi Kebiasaan Mahasiswa")
    st.markdown("""
    Pie chart digunakan untuk memperlihatkan proporsi atau distribusi kategori dalam suatu variabel. 
    Dalam proyek ini, visualisasi pie chart memberikan gambaran menyeluruh tentang **komposisi kebiasaan mahasiswa**, seperti jenis kelamin, durasi belajar, waktu tidur, sosmed, dan Netflix.
    """)
    opsi = st.selectbox("Pilih salah satu variabel di bawah ini untuk melihat sebaran distribusinya:", [
        "Jenis Kelamin",
        "Jam Belajar",
        "Jam Sosial Media",
        "Jam Netflix",
        "Jam Tidur"
    ])
    st.markdown("""
    ---
    """)
    # Mengisi nilai 'Other' pada jenis_kelamin dengan modus
    mydata['jenis_kelamin'] = mydata['jenis_kelamin'].replace('Other', mydata['jenis_kelamin'].mode()[0])

    if opsi == "Jenis Kelamin":
        fig, ax = plt.subplots()
        mydata['jenis_kelamin'].value_counts().plot.pie(
            autopct='%1.1f%%',
            startangle=90,
            colors=['#66b3ff','#ff9999'],
            ax=ax
        )
        ax.set_ylabel('')
        ax.set_title('Distribusi Jenis Kelamin')
        st.pyplot(fig)
        st.markdown("""
        Visualisasi diagram pie dengan judul “Distribusi Jenis Kelamin” menggambarkan proporsi antara jenis kelamin perempuan dan laki-laki dalam dataset. Berdasarkan grafik tersebut, diketahui bahwa persentase perempuan (Female) sebesar 52,3%, sementara laki-laki (Male) sebesar 47,7%. Selisih sebesar 4,6% menunjukkan bahwa jumlah perempuan sedikit lebih banyak dibandingkan laki-laki. Meskipun demikian, distribusinya tergolong seimbang sehingga memungkinkan analisis lanjutan berdasarkan gender dilakukan secara adil. Komposisi yang relatif merata ini juga memberikan representasi yang baik untuk masing-masing kelompok, sehingga hasil analisis dapat dianggap mencerminkan kondisi populasi dalam dataset secara keseluruhan.
        """)
        if show_code:
            with st.expander("Lihat kode Jenis Kelamin"):
                st.code("""
# Mengisi jenis_kelamin 'Other' dengan modus
mydata['jenis_kelamin'] = mydata['jenis_kelamin'].replace('Other', mydata['jenis_kelamin'].mode()[0])

# Pie chart
mydata['jenis_kelamin'].value_counts().plot.pie(
    autopct='%1.1f%%',
    startangle=90,
    colors=['#66b3ff','#ff9999']
)
plt.ylabel('')
plt.title('Distribusi Jenis Kelamin')
plt.show()
""")
    elif opsi == "Jam Belajar":
        def kategori_jam_belajar(jam):
            if jam < 1:
                return '<1 Jam'
            elif jam < 2:
                return '1-2 Jam'
            elif jam < 3:
                return '2-3 Jam'
            elif jam < 4:
                return '3-4 Jam'
            elif jam < 5:
                return '4-5 Jam'
            else:
                return '>5 Jam'
        
        mydata['kategori_jam_belajar'] = mydata['jam_belajar_per_hari'].apply(kategori_jam_belajar)
        fig, ax = plt.subplots()
        mydata['kategori_jam_belajar'].value_counts().sort_index().plot.pie(
            autopct='%1.1f%%',
            startangle=90,
            colors=['#3b0a45', '#6a0d83', '#a03b8f', '#c35d75', '#db8b4d', '#e2b93b'],
            ax=ax
        )
        ax.set_ylabel('')
        ax.set_title('Distribusi Kategori Jam Belajar')
        st.pyplot(fig)
        st.markdown("""
        Visualisasi diagram pie ini menunjukkan distribusi waktu belajar yang dikelompokkan ke dalam beberapa kategori jam. Kategori dengan proporsi terbesar adalah 3–4 jam, yaitu sebesar 28,1%, disusul oleh kategori 4–5 jam sebesar 21,8%, dan 2–3 jam sebesar 20,1%. Hal ini mengindikasikan bahwa sebagian besar individu dalam dataset memiliki kebiasaan belajar yang cukup intensif, yaitu antara 2 hingga 5 jam per hari. Sementara itu, kategori >5 jam tercatat sebanyak 16,7%, menunjukkan bahwa ada pula sebagian yang memiliki waktu belajar sangat tinggi. Sebaliknya, persentase terendah terdapat pada kategori <1 jam, yaitu hanya 3,9%, yang menunjukkan bahwa hanya sedikit individu yang memiliki durasi belajar sangat singkat.
        """)
        if show_code:
            with st.expander("Lihat kode Jam Belajar"):
                st.code("""
def kategori_jam_belajar(jam):
    if jam < 1:
        return '<1 Jam'
    elif jam < 2:
        return '1-2 Jam'
    elif jam < 3:
        return '2-3 Jam'
    elif jam < 4:
        return '3-4 Jam'
    elif jam < 5:
        return '4-5 Jam'
    else:
        return '>5 Jam'

mydata['kategori_jam_belajar'] = mydata['jam_belajar_per_hari'].apply(kategori_jam_belajar)

mydata['kategori_jam_belajar'].value_counts().sort_index().plot.pie(
    autopct='%1.1f%%',
    startangle=90,
    colors=['#3b0a45', '#6a0d83', '#a03b8f', '#c35d75', '#db8b4d', '#e2b93b']
)
plt.ylabel('')
plt.title('Distribusi Kategori Jam Belajar')
plt.show()
""")

    elif opsi == "Jam Sosial Media":
        def kategori_jam_sosmed(jam):
            if jam < 1:
                return '<1 Jam'
            elif jam < 2:
                return '1-2 Jam'
            elif jam < 3:
                return '2-3 Jam'
            elif jam < 4:
                return '3-4 Jam'
            elif jam < 5:
                return '4-5 Jam'
            else:
                return '>5 Jam'

        mydata['kategori_jam_sosmed'] = mydata['jam_sosmed'].apply(kategori_jam_sosmed)
        kategori_urut = ['<1 Jam', '1-2 Jam', '2-3 Jam', '3-4 Jam', '4-5 Jam', '>5 Jam']
        data_sosmed = mydata['kategori_jam_sosmed'].value_counts().reindex(kategori_urut)
        colors = ['#d4b5f9', '#c7a1f7', '#ba8df4', '#ae7bf2', '#a268f0', '#9556ee']

        fig, ax = plt.subplots(figsize=(6, 6))
        ax.pie(
            data_sosmed,
            labels=data_sosmed.index,
            autopct='%1.1f%%',
            startangle=90,
            colors=colors,
            wedgeprops={'edgecolor': 'white'}
        )
        ax.set_title('Distribusi Waktu Bermain Sosial Media')
        st.pyplot(fig)
        st.markdown("""
        Visualisasi ini menunjukkan distribusi durasi waktu yang dihabiskan untuk bermain media sosial dalam satu hari. Kategori yang paling dominan adalah 2–3 jam, dengan persentase sebesar 31,1%, diikuti oleh 3–4 jam sebanyak 25,1%, serta 1–2 jam sebesar 22,7%. Hal ini menunjukkan bahwa mayoritas individu dalam dataset menghabiskan antara 1 hingga 4 jam per hari di media sosial, yang merupakan durasi yang cukup signifikan.
        """)
        if show_code:
            with st.expander("Lihat kode Jam Sosial Media"):
                st.code("""
def kategori_jam_sosmed(jam):
    if jam < 1:
        return '<1 Jam'
    elif jam < 2:
        return '1-2 Jam'
    elif jam < 3:
        return '2-3 Jam'
    elif jam < 4:
        return '3-4 Jam'
    elif jam < 5:
        return '4-5 Jam'
    else:
        return '>5 Jam'

mydata['kategori_jam_sosmed'] = mydata['jam_sosmed'].apply(kategori_jam_sosmed)
kategori_urut = ['<1 Jam', '1-2 Jam', '2-3 Jam', '3-4 Jam', '4-5 Jam', '>5 Jam']
data_sosmed = mydata['kategori_jam_sosmed'].value_counts().reindex(kategori_urut)

plt.pie(
    data_sosmed,
    labels=data_sosmed.index,
    autopct='%1.1f%%',
    startangle=90,
    colors=['#d4b5f9', '#c7a1f7', '#ba8df4', '#ae7bf2', '#a268f0', '#9556ee'],
    wedgeprops={'edgecolor': 'white'}
)
plt.title('Distribusi Waktu Bermain Sosial Media')
plt.tight_layout()
plt.show()
""")

    elif opsi == "Jam Netflix":
        def kategori_jam_netflix(jam):
            if jam < 1:
                return '<1 Jam'
            elif jam < 2:
                return '1-2 Jam'
            elif jam < 3:
                return '2-3 Jam'
            elif jam < 4:
                return '3-4 Jam'
            elif jam < 5:
                return '4-5 Jam'
            else:
                return '>5 Jam'

        mydata['kategori_jam_netflix'] = mydata['jam_netflix'].apply(kategori_jam_netflix)
        kategori_urut = ['<1 Jam', '1-2 Jam', '2-3 Jam', '3-4 Jam', '4-5 Jam', '>5 Jam']
        data_netflix = mydata['kategori_jam_netflix'].value_counts().reindex(kategori_urut)
        fig, ax = plt.subplots()
        ax.pie(
            data_netflix,
            labels=data_netflix.index,
            autopct='%1.1f%%',
            startangle=90,
            wedgeprops={'edgecolor': 'white'}
        )
        ax.set_title('Distribusi Waktu Menonton Netflix')
        st.pyplot(fig)
        st.markdown("""
        Visualisasi pie chart ini menampilkan distribusi durasi waktu yang dihabiskan untuk menonton Netflix dalam satu hari. Kategori yang paling dominan adalah 1–2 jam dengan persentase sebesar 30,4%, diikuti oleh 2–3 jam sebesar 29,8%, serta <1 jam sebanyak 23,8%. Hal ini mengindikasikan bahwa sebagian besar individu menonton Netflix dalam durasi yang relatif singkat hingga sedang.
        """)
        if show_code:
            with st.expander("Lihat kode Jam Netflix"):
                st.code("""
def kategori_jam_netflix(jam):
    if jam < 1:
        return '<1 Jam'
    elif jam < 2:
        return '1-2 Jam'
    elif jam < 3:
        return '2-3 Jam'
    elif jam < 4:
        return '3-4 Jam'
    elif jam < 5:
        return '4-5 Jam'
    else:
        return '>5 Jam'

mydata['kategori_jam_netflix'] = mydata['jam_netflix'].apply(kategori_jam_netflix)
kategori_urut = ['<1 Jam', '1-2 Jam', '2-3 Jam', '3-4 Jam', '4-5 Jam', '>5 Jam']
data_netflix = mydata['kategori_jam_netflix'].value_counts().reindex(kategori_urut)

plt.pie(
    data_netflix,
    labels=data_netflix.index,
    autopct='%1.1f%%',
    startangle=90,
    colors=colors,
    wedgeprops={'edgecolor': 'white'}
)
plt.title('Distribusi Waktu Menonton Netflix')
plt.tight_layout()
plt.show()
""")

    elif opsi == "Jam Tidur":
        def kategori_jam_tidur(jam):
            if jam < 1:
                return '<1 Jam'
            elif jam < 2:
                return '1-2 Jam'
            elif jam < 3:
                return '2-3 Jam'
            elif jam < 4:
                return '3-4 Jam'
            elif jam < 5:
                return '4-5 Jam'
            else:
                return '>5 Jam'

        mydata['kategori_jam_tidur'] = mydata['jam_tidur'].apply(kategori_jam_tidur)
        kategori_urut = ['<1 Jam', '1-2 Jam', '2-3 Jam', '3-4 Jam', '4-5 Jam', '>5 Jam']
        data_tidur = mydata['kategori_jam_tidur'].value_counts().reindex(kategori_urut).fillna(0)
        cmap = plt.cm.tab20
        colors = [cmap(i / len(data_tidur)) for i in range(len(data_tidur))]

        fig, ax = plt.subplots(figsize=(7, 7))
        wedges, texts, autotexts = ax.pie(
            data_tidur,
            autopct='%1.1f%%',
            startangle=90,
            colors=colors,
            wedgeprops={'edgecolor': 'white'},
            pctdistance=0.8,
            labeldistance=1.2
        )
        for text in texts:
            text.set_visible(False)

        ax.set_title('Distribusi Waktu Tidur')
        ax.legend(wedges, data_tidur.index, title="Kategori", loc="center left", bbox_to_anchor=(1, 0.5))
        st.pyplot(fig)
        st.markdown("""
        Visualisasi pie chart ini menggambarkan distribusi durasi waktu tidur responden dalam satu hari. Mayoritas individu memiliki waktu tidur dalam kategori 4–5 jam, dengan persentase sangat dominan yaitu sebesar 89,1%. Hal ini bisa menjadi perhatian penting karena durasi tidur yang terlalu pendek dapat berdampak pada kesehatan fisik dan mental, serta menurunkan produktivitas dan konsentrasi sehari-hari.
        """)
        if show_code:
            with st.expander("Lihat kode Jam Tidur"):
                st.code("""
def kategori_jam_tidur(jam):
    if jam < 1:
        return '<1 Jam'
    elif jam < 2:
        return '1-2 Jam'
    elif jam < 3:
        return '2-3 Jam'
    elif jam < 4:
        return '3-4 Jam'
    elif jam < 5:
        return '4-5 Jam'
    else:
        return '>5 Jam'

mydata['kategori_jam_tidur'] = mydata['jam_tidur'].apply(kategori_jam_tidur)
data_tidur = mydata['kategori_jam_tidur'].value_counts().reindex(['<1 Jam', '1-2 Jam', '2-3 Jam', '3-4 Jam', '4-5 Jam', '>5 Jam']).fillna(0)

cmap = plt.cm.tab20
colors = [cmap(i / len(data_tidur)) for i in range(len(data_tidur))]

plt.figure(figsize=(7, 7))
wedges, texts, autotexts = plt.pie(
    data_tidur,
    autopct='%1.1f%%',
    startangle=90,
    colors=colors,
    wedgeprops={'edgecolor': 'white'},
    pctdistance=0.8,
    labeldistance=1.2
)
for text in texts:
    text.set_visible(False)

plt.title('Distribusi Waktu Tidur')
plt.legend(wedges, data_tidur.index, title="Kategori", loc="center left", bbox_to_anchor=(1, 0.5))
plt.tight_layout()
plt.show()
""")

# SCATTER PLOT PAGE
elif menu == "Visualisasi Scatter Plot":
    st.markdown("""
    ---
    """)
    st.subheader("🔷 Scatter Plot - Hubungan Variabel dan Nilai Ujian")
    st.markdown("""
    Scatter plot digunakan untuk menunjukkan **hubungan antara dua variabel numerik**. Dalam proyek ini, scatter plot akan menampilkan bagaimana **berbagai kebiasaan** seperti jam tidur, jam sosial media, Netflix, kehadiran, dan kesehatan mental berhubungan dengan nilai ujian mahasiswa.
    """)
    opsi = st.selectbox("Pilih Variabel untuk Scatter Plot:", [
        "Jam Tidur",
        "Jam Sosial Media",
        "Jam Netflix",
        "Kehadiran Kuliah",
        "Kesehatan Mental"
    ])
    st.markdown("""
    ---
    """)
    if opsi == "Jam Tidur":
        fig = plt.figure(figsize=(10, 6))
        sns.scatterplot(data=mydata, x='jam_tidur', y='nilai_ujian', hue='jenis_kelamin', alpha=0.7)
        plt.title('Hubungan Jam Tidur dengan Nilai Ujian')
        plt.xlabel('Jam Tidur per Hari')
        plt.ylabel('Nilai Ujian')
        plt.grid(True)
        plt.legend(title='Jenis Kelamin')
        plt.tight_layout()
        st.pyplot(fig)
        st.markdown("""
        Visualisasi scatter plot ini menggambarkan hubungan antara durasi waktu tidur per hari dengan nilai ujian, serta dibedakan berdasarkan jenis kelamin. Titik-titik berwarna biru mewakili perempuan (Female), sedangkan titik-titik oranye mewakili laki-laki (Male). Secara umum, distribusi data menunjukkan bahwa nilai ujian tersebar di berbagai rentang jam tidur, dengan kepadatan yang cukup tinggi pada durasi tidur antara 5 hingga 8 jam per hari. Tidak tampak pola korelasi yang kuat antara jam tidur dan nilai ujian, yang berarti peningkatan durasi tidur tidak selalu diikuti dengan peningkatan nilai ujian secara konsisten. Namun, sebagian besar individu yang memperoleh nilai tinggi (di atas 80) memiliki jam tidur yang berada dalam rentang sedang, yaitu sekitar 6 hingga 8 jam. Ini dapat menjadi indikasi bahwa tidur dalam durasi cukup — tidak terlalu singkat maupun berlebihan — berpotensi mendukung performa akademik yang baik. Selain itu, distribusi titik-titik untuk laki-laki dan perempuan tampak cukup merata, yang menunjukkan bahwa perbedaan jenis kelamin tidak secara signifikan memengaruhi hubungan antara jam tidur dan hasil ujian dalam dataset ini.""")
        if show_code:
            with st.expander("Lihat kode Jam Tidur"):
                st.code("""
plt.figure(figsize=(10, 6))
sns.scatterplot(data=mydata, x='jam_tidur', y='nilai_ujian', hue='jenis_kelamin', alpha=0.7)
plt.title('Hubungan Jam Tidur dengan Nilai Ujian')
plt.xlabel('Jam Tidur per Hari')
plt.ylabel('Nilai Ujian')
plt.grid(True)
plt.legend(title='Jenis Kelamin')
plt.tight_layout()
plt.show()
""")

    elif opsi == "Jam Sosial Media":
        fig = plt.figure(figsize=(10, 6))
        sns.scatterplot(data=mydata, x='jam_sosmed', y='nilai_ujian', hue='jenis_kelamin', alpha=0.7)
        plt.title('Hubungan Jam Sosial Media dengan Nilai Ujian')
        plt.xlabel('Jam Sosial Media per Hari')
        plt.ylabel('Nilai Ujian')
        plt.grid(True)
        plt.legend(title='Jenis Kelamin')
        plt.tight_layout()
        st.pyplot(fig)
        st.markdown("""
        Visualisasi di atas menunjukkan hubungan antara jam penggunaan media sosial per hari dengan nilai ujian mahasiswa, yang juga dibedakan berdasarkan jenis kelamin (Female dan Male). Secara umum, terlihat bahwa mahasiswa dengan tingkat penggunaan media sosial yang lebih rendah (terutama di bawah 2 jam per hari) cenderung memiliki sebaran nilai ujian yang lebih tinggi dan stabil. Sebaliknya, semakin tinggi intensitas penggunaan media sosial, nilai ujian cenderung lebih menyebar dan terdapat penurunan konsistensi, dengan lebih banyak mahasiswa yang memperoleh nilai di bawah rata-rata. Meskipun tidak menunjukkan korelasi negatif yang sangat kuat secara linear, pola ini mengindikasikan bahwa penggunaan media sosial yang berlebihan dapat berdampak pada performa akademik. Tidak tampak perbedaan signifikan antara mahasiswa laki-laki dan perempuan dalam hal pengaruh media sosial terhadap nilai ujian—kedua kelompok menunjukkan pola sebaran yang relatif serupa. Insight ini dapat menjadi bahan pertimbangan penting bagi mahasiswa dan institusi pendidikan dalam mengatur kebiasaan digital agar tidak mengganggu pencapaian akademik.
        """)
        if show_code:
            with st.expander("Lihat kode Jam Sosial Media"):
                st.code("""
plt.figure(figsize=(10, 6))
sns.scatterplot(data=mydata, x='jam_sosmed', y='nilai_ujian', hue='jenis_kelamin', alpha=0.7)
plt.title('Hubungan Jam Sosial Media dengan Nilai Ujian')
plt.xlabel('Jam Sosial Media per Hari')
plt.ylabel('Nilai Ujian')
plt.grid(True)
plt.legend(title='Jenis Kelamin')
plt.tight_layout()
plt.show()
""")

    elif opsi == "Jam Netflix":
        fig = plt.figure(figsize=(10, 6))
        sns.scatterplot(data=mydata, x='jam_netflix', y='nilai_ujian', hue='jenis_kelamin', alpha=0.7)
        plt.title('Hubungan Jam Menonton Netflix dengan Nilai Ujian')
        plt.xlabel('Jam Netflix per Hari')
        plt.ylabel('Nilai Ujian')
        plt.grid(True)
        plt.legend(title='Jenis Kelamin')
        plt.tight_layout()
        st.pyplot(fig)
        st.markdown("""
        Visualisasi scatter plot ini menggambarkan hubungan antara durasi menonton Netflix per hari dengan nilai ujian, serta dibedakan berdasarkan jenis kelamin. Titik-titik berwarna biru mewakili responden perempuan (Female), sedangkan titik-titik oranye mewakili laki-laki (Male). Secara keseluruhan, data menunjukkan bahwa sebagian besar individu menonton Netflix dalam durasi 0 hingga 3 jam per hari. Tidak terdapat pola korelasi yang jelas antara durasi menonton Netflix dengan nilai ujian — nilai tinggi maupun rendah muncul secara acak pada berbagai rentang jam menonton. Namun, terlihat bahwa mereka yang memiliki durasi menonton di atas 3 jam per hari cenderung memiliki sebaran nilai yang lebih rendah dibandingkan mereka yang menonton lebih sedikit. Hal ini dapat mengindikasikan bahwa menonton Netflix dalam durasi berlebihan berpotensi mengganggu pencapaian akademik. Di sisi lain, persebaran antara jenis kelamin cukup merata, menandakan bahwa pengaruh menonton Netflix terhadap nilai ujian tidak terlalu berbeda antara laki-laki dan perempuan
        """)
        if show_code:
            with st.expander("Lihat kode Jam Netflix"):
                st.code("""
plt.figure(figsize=(10, 6))
sns.scatterplot(data=mydata, x='jam_netflix', y='nilai_ujian', hue='jenis_kelamin', alpha=0.7)
plt.title('Hubungan Jam Menonton Netflix dengan Nilai Ujian')
plt.xlabel('Jam Netflix per Hari')
plt.ylabel('Nilai Ujian')
plt.grid(True)
plt.legend(title='Jenis Kelamin')
plt.tight_layout()
plt.show()
""")

    elif opsi == "Kehadiran Kuliah":
        fig = plt.figure(figsize=(10, 6))
        sns.scatterplot(data=mydata, x='persentase_kehadiran', y='nilai_ujian', hue='jenis_kelamin', alpha=0.7)
        plt.title('Hubungan Kehadiran Kuliah dengan Nilai Ujian')
        plt.xlabel('Persentase Kehadiran (%)')
        plt.ylabel('Nilai Ujian')
        plt.grid(True)
        plt.legend(title='Jenis Kelamin')
        plt.tight_layout()
        st.pyplot(fig)
        st.markdown("""
        Visualisasi scatter plot ini menunjukkan hubungan antara persentase kehadiran kuliah dengan nilai ujian, dengan perbedaan warna berdasarkan jenis kelamin. Titik-titik biru mewakili mahasiswa perempuan (Female) dan titik-titik oranye mewakili mahasiswa laki-laki (Male). Secara umum, terdapat kecenderungan bahwa nilai ujian cenderung lebih tinggi pada mahasiswa dengan tingkat kehadiran yang lebih tinggi, khususnya pada rentang kehadiran di atas 90%. Meskipun terdapat penyebaran nilai yang bervariasi di seluruh tingkat kehadiran, mahasiswa dengan kehadiran rendah (di bawah 70%) tampak lebih sering memiliki nilai ujian yang cenderung lebih rendah. Hal ini mengindikasikan adanya korelasi positif antara kehadiran kuliah dan pencapaian nilai ujian. Selain itu, distribusi data antara mahasiswa laki-laki dan perempuan tampak cukup merata di seluruh rentang kehadiran dan nilai, yang menunjukkan bahwa pengaruh kehadiran terhadap nilai ujian berlaku secara konsisten untuk kedua jenis kelamin.
        """)
        if show_code:
            with st.expander("Lihat kode Kehadiran Kuliah"):
                st.code("""
plt.figure(figsize=(10, 6))
sns.scatterplot(data=mydata, x='persentase_kehadiran', y='nilai_ujian', hue='jenis_kelamin', alpha=0.7)
plt.title('Hubungan Kehadiran Kuliah dengan Nilai Ujian')
plt.xlabel('Persentase Kehadiran (%)')
plt.ylabel('Nilai Ujian')
plt.grid(True)
plt.legend(title='Jenis Kelamin')
plt.tight_layout()
plt.show()
""")

    elif opsi == "Kesehatan Mental":
        fig = plt.figure(figsize=(10, 6))
        sns.scatterplot(data=mydata, x='skor_kesehatan_mental', y='nilai_ujian', hue='jenis_kelamin', alpha=0.7)
        plt.title('Skor Kesehatan Mental vs Nilai Ujian')
        plt.xlabel('Skor Kesehatan Mental (1–10)')
        plt.ylabel('Nilai Ujian')
        plt.grid(True)
        plt.legend(title='Jenis Kelamin')
        plt.tight_layout()
        st.pyplot(fig)
        st.markdown("""
        Scatter plot ini menunjukkan hubungan antara skor kesehatan mental (skala 1–10) dengan nilai ujian, yang dibedakan berdasarkan jenis kelamin. Titik-titik biru merepresentasikan mahasiswa perempuan (Female), sedangkan titik-titik oranye merepresentasikan mahasiswa laki-laki (Male). Secara umum, data tersebar merata di seluruh rentang skor kesehatan mental, dengan nilai ujian yang bervariasi mulai dari rendah hingga tinggi di setiap tingkat skor. Meskipun tidak terdapat pola korelasi yang kuat secara visual, terlihat bahwa mahasiswa dengan skor kesehatan mental yang lebih tinggi (antara 7 hingga 10) cenderung memiliki persebaran nilai yang sedikit lebih terfokus di rentang menengah hingga tinggi (sekitar 60 ke atas). Hal ini dapat memberikan indikasi bahwa kondisi kesehatan mental yang baik berpotensi mendukung pencapaian akademik, meskipun pengaruhnya tidak sepenuhnya determinan. Selain itu, distribusi antara jenis kelamin tampak seimbang, menunjukkan bahwa hubungan antara kesehatan mental dan nilai ujian tidak terlalu berbeda secara signifikan antara laki-laki dan perempuan.
        """)
        if show_code:
            with st.expander("Lihat kode Kesehatan Mental"):
                st.code("""
plt.figure(figsize=(10, 6))
sns.scatterplot(data=mydata, x='skor_kesehatan_mental', y='nilai_ujian', hue='jenis_kelamin', alpha=0.7)
plt.title('Skor Kesehatan Mental vs Nilai Ujian')
plt.xlabel('Skor Kesehatan Mental (1–10)')
plt.ylabel('Nilai Ujian')
plt.grid(True)
plt.legend(title='Jenis Kelamin')
plt.tight_layout()
plt.show()
""")

# TOP PENGARUH AKADEMIK
elif menu == "Top Pengaruh Akademik":
    st.markdown("""
    ---
    """)
    st.subheader("🏆 Kombinasi Gaya Hidup Mahasiswa dengan Nilai Tertinggi")
    st.markdown("""
    Visualisasi berikut menampilkan **10 kombinasi faktor gaya hidup mahasiswa** yang memiliki rata-rata nilai ujian tertinggi. Kombinasi tersebut mencakup **tidur, sosmed, kerja**, **mental, kehadiran, olahraga**, dan lain-lain.
    """)

    opsi = st.selectbox("Pilih kombinasi faktor di bawah untuk mengeksplorasi dampaknya terhadap performa akademik mahasiswa:", [
        "Tidur, Sosmed, Kerja",
        "Mental, Kehadiran, Olahraga",
        "Tidur, Sosmed, Kehadiran",
        "Sosmed, Kerja, Mental"
    ])
    st.markdown("""
    ---
    """)
    if opsi == "Tidur, Sosmed, Kerja":
        mydata['kategori_jam_tidur'] = pd.cut(mydata['jam_tidur'], bins=[0, 4, 5, 6, 7, 8, 24], labels=['<4', '4-5', '5-6', '6-7', '7-8', '>8'])
        mydata['kategori_jam_sosmed'] = pd.cut(mydata['jam_sosmed'], bins=[0, 1, 2, 3, 4, 5, 24], labels=['<1', '1-2', '2-3', '3-4', '4-5', '>5'])
        mydata['label_3faktor'] = 'Tidur: ' + mydata['kategori_jam_tidur'].astype(str) + ' | Sosmed: ' + mydata['kategori_jam_sosmed'].astype(str) + ' | Kerja: ' + mydata['kerja_paruh_waktu']
        top = mydata.groupby('label_3faktor')['nilai_ujian'].mean().reset_index().sort_values(by='nilai_ujian', ascending=False).head(10)
        fig, ax = plt.subplots(figsize=(12, 7))
        sns.barplot(y='label_3faktor', x='nilai_ujian', data=top, palette=sns.color_palette("Greens", n_colors=10)[::-1], ax=ax)
        plt.xlabel('Rata-rata Nilai Ujian')
        plt.title('Top 10 Kombinasi Gaya Hidup (Tidur, Sosmed, Kerja) dengan Nilai Tertinggi')
        st.pyplot(fig)
        st.markdown("""Berdasarkan visualisasi yang menampilkan sepuluh kombinasi gaya hidup mahasiswa dengan rata-rata nilai ujian tertinggi, diperoleh beberapa temuan yang menarik. Kombinasi yang dianalisis meliputi tiga variabel utama, yaitu durasi tidur, intensitas penggunaan media sosial, dan status kerja paruh waktu mahasiswa. Dari visualisasi tersebut, terlihat bahwa kombinasi gaya hidup dengan nilai akademik tertinggi justru berasal dari kelompok mahasiswa yang bekerja paruh waktu dan memiliki durasi tidur yang cukup, bahkan lebih dari delapan jam per hari. Hal ini mengindikasikan bahwa bekerja paruh waktu tidak selalu berdampak negatif terhadap performa akademik. Sebaliknya, dalam beberapa kasus, kerja sambil kuliah dapat mendorong mahasiswa menjadi lebih terorganisir, disiplin, dan terampil dalam manajemen waktu.

Selain itu, durasi tidur tampak menjadi salah satu faktor penting dalam mendukung nilai akademik. Mahasiswa dengan rata-rata nilai tertinggi umumnya memiliki durasi tidur minimal 7 hingga 8 jam per hari. Tidur yang cukup secara konsisten diasosiasikan dengan peningkatan konsentrasi, kestabilan emosi, serta kemampuan memproses informasi, yang kesemuanya berkontribusi positif terhadap hasil belajar. Meski demikian, terdapat satu kombinasi dengan durasi tidur rendah (4–5 jam) namun tetap berada di peringkat atas, yang menandakan adanya faktor lain seperti motivasi tinggi atau rutinitas belajar intensif yang dapat mengimbangi kekurangan waktu tidur.

Menariknya, sebagian besar kombinasi dengan nilai tertinggi tidak mencantumkan informasi penggunaan media sosial (bernilai ‘nan’). Hal ini dapat diinterpretasikan sebagai kemungkinan bahwa mahasiswa dengan nilai tinggi cenderung tidak banyak menggunakan media sosial, atau setidaknya tidak menginputkannya dalam data. Pada kombinasi yang mencantumkan durasi penggunaan media sosial secara eksplisit, nilai ujian tetap tinggi selama durasinya berkisar 1–2 jam per hari. Namun, pada kombinasi dengan durasi media sosial lebih dari 5 jam per hari, rata-rata nilai akademik terlihat menurun secara signifikan, bahkan menjadi yang paling rendah di antara 10 kombinasi tersebut. Temuan ini mendukung asumsi bahwa penggunaan media sosial secara berlebihan dapat mengalihkan fokus dan waktu belajar mahasiswa, yang akhirnya berdampak negatif pada performa akademik.

Secara keseluruhan, visualisasi ini memberikan pemahaman bahwa gaya hidup yang seimbang, mencakup tidur yang cukup, penggunaan media sosial yang moderat, serta aktivitas kerja paruh waktu yang terkontrol, berpotensi besar dalam menunjang pencapaian akademik yang optimal. Insight ini diharapkan dapat menjadi bahan refleksi bagi mahasiswa dalam menyusun rutinitas harian yang sehat dan produktif, serta bagi institusi pendidikan dalam memberikan arahan atau intervensi yang berbasis data terhadap perilaku mahasiswa.""")

    elif opsi == "Mental, Kehadiran, Olahraga":
        mydata['kategori_kehadiran'] = pd.cut(mydata['persentase_kehadiran'], bins=[0, 60, 70, 80, 90, 100], labels=['<60%', '60-70%', '70-80%', '80-90%', '90-100%'])
        mydata['label_mental_hadir_olahraga'] = 'Mental: ' + mydata['skor_kesehatan_mental'].astype(str) + ' | Hadir: ' + mydata['kategori_kehadiran'].astype(str) + ' | Hari Olahraga: ' + mydata['frekuensi_olahraga'].astype(str) + ' Hari'
        top = mydata.groupby('label_mental_hadir_olahraga')['nilai_ujian'].mean().reset_index().sort_values(by='nilai_ujian', ascending=False).head(10)
        fig, ax = plt.subplots(figsize=(12, 7))
        sns.barplot(y='label_mental_hadir_olahraga', x='nilai_ujian', data=top, palette=sns.color_palette("Reds", n_colors=10)[::-1], ax=ax)
        plt.xlabel('Rata-rata Nilai Ujian')
        plt.title('Top 10 Kombinasi Mental, Kehadiran, & Olahraga dengan Nilai Tertinggi')
        st.pyplot(fig)
        st.markdown("""Visualisasi ini menampilkan sepuluh kombinasi tertinggi dari tiga faktor gaya hidup mahasiswa, yaitu kesehatan mental, tingkat kehadiran kuliah, dan frekuensi olahraga dalam seminggu, terhadap rata-rata nilai ujian. Tujuan dari visualisasi ini adalah untuk mengeksplorasi bagaimana interaksi antara kondisi psikologis, keterlibatan akademik, dan aktivitas fisik dapat memengaruhi performa akademik mahasiswa.

Berdasarkan grafik, kombinasi tertinggi nilai ujian justru tidak selalu berasal dari mahasiswa dengan skor kesehatan mental tertinggi. Contohnya, kombinasi teratas berasal dari mahasiswa dengan skor mental 8, kehadiran 70–80%, dan berolahraga 2 hari dalam seminggu. Posisi kedua dan ketiga bahkan mencakup mahasiswa dengan skor kesehatan mental sedang hingga rendah (mental 4–6), namun memiliki frekuensi olahraga tinggi yaitu 6 hari per minggu. Hal ini mengindikasikan bahwa aktivitas fisik yang konsisten dapat berperan sebagai kompensasi terhadap kondisi mental yang kurang ideal, dan tetap berkontribusi positif terhadap performa akademik.

Di sisi lain, mahasiswa dengan skor mental 10 (maksimal) namun tidak berolahraga sama sekali dan hanya hadir di kelas sebanyak 60–70%, tercatat memiliki rata-rata nilai yang lebih rendah dibandingkan kombinasi lain. Ini menunjukkan bahwa tingkat kesehatan mental yang tinggi saja tidak cukup, apabila tidak didukung oleh kehadiran aktif dan rutinitas fisik yang sehat.

Beberapa kombinasi lain dengan tingkat kehadiran tinggi (90–100%) dan frekuensi olahraga sedang (4 hari) menunjukkan nilai yang relatif baik, meskipun skor mental mereka rendah. Hal ini menggarisbawahi pentingnya disiplin kehadiran dan gaya hidup aktif, yang dapat membantu menjaga performa belajar bahkan saat kondisi mental tidak optimal.

Secara umum, insight dari visualisasi ini menunjukkan bahwa performa akademik mahasiswa dipengaruhi oleh interaksi multifaktor. Tidak ada satu variabel tunggal yang dominan, tetapi kombinasi antara mental yang stabil, kehadiran tinggi, dan aktivitas olahraga rutin memiliki peran besar dalam mendukung nilai ujian yang lebih baik. Oleh karena itu, pendekatan holistik terhadap gaya hidup mahasiswa menjadi sangat penting, baik dari sisi fisik, psikologis, maupun akademik.""")

    elif opsi == "Tidur, Sosmed, Kehadiran":
        mydata['label_tidur_sosmed_hadir'] = 'Tidur: ' + mydata['kategori_tidur'].astype(str) + ' | Sosmed: ' + mydata['kategori_jam_sosmed'].astype(str) + ' | Hadir: ' + mydata['kategori_kehadiran'].astype(str)
        top = mydata.groupby('label_tidur_sosmed_hadir')['nilai_ujian'].mean().reset_index().sort_values(by='nilai_ujian', ascending=False).head(10)
        fig, ax = plt.subplots(figsize=(12, 7))
        sns.barplot(y='label_tidur_sosmed_hadir', x='nilai_ujian', data=top, palette=sns.color_palette("Blues", n_colors=10)[::-1], ax=ax)
        plt.xlabel('Rata-rata Nilai Ujian')
        plt.title('Top 10 Kombinasi Tidur, Sosmed, Kehadiran')
        st.pyplot(fig)
        st.markdown("""Visualisasi ini menyajikan sepuluh kombinasi gaya hidup mahasiswa berdasarkan durasi tidur, penggunaan media sosial, dan persentase kehadiran kuliah, yang kemudian diurutkan berdasarkan rata-rata nilai ujian tertinggi. Tiga aspek ini merepresentasikan keseimbangan antara kebugaran fisik, kontrol digital, dan keterlibatan akademik dalam kehidupan mahasiswa.

Berdasarkan grafik, kombinasi tertinggi diperoleh oleh mahasiswa yang memiliki durasi tidur lebih dari 8 jam, tidak mencantumkan data penggunaan media sosial, dan memiliki tingkat kehadiran 80–90%. Diikuti oleh kombinasi serupa dengan durasi tidur 7–8 jam dan kehadiran 90–100%, masih tanpa data penggunaan sosmed. Ini memperkuat pola yang sudah terlihat pada visualisasi sebelumnya, bahwa tidur cukup dan kehadiran tinggi menjadi dua komponen dominan yang berkontribusi positif terhadap performa akademik.

Menariknya, posisi tiga hingga lima menunjukkan bahwa meskipun mahasiswa menggunakan media sosial (baik kurang dari 1 jam atau 1–2 jam), mereka tetap dapat mempertahankan nilai tinggi selama kehadiran tetap tinggi dan tidur dalam durasi ideal. Ini memberikan insight bahwa penggunaan media sosial secara moderat masih dapat diterima dalam rutinitas mahasiswa tanpa mengorbankan hasil akademik — selama dikelola dengan baik dan tidak mengganggu jadwal utama seperti tidur dan kuliah.

Sebaliknya, kombinasi dengan nilai rata-rata yang lebih rendah mulai terlihat pada mahasiswa yang memiliki durasi tidur kurang (4–5 jam), intensitas media sosial sedang hingga tinggi (4–5 jam), dan tingkat kehadiran yang rendah (sekitar 70–80%). Kombinasi ini memperlihatkan tren bahwa kurang tidur yang dikombinasikan dengan konsumsi digital tinggi dan keterlibatan akademik rendah berdampak langsung terhadap penurunan capaian nilai.

Dari keseluruhan pola yang ditampilkan dalam grafik ini, dapat disimpulkan bahwa tidur yang cukup dan kehadiran aktif dalam perkuliahan merupakan fondasi utama dalam menunjang keberhasilan akademik. Sementara itu, penggunaan media sosial bukan faktor tunggal yang merugikan, selama tidak mengganggu aktivitas utama mahasiswa. Visualisasi ini menegaskan pentingnya keseimbangan antara kebutuhan biologis, keterlibatan akademik, dan pengelolaan waktu digital dalam kehidupan mahasiswa.""")

    elif opsi == "Sosmed, Kerja, Mental":
        mydata['label_sosmed_kerja_mental'] = 'Sosmed: ' + mydata['kategori_jam_sosmed'].astype(str) + ' | Kerja: ' + mydata['kerja_paruh_waktu'].astype(str) + ' | Mental: ' + mydata['skor_kesehatan_mental'].astype(str)
        top = mydata.groupby('label_sosmed_kerja_mental')['nilai_ujian'].mean().reset_index().sort_values(by='nilai_ujian', ascending=False).head(10)
        fig, ax = plt.subplots(figsize=(12, 7))
        sns.barplot(y='label_sosmed_kerja_mental', x='nilai_ujian', data=top, palette=sns.color_palette("YlOrBr", n_colors=10)[::-1], ax=ax)
        plt.xlabel('Rata-rata Nilai Ujian')
        plt.title('Top 10 Kombinasi Sosmed, Kerja, Mental Health')
        st.pyplot(fig)
        st.markdown("""Visualisasi ini menampilkan sepuluh kombinasi teratas dari variabel penggunaan media sosial, status kerja paruh waktu, dan kesehatan mental, yang kemudian diurutkan berdasarkan rata-rata nilai ujian mahasiswa. Tujuan dari visualisasi ini adalah untuk memahami bagaimana interaksi antara perilaku digital, beban aktivitas di luar studi, dan kondisi psikologis mahasiswa memengaruhi performa akademik mereka.

Secara umum, terlihat bahwa kombinasi dengan nilai tertinggi didominasi oleh mahasiswa yang tidak mencantumkan data penggunaan media sosial, tidak bekerja, dan memiliki kesehatan mental sedang hingga tinggi (skor 8–10). Hal ini menunjukkan bahwa fokus penuh pada kegiatan akademik tanpa gangguan digital atau beban kerja tambahan, disertai kondisi mental yang relatif stabil, merupakan kombinasi ideal yang mendukung capaian akademik tertinggi.

Menariknya, posisi kedua dan ketiga justru diisi oleh mahasiswa yang bekerja paruh waktu, tanpa data sosmed, dengan skor mental yang ekstrem — yakni mental 10 (tinggi) dan mental 1 (sangat rendah). Pola ini menunjukkan bahwa meskipun secara umum kesehatan mental positif dikaitkan dengan nilai yang baik, terdapat pengecualian di mana mahasiswa dengan kondisi mental rendah tetap mampu mencapai nilai tinggi. Kemungkinan ini bisa disebabkan oleh faktor-faktor lain seperti motivasi tinggi, kebutuhan finansial yang mendorong etos kerja, atau sistem dukungan eksternal.

Dalam jajaran tengah grafik, kombinasi antara penggunaan media sosial dalam batas moderat (2–4 jam), status bekerja, dan kesehatan mental baik (skor 8–9), masih menghasilkan nilai yang kompetitif. Artinya, media sosial dan pekerjaan tidak secara otomatis menurunkan prestasi, selama kondisi mental tetap terjaga dan mahasiswa mampu mengelola waktu serta tekanan dengan baik.

Di sisi lain, kombinasi dengan frekuensi penggunaan sosmed lebih tinggi (4–5 jam) dan tidak bekerja, meskipun memiliki mental health sempurna (skor 10), justru menunjukkan nilai yang lebih rendah. Hal ini memperkuat dugaan bahwa tingkat penggunaan media sosial tetap menjadi faktor risiko terhadap performa akademik, bahkan jika kondisi psikologis mahasiswa dalam keadaan optimal.

Dari keseluruhan temuan ini, dapat disimpulkan bahwa kesehatan mental merupakan faktor yang konsisten mendukung nilai tinggi, namun dampaknya bisa tereduksi jika diimbangi dengan kebiasaan digital yang tidak sehat. Sementara itu, pekerjaan paruh waktu tidak serta merta menjadi hambatan, bahkan dalam beberapa kasus mendampingi mahasiswa dengan performa akademik baik. Oleh karena itu, penting bagi mahasiswa untuk menjaga keseimbangan antara aspek psikologis, aktivitas sosial digital, dan beban kerja, agar dapat mencapai hasil akademik yang maksimal.

""")


# Footer (untuk semua halaman)
st.markdown("""
    <hr style='margin-top:50px;'>
    <p style='text-align:center; color: grey;'>© 2025 Kelompok Chartastic - STT Terpadu Nurul Fikri</p>
""", unsafe_allow_html=True)
