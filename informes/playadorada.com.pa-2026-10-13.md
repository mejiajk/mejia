# Auditoría SEO · E-E-A-T · AEO · GEO — playadorada.com.pa (Playa Dorada Residences & Beach Club)

Fecha: 2026-10-13 (UTC) · Prompt: `prompts/seo-auditoria-inmobiliaria-panama.md` (versión con variables de Playa Dorada) · Fuente: DataForSEO + respuestas de ChatGPT, Gemini, Perplexity y Claude vía API.

---

## 1. CONTEXTO

| Parámetro | Valor |
|---|---|
| Web | https://www.playadorada.com.pa/ |
| Marca | Playa Dorada (og:site_name "Playa Dorada Panamá"). Las IA lo llaman *Playa Dorada Residences & Beach Club*. |
| Modelo de negocio | **Desarrollo residencial de playa con web propia de proyecto** (variable sin rellenar). Evidencia en la home: H1 "Propiedades en la playa", H2 "Variedad de Modelos", "Amenidades"; en las URLs: `/casas/`, `/apartamentos/`, `/club-de-playa/`, `/alquileres/`, `/property-management/`. |
| Ubicación del proyecto | **Vacamonte, distrito de Arraiján, Panamá Oeste.** La home dice "A 30 minutos de la ciudad" y "Panamá Oeste". El corregimiento exacto (Vista Alegre) lo dan las IA y **no está verificado**. |
| `ZONAS` de tu archivo | Panamá, Costa del Este, Punta Pacífica, Coronado. **El proyecto no está en ninguna de las cuatro.** Costa del Este aparece solo por la sección `/alquileres/` del sitio; Coronado es la zona de playa comparable. Punta Pacífica: sin relación encontrada. |
| Relación con GLP | **Sin confirmar.** ChatGPT lo atribuye a Grupo Los Pueblos (GLP) y cita tanto `glp.com.pa/proyecto/playa-dorada/` como `playadorada.com.pa`. Pero en la SERP de "playa dorada vacamonte" también aparece `grupogeapanama.com` ("Playa Dorada – Grupo GEA Panamá – Desarrollo de Proyectos"), así que el papel de **Grupo GEA** está por aclarar. |
| `location_code` | **2591** (Panamá, país). Vacamonte figura como 9244635 (no usado). |
| Idiomas | `es` y `en`. Existe subcarpeta `/en/` (`/en/home/`, `/en/news-en/...`); hreflang: N/D. |
| Dispositivo SERP | desktop |
| Ventana de tendencia | 24 meses (2024-08 → 2026-08) |
| Gasto | ≈ 4,7 USD (saldo 51,10 → 46,40) |

Pie general: `DataForSEO · location_code 2591 · es/en · 2026-10-13`.

**Limitación de acceso:** `playadorada.com.pa` tampoco es accesible desde este entorno (política de red). Lo on-page viene de `/v3/on_page/instant_pages` y cubre solo la home.

---

## 2. RESUMEN EJECUTIVO

1. **Estado:** 218 keywords posicionadas en Panamá (7 en pos. 1, 6 en pos. 2–3, 31 en pos. 4–10, 48 en pos. 11–20) y ~911 de tráfico orgánico estimado. **El 84 % de ese tráfico (762) cae en la home.** En la SERP en vivo, la web es **#1 y #2 para "casas de playa panamá"**.
2. **Mayor riesgo:** el proyecto está repartido en varios dominios. `glp.com.pa/proyecto/playa-dorada/` (pos. 13 para "playa dorada"), un listado del banco (`cajadeahorros.com.pa`, pos. 1 para "playa dorada vacamonte") y la propia web compiten por las mismas búsquedas, y la desarrolladora no está clara en las fuentes.
3. **Mayor oportunidad:** `playa dorada vacamonte` (387/mes, +93 %, Emergente real) y `playa vacamonte` (1.263/mes; CPC 2,80 USD, el más alto de la auditoría). Atención: el +96 % de `playa vacamonte` está **inflado por 6 meses en cero** al inicio de la serie; comparando solo meses con datos sale ≈ +31 %.
4. **Brecha E-E-A-T principal:** sin schema, sin autores en el blog, tiempos de carga muy malos (TTFB 3,6 s; LCP 7,2 s medido por el rastreador) y desarrolladora sin una declaración clara en lo rastreado.
5. **Estado en IA:** es el mejor de los tres sitios auditados. `playadorada.com.pa` es **el dominio más citado (67 veces)** en las respuestas sin nombrar la marca, gracias al blog y a las noticias en inglés. Perplexity la menciona en 12/33 respuestas sin marca, Gemini en 14/33, ChatGPT en 3/33. **Claude (sin búsqueda web) no conoce el proyecto** y sugiere que podría ser la Playa Dorada de la República Dominicana.
6. **Acción única prioritaria:** definir y declarar la **entidad** (qué es, quién lo desarrolla, dónde está) en una página con datos fechados, y ordenar la relación con `glp.com.pa` y el listado bancario para que el proyecto tenga una sola fuente principal.

