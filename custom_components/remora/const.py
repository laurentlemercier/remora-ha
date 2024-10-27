"""Constants used by the Remora component."""

""" Les constantes pour l'intégration Tuto HACS """

from homeassistant.const import Platform

DOMAIN = "remora"
PLATFORM: list[Platform] = [Platform.SENSOR, Platform.BINARY_SENSOR, Platform.CLIMATE]
FILPILOTE = "filpilote"
FP = "fp"
RELAIS = "relais"
FNCT_RELAIS = "fnct_relais"
CONF_TEMP_SENSOR = "temp_sensor"
SERVICE_RESET = "reset"
