##Look at tester branch

1. Repoyu klonla
https://github.com/ertanAlabay/dj-website.git
tester branchinden al

2. python environment oluştur 
  * pip install virtualenv
  * python -m venv myenv

3. environmenti active et
  * .\myenv\Scripts\activate
  * ya da \myenv\Scripts\activate

4. requirement dosyalarını indir. 
Bunun için requirements.txt dosyalarıyla aynı dizinde olmaya dikkat et
  * pip install -r requirements.txt

5. "code" dizinine gir ve projeyi çalıştır
  * cd code
  * python manage.py runserver

Sonrada http://127.0.0.1:8000/ portuna bakabilirsin
