# Decorando Espacios · Estrategia v2: datos en la web y en la ficha de búsqueda

Complementa a `decorandoespacios-cucuta-estrategia.md`. Base de datos: DataForSEO (Google Ads y SERP, 2026-10-01) y el estado verificado del sitio (guía de acabados PVC con 141 keywords y sin páginas de muebles).

**Idea central:** Google debe entender una sola entidad, *Decorando Espacios, muebles y decoración en Cúcuta*, con los mismos datos en cuatro sitios: la web, la ficha de Google Business, el snippet orgánico y las redes. Cada dato (nombre, dirección o zona, teléfono, categorías, horario, precios) se define una vez y se copia igual en todos.

## 1. Datos maestros (la fuente única)

Antes de tocar nada, completar esta tabla. Todo lo demás sale de aquí. `[ ]` = falta confirmar con el negocio.

| Dato | Valor |
|---|---|
| Nombre comercial | Decorando Espacios |
| Tipo de negocio | `[ ]` tienda con local, o negocio de entrega y servicio a domicilio |
| Dirección / barrio | `[ ]` (si no hay local visitable, no se publica dirección) |
| Teléfono y WhatsApp | `[ ]` el mismo en web, ficha y redes |
| Horario | `[ ]` |
| Zona de servicio | Cúcuta, Villa del Rosario, Los Patios, El Zulia `[ ]` confirmar entrega |
| Medios de pago, garantía, entrega | `[ ]` |
| Moneda | COP en todas las fichas |

## 2. La ficha de búsqueda (Google Business Profile)

Es el activo que decide el mapa local, donde hoy ganan UDM (158 reseñas) y CELCO del Norte (139).

- **Nombre:** el nombre real del negocio, sin añadir keywords ("Decorando Espacios", no "Decorando Espacios muebles baratos Cúcuta"). Google suspende fichas con relleno.
- **Dirección:** solo si el local existe y recibe clientes. Si no, configurar **negocio de área de servicio** y ocultar la dirección. Nunca usar una dirección ficticia.
- **Categoría principal:** "Tienda de muebles". **Secundarias** a elegir entre las que Google ofrezca: tienda de decoración del hogar, tienda de colchones, fabricante de muebles (solo si fabrican), contratista de cielos rasos o de acabados (si instalan PVC). Confirmar los nombres exactos en el panel.
- **Descripción (750 caracteres):** qué venden, a quién, zona, y lo que los diferencia (PVC, medida, entrega). Sin enlaces ni promociones.
- **Productos:** un producto por categoría con precio en COP: comedores, cocinas integrales, camas, cunas, closets, sofá cama, colchones, escritorios.
- **Servicios:** instalación de cielo raso PVC, muebles a medida, diseño de cocinas (si aplica).
- **Fotos y video:** mínimo 25 fotos reales (local, productos, entregas, instalaciones). Es lo que los competidores del mapa tienen y lo que más pesa en móvil.
- **Mensajes y WhatsApp** como enlace de contacto; enlace web a `/muebles-cucuta/` (página local, ver sección 3), no a la home.
- **Preguntas y respuestas:** sembrar 8 preguntas reales con respuesta (envío, garantía, medidas a medida, formas de pago, tiempos).
- **Publicaciones:** 1 a la semana (producto nuevo, oferta, instalación).
- **Reseñas:** meta de 50 en 90 días (QR en la entrega y mensaje de WhatsApp a los 7 días). Responder todas. Nunca comprar ni incentivar con descuento por reseña positiva.

## 3. Organización de la web

### 3.1 Arquitectura
```
/                       Home: muebles y decoración para el hogar en Cúcuta (reposicionada)
/muebles-cucuta/        Página local: zona, entrega, contacto, mapa, reseñas, categorías
/comedores/ /cocinas-integrales/ /camas/ /cunas-y-bebes/ /closets/
/salas-y-sofa-cama/ /escritorios/ /colchones/ /muebles-a-medida/
/acabados-pvc/          Hub de lo que ya rankea
   /techo-pvc.html  /paredes-pvc.html  /piso-laminado.html  /paredes-3d.html   (NO cambiar URL)
/guias/                 Guías de precios, medidas y cómo elegir
/entrega-garantia-pagos/  /nosotros/  /contacto/
```
Regla: el sitio actual usa `.html`. Mantener ese patrón en lo nuevo o migrar todo con redirecciones 301; no mezclar.

### 3.2 Plantillas y datos que lleva cada una

