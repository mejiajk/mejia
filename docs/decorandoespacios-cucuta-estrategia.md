# Decorando Espacios · Cúcuta — mercado, keywords y estrategia

Datos: DataForSEO (Google Ads search volume y SERP en vivo, móvil, ubicación Cúcuta `1029301`), 2026-10-01. Costo total ≈ 0,20 USD.
El sitio no es accesible desde el entorno (el proxy lo bloquea), pero se verificó con el rastreador y Labs de DataForSEO (sección 1).

## 0. Punto de partida: el sitio hoy no vende muebles

Verificado el 2026-10-01 con DataForSEO:

- **Contenido actual:** guía de acabados en PVC (techos, paredes, piso laminado, paredes 3D). La home se titula "Proyectos y recursos recomendados de acabados en PVC" y lista proyectos inmobiliarios de Colombia y Panamá (Grupo Los Pueblos, Playa Dorada, Ocean Reef, Armonía, Bosco di Santa María). **Hay 0 páginas de camas, cocinas, cunas o comedores.**
- **Técnico:** WordPress con LiteSpeed y Cloudflare, HTTPS, HTTP/3, puntaje on-page 97, LCP 1,6 s en la home. `sitemap.xml` existe; `robots.txt` da 404. La home declara canonical en `www`. Las URL terminan en `.html`.
- **Enlaces rotos o provisionales:** tres proyectos de la home enlazan a dominios con prefijo `verificar-` (verificar-armonia.com, verificar-oceanreef.com, verificar-playacaracol.com). Hay que sustituirlos o quitarlos.
- **Posicionamiento:** 141 keywords en Google Colombia, ninguna en el top 3, 7 en el 4–10, 32 en el 11–20; tráfico estimado ~512 visitas/mes. Lo aportan `/techo-pvc.html` (95 keywords), `/paredes-pvc.html` (30), `/piso-laminado.html` (9) y `/paredes-3d.html` (7). Ejemplos: "techo pvc bogota" #7, "cielo raso pvc madera" #12, "laminas en pvc para pared" #22 (1.000 búsquedas/mes). Son posiciones nacionales, no de Cúcuta.
- **Autoridad:** 75 enlaces desde 52 dominios, desde noviembre de 2023.

Decisión acordada: **añadir muebles al sitio sin perder lo que ya rankea**. Las páginas de PVC se conservan y se enlazan con las nuevas categorías (cocinas y closets combinan con techos y paredes).

## 1. Hallazgos del mercado

**La demanda local es pequeña pero concentrada.** Búsquedas mensuales en Cúcuta (Google Ads, redondeadas):

| Grupo | Keyword (vol/mes en Cúcuta) | Mismo término, Colombia |
|---|---|---|
| Genérico local | muebles cucuta 390 · mueblerias en cucuta 390 · colchones cucuta 210 | muebles 27.100 |
| Closets/escritorios | closets 590 · escritorios 590 | closets 40.500 · escritorios 49.500 |
| Sofá cama | sofa cama 390 | 49.500 |
| Comedores | comedores 320 · comedor 4 puestos 320 · comedores modernos 90 · comedor 6 puestos 90 | comedores 27.100 |
| Cocinas | cocinas integrales 260 · cocinas modernas 210 · diseño de cocinas 70 | integrales 22.200 |
| Camas | camas modernas 170 · cama queen 110 · cama doble 110 · camas cucuta 70 | camas 14.800 |
| Cunas | cunas para bebe 110 · cuna colecho 90 | 8.100 / 5.400 |
| Decoración | decoracion de interiores 10 · decoracion cucuta 20 | 880 |

Lecturas útiles:
- Las búsquedas con la palabra "cucuta" son pocas (10–390). El grueso del volumen está en términos **sin ciudad** ("comedores", "closets") que Google localiza por ubicación. Hay que apuntar a ambos.
- "Decoración" casi no tiene demanda; **se busca por producto**. El sitio debe organizarse por categoría de mueble, no por "inspiración".
- Costo por clic de Google Ads bajo (0,05–0,60 USD): la pauta de búsqueda es barata, pero el volumen pequeño limita su alcance.
- Cifras de volumen de Google Ads son redondeadas y las de ciudad pueden subestimar; úsalas para priorizar, no como pronóstico.

