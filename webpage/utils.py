import reflex as rx
from webpage import constants

def lang() -> rx.Component:
    return rx.script("document.documentElement.lang = 'es'")

INDEX_TITLE = "Seraph page"
INDEX_DESCRIPTION = "Bienvenido a la página de Seraph!"
INDEX_IMAGE = "favicon.ico"

PRESENTER_TITLE = "Presentaciones de Seraph"
PRESENTER_DESCRIPTION = "Listado presentaciones realizadas por Seraph"
PRESENTER_IMAGE = "favicon.ico"

meta = [
    {"name": "og:type", "content": "website"},
    {"name": "og:title", "content": INDEX_TITLE},
    {"name": "og:description", "content": INDEX_DESCRIPTION},
]



slideshare_urls = {
    "Matemáticas Aplicadas usando Python": """<iframe src="https://www.slideshare.net/slideshow/embed_code/key/3N67sQdbwgTnH4?startSlide=1" width="597" height="486" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px;max-width: 100%;" allowfullscreen></iframe><div style="margin-bottom:5px"><strong><a href="https://es.slideshare.net/slideshow/matematicas-aplicadas-usando-python/267742777" title="Matemáticas Aplicadas usando Python" target="_blank">Matemáticas Aplicadas usando Python</a></strong> from <strong><a href="https://www.slideshare.net/ecrespo" target="_blank">Ernesto Crespo</a></strong></div>""",
    "Extracción de datos con Python": """<iframe src="https://www.slideshare.net/slideshow/embed_code/key/ggicOXKm2vxnYO?startSlide=1" width="597" height="486" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px;max-width: 100%;" allowfullscreen></iframe><div style="margin-bottom:5px"><strong><a href="https://es.slideshare.net/ecrespo/webscraping" title="Extracción de datos con Python (webscraping" target="_blank">Extracción de datos con Python (webscraping</a></strong> from <strong><a href="https://www.slideshare.net/ecrespo" target="_blank">Ernesto Crespo</a></strong></div>""",
    "Python en Android": """<iframe src="https://www.slideshare.net/slideshow/embed_code/key/4aKw19JhmDSghK?startSlide=1" width="597" height="486" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px;max-width: 100%;" allowfullscreen></iframe><div style="margin-bottom:5px"><strong><a href="https://es.slideshare.net/ecrespo/python-en-androidcharla-del-fudcon-latam-2012" title="Python en Android,Charla del FUDcon Latam 2012" target="_blank">Python en Android,Charla del FUDcon Latam 2012</a></strong> from <strong><a href="https://www.slideshare.net/ecrespo" target="_blank">Ernesto Crespo</a></strong></div>""",
    "Mensajeria de Colas con ZeroMQ": """<iframe src="https://www.slideshare.net/slideshow/embed_code/key/4gUyvrA05y6vSX?startSlide=1" width="597" height="486" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px;max-width: 100%;" allowfullscreen></iframe><div style="margin-bottom:5px"><strong><a href="https://es.slideshare.net/slideshow/sistema-de-mensajeria-de-colas-con-zeromq-y-python/14040232" title="Sistema de Mensajeria de Colas con ZeroMQ y Python" target="_blank">Sistema de Mensajeria de Colas con ZeroMQ y Python</a></strong> from <strong><a href="https://www.slideshare.net/ecrespo" target="_blank">Ernesto Crespo</a></strong></div>""",
    "Gestionar archivos de configuración": """<iframe src="https://www.slideshare.net/slideshow/embed_code/key/JeTnQHWWkyt8N1?startSlide=1" width="597" height="486" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px;max-width: 100%;" allowfullscreen></iframe><div style="margin-bottom:5px"><strong><a href="https://es.slideshare.net/ecrespo/gestin-de-configuracin-con-mercurial-y-etckeeper" title="Gestionar archivos de configuración en /etc con etckeeper y mercurial" target="_blank">Gestionar archivos de configuración en /etc con etckeeper y mercurial</a></strong> from <strong><a href="https://www.slideshare.net/ecrespo" target="_blank">Ernesto Crespo</a></strong></div>"""
}


index_meta = [
    {"name": "og:type", "content": "website"},
    {"name": "og:title", "content": INDEX_TITLE},
    {"name": "og:description", "content": INDEX_DESCRIPTION},
]

presenter_meta = [
    {"name": "og:title", "content": PRESENTER_TITLE},
    {"name": "og:description", "content": PRESENTER_DESCRIPTION},
]