| Plantilla | Debe mostrar | Schema |
|---|---|---|
| Home | Qué vendemos, zona, teléfono/WhatsApp, 6 categorías, reseñas | `Organization`, `WebSite` |
| Local `/muebles-cucuta/` | Zona de entrega, horario, mapa, reseñas, preguntas frecuentes | `FurnitureStore` o `LocalBusiness`, `FAQPage` |
| Categoría | Texto único de 250–400 palabras, filtros, rango de precios en COP, FAQ | `CollectionPage`, `BreadcrumbList` |
| Producto | Precio COP, medidas, material, disponibilidad, entrega, 3+ fotos, botón WhatsApp | `Product` + `Offer` (precio, `availability`) |
| Guía | Respuesta directa en las 2 primeras líneas, tabla, enlaces a categoría | `Article`, `FAQPage` |
| Footer global | Nombre, teléfono, zona, horario, redes (idénticos a la ficha) | `Organization` con `sameAs` a Instagram, Facebook, TikTok, ficha |

Los datos estructurados deben coincidir con lo visible; no marcar precios o reseñas que no se muestran en la página.

### 3.3 Cómo se ve en el resultado de búsqueda (snippet)

| Página | Title (≤60) | Meta description (≤155) |
|---|---|---|
| Home | Muebles y decoración en Cúcuta \| Decorando Espacios | Comedores, cocinas integrales, camas, cunas y closets con entrega en Cúcuta. Pide por WhatsApp y recibe asesoría. |
| Comedores | Comedores en Cúcuta: 4 y 6 puestos \| Decorando Espacios | Comedores modernos de 4 y 6 puestos con precio en pesos y entrega en Cúcuta y área metropolitana. Cotiza por WhatsApp. |
| Cocinas | Cocinas integrales en Cúcuta \| Diseño y precios | Cocinas integrales a medida. Mira modelos, precios por metro y tiempos de entrega en Cúcuta. |
| Cielo raso PVC | Cielo raso PVC en Cúcuta: precios e instalación | Techo PVC blanco y color madera. Precio por m², instalación y entrega en Cúcuta. |

Estas son propuestas: confirmar precios y condiciones reales antes de publicar.

### 3.4 Enlazado interno
- Cada página PVC enlaza a la categoría de muebles afín (cielo raso PVC → cocinas, closets, salas).
- Cada categoría enlaza a `/muebles-cucuta/` y a 2–3 guías.
- Breadcrumbs en todas las páginas.

### 3.5 Técnico
Crear `robots.txt` (hoy da 404), declarar el sitemap, decidir `www` o dominio simple y hacer 301 al otro (la canonical actual dice `www`), arreglar los tres enlaces `verificar-*` de la home, conectar Search Console y GA4 con eventos: clic en WhatsApp, clic en teléfono, solicitud de cotización, clic en "cómo llegar".

## 4. Keywords regionales

### 4.1 Lo que dicen los datos (Google Ads, búsquedas mensuales)
Hay dos medidas distintas: la frase buscada en Colombia, y las búsquedas hechas desde la región.

**Frases con lugar (en todo Colombia):**

| Keyword | Vol. | Keyword | Vol. |
|---|---|---|---|
| muebles cucuta | 590 | muebles ocaña | 50 |
| colchones cucuta | 260 | escritorios cucuta | 50 |
| drywall cucuta | 110 | muebles villa del rosario | 40 |
| camas cucuta | 90 | cocinas integrales cucuta | 40 |
| comedores cucuta | 70 | muebles pamplona | 30 |
| sofa cama cucuta | 30 | decoracion cucuta | 30 |
| cielo raso pvc cucuta | 10 | colchones ocaña | 20 |

**Búsquedas hechas desde Norte de Santander (sin escribir la ciudad):**
escritorios 1.000 · closets 880 · sofá cama 590 · muebles 590 · mueblerías 590 · colchones 590 · **cielo raso pvc 480** · drywall 480 · comedores 480 · cocinas integrales 320 · camas 320 · láminas pvc para pared 170 · cunas 170 · carpintería 170 · muebles cerca de mi 110.

**Búsquedas hechas desde Cúcuta (palabras reales del lugar):**
escritorio 590 · sofá cama 390 · muebles 390 · **mueblería 390** · mesas 390 · sillas de escritorio 320 · comedores 320 · comedor 4 puestos 320 · **cielorraso pvc 320** · cocinas integrales 260 · cocina integral 210 · closets modernos 210 · repisas flotantes 210 · estanterías 210 · camas 210 · armarios 170 · tocador 140 · peinadora 140 · zapatero 110 · mueble para tv 110 · cómoda 110 · alacena 110 · somier cama 110 · pvc para techos 110.

