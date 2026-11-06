# Guía de optimización SEO: glppanamaresidency.com

Fecha del análisis: 6 nov 2026 · Alcance: rastreo de la home, robots.txt, sitemaps y las 45 URLs del sitemap (45 de 45 respondieron 200).

**Qué cubre y qué no.** Todo lo de abajo viene del HTML servido por el sitio. No tuve acceso a Search Console, analítica, posiciones, datos de Core Web Vitals ni al sitio renderizado con JavaScript. Las recomendaciones de rendimiento y las de keywords son por tanto hipótesis a validar con esas fuentes. El schema sí aparece en el HTML estático (JSON-LD), así que esa parte es fiable.

---

## 1. Resumen ejecutivo

**Base técnica sólida:** HTTPS, Cloudflare, 45/45 páginas indexables sin `noindex`, canonical autorreferenciado en todas, sitemap declarado en robots.txt, redirección www → sin www, TTFB de 0,15–0,8 s, títulos únicos en casi todo el sitio y schema Article/Breadcrumb en cada página.

**El problema principal no es técnico, es de estructura de contenido.** El sitio tiene 45 URLs que compiten entre sí por muy pocas intenciones de búsqueda, y mezcla español e inglés sin señalizarlo a Google.

### Top 5 prioridades

| # | Problema | Impacto |
|---|----------|---------|
| 1 | **Canibalización**: ~10 páginas de "real estate Panama", 5 de "qualified investor / golden visa", 5 de "pensionado" | Alto |
| 2 | **11 páginas en español marcadas como `en-US`**, con hreflang solo `en`/`x-default` y sin versión en español de las páginas clave | Alto |
| 3 | **URLs inexistentes devuelven 301 a la home** (soft 404) | Medio-Alto |
| 4 | **Títulos duplicados / desalineados** (`requisito-visa-dorada-panama` tiene el título de otra página; `why-glp` = `why-panama`) | Medio-Alto |
| 5 | **Schema pobre en la home** (LocalBusiness vacío, sin FAQPage/Service, `WebSite` duplicado) y sin datos de contacto estructurados | Medio |

### Quick wins (menos de un día)
1. Corregir título duplicado de `/requisito-visa-dorada-panama/` y de `/why-glp/`.
2. Reducir la home a un solo H1; quitar el segundo H1 de `/contact/`, `/panama-visa-requirements/` (contiene "Bosco di Santa María", un H1 perdido), `/why-glp/`, `/inversionista-calificado-panama/`, `/panama-qualified-investor-program-guide/` y `/residencia-fiscal-panama/`.
3. Añadir `alt` a las imágenes sin él (8 de 16 en la home; 34 de 38 en `/why-glp/`).
4. Cambiar `twitter:card` a `summary_large_image` y eliminar el segundo bloque Open Graph de la home (`og:title="Home"`).
5. Hacer que las URLs inexistentes devuelvan un 404 real.

---

## 2. Hallazgos técnicos

### 2.1 Rastreo e indexación
- **robots.txt**: correcto. Solo bloquea `/wp-admin/` (permite `admin-ajax.php`) y declara `sitemaps.xml`. Sin bloqueos accidentales.
- **Sitemap** (`/sitemaps.xml`): índice con `post`, `page` y `category`. Funciona, pero:
  - `/sitemap.xml`, `/wp-sitemap.xml` y `/sitemap_index.xml` redirigen 301 al real. Aceptable.
  - **Los proyectos (`/proyecto/oceana/`, `/proyecto/the-tides/`, `/proyecto/armonia/`) y las taxonomías `/tipo-de-proyecto/beach|city/` están enlazados desde la home pero no aparecen en el sitemap** (son un custom post type). Son tus páginas más cercanas a la conversión (inmuebles que califican para la visa). Añádelos al sitemap.
  - Revisa que `/category/panama-en/` (páginas de archivo con 700 palabras) merezca estar indexada; si no aporta, `noindex` y fuera del sitemap.
- **Soft 404 (Alto/Medio)**: `/pagina-que-no-existe-xyz/` y `/es/` responden **301 → home**. Google lo trata como soft 404 y diluye señales. **Fix:** que cualquier URL inexistente devuelva 404 con una página útil (buscador + enlaces a las guías principales). Revisa también si hay una regla global de redirección en el plugin SEO/redirecciones.
- **Barra final**: `/faqs` → `/faqs/` (301, correcto). La home enlaza `/real-estate-panama-central-america` **sin** barra final: enlaza siempre a la versión canónica con barra para evitar un salto.

