# Prompts para Claude en Chrome · parásitos y backlinks · glp.com.pa

Contexto real (del `configs/glp.com.pa.yaml`): Grupo Los Pueblos es una promotora inmobiliaria panameña (vivienda, locales, centros comerciales; Ocean Reef Islands, Albrook Mall). Dos mercados: comprador panameño (es) e inversor extranjero (en).
Nota: en una respuesta anterior asumí que GLP era gas licuado. Era un error; todo lo de abajo parte del negocio inmobiliario.

## Reglas de uso (valen para todos los prompts)
- Claude en Chrome trabaja **con tus cuentas reales ya abiertas**. No crea cuentas en masa, no resuelve captchas y no rota proxies.
- Humano en el circuito: Claude **prepara y rellena**, tú revisas y pulsas "Publicar".
- Máximo 2–3 publicaciones por plataforma por semana. Contenido útil, sin texto spun.
- Enlaza a glp.com.pa con 1 enlace natural por pieza; el resto, fuentes externas de autoridad.
- Anchors: 60 % marca/URL desnuda, 25 % genéricos, 15 % keyword parcial.
- Datos de proyectos (precios, entregas, m²) solo desde glp.com.pa o información que tú pegues. No inventar cifras.
- Verifica cada URL antes de usarla: aquí no pude navegar, la lista es candidata, no confirmada.

---

## A. Prompts de investigación (solo lectura)

**A1 · Mapear SERPs parasitables**
```
Abre Google (google.com.pa, ubicación Panamá, idioma es). Para cada keyword de la lista, busca y anota las URLs de las posiciones 1-10 y qué tipo de sitio es cada una (promotora, agregador, foro, red social, medio, UGC).
Keywords: apartamentos en venta en panamá; casas en venta en panamá oeste; proyectos nuevos en panamá; apartamentos en preventa panamá; invertir en bienes raíces en panamá; requisitos para comprar casa en panamá; promotora inmobiliaria panamá.
Devuélveme una tabla: keyword | URL top-10 | dominio | tipo | ¿es UGC (Reddit, Quora, Medium, LinkedIn, YouTube…)? | ¿glp.com.pa aparece?
No hagas clic en anuncios. No modifiques nada.
```

**A2 · Evaluar viabilidad de una plataforma**
```
Entra a [URL de la plataforma]. Sin publicar nada, responde: ¿permite enlaces dofollow o nofollow?, ¿permite enlaces en el cuerpo?, ¿pide verificación o antigüedad de cuenta?, ¿prohíbe contenido promocional en sus términos?, ¿rankea en Google para inmobiliario Panamá (búsqueda site:)? Veredicto: viable / riesgoso / descartar, con 2 líneas de motivo.
```

**A3 · Auditar menciones sin enlace**
```
Busca en Google: "Grupo Los Pueblos" -site:glp.com.pa, "Ocean Reef Islands" -site:glp.com.pa, "GLP Panamá" inmobiliaria -site:glp.com.pa. Lista las páginas que mencionan la marca sin enlazar a glp.com.pa: URL, medio, fecha, contacto visible. Prioriza las de medios o sitios con autoridad.
```

---

## B. Prompts de redacción (preparar borradores)

**B1 · Artículo de LinkedIn / Medium / Substack**
```
Escribe un artículo de 900-1.200 palabras en español para [plataforma], tema: "[tema]". Tono profesional, útil, sin lenguaje de venta agresivo. Estructura: titular claro, introducción con el problema, 4-5 secciones con subtítulos, una lista práctica y cierre. Incluye UN enlace natural a [URL de glp.com.pa] con anchor de marca o genérico, y 2 enlaces a fuentes oficiales (p. ej. ANATI, Registro Público, MIVIOT). No inventes cifras; si falta un dato, márcalo como [DATO A COMPLETAR].
Déjalo como borrador en el editor; NO lo publiques.
```

**B2 · Respuesta en Quora / Reddit**
```
Busca la pregunta [URL] y redacta una respuesta de 150-300 palabras que resuelva la duda con información concreta. Menciona a GLP solo si es relevante, de forma transparente ("trabajo con/represento a…"). Un enlace como máximo, y solo si aporta. Si la normativa del subreddit o de Quora prohíbe autopromoción, dímelo y no lo redactes. Déjalo en borrador.
```

**B3 · Guion y ficha de YouTube**
```
Redacta un guion de 4-6 minutos sobre "[tema]" para Ocean Reef Islands / vivienda en Panamá. Título (≤60 caracteres), descripción de 150-250 palabras con el enlace a glp.com.pa en la primera línea, capítulos con marcas de tiempo, 10 etiquetas y texto alternativo de miniatura.
```

**B4 · Pin e infografía de Pinterest**
```
Propón 5 pines: título, descripción (≤500 caracteres) y texto para la imagen, sobre guías de compra (gastos de cierre, preventa vs. entrega inmediata, requisitos para extranjeros). Cada pin enlaza a la página de glp.com.pa más relevante.
```

**B5 · Versión en inglés para inversor extranjero**
```
Adapta el artículo [pegar] a inglés para un inversor extranjero: contexto (Panama City, Panama Oeste), proceso de compra, residencia por inversión, impuestos. Mismo criterio: un enlace a glp.com.pa/en/, sin cifras inventadas.
```

---

## C. Prompts de publicación asistida (con tu confirmación)