---

## 3. INVENTARIO

Fuente: `ranked_keywords`, `relevant_pages` (es-PA) y URLs citadas por los LLM. Tráfico estimado (ETV) de DataForSEO, no de Analytics. Pie: `/v3/dataforseo_labs/google/relevant_pages/live` · 2591 · es · 2026-10-13.

| URL | Tipo | Keywords | ETV | Notas |
|---|---|---|---|---|
| `/` | home | 93 | 762 | `playa dorada` pos. 4; `playa dorada panama` pos. 5; `playa dorada vacamonte` pos. 1 (base de datos) |
| `/club-de-playa/` | amenidades | 15 | 37 | `beach club` pos. 17; `playa la piscina` (1.900/mes) pos. 21 |
| `/ubicacion/` | zona | 6 | 33 | `playa vacamonte` pos. 15 |
| `/panama-oeste/` | zona | 1 | 12 | |
| `/producto/caracol/` | modelo de casa | 3 | 10 | **rankea pos. 55 por "playa caracol" (4.400/mes): ruido, ver §4.2** |
| `/alquileres/` | alquileres | 27 | 8 | keywords de **Costa del Este** (`alquileres costa del este`, pos. 45–49): ver §3.1 |
| `/casas/`, `/apartamentos/` | categoría | 13 / 2 | 8 / 1 | `casa de playa` pos. 14 |
| `/tour-virtual/` | medios | 6 | 4 | |
| `/blog/noticias-es/descubre-los-mejores-proyectos-residenciales-en-arraijan-vacamonte/` | blog | 16 | 7 | |
| `/blog/noticias-es/villamarina-avance-de-obras/` | blog | 1 | 8 | `villamarina` pos. 13: **homónimo de un hotel**, ver §4.2 |
| `/blog/casas-de-playa-en-panama-con-amenidades-para-toda-la-familia/`, `/blog/casas-en-arraijan-con-club-de-playa-.../` | blog | 1–3 | 1–3 | `casas de playas en panama` pos. 15; `arraiján country club` pos. 30 |
| `/blog/noticias-es/venta-casas-vacamonte/`, `/blog/noticias-es/propiedad-de-playa-asequible-panama/`, `/blog/que-hace-unico-al-desarrollo-de-playa-dorada-en-la-costa-pacifica/` | blog | — | — | **citadas 9 veces cada una por las IA** |
| `/en/news-en/beach-condos-30-minutes-from-panama-city/` (y `-2/`) | blog EN | — | — | **citadas 11 veces cada una** |
| `/en/news-en/live-in-playa-dorada-the-most-comprehensive-residential-project-in-west-panama/`, `/en/home/` | EN | — | — | citadas 6 veces cada una |
| `/producto/altamarina-19/`, `/producto/miramar/`, `/propiedades/5-beneficios-de-tener-una-casa-frente-al-mar-en-playa-dorada/`, `/contacto/`, `/property-management/` | producto/otros | 1–3 | 0–2 | |

Serie EN medida en EE. UU.: no se midió; en Panamá/inglés `domain_rank_overview` no devolvió datos (N/D). Fichas vendidas, URLs indexadas y fecha de último cambio: **N/D**.

**Movimiento (es-PA):** 144 keywords nuevas, 31 suben, 35 bajan, 75 perdidas.

### 3.1 La sección de alquileres

`/alquileres/` posiciona 27 keywords de **Costa del Este** y de alquiler (`alquiler en costa del este` 210/mes, `alquiler casa de playa` 170/mes), todas en pos. 26–49 y con tráfico casi nulo (ETV 8). No pude comprobar el contenido. Hay que confirmar si la empresa gestiona alquileres en Costa del Este: si sí, merece su propio hub; si no, la sección diluye el tema del sitio.

---

## 4. UNIVERSO DE KEYWORDS (con tendencia)

Pie: `/v3/keywords_data/google_ads/search_volume/live` y `/v3/dataforseo_labs/google/keyword_suggestions/live` · 2591 · es/en · 2026-10-13. `yoy` = media 12 m ÷ media 12 m previos − 1. Clases según el prompt.

### 4.1 Con tendencia medida