### 2.2 Idioma e internacionalización (Alto)
- Todas las páginas declaran `<html lang="en-US">` y `hreflang` solo `en` + `x-default`, incluidas **11 páginas en español**: `beneficios-visa-pensionado-panama`, `calculadora-costos-inversion-panama`, `como-convierto-mi-residencia-permanente-panamena-en-ciudadania`, `inversionista-calificado-panama`, `paises-sin-visa-a-panama`, `requisito-visa-dorada-panama`, `residencia-fiscal-panama`, `timeline-visa-panama`, `tipos-de-visas-panama`, `visa-panama-britanicos`, `visa-panama-mexicanos`.
- WPML está instalado (5.1.0) pero solo con inglés configurado. Consecuencia: Google puede mostrar contenido en español a audiencia inglesa y no sabe emparejar `calculadora-…` con `cost-calculator-…`.
- **Fix recomendado (elige una):**
  1. *Preferida:* configurar el español en WPML (`/es/…`), mover las 11 páginas, emparejarlas con su equivalente en inglés y emitir `hreflang` recíproco `en` ↔ `es` + `x-default`. `<html lang="es">` en cada una.
  2. *Mínima:* si no vas a mantener dos idiomas, al menos fijar `lang="es"` en esas páginas y no mezclarlas con la navegación inglesa.
- Hay una incoherencia de público: el título de la home apunta a "US buyers", pero 11 páginas apuntan a hispanohablantes (incluyendo México y Reino Unido, con `visa-panama-britanicos`, que está en español). Define a quién sirve cada idioma.

### 2.3 Velocidad y rendimiento (validar con PageSpeed/CrUX)
Medido solo desde HTML y cabeceras:
- Home: **230 KB de HTML**, **42 `<script>` y 16 hojas de estilo**, sólo 3 imágenes con `loading="lazy"`. Constructor Bricks + JetEngine + Bricksforge + Nextbricks + WPML + Site Kit: mucha carga potencial de CSS/JS.
- Las páginas internas pesan 150–170 KB de HTML.
- Cache: `cf-cache-status: DYNAMIC` y `x-kinsta-cache: MISS`: el HTML no se está sirviendo desde caché de Cloudflare aunque envías `s-maxage=86400`. Configura una regla de caché de página en Cloudflare (con purga al publicar) para bajar el TTFB (hoy 0,15–0,8 s, de hecho ya aceptable; lo importante son LCP/INP).
- Imágenes: en la home hay 35 referencias WebP/AVIF frente a 46 JPG/PNG. Convierte las restantes, define `width`/`height` (CLS) y pon `fetchpriority="high"` solo en la imagen LCP.
- **Acción:** pasar PageSpeed Insights y el informe de Core Web Vitals de Search Console en móvil para la home, `/panama-qualified-investor-visa-2/` y un proyecto. Objetivos: LCP < 2,5 s, INP < 200 ms, CLS < 0,1. Desactivar los módulos de Bricks/JetEngine/Bricksforge que no usen las plantillas (carga condicional por página).

### 2.4 Seguridad y cabeceras
- HTTPS válido y redirección www → apex. No pude comprobar `http://` desde el entorno de análisis; verifica manualmente que redirige a HTTPS.
- Sin `Strict-Transport-Security` ni `X-Frame-Options`/`Content-Security-Policy` visibles. Añade HSTS (bonus de confianza) desde Cloudflare.
- Se exponen `/wp-json/`, `xmlrpc.php?rsd` y la versión de WordPress/plugins en las metaetiquetas `generator`. Quita los `generator` y desactiva XML-RPC si no se usa.

---

## 3. Hallazgos on-page

### 3.1 Títulos y metadescripciones
Sobre 45 páginas:

| Problema | Páginas |
|---|---|
| **Título duplicado** | `/requisito-visa-dorada-panama/` y `/panama-visa-cost-lawyer-fee/` ("Panama Immigration Attorney Fees…"). El H1 de la primera es "Requisitos de la Visa Dorada de Panamá", así que **el título de SEO está mal copiado** |
| **Título duplicado** | `/why-glp/` y `/why-panama/` ("Why Invest in Panama: Taxes, Residency & Dollar Economy"). `why-glp` es una página sobre la empresa (Grupo Los Pueblos) y no debe llevar ese título |
| Título > 60 caracteres | `como-convierto…` (84), `panama-qualified-investor-visa` (82), `panama-citizenship-by-investment` (72), `panama-pensionado-visa-requirements` (72), `residencia-fiscal-panama` (69), `visa-panama-mexicanos` (65), `calculadora-costos…` (62) y otras |
| Meta > 160 | `panama-citizenship-by-investment` (192), `panama-second-passport-1` (181), `como-convierto…` (179), `residencia-fiscal-panama` (178), `panama-qualified-investor-visa` (178), `panama-pensionado-visa-requirements` (164) |
| Meta < 120 | `visa-panama-mexicanos` (85), `visa-panama-britanicos` (86), `beneficios-visa-pensionado-panama` (92), `golden-visa-panama` (114), `timeline-visa-panama` (115), `pensioner-visa-benefits-panama` (117), `paises-sin-visa-a-panama` (121) |

**Fix:** una tabla de keyword → título → meta por URL (ver plantilla en la sección 6). Título 50–60 caracteres con la keyword principal al inicio; meta 140–160 con beneficio y llamada a la acción. Las páginas de ficha de proyecto y la home son las que más ganan por CTR.

La home: `Panama Residency by Real Estate Investment | GLP` (48) está bien, pero el H1 visible es "Panama Qualified Investor Program"; alinéalos (el H1 debería contener la misma keyword principal).

### 3.2 Encabezados
- **H1 múltiples** en 7 páginas (lista en Quick wins). En la home el segundo H1 es "From our Blog".
- **H1 genéricos o sin keyword:** `/blog/` y `/category/panama-en/` ("Blog"), `/book-appointment/` ("Book Appointment"), `/projects/` ("Real Estate Projects"), **`/faqs/` ("Personalized Advisory")**: la página de FAQ no tiene ningún H1 sobre preguntas frecuentes. Pon "Panama Residency FAQs: …".
- **Mojibake** en `/panama-qualified-investor-program-guide/`: el segundo H1 contiene `30â€“45` (codificación UTF-8 rota). Corrige el carácter en el editor.
- **Slugs con sufijos de duplicado:** `/panama-qualified-investor-visa-2/` y `/panama-second-passport-1/`, delatan copias. Renombra y redirige 301.
- Las páginas de la home usan H3 como etiquetas de enlace (listado de "Panama Real Estate Investment", "Buy House In Panama", "Panama City Houses For Sale", etc.). Eso es un bloque de enlaces internos con anclas exactas; mejor un listado normal bajo un H2 descriptivo.

### 3.3 Imágenes
- Alt faltante: home 8/16, `/why-glp/` 34/38, la mayoría de guías 8/8 (en las páginas de guía parecen ser imágenes de plantilla/iconos; revisa si son decorativas → `alt=""` explícito, o contenido → alt descriptivo).
- Nombres de archivo descriptivos y WebP en todo.

### 3.4 Open Graph / Twitter
- La home tiene **dos bloques OG** con valores distintos (`og:title` = "Home" en el segundo). Deja uno.
- `twitter:card = summary`; usa `summary_large_image` con imagen 1200×630 por página.
- `fb:app_id`, `fb:pages`, `twitter:site` y `twitter:creator` están vacíos; elimínalos o rellénalos.
- No hay `og:image` en la home: añádelo (afecta a cómo se ve el enlace al compartirlo por WhatsApp/LinkedIn, que es un canal clave para este público).

---

## 4. Estructura de contenido y canibalización (el mayor potencial)

Clústeres con intención solapada, que hoy se disputan el mismo ranking:

### 4.1 Qualified Investor / Golden Visa (5 páginas + home)
`/` · `/panama-qualified-investor-visa/` · `/panama-qualified-investor-visa-2/` · `/panama-qualified-investor-program-guide/` · `/golden-visa-panama/` · `/inversionista-calificado-panama/` (ES)

**Acción:** una **página pilar** (la del programa QIP, que además es el H1 de la home) y dos o tres satélites con intención diferenciada (requisitos/documentos, plazos, comparativa con otras visas). Fusiona `-visa` y `-visa-2` y la guía en una sola URL y redirige las otras con 301. `golden-visa-panama` se queda solo si apuntas a esa búsqueda concreta con ángulo distinto ("golden visa" suele ser la consulta de mayor volumen; si es así, es candidata a pilar en lugar de la actual).