### 4.2 Lecturas útiles
1. **El PVC tiene demanda real en la región.** "Cielo raso pvc" suma 480 búsquedas desde Norte de Santander y "cielorraso pvc" 320 desde Cúcuta, y el sitio ya tiene autoridad en PVC. Es el puente más fuerte: una página de cielo raso PVC para Cúcuta, con instalación, tiene demanda y base.
2. **"Muebles cerca de mi" (6.600 en Colombia, 110 en Norte de Santander)** es intención de mapa. Se gana con la ficha, no con texto: cercanía, reseñas y categoría.
3. **Municipios:** los volúmenes de Villa del Rosario, Ocaña y Pamplona son de 20–50. No crear una página por municipio (páginas casi vacías perjudican). Basta una sección "Zona de entrega" en `/muebles-cucuta/` con los municipios. Solo Ocaña (50) y Pamplona (30) merecerían página si el negocio entrega allí con condiciones propias.
4. **Vocabulario local:** mueblería, peinadora, tocador, somier, alacena, zapatero, cielorraso. Usarlo en títulos y descripciones; no cambia la intención pero captura variantes.
5. **Comparación con Homecenter:** "closets homecenter" (260) y "sofa cama homecenter" (110) muestran que el comprador compara con grandes cadenas. Responder con guías de comparación (precio, medida, entrega local), sin usar su marca como keyword principal.

### 4.3 Qué página apunta a qué

| Página | Keyword principal | Regionales y variantes |
|---|---|---|
| `/muebles-cucuta/` | muebles cucuta | mueblería cucuta, mueblerías en cucuta, muebles norte de santander, muebles villa del rosario, muebles los patios |
| `/comedores/` | comedores cucuta | comedor 4 puestos, comedor 6 puestos, comedores modernos |
| `/cocinas-integrales/` | cocinas integrales cucuta | cocina integral, alacena, cocinas modernas |
| `/camas/` | camas cucuta | camas modernas, camas queen, somier cama, cómoda, peinadora |
| `/cunas-y-bebes/` | cunas para bebe cucuta | cuna colecho |
| `/closets/` | closets cucuta | closets modernos, armarios, zapatero |
| `/salas-y-sofa-cama/` | sofa cama cucuta | mueble para tv, mesas |
| `/escritorios/` | escritorios cucuta | sillas de escritorio |
| `/colchones/` | colchones cucuta | colchones ocaña, colchones pamplona |
| `/acabados-pvc/` + `/techo-pvc.html` | cielo raso pvc cucuta | cielorraso pvc, pvc para techos, techo pvc color madera, drywall cucuta (si lo ofrecen) |

## 5. Qué más agregar

- Página **"Entrega, garantía y pagos"** con tiempos por municipio y condiciones reales.
- **Cotizador por WhatsApp:** mensaje precargado con el producto y la medida.
- **Catálogo en Facebook/Instagram Shop y Google Merchant Center** (fichas gratuitas de producto; verificar disponibilidad para Colombia).
- **Galería de proyectos** con ubicación general (barrio o municipio), fotos reales y qué se instaló.
- **Testimonios y reseñas** visibles con nombre y producto, con permiso del cliente.
- **Guías** con respuesta directa: precio de cielo raso PVC por m² en Cúcuta, medidas de comedor por tamaño de sala, cuánto cuesta una cocina integral, cómo elegir cuna.
- **Video corto** por categoría (también sirve para TikTok y la ficha).
- **Servicio de instalación PVC** como producto visible: une lo que ya rankea con la venta nueva.
- **Hipótesis a validar:** Cúcuta es zona de frontera; si hay compradores de otros países, ofrecer envío o retiro y medios de pago acordes. No está medido.

## 6. Cronograma

| Plazo | Entregables |
|---|---|
| Días 1–14 | Tabla de datos maestros; ficha de Google Business completa (categorías, productos, 25 fotos, WhatsApp); `robots.txt`, www/redirección, enlaces `verificar-*`; Search Console y GA4 |
| Días 15–45 | Home reposicionada; `/muebles-cucuta/`; páginas de comedores, cocinas, camas, closets; schema; títulos y metas |
| Días 45–90 | Cunas, sofás, escritorios, colchones; guías; hub PVC con enlazado a muebles; 50 reseñas; primera medición con `/seo-run` |

## 7. Cómo medir
- Posición de las 16 keywords semilla (config), mensual, móvil.
- Ficha: vistas, llamadas, clics a WhatsApp, "cómo llegar", reseñas.
- Web: clics y consultas en Search Console, eventos de contacto, páginas de muebles con impresiones.
- Control: que las páginas PVC (`/techo-pvc.html`, `/paredes-pvc.html`) no pierdan posiciones durante la transición.

## 8. Pendientes de validar
1. Si existe local visitable o es negocio de área de servicio.
2. Municipios con entrega y sus tiempos.
3. Si instalan PVC y drywall (condiciona categorías y servicios en la ficha).
4. Precios, garantía y medios de pago reales para el schema y los snippets.
5. Categorías exactas disponibles en Google Business en el panel.
