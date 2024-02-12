from phonenumbers import carrier, timezone, geocoder
import phonenumbers

ro_number = phonenumbers.parse("+919890818512")

print(carrier.name_for_number(ro_number, "en"))
print(timezone.time_zones_for_number(ro_number))
print(geocoder.description_for_number(ro_number, "en"))