### 4.2 Inmobiliario (10 páginas)
`homes-for-sale-in-panama` · `houses-for-sale-in-panama` · `buy-house-in-panama` · `panama-city-houses-for-sale` · `beach-houses-for-sale-panama-city` · `panama-city-beach-apartments-coast-city-options` · `panama-real-estate-investment` · `investing-in-panama-real-estate` · `real-estate-panama-central-america` · `panama-real-estate-invest-residency`

Muchas son variantes de la misma consulta ("houses/homes for sale Panama") y compiten con portales inmobiliarios muy fuertes. Tu ventaja real es **inmueble + residencia**.
**Acción:**
1. Consolidar en: un pilar "Panama real estate for foreigners" (fusiona `real-estate-panama-central-america`, `investing-in-panama-real-estate` y `panama-real-estate-investment`), una guía "Can foreigners buy a house in Panama" (`buy-house-in-panama`), una página de zona costera y una de ciudad.
2. Fusionar `homes-for-sale` y `houses-for-sale` y redirigir.
3. Todo el clúster debe enlazar a las fichas de proyecto (`/proyecto/…`) y al pilar de QIP con anclas que mencionen la residencia.

### 4.3 Pensionado / retiro (5 páginas, dos idiomas)
`panama-retirement-visa` · `panama-pensionado-visa-requirements` · `pensioner-visa-benefits-panama` · `beneficios-visa-pensionado-panama` (ES) · `us-veterans-retire-in-panama`

Es un público distinto de tu oferta principal (inversión de 300.000 USD). Decide si es línea de negocio; si no, no inviertas más y deja una página y la de veteranos.

### 4.4 Costes y abogados
`cost-calculator-panama-residency-investment` ↔ `calculadora-costos-inversion-panama` (par EN/ES, enlazar con hreflang) · `panama-visa-cost-lawyer-fee` · `panama-immigration-lawyers` · `requisito-visa-dorada-panama` (título mal asignado).

### 4.5 Páginas de "marca"
`/why-glp/` y `/why-panama/` con el mismo título. Separa: `/why-panama/` = beneficios del país; `/why-glp/` = quiénes son, trayectoria, equipo, proyectos entregados (E-E-A-T).

### 4.6 Huecos de contenido que no veo cubiertos
- **Página por proyecto con contenido propio** (precio desde, tipologías, ubicación, tiempos de entrega, cómo encaja con los 300.000 USD). Las tres fichas existen; comprueba que no sean escaparates finos.
- Comparativas "Panama QIP vs. otros programas golden visa" (Portugal, Grecia, España…) para el público estadounidense.
- Contenido de prueba: casos reales de clientes, plazos reales, testimonios verificables, equipo legal con nombre y credenciales.

### 4.7 Enlazado interno
- El 90% del enlazado hacia los artículos parece venir de listados y plantillas. Añade enlaces contextuales dentro del texto desde las guías hacia el pilar de QIP y hacia las fichas de proyecto.
- Cada URL importante a máximo 3 clics de la home: hoy `/blog/` y las guías largas parecen colgar sólo del listado.
- Crea migas de pan visibles (ya hay `BreadcrumbList` en schema; falta mostrarlas).

---

## 5. Schema y datos estructurados

Estado actual en la home: `WebSite` (dos veces), `LocalBusiness` **sin ningún dato salvo el nombre**, `Corporation` con logo y redes sociales. En las páginas internas: `Article`, `WebPage`, `Person`, `Organization`, `BreadcrumbList`.

**Mejoras:**
1. **Unifica en un solo grafo** con `@id` consistentes: un `Organization`/`ProfessionalService` (o `RealEstateAgent`) + un `WebSite`. Elimina el `WebSite` duplicado y el `LocalBusiness` vacío.
2. Completa: dirección, teléfono, email, horario, `areaServed`, `sameAs` y logo. Mantén esos datos idénticos en el pie, la página de contacto y Google Business Profile (NAP consistente).
3. **`FAQPage`** en `/faqs/` y en las guías que ya tienen preguntas y respuestas.
4. **`Service`** para la oferta de gestión de residencia (con `provider` apuntando a la organización).
5. Corrige `"@type": "person"` en minúscula (aparece en `panama-immigration-lawyers`, `panama-visa-cost-lawyer-fee`, `requisito-visa-dorada-panama`, `tipos-de-visas-panama`, `paises-sin-visa-a-panama`): debe ser `Person`.
6. Autores reales con credenciales (`Person` con `jobTitle`, `sameAs` a LinkedIn / colegio de abogados) en los artículos legales.
7. Valida con el Rich Results Test (renderiza JavaScript).