| Keyword | Idioma | Vol. 12 m | Previo | yoy | Mom. 3 m | Clase |
|---|---|---|---|---|---|---|
| **playa vacamonte** | es | 1.263 | 643 | +96 %* | 1,25 | **Creciente / Emergente (ver nota)** |
| playa dorada | es | 1.035 | 853 | +21 % | 1,22 | Creciente |
| playa dorada panamá / panama | es/en | 967 | 1.013 | −5 % | 1,0 | Estable |
| villamarina | es | 717 | 500 | +43 % | 1,22 | Emergente (**ruido: hotel homónimo**) |
| **playa dorada vacamonte** | es | 387 | 200 | **+93 %** | 1,31 | **Emergente** |
| vacamonte panama | en | 240 | 207 | +16 % | 1,34 | Creciente |
| alquileres costa del este | es | 221 | 189 | +17 % | 0,92 | Creciente |
| arraiján country club | es | 219 | 157 | +40 % | 1,24 | Emergente (proyecto de otra empresa) |
| alquiler apartamento costa del este | es | 174 | 136 | +28 % | 0,96 | Creciente |
| buy house in panama | en | 127 | 126 | +1 % | 0,85 | Estable |
| coronado panama real estate | en | 124 | 103 | +20 % | 1,0 | Creciente |
| casas en venta costa del este | es | 108 | 89 | +21 % | 1,16 | Creciente |
| beach houses panama | en | 93 | 95 | −3 % | 1,0 | Estable |
| casa de playa coronado | es | 66 | 60 | +10 % | 1,0 | Estable |
| casas en venta coronado | es | 57 | 63 | −11 % | 0,52 | Declive |
| apartamentos en venta costa del este | es | 51 | 45 | +13 % | 1,38 | Creciente |
| casas en vacamonte | es | 43 | 39 | +9 % | 0,87 | Estable |
| vacamonte panamá | es | 37 | 23 | +63 % | 1,71 | Emergente (volumen bajo) |
| casas en venta panamá oeste | es | 21 | 22 | −4 % | 1,17 | Estable |
| casa de playa panamá | es | 20 | 17 | +20 % | 0,6 | Creciente |
| panama beach house for sale | en | 16 | 14 | +12 % | 3,0 | Creciente |
| casas en arraiján | es | 11 | 18 | −41 % | 0,5 | Declive |
| casas en venta arraiján | es | 4 | 9 | −55 % | 1,0 | Declive |

\* **Nota sobre `playa vacamonte`:** la serie de Google Ads tiene 0 en los primeros 6 meses (2024-08 a 2025-01), lo que hace el "previo" artificialmente bajo. Comparando solo los meses con datos (feb–ago 2025: media 1.103 vs feb–ago 2026: media 1.443) sale **+31 %**, con momentum 1,25. Trátala como **Creciente con tendencia a Emergente**, no como +96 %.

**Sub-demanda (Labs, 12 m):** `playa dorada residences` 1.600/mes (informacional) · `vacamonte` 8.100 · `playa dorada arraijan` 110 · `bayside playa dorada` 110. **`casas de playa en panama`** y `casas de playa panama`: 320/mes cada una (Labs; Google Ads devuelve 20/mes para `casa de playa panamá`, una discrepancia a tener en cuenta). Alquiler: `casas de alquiler en la playa panama` 170/mes en varias formas.

### 4.2 Ruido de intención (no optimizar)

Una parte grande de las keywords posicionadas no tiene que ver con el proyecto:
- **Homónimos de "dorado":** `dorado`, `dorado lakes`, `dorado springs`, `residencial bosque dorado` (1.900), `plaza dorado`, `paseo dorado`, `urbanizacion el dorado`.
- **`praia amador`** (3.600) y `praia`: de otro país/idioma.
- **`playa caracol`** (4.400): la web posiciona (pos. 55) por una de sus casas llamada "Caracol" (`/producto/caracol/`). Es el nombre de otro lugar y de un proyecto de GLP: genera confusión de entidad. Recomiendo no apuntar a esa palabra.
- **`villamarina`** (717, +43 %): la SERP la domina el hotel Villa Marina de Playa Venao (Pedasí), no el proyecto. La subida de volumen es probablemente del hotel.
- **`playa la piscina`, `playa banco`, `playa honda`, `playa monagre`:** nombres de otras playas, con la página `/club-de-playa/`.

### 4.3 Lecturas

- **Los términos con mejor señal son locales y de marca**: `playa dorada`, `playa dorada vacamonte`, `playa vacamonte`. La demanda de compra por categoría ("casas de playa", "casas en venta panamá oeste") es pequeña en Google Ads (20–320/mes).
- **35 de 72 semillas son N/D en Google Ads**: `casas de playa en venta`, `vivir en panamá oeste`, proceso de compra, gastos de cierre, financiamiento, `casas con club de playa panamá` y similares. Siguen apareciendo en PAA y en respuestas de IA.
- **Google Trends no se consultó para este sitio** (en los otros dos casos devolvió casi todo 0 para estos términos).
- **Costa del Este y Punta Pacífica** aparecen solo por la sección de alquileres; para compra de casa de playa, la competencia directa es **Coronado** (`coronado panama real estate` 124/mes en inglés, +20 %).