**La SERP la ocupan las redes sociales y los marketplaces.** En las 6 consultas revisadas, Instagram es #1 en 4 y aparece Facebook/TikTok en todas. Mercado Libre aparece en todas. Eso significa que el comprador de Cúcuta ya descubre y compra muebles por Instagram/Facebook/WhatsApp.

| Quién aparece | Ejemplos |
|---|---|
| Locales con web | industriascelco.com.co, starhouse.com.co, penalosa.com.co, cocinasintegralescucuta.com, decoralvarez.com, lacasadelpino.co |
| Nacionales | lucena.com.co, alfa.com.co, homecenter.com.co, madecentro.com, corona.co, exito.com |
| Mapa local (3 resultados) | **UDM** 4,8★ (158 reseñas), Industrias CELCO del Norte 4,4★ (139), Muebles Medina 4,5★ (13), Muebles Alejandra Cúcuta 4,5★ (11) |
| Directorios | cucuta.infoisinfo.com.co, homify, starofservice |

Oportunidades concretas:
1. **Pocos sitios locales propios rankean.** En "comedores cucuta" el #2 es una web en Jimdo gratuito y en "cunas" aparece una en Ueniweb: la barrera técnica es baja.
2. **Reseñas:** los líderes locales tienen ~150; competidores del pack con 1–13 reseñas son alcanzables.
3. **Cunas y decoración de interiores** tienen competencia local débil o inexistente.

## 2. Estrategia

### Fase 0 · Base (semanas 1–2)
- **Reposicionar la home:** hoy se presenta como directorio inmobiliario de PVC. Debe mostrar muebles y decoración para el hogar con acceso a las guías de PVC. Mover o retirar los proyectos de Panamá, que no sirven al público de Cúcuta.
- **Corregir los tres enlaces `verificar-*`**, crear `robots.txt` y decidir si el sitio vive en `www` o en el dominio simple (hoy la canonical dice `www`).
- **No tocar** las URL ni el contenido de `/techo-pvc.html`, `/paredes-pvc.html` y `/piso-laminado.html`; subirlas del puesto 11–26 al top 10 con mejoras de contenido es la victoria más barata.
- Confirmar Search Console y GA4 instalados.
- **Google Business Profile** (esencial si hay local, bodega o punto de entrega; si no, definir área de servicio "Cúcuta y área metropolitana"). Categoría principal "Tienda de muebles". Fotos reales de producto, horarios, WhatsApp.
- **Botón de WhatsApp** en cada página y producto, con mensaje precargado. Es el canal de cierre en este mercado.
- Datos estructurados: `Organization`, `LocalBusiness`, `Product`, `BreadcrumbList`, `FAQPage`.

### Fase 1 · Arquitectura y contenido transaccional (semanas 2–6)
Una página de categoría por intención, con título "X en Cúcuta" y texto único (no solo cuadrícula de productos). Seguir el patrón de URL actual (`.html`) o migrar con redirecciones, sin mezclar ambos:

| URL | Keyword principal | Secundarias |
|---|---|---|
| `/comedores/` | comedores cucuta | comedor 4 puestos, comedor 6 puestos, comedores modernos, mesas de comedor |
| `/cocinas-integrales/` | cocinas integrales cucuta | cocinas modernas, cocina integral pequeña, diseño de cocinas |
| `/camas/` | camas cucuta | cama queen, cama doble, camas modernas, base cama, cama con baúl |
| `/cunas-y-bebes/` | cunas para bebe cucuta | cuna colecho, cuna convertible, muebles para bebe |
| `/closets/` | closets cucuta | closets a medida |
| `/salas/` | muebles de sala cucuta | sofa cama, mesa de centro, centro de entretenimiento |
| `/escritorios/` | escritorios cucuta | escritorios modernos |
| `/colchones/` | colchones cucuta | — |
| `/muebles-a-medida/` | muebles a medida cucuta | carpintería cucuta, fabrica de muebles cucuta |

