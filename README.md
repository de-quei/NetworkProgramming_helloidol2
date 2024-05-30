# helloidol2

---

1. startproject helloidol2
   1. python -m pip install django~=4.2
   2. django-admin startproject helloidol2 .
   3. File > Settings.. > Language&Framework > Django
      [v] Enable Django Support
   4. Run > Edit Configurations > + > Django Server > Name : runserver
   5. VCS > Enable Version Control Integration.. > git > ok

2. startapp 루시
   1. python manage.py startapp 루시
   2. '루시', in INSTALLED_APPS in settings.py

3. 루시/
   1. models
      1. Character
         1. name, feature, created_at, updated_at
         2. photo
            1. Terminal
               1. python -m pip install pillow
         3. `__str__()` : 객체를 출력할 때, 알맞은 String으로 포맷하여 출력.
         4. `get_absolute_url()`: 캐릭터 하나 데이터 가져오자
      2. python manage.py makemigrations 루시
      3. python manage.py migrate 루시
   2. admin
      1. Character
      2. python manage.py createsuperuser
   3. views
      1. R : CharacterListView
      2. R : CharacterDetailView
      3. C : CharacterCreateView
         1. add 'photo' in fields
      4. U : CharacterUpdateView
         1. add 'photo' in fields
      5. D : CharacterDeleteView
   4. templates/루시/
      1. character_list.html
         1. {{ character.photo.url }}
      2. character_detail.html
         1. {{ character.photo.url }}
      3. character_create.html
         1. enctype="multipart/form-data"
      4. character_update.html
         1. enctype="multipart/form-data"
      5. character_confirm_delete.html
   5. urls
      1. 루시:character_list
      2. 루시:character_detail
      3. 루시:character_create
      4. 루시:character_update
      5. 루시:character_delete
   6. static/루시/
      1. photo/no_photo
      2. settings
         1. STATICFIELS_DIRS

4. helloidol2/
   1. urls
      1. MEDIA
   2. settings
      1. MEDIA_ROOT, MEDIA_URL

5. templates/
   1. base.html
      1. settings.py > TEMPLATES
         1. 'DIRS': [BASE_DIR / 'templates']