### 4.4 Score de oportunidad

`volumen` (log, tope 1.500) y `tendencia` de datos; `valor_comercial`, `facilidad` y `encaje_aeo_geo` son **estimaciones mías**, no de API. Para ordenar, no para medir.

| Keyword | Vol. | Clase | Score |
|---|---|---|---|
| playa dorada vacamonte | 387 | Emergente | 0,76 |
| casas de playa panamá (volumen Labs 320) | 320 | Creciente | 0,74 |
| playa vacamonte | 1.263 | Creciente–Emergente | 0,73 |
| playa dorada | 1.035 | Creciente | 0,69 |
| coronado panama real estate | 124 | Creciente | 0,65 |
| arraiján country club | 219 | Emergente | 0,63 |
| alquileres costa del este | 221 | Creciente | 0,62 |
| beach houses panama | 93 | Estable | 0,58 |
| buy house in panama | 127 | Estable | 0,57 |
| casas en venta coronado | 57 | Declive | 0,45 |

**Quick wins (pos. 4–20):** `playa dorada` (4; en vivo 9), `playa dorada panama` (5), `beach club` (17), `playa vacamonte` (15; en vivo 13), `casas de playa en panama` (9–15; **en vivo #1 y #2**), `casa de playa` (14), `actividades aire libre` (9; 170/mes), `playa en panama oeste` (11; 210/mes).
**Dejar de alimentar:** `casas en arraiján`, `casas en venta arraiján` (en declive) y el ruido del §4.2.
**Competidores directos nombrados:** Grupo GEA (aparece en la SERP), proyectos de casas en Panamá Oeste (Viviendas de Primera, Grupo Su Casa, GPRO Vivienda). **Portales:** `compreoalquile.com`, `encuentra24.com`, `icasas.com.pa`, `mlsacobir.com`. Backlinks de competidores: N/D.

---

## 5. SERP · AEO · GEO

### 5.1 SERP y AI Overview (14 de 14 resueltas)

Pie: `/v3/serp/google/organic/live/advanced` · 2591 · desktop · profundidad 20 · 2026-10-13.

| Keyword | AI Overview | Web en top 20 | Qué gana |
|---|---|---|---|
| **casas de playa panamá** | no | **1, 2, 11** | su web ocupa las dos primeras posiciones; Airbnb y `encuentra24` detrás |
| playa dorada | no | **9** (GLP en **13**) | `cajadeahorros.com.pa` (4), Facebook; PAA "¿Dónde queda Playa Dorada?", "¿Qué hay para hacer…?"; resultados de la Playa Dorada de Puerto Plata (Tripadvisor) |
| playa dorada vacamonte | no | **8, 21, 23** | **`cajadeahorros.com.pa` (1)**, Facebook, **`grupogeapanama.com` (7)**; PAA "¿A qué corregimiento pertenece Playa Dorada?" |
| playa vacamonte | no | **13** (GLP en 19) | Instagram, TikTok, Booking: intención turística; knowledge graph y "top sights" |
| villamarina | no | 16 | el hotel Villa Marina (Playa Venao, Pedasí) |
| arraiján country club | no | fuera | `acobir.com`, `bgeneral.com`: proyecto de otra empresa |
| casas en venta vacamonte | sí (sin fuentes devueltas) | fuera | `icasas.com.pa`, `inmopanama.com`, `gprovivienda.com`; PAA "¿Dónde queda Vacamonte?" |
| casas en venta panamá oeste | sí (sin fuentes devueltas) | fuera | `viviendasdeprimera.com`, `icasas`, `gruposucasa.com` |
| casas en venta coronado | sí | fuera | `panamaequity.com`, `compreoalquile`, `metrorealtypanama` |
| alquileres costa del este | sí (sin fuentes) | fuera | `mlsacobir`, `encuentra24`, `kcpanama` |
| vivir en panamá oeste | sí (sin fuentes) | fuera | `gruporesidencial.com`, Reddit, Instagram; `vive.baysidepanama.com` |
| cómo comprar una casa en panamá | sí | fuera (GLP en 19) | `icasas`, `compreoalquile`, `gruporesidencial`; AIO cita `cajadeahorros.com.pa` |
| buy beach house in panama | no | fuera | `bocasdeltoropanamaproperties.com`, `rootspanama`, `properstar` |
| panama beach property | sí (sin fuentes) | fuera | `panama-real-estate.com`, `rootspanama`, `jamesedition` |

**AI Overview presente en 7 de 14**, y en ninguno cita a `playadorada.com.pa`. **Discrepancia a investigar:** la base de `ranked_keywords` da pos. 1 para `playa dorada vacamonte` y 4 para `playa dorada`, pero la SERP en vivo muestra 8 y 9. Puede ser volatilidad, dispositivo o momento; medir con Search Console.

**Qué formato crear:** para "playa dorada" y "playa dorada vacamonte" ganan fichas del banco, Facebook y páginas de desarrolladora: una **página de entidad con datos oficiales** puede desplazarlas. Para "playa vacamonte" gana contenido turístico (Instagram, TikTok): la intención no es de compra, se atrapa solo con guías que conecten el visitante con el comprador. Para "casas de playa panamá" la web ya es #1–#2.

### 5.2 GEO — 15 prompts × 4 motores × 3 repeticiones = 180 respuestas

Pie: `/v3/ai_optimization/{chat_gpt,claude,gemini,perplexity}/llm_responses/live` · modelos `gpt-6-sol`, `claude-sonnet-5-5`, `gemini-3.5-flash`, `sonar` · 2026-10-13. Búsqueda web activa en ChatGPT, Gemini y Perplexity; **Claude sin búsqueda** (mide conocimiento base).

**Prompts de marca (4: qué es y quién lo desarrolla, ¿vale la pena?, y sus versiones en inglés):**

| Motor | Describe el proyecto | Cita `playadorada.com.pa` |
|---|---|---|
| ChatGPT | Sí (comunidad residencial y de playa en Vacamonte; en inglés lo atribuye a Grupo Los Pueblos) | 8 de 12; también cita `glp.com.pa/proyecto/playa-dorada/` |
| Perplexity | Sí (~1 km de playa, ~30 min de la ciudad, casas y apartamentos) | 12 de 12 |
| Gemini | Sí | 0 verificable (enlaces como redirección) |
| Claude (sin web) | **No**: "no tengo información confiable"; en inglés sugiere que podrías referirte a la Playa Dorada de la República Dominicana | — |

**Prompts sin nombrar la marca (11 prompts × 3 réplicas = 33 por motor):**

| Motor | Menciona "Playa Dorada" | Cita la web |
|---|---|---|
| Gemini | 14/33 (42 %) | 0 verificable |
| Perplexity | 12/33 (36 %) | 15 |
| ChatGPT | 3/33 (9 %) | 4 |
| Claude (sin web) | 3/33 (9 %) | — |

**Dónde aparece:** *¿qué tan lejos está Playa Dorada de la ciudad?* (ChatGPT, Claude, Gemini y Perplexity 3/3), *¿cómo es vivir en Vacamonte?* (Perplexity 3/3, Gemini 2/3), *¿es buena zona Vacamonte para una casa de playa?* (EN: Perplexity y Gemini 3/3), *mejores residenciales de casas de playa en Panamá Oeste* (Perplexity y Gemini 3/3). **No aparece en ningún motor** en: proceso de compra para extranjeros (ES y EN), gastos de cierre e impuestos, y *Best beach communities to buy a house in Panama* (EN). Casi nada (Gemini 1/3) en precio, comparativa con Coronado e inversión en casa de playa para alquilar; en esta última Perplexity cita la web en 3/3 respuestas sin nombrar el proyecto.

**Quién se cita en respuestas sin marca:** **`playadorada.com.pa` 67**, `encuentra24.com` 42, `panamaprop.com` 27, `panamapropertyexperts.com` 24, `dgi.mef.gob.pa` 14, `panamadigital.gob.pa` 13, `panama-real-estate.com` 12, `wise.com` 12, **`glp.com.pa` 11**, `registro-publico.gob.pa` 7. **Páginas propias más citadas:** `/en/news-en/beach-condos-30-minutes-from-panama-city/` (11), su duplicado `-2/` (11), `/blog/que-hace-unico-al-desarrollo-de-playa-dorada-en-la-costa-pacifica/` (9), `/blog/noticias-es/venta-casas-vacamonte/` (9), `/blog/noticias-es/propiedad-de-playa-asequible-panama/` (9), `/ubicacion/` (7).

**Hallazgos de contenido:**
- **El blog está funcionando para GEO**: las páginas de zona, accesos y "30 minutos de la ciudad" son las que las IA citan. Hay que mantenerlas y fecharlas.
- **Las duplicadas se citan por separado.** `beach-condos-30-minutes-from-panama-city/` y `...-2/` reciben 11 citas cada una: dos URLs para lo mismo, lo cual diluye. Consolidar con canonical o 301.
- **Cifras que dicen las IA y no están verificadas por mí:** Perplexity indica "casas desde aproximadamente US$97.000", "~1 km de playa", "cerca de Westland Mall". ChatGPT y Perplexity advierten que las afirmaciones de apreciación y alquiler "provienen del propio material de marketing del desarrollo". Hay que publicar datos fechados y con fuente.
- **Confusión de entidad.** En la SERP de "playa dorada" aparece la Playa Dorada de Puerto Plata (República Dominicana), y Claude la sugiere. La página de entidad debe nombrar el país y el distrito en la primera frase.
- **Atribución a la desarrolladora.** ChatGPT cita `glp.com.pa` como fuente de que GLP desarrolla el proyecto; la SERP muestra a Grupo GEA. Declarar el rol de cada empresa evita contradicciones.
- **Temas legales:** las IA citan `dgi.mef.gob.pa` (14), `registro-publico.gob.pa` (7) y `panamadigital.gob.pa` (13); el sitio no está en esas respuestas.

---

## 6. AUDITORÍA TÉCNICA

Solo la home pudo rastrearse. Pie: `/v3/on_page/instant_pages` · 2026-10-13. Lo no listado: **N/D**.

| Área | Estado | Evidencia |
|---|---|---|
| Código, HTTPS, canonical | ✔ | home 200, canonical a sí misma |
| Title | ✔ | "Playa Dorada \| Residencias de playa en Panamá" (46 caracteres) |
| Meta description | ✔ | "Descubre las mejores residencias de playa en Panamá. Encuentra en Playa Dorada tu hogar ideal…" |
| H1 | parcial | "Propiedades en la playa": genérico, sin marca ni lugar |
| Estructura H2/H3 | ✖ | H2 en mayúsculas y fragmentos de interfaz: "RECORRE EL PROYECTO" x3, "INSUPERABLE", "¿NECESITA MÁS INFORMACIÓN?"; H3 repetidos "desde tu casa!" x3 |
| Contenido | ✖ | 469 palabras; flags `low_content_rate` y `low_readability_rate` |
| Meta duplicados | ✖ | flag `duplicate_meta_tags` |
| Imágenes | ✖ | 11 imágenes; flag `no_image_alt` |
| **Schema** | ✖ | `has_micromarkup: false` |
| **Rendimiento (medido desde DataForSEO)** | ✖ | TTFB 3.645 ms; LCP 7.180 ms; flags `high_loading_time` y `has_render_blocking_resources` |
| Open Graph / idioma | parcial | `og:locale` es_ES; título "Playa Dorada \| Residencias de playa en Panamá" |
| Idiomas | N/D | `/en/home/` y `/en/news-en/` existen; hreflang sin verificar |
| `robots.txt`, `llms.txt`, sitemap | **N/D** | sin acceso: no puedo decir si se bloquea a GPTBot, ClaudeBot o PerplexityBot |
| URLs duplicadas | ✖ | `beach-condos-30-minutes-from-panama-city/` y `-2/` |
| On-page score (API) | 87,1 | home |
| Backlinks | informativo | 4.795 backlinks, 521 dominios (520 principales), rank 328, spam score 5, primera detección 2023-02-13 |

---

## 7. AUDITORÍA E-E-A-T

Puntuación 0–3 sobre lo observable; "N/D" donde no hay evidencia.

| Pilar | Señal | Punt. | Evidencia |
|---|---|---|---|
| Experience | Tour virtual, club de playa, avance de obras | 2 | existen `/tour-virtual/`, `/club-de-playa/` y `/blog/.../villamarina-avance-de-obras/`; autenticidad de fotos: N/D |
| Experience | Casos o clientes reales | N/D | no encontrado |
| Expertise | Autores con bio en el blog | N/D | no verificado |
| Expertise | Revisión legal de contenido de compra | 0 | no hay guías de proceso en lo rastreado; las IA no citan el sitio en esos temas |
| Authoritativeness | Perfil de enlaces | 2 | 520 dominios principales, spam 5 |
| Authoritativeness | Respaldo de empresa | 1 | la desarrolladora no se declara con claridad en lo rastreado; hay un listado en `cajadeahorros.com.pa` |
| Trust | Razón social / RUC / dirección | N/D | no visible en lo rastreado |
| Trust | Calidad editorial | 1 | H2 fragmentados, páginas duplicadas |
| Trust | Precios y fechas citables | 0 | las IA dan cifras sin respaldo del sitio |

### Qué debe aportar el cliente

1. **Quién es la desarrolladora** (razón social, RUC) y el papel de GLP y Grupo GEA, si lo tienen.
2. **Lista oficial de precios, modelos y fechas** de entrega, con fecha de vigencia.
3. Si la empresa **gestiona alquileres en Costa del Este** (y cuántas unidades).
4. Autores y revisores nombrados (legal, fiscal).
5. Fotos y vídeos propios de obra y entregas; casos demostrables.
6. Confirmación de qué páginas son canónicas entre `playadorada.com.pa` y `glp.com.pa/proyecto/playa-dorada/`.
7. Acceso a Search Console y a `robots.txt` / `llms.txt` / sitemap.

---

## 8. MAPA DE CONTENIDO (19 piezas)

Datos de §4. "Insumo" = lo que se pide antes de redactar. Las piezas legales llevan fuente oficial y revisor.

### Pilar A — Entidad y proyecto

| # | Pieza | Dato | Formato | Insumo |
|---|---|---|---|---|
| 1 | **Playa Dorada Residences & Beach Club: qué es, dónde está y quién lo desarrolla** (ES) | `playa dorada` 1.035; `playa dorada vacamonte` +93 %; PAA "¿A qué corregimiento pertenece…?"; Claude no lo conoce | Definición con país, distrito y desarrolladora en la 1.ª frase; aclarar que **no es** la Playa Dorada de Puerto Plata | datos oficiales |
| 2 | **What is Playa Dorada, Panama?** (EN) | ChatGPT y Perplexity sí lo conocen; Claude lo confunde | Versión EN con hreflang | datos oficiales |
| 3 | **Consolidar duplicados** `beach-condos-30-minutes-from-panama-city/` y `-2/` | 11 citas cada una | canonical/301 y actualización fechada | — |
| 4 | **Modelos de casa** (una página por modelo, sin el nombre "Caracol" como keyword) | `/producto/...` casi sin tráfico | Ficha con m², recámaras, precio desde y fecha | planos y precios |

### Pilar B — Zona (Vacamonte y Panamá Oeste)

| # | Pieza | Dato | Formato | Insumo |
|---|---|---|---|---|
| 5 | **Playa Vacamonte: guía y qué hay cerca** | 1.263/mes, CPC 2,80; intención turística | Guía que conecta al visitante con el comprador | datos medidos |
| 6 | **Vivir en Vacamonte** (hub de zona) | `vacamonte` 8.100 (mayormente navegacional); PAA "¿Dónde queda Vacamonte?" | Servicios, colegios, supermercados, accesos | visita |
| 7 | **Cómo llegar a Playa Dorada desde Ciudad de Panamá** (renovar la entrada de accesos) | las 4 IA respondieron esto con 3/3 | Rutas con tiempos **medidos** y fecha | mediciones |
| 8 | **Vivir en Panamá Oeste: ventajas, trayecto y costos** | AIO presente; PAA | Guía con transporte y servicios | datos |
| 9 | **Panamá Oeste vs Coronado: dónde comprar una casa de playa** | 0 visibilidad en IA; Coronado EN 124/mes | Tabla de criterios | precios por m² con fuente |

### Pilar C — Producto y precio

| # | Pieza | Dato | Formato | Insumo |
|---|---|---|---|---|
| 10 | **Casas de playa en Panamá: guía de compra** (defender el #1–#2) | 320/mes (Labs) | Criterios, rangos fechados | precios |
| 11 | **Casas de playa asequibles en Panamá** (renovar la entrada citada 9 veces) | citada por las IA | Rangos oficiales y fecha | lista de precios |
| 12 | **Club de playa y amenidades** | `beach club` pos. 17 | Qué hay hoy y qué está planificado | confirmación |
| 13 | **Beach houses in Panama: a buyer's guide** (EN) | 93/mes; 0 visibilidad | Guía con criterios | datos |

### Pilar D — Proceso y legal (con fuente oficial)

| # | Pieza | Dato | Formato | Insumo |
|---|---|---|---|---|
| 14 | **Cómo comprar una casa en Panamá siendo extranjero** | 0 visibilidad; AIO presente | Pasos, enlaces oficiales | revisor legal |
| 15 | **Can foreigners buy a beach house in Panama?** (EN) | 0 visibilidad | Misma estructura con fuentes | revisor legal |
| 16 | **Gastos de cierre e impuestos al comprar una casa** | 0 visibilidad; `dgi.mef.gob.pa` 14 citas | Cifras solo con fuente y fecha | revisor fiscal |
| 17 | **Cómo financiar una casa en Panamá** | PAA "¿Cuál es el monto del abono inicial?"; existe un listado bancario | Pasos, con información oficial del banco aliado | datos del banco |

### Pilar E — Inversión

| # | Pieza | Dato | Formato | Insumo |
|---|---|---|---|---|
| 18 | **¿Conviene comprar una casa de playa para alquilarla?** | 0 visibilidad; las IA avisan que las cifras vienen del marketing | Análisis equilibrado; solo datos con fuente | datos de alquiler |
| 19 | **Informe trimestral de Panamá Oeste** | activo citable | Datos propios, fechados | datos de ventas |

**No perseguir:** `playa caracol`, `villamarina`, `praia amador` y las variantes "dorado" (§4.2); `casas en venta costa del este` salvo que la empresa tenga oferta allí.

---

## 9. PLAN DE 90 DÍAS

Ordenado por impacto ÷ esfuerzo.

| # | Acción | Cuándo | Métrica | Insumo |
|---|---|---|---|---|
| 1 | Acceso a Search Console; revisar `robots.txt`, `llms.txt`, sitemap y hreflang; **cerrar los N/D** | Sem. 1 | indexación y bots de IA conocidos | cliente |
| 2 | **Definir la desarrolladora y la fuente principal del proyecto**: qué vive en `playadorada.com.pa`, qué en `glp.com.pa` y qué en el listado bancario; canonicales y enlaces cruzados | Sem. 1–2 | una sola página principal por consulta | cliente |
| 3 | **Rendimiento**: TTFB (3,6 s) y LCP (7,2 s), recursos que bloquean el render | Sem. 1–4 | LCP < 2,5 s en Lighthouse | desarrollo web |
| 4 | Arreglos on-page: H1 con marca y lugar, H2 sin fragmentos de interfaz, metas duplicadas, `alt` en 11 imágenes | Sem. 2 | flags en verde | — |
| 5 | Consolidar las dos URLs de `beach-condos-30-minutes-from-panama-city` | Sem. 2 | una URL con las 22 citas | — |
| 6 | Schema: `Organization`, `BreadcrumbList`, `Product`+`Offer` por modelo | Sem. 2–4 | `has_micromarkup` verdadero | datos de empresa |
| 7 | Página de **precios y modelos vigentes** (pieza 4 y 11) | Sem. 3 | las IA citan las cifras oficiales | lista oficial |
| 8 | Página de entidad ES/EN (piezas 1 y 2) con país y distrito en la primera frase | Sem. 3–5 | Claude describe bien el proyecto; sin confusión con Puerto Plata | datos oficiales |
| 9 | Pilar B: piezas 5–9 | Sem. 4–9 | `playa dorada vacamonte` a top 5; presencia en el prompt de Coronado (hoy 1/12) | mediciones |
| 10 | Pilar D con revisor legal: piezas 14–17 | Sem. 6–12 | menciones en los 3 prompts legales (hoy 0) | revisor |
| 11 | Decidir el destino de `/alquileres/` (hub propio o retirar) | Sem. 4 | las 27 keywords de Costa del Este dejan de diluir el tema | cliente |
| 12 | **Repetir esta batería de LLM y las 14 SERPs** a 30 y 90 días | Sem. 4, 12 | menciones sin marca > 42 % (Gemini), > 9 % (ChatGPT); aparición en los prompts hoy vacíos | — |

---

## 10. LIMITACIONES

- **No pude abrir `playadorada.com.pa`** (política de red del entorno). Lo on-page cubre solo la home. Para el resto hay que permitir el dominio en *Network access → Allowed domains* o aportar una exportación.
- **Sin contenido de `robots.txt`, `llms.txt`, sitemap, schema del resto de páginas ni hreflang.** Estado de bots de IA: **N/D**.
- **Volumen de búsqueda:** 35 de 72 semillas son N/D en Google Ads. Los temas de proceso, legales, financiamiento y comparativas no se pueden priorizar por volumen.
- **`playa vacamonte`:** la serie de Google Ads tiene 6 meses en cero al inicio; el yoy estándar (+96 %) está inflado y el like-for-like es ≈ +31 %.
- **Google Ads y Labs difieren** para `casas de playa panama` (20 frente a 320/mes).
- **Google Trends no se consultó** para este sitio.
- **Discrepancia** de posición entre `ranked_keywords` y la SERP en vivo (`playa dorada`, `playa dorada vacamonte`, `casas de playa panamá`).
- **AI Overview:** en 5 SERPs se detectó el bloque pero sin fuentes devueltas.
- **Gemini:** los enlaces llegan como redirección; el 0 de citas es "no verificable". **Claude se midió sin búsqueda web.**
- **Cifras de precio, kilometraje de playa y distancias** que citan las IA no están verificadas por mí. Tampoco **el corregimiento exacto** (Vista Alegre) ni el papel de GLP y de Grupo GEA.
- **Backlinks de competidores, Core Web Vitals de campo, fichas vendidas y URLs indexadas: no medidos.**
- **Afirmaciones legales/fiscales:** el informe no contiene ninguna cifra legal; cada pieza del Pilar D necesita fuente oficial y revisión de un abogado panameño.