---

## 6. E-E-A-T (crítico en este sector)

Panama residency/inversión es un tema **YMYL** (dinero e inmigración). Google exige señales fuertes de confianza:
- Autoría con nombre, foto y credenciales en cada guía legal; fecha de actualización visible (ya publicas "2026", mantén "Actualizado el…").
- Datos de la empresa verificables: razón social, dirección, licencias, abogados colegiados, registro en Panamá.
- Citas a fuentes oficiales (Servicio Nacional de Migración, Gaceta Oficial, Decreto del programa QIP) con enlace.
- Reseñas y casos reales; perfil de Google Business Profile completo.
- Aviso legal claro de que no es asesoría legal, con política de privacidad y términos (comprueba que están enlazados desde el pie).

---

## 7. Plan de acción por fases

### Semana 1: correcciones
- [ ] Títulos: `/requisito-visa-dorada-panama/`, `/why-glp/`; recortar los >60 caracteres.
- [ ] Metadescripciones fuera de rango (lista arriba).
- [ ] Un solo H1 por página; H1 útil en `/faqs/`, `/blog/`, `/projects/`, `/book-appointment/`.
- [ ] Corregir el mojibake `30â€“45` y el H1 perdido "Bosco di Santa María".
- [ ] 404 reales; probar `/es/` y rutas antiguas.
- [ ] Un solo bloque OG en la home; `summary_large_image`; `og:image`.
- [ ] Alt en imágenes de contenido.
- [ ] Añadir `proyecto/*` y `tipo-de-proyecto/*` al sitemap.
- [ ] Enviar sitemap en Search Console y Bing Webmaster Tools; revisar cobertura e informe de Core Web Vitals.

### Semanas 2–4: estructura
- [ ] Decidir idioma(s) y configurar WPML con español y hreflang recíproco.
- [ ] Mapa de keywords (una intención = una URL); fusionar y redirigir 301 los clústeres 4.1 y 4.2.
- [ ] Renombrar slugs `-2` / `-1` con redirección.
- [ ] Rediseñar el schema (sección 5).
- [ ] Caché de página en Cloudflare, reducción de JS/CSS, imágenes (sección 2.3).

### Meses 2–3: autoridad y contenido
- [ ] Fichas de proyecto con contenido original y casos de uso reales.
- [ ] Páginas de equipo/autor y prueba social.
- [ ] Contenido comparativo y de decisión para público de EE. UU.
- [ ] Digital PR / enlaces desde medios inmobiliarios, de expatriados y de inversión (hoy no tengo datos de backlinks: medir con Ahrefs/Semrush o Search Console → Enlaces).
- [ ] Google Business Profile y citas locales consistentes.

### Medición
- Search Console: impresiones, CTR y posición por clúster (QIP, real estate, pensionado), y las URLs fusionadas.
- GA4 (Site Kit ya está instalado): evento de clic en "Book appointment" y envío del formulario de contacto como conversiones.
- Revisión mensual de canibalización (consultas con más de una URL del sitio en top 20).

---

## 8. Plantilla de mapa de keywords (rellenar con datos de Search Console)

| URL canónica | Keyword principal | Intención | Título (50–60) | Meta (140–160) | Enlaza a | Estado |
|---|---|---|---|---|---|---|
| `/` | panama residency by investment | transaccional | … | … | pilar QIP, proyectos | revisar H1 |
| `/panama-qualified-investor-visa/` | panama qualified investor visa | informativa/comercial | … | … | proyectos, calculadora, contacto | pilar (fusionar `-2` y guía) |
| `/golden-visa-panama/` | golden visa panama | informativa | … | … | pilar QIP | decidir rol |
| … | … | … | … | … | … | … |

---

## 9. Qué no he podido verificar
- Posiciones, tráfico, CTR, páginas indexadas reales (`site:` / Search Console).
- Core Web Vitals reales (CrUX) y puntuación de PageSpeed.
- Backlinks y autoridad de dominio.
- Si `http://` redirige a HTTPS (el entorno de análisis no lo permite).
- Comportamiento tras ejecución de JavaScript (menú, contenido cargado dinámicamente, calculadora).

Si me das exportaciones de Search Console (consultas y páginas, últimos 3–6 meses) puedo convertir las secciones 4 y 8 en un mapa de keywords cerrado y priorizado por tráfico real.