**C1 · Rellenar el editor**
```
Estoy en el editor de [plataforma] con mi cuenta. Pega el contenido del borrador [texto], configura título, etiquetas, imagen de portada y enlace. Antes de publicar, muéstrame una vista previa y espera mi confirmación. No pulses "Publicar".
```

**C2 · Completar un perfil de directorio**
```
Abre [URL del directorio]. Rellena el formulario con estos datos exactos: nombre, dirección, teléfono, web, categoría, descripción [pegar]. Mantén el NAP idéntico al de Google Business Profile. Si hay captcha, verificación por correo o pago, detente y avísame.
```

**C3 · Pedir enlace en una mención sin enlace**
```
Abre [URL de la mención] y localiza el contacto de la redacción. Redacta (sin enviar) un correo breve y cortés pidiendo que enlacen "Grupo Los Pueblos" a glp.com.pa. Déjalo como borrador en Gmail.
```

---

## D. Prompts de control

**D1 · Registro de lo publicado**
```
Abre mi hoja [URL de Google Sheets] y añade una fila por cada pieza publicada hoy: fecha | plataforma | URL | keyword objetivo | anchor | destino en glp.com.pa | estado de indexación (pendiente).
```

**D2 · Verificar indexación (a los 7 días)**
```
Para cada URL de la hoja con estado "pendiente", busca en Google "site:[URL]" y anota si está indexada, y en qué posición aparece para su keyword. Actualiza el estado. No envíes solicitudes de indexación.
```

---

## URLs candidatas (verificar con A2 antes de usar)

### Tier 1 · Perfiles y contenido propio (viables)
| Plataforma | URL | Uso | Enlace |
|---|---|---|---|
| LinkedIn (página + artículos) | linkedin.com/company/… | Artículos de mercado, ejecutivos | nofollow, aporta autoridad y tráfico |
| YouTube | youtube.com | Tours de proyectos, guías | nofollow, rankea en vídeo |
| Google Business Profile | business.google.com | Local, sala de ventas | señal local clave |
| Pinterest | pinterest.com | Infografías y fotos de proyectos | nofollow |
| Facebook / Instagram | facebook.com, instagram.com | Señal de marca | nofollow |
| Issuu / Scribd / SlideShare | issuu.com | Brochures y catálogos en PDF | varía |
| Medium / Substack | medium.com, substack.com | Guías de inversión (es/en) | nofollow o variable |

### Tier 2 · Comunidades (con cuentas reales y cautela)
| Plataforma | URL | Uso | Riesgo |
|---|---|---|---|
| Reddit | reddit.com/r/Panama | Responder dudas de compra | Alto si hay autopromoción |
| Quora | es.quora.com | Preguntas "comprar casa en Panamá" | Medio |
| Foros de expatriados | por verificar | Inversor extranjero | Medio, revisar normas |

### Tier 3 · Directorios y cámaras (Panamá)
| Entidad | Nota |
|---|---|
| Cámara Panameña de la Construcción (CAPAC) | Membresía, enlace de alto valor |
| Cámara de Comercio, Industrias y Agricultura de Panamá | Directorio de socios |
| ACOBIR / APADE (gremios inmobiliarios) | Verificar si GLP es miembro |
| Páginas Amarillas Panamá, Yelu, Foursquare | Citas NAP |
| Encuentra24, Compreoalquile, Inmoproyectos Panamá | Agregadores: fichas de proyectos, y son competidores reales en la SERP |

### Tier 4 · Prensa y medios (outreach, ver C3)
La Prensa, Panamá América, TVN, Metro Libre, Forbes Centroamérica, medios de real estate internacionales para la serie B.

### Descartar
Directorios de enlaces genéricos, bookmarking masivo, foros con spam, cuentas nuevas sin historial.

---

## Contenidos recomendados (por intención de búsqueda)

| Prioridad | Contenido | Plataformas | Keyword |
|---|---|---|---|
| Alta | Guía: requisitos para comprar casa en Panamá (nacional y extranjero) | LinkedIn, Medium, Quora, YouTube | requisitos para comprar casa en panamá |
| Alta | Preventa vs. entrega inmediata: ventajas y riesgos | LinkedIn, Pinterest, YouTube | apartamentos en preventa panamá |
| Alta | Invertir en bienes raíces en Panamá (versión es y en) | Medium, Substack, LinkedIn | invertir en bienes raíces en panamá |
| Media | Panamá Oeste: dónde comprar casa y cómo es vivir allí | LinkedIn, YouTube, Reddit | casas en venta en panamá oeste |
| Media | Gastos de cierre, hipoteca e impuestos al comprar | Quora, Medium, Pinterest | comprar apartamento en ciudad de panamá |
| Media | Ocean Reef Islands: qué es y cómo funciona la compra | YouTube, LinkedIn, Issuu | ocean reef islands |
| Baja | Historia de GLP desde 1985, proyectos entregados | LinkedIn, Wikipedia-style en Crunchbase | grupo los pueblos |

## Orden de ejecución sugerido
1. Semana 1: A1 y A3, Google Business Profile, directorios (C2).
2. Semana 2: B1 y B3 → C1 en LinkedIn y YouTube.
3. Semana 3: A2 en Quora/Reddit, B2; outreach de menciones (C3).
4. Semana 4: serie en inglés (B5), registro (D1) y primera medición (D2).
