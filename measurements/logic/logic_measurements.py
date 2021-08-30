from ..models import Measurement

def get_all_measurements():
    measurements = Measurement.objects.all()
    return measurements

def get_one_measurement():
    measurement = Measurement.objects.filter(pk=1)
    return measurement

def delete_one_measurement():
    deleted = Measurement.objects.filter(pk=1).delete()
    return deleted