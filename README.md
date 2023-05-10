# secops_log_analyzer

Bu proje, güvenlik operasyonları (SecOps) için bir log analizörüdür. Log dosyalarını okur, başarısız giriş denemelerini analiz eder ve şüpheli IP adreslerini raporlar.

## Proje Yapısı

Proje aşağıdaki dosyalardan oluşur:
````
secops_log_analyzer/
│
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── log_reader.py
│   ├── log_analyzer.py
│   └── report_writer.py
│
├── logs/
│   ├── log1.txt
│   ├── log2.txt
│   └── ...
│
├── reports/
│   ├── suspicious_ips_report.csv
│   └── ...
│
└── README.md
````

- `src/`: Kaynak kodların bulunduğu dizindir.
- `logs/`: Log dosyalarının bulunduğu dizindir. İsteğe bağlı olarak log dosyalarını buraya ekleyebilirsiniz.
- `reports/`: Rapor dosyalarının oluşturulduğu dizindir.
- `README.md`: Proje hakkında açıklama içeren dosyadır.

## Kullanılan Dosyalar 

### log_reader.py

Bu dosya, log dosyasını okumak için kullanılan bir modül içerir.

### log_analyzer.py

Bu dosya, log satırlarını analiz etmek için kullanılan bir modül içerir.

### report_writer.py

Bu dosya, şüpheli IP adreslerini bir CSV dosyasına yazmak için kullanılan bir modül içerir.

### main.py

Bu dosya, log analizini gerçekleştiren ana programdır.


