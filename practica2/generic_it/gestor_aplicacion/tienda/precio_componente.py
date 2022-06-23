# @author: Emilio Porras
# @summary La enumeracion PrecioComponente asocia el nombre de los componentes con su precio unico y constante

from enum import Enum
class PrecioComponente(Enum):
    RAM_4GB = 20000
    RAM_8GB = 50000
    DISCO_DURO_HDD_512GB = 100000
    DISCO_DURO_SSD_256GB = 200000
    BATERIA_LAPTOP = 150000
    BATERIA_LAPTOP_SUPERCHARGER = 120000
    PROCESADOR_INTEL = 80000
    PROCESADOR_AMD = 70000
    DISPLAY_LAPTOP_17In = 120000
    DISPLAY_LAPTOP_15In = 110000

