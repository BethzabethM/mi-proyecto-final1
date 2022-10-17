from ejemplo.models import Familiar

Familiar(nombre="Anibal", direccion="Gabrieles 98-4b", numero_pasaporte=12172548).save()
Familiar(nombre="Carmen", direccion="Gabrieles 98-4b", numero_pasaporte=3660032).save()
Familiar(nombre="Barbara", direccion="Gabrieles 98-4b", numero_pasaporte=10785673).save()
Familiar(nombre="Clara", direccion="Gabrieles 98-4b", numero_pasaporte=3289657).save()

print("Se cargo con exito los usuarios de pruebas")