Prioridad por volumen y debilidad de competencia: **comedores, cocinas, closets, sofá cama, camas, cunas**.
Cada ficha de producto: precio en COP, medidas, material, disponibilidad, tiempo de entrega en Cúcuta, 3+ fotos, y opción "pedir por WhatsApp".

### Fase 2 · Contenido informativo y de confianza (semanas 4–12)
Pocas piezas, orientadas a captar y a ser citadas por buscadores de IA:
- "Cuánto cuesta una cocina integral en Cúcuta (guía de precios 2026)"
- "Medidas de comedor según el tamaño de tu sala"
- "Qué cuna elegir: colecho vs convertible vs tradicional"
- "Cómo amueblar un apartamento pequeño en Cúcuta"
- Página "Quiénes somos" con dirección, entrega, garantía y política de cambios.

### Fase 3 · Autoridad local (continuo)
- Reseñas en Google: objetivo 50 en 90 días (QR en entregas, mensaje de WhatsApp posventa).
- Citas NAP consistentes: cucuta.infoisinfo.com.co, directorios locales, Cámara de Comercio de Cúcuta si aplica.
- Alianzas con arquitectos, constructoras y administradores de proyectos de vivienda nuevos en Cúcuta (backlinks y ventas B2B).
- Usar el nombre "Decorando Espacios" idéntico en web, redes y directorios.

## 3. Redes sociales

Dado que la SERP la dominan Instagram, Facebook y TikTok, aquí compite el negocio, no solo el sitio.

| Red | Rol | Formato | Frecuencia sugerida |
|---|---|---|---|
| **Instagram** (prioridad 1) | Catálogo visual y generación de consultas | Reels de antes/después, tours de ambientes, entrega a clientes; Stories con precio; highlights por categoría | 4–5 posts + 3–5 stories/semana |
| **Facebook** (prioridad 1) | Marketplace y grupos de Cúcuta; público de más edad | Catálogo de Facebook Shop, publicar en grupos locales, anuncios a Cúcuta | 3–4 posts/semana |
| **WhatsApp Business** (prioridad 1) | Cierre de ventas | Catálogo, respuestas rápidas, etiquetas, lista de difusión | diario |
| **TikTok** (prioridad 2) | Alcance económico | Videos cortos de armado, medidas, "cuánto cuesta", detrás de cámaras | 3/semana |
| **Pinterest** (prioridad 3) | Tráfico de inspiración a categorías | Pines de ambientes enlazados a páginas de categoría | 10 pines/semana, automatizable |
| **Mercado Libre** (opcional) | Canal adicional, lo domina en SERP | Publicar los productos más vendidos | según margen |

Regla: **cada publicación lleva a una URL de categoría o producto del sitio**, no solo a mensajes directos, para medir y sumar autoridad.

## 4. Pauta pagada (complemento)
- Google Ads búsqueda local: "comedores", "closets", "cocinas integrales", "cunas para bebe", segmentado a Cúcuta. CPC de referencia 0,05–0,60 USD.
- Meta Ads (Instagram/Facebook) con catálogo y mensajes a WhatsApp, radio de 25 km alrededor de Cúcuta.
- Presupuesto de arranque sugerido: dividir 60/40 entre Meta y Google, ajustando a las ventas por canal tras 30 días.

## 5. Medición
- Posición (`/seo-run decorandoespacios.com.co`), mensual al menos; cada run cuesta ~0,05–0,10 USD con esta config.
- KPIs: clics de Search Console, llamadas/clics de WhatsApp, solicitudes de cotización, reseñas, ventas por canal.
- Metas orientativas a 90 días: top 10 móvil en 4–5 keywords de categoría; presencia en pack local; 50 reseñas.

## 6. Qué falta por verificar
1. Si existe local físico o fábrica en Cúcuta (define el enfoque de Google Business Profile). Las posiciones actuales son nacionales, sobre todo Bogotá.
2. Qué hacer con los proyectos inmobiliarios de Panamá de la home.
3. Margen y logística de entrega, que condicionan la pauta.
4. Volúmenes de TikTok/Instagram: no medidos aquí.
