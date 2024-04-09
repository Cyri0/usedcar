### 2-es szint

`python -m venv my_venv`

`my_venv\Scripts\activate`

`pip install django`

`django-admin startproject config`

`rename config backend`

`cd backend`

`python manage.py runserver`

leállítjuk Ctrl + C-vel

`python manage.py migrate`

`python manage.py createsuperuser`

`python manage.py startapp autok`

VSC-ben megnyitjuk

config/settings.py -ba beírjuk az INSTALLED_APPS listába az 'autok' elemet

### 3-es szint

templates mappa létrehozása és templates-ben index.html
config/settings.py -ba a TEMPLATES-hez hozzáadjuk a

`'DIRS': [ BASE_DIR / 'templates/' ]`

-sort

config/urls.py-ban beimportáljuk a render-t és létrehozunk egy view-t

```
from django.shortcuts import render

def indexPage(request):
    return render(request, 'index.html')
```

az urlpatterns-höz hozzáadni a következő sort

`path('', indexPage, name="index"),`

### 4-as szint

autok/models.py-ban létrehozunk egy modellt

pl.:

```
class Auto(models.Model):
    brand = models.CharField(max_length=255)
    car_type = models.CharField(max_length=255)
    year = models.IntegerField()
    mileage = models.IntegerField()
    color = models.CharField(max_length=255)

    fuel_options = [
        ('petrol','petrol'),
        ('diesel','diesel'),
        ('lpg','lpg'),
        ('electric','electric')
    ]

    fuel_type = models.CharField(choices=fuel_options, max_length=255)

    def __str__(self):
        return f"{self.brand} - {self.car_type} ({self.year})"
```

migráljuk a modellt

`python manage.py makemigrations`
`python manage.py migrate`


autok/admin.py-ba beírjuk a következőt

```
from .models import Auto

admin.site.register(Auto)

```

Hozzáadni pár teszt adatot az admin felületen.

### 5-as szint

config/urls.py-ban beimportáljuk az Auto modellt, és kiegészítjük a korábbi indexPage view-t

```
from autok.models import Auto

def indexPage(request):
    autok = Auto.objects.all()
    return render(request, 'index.html', {'cars': autok})
```

az templates/index.html-be valahogy megjelenítjük, pl:

```
    <table>
        <tr>
            <th>Típus</th>
            <th>Futott km</th>
            <th>Üzemanyag</th>
        </tr>
    {% for car in cars %}
        <tr>
            <td>{{ car.brand }} - {{ car.car_type }} ({{ car.year }})</td>
            <td>{{ car.mileage }} km</td>
            <td>{{ car.fuel_type }}</td>
        </tr>
    {% endfor %}
    </table>
```

### 😎🧠