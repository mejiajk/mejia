# Auditoría SEO · E-E-A-T · AEO · GEO — glppanamaresidency.com (GLP Panama Residency)

Fecha: 2026-10-14 (UTC) · Prompt: `prompts/seo-auditoria-inmobiliaria-panama.md` (versión con variables de GLP Residency) · Fuente: DataForSEO + respuestas de ChatGPT, Gemini, Perplexity y Claude vía API.

> **Aviso:** este sitio vende un servicio de **residencia por inversión inmobiliaria**, un tema legal y migratorio. Este informe **no verifica** ninguna afirmación legal del sitio ni de las IA. Donde cito montos, plazos o requisitos, son lo que dicen el sitio, las IA o la prensa, y están **pendientes de verificación con un abogado de inmigración y con la fuente oficial vigente**.

---

## 1. CONTEXTO

| Parámetro | Valor |
|---|---|
| Web | https://glppanamaresidency.com/ |
| Marca | GLP Panama Residency (og:site_name del sitio). Title: "Panama Residency by Real Estate Investment \| GLP". |
| Modelo de negocio | **Servicio de residencia por inversión inmobiliaria asociado a una promotora** (la variable venía sin rellenar). La home ofrece el "Panama Qualified Investor Program (QIP)", proyectos destacados (Oceana Residences & Skyhomes, The Tides, Armonía) y "GLP Property Management". Perplexity lo describe como un servicio "asociado con Grupo Los Pueblos y sus asesores socios". |
| Público | **Compradores de EE. UU. y otros países** (la meta description dice "for US buyers"; hay páginas para mexicanos y británicos). No es un sitio de venta local. |
| `ZONAS` de tu archivo | Panamá, Costa del Este, Punta Pacífica, Coronado. **No aplican como zonas de foco**: el sitio no se organiza por zona, sino por programa migratorio. Los proyectos que muestra están en otras zonas (por ejemplo The Tides, Playa Caracol; Playa Dorada). |
| `location_code` | Resueltos por `/v3/serp/google/locations`: **Panamá 2591**, **Estados Unidos 2840**, **México 2484**, **Reino Unido 2826** (Canadá 2124, no usado). El mercado principal se midió en **EE. UU./inglés**. |
| Idiomas | `en` (principal) y `es`. Existe versión en español (`/inversionista-calificado-panama/`); hreflang: N/D. |
| Dispositivo SERP | desktop |
| Ventana de tendencia | 24 meses (2024-08 → 2026-08) |
| Gasto | ≈ 5,1 USD (saldo 41,94 → 36,85) |

Pie general: `DataForSEO · location_code 2840 (en) / 2591 (es) · 2026-10-14`.

**Limitación de acceso:** desde este entorno no se pudo abrir el sitio (política de red). La home sí se rastreó con `/v3/on_page/instant_pages`; el resto de URLs figura por otras fuentes.

---

## 2. RESUMEN EJECUTIVO

1. **Estado:** presencia orgánica casi nula: **34 keywords en EE. UU./inglés (≈ 9 de tráfico estimado)** y **16 en Panamá/español (≈ 8)**. Ninguna en el top 3; la mayor parte, entre las posiciones 20 y 109.
2. **Mayor riesgo: afirmaciones legales sin respaldo visible.** La meta description dice "Get permanent Panama residency by investing $300,000 in real estate. GLP handles the property, the visa filing and the legal work", y la home usa títulos como "Instant Permanent Status", "Expedited Processing", "Fiscal Optimization" y "Path to Citizenship". Las IA y fuentes de prensa citadas en las SERPs hablan de **umbrales distintos según el tipo de propiedad** y de **cambios con fecha de entrada en vigor**. El sitio también tiene una página sobre "Panama citizenship by investment" mientras Perplexity y ChatGPT responden que **comprar propiedad no da ciudadanía de forma directa**. **No verifico quién tiene razón**, pero son afirmaciones que un abogado debe revisar ya.
3. **Mayor oportunidad:** en EE. UU., `panama pensionado visa` sube un 85 % (933/mes) y `panama friendly nations visa` se mantiene en ~810/mes, mientras los términos de residencia por inversión **caen** (`panama residency by investment` −64 %, `panama golden visa` −20 %, `panama citizenship by investment` −34 %). La demanda de este sitio es pequeña y cambiante.
4. **Brecha E-E-A-T principal:** un sitio que ofrece trámites migratorios y asesoría legal debe mostrar **quién presta el servicio, con qué licencia y quién lo revisa**. En lo rastreado no hay autores ni revisor legal visibles, y la pregunta "¿es GLP confiable?" la responden las IA con prudencia.
5. **Estado en IA:** las IA describen a GLP Panama Residency cuando se les pregunta por su nombre (ChatGPT, Gemini y Perplexity sí; **Claude, sin búsqueda web, no la identifica**). En las **12 preguntas sin nombrar la marca**, ningún motor la menciona (0/36 en cada uno). Las respuestas citan fuentes oficiales y despachos: `migracion.gob.pa` (54), `mici.gob.pa` (28), `gacetaoficial.gob.pa` (14).
6. **Acción única prioritaria:** **revisión legal del contenido** por un abogado de inmigración panameño: confirmar los montos, plazos y condiciones vigentes del programa, corregir o retirar las afirmaciones no sustentadas (ciudadanía, "estatus permanente instantáneo") y publicar quién presenta el trámite.

---

## 3. INVENTARIO

Fuente: `ranked_keywords`, `relevant_pages` (EE. UU./en y Panamá/es) y URLs citadas por los LLM. Tráfico estimado (ETV) de DataForSEO, no de Analytics. Pie: `/v3/dataforseo_labs/google/relevant_pages/live` · 2840/2591 · en/es · 2026-10-14.

| URL | Tipo | Keywords | ETV | Notas |
|---|---|---|---|---|
| `/` | home | — | — | **rastreada**: 1.946 palabras, 2 H1, 20 imágenes, on-page score 87,1 |
| `/panama-retirement-visa/` | guía (pensionado) | 7 | 2 | `panama pensionado program` pos. 96; `retire to panama from us` 109 |
| `/beach-houses-for-sale-panama-city/` | categoría de venta | 5 | 1 | `beach property in panama` pos. 26; `beach house panama for sale` 26 |
| `/investing-in-panama-real-estate/` | guía | 4 | 0 | `can americans buy property in panama` pos. 58 |
| `/panama-qualified-investor-program-guide/` | guía QIP | 2 | 0 | `panama residency by investment program` pos. 86 |
| `/panama-citizenship-by-investment/` | guía (**ciudadanía**) | 2 | 0 | `panama dual citizenship requirements` pos. 74 · **afirmación a revisar** |
| `/panama-qualified-investor-visa/` y `-2/` | guías (duplicadas) | 1 | 0 | dos URLs casi idénticas |
| `/golden-visa-panama/`, `/panama-visa-requirements/`, `/panama-pensionado-visa-requirements/`, `/us-veterans-retire-in-panama/`, `/homes-for-sale-in-panama/`, `/panama-real-estate-investment/` | guías | 1–2 | 0 | |
| `/proyecto/playa-dorada/` | proyecto | 2 | 3 | `playa dorada panama` (480/mes) pos. 22 |
| `/proyecto/armonia/`, `/tipo-de-proyecto/beach/` | proyectos | 3–4 | 1 | `ph armonia` pos. 50 |
| `/why-glp/` | corporativa | 2 | 3 | `grupo los pueblos` pos. 18 |
| `/residencia-fiscal-panama/`, `/visa-panama-mexicanos/`, `/visa-panama-britanicos/` | guías (ES) | 1 | 0 | ver §4.3 |
| `/faqs/`, `/services/`, `/why-panama/`, `/blog/`, `/inversionista-calificado-panama/` | corporativas/guías | — | — | **citadas por las IA** (3–9 veces); no rastreadas por mí |

Fichas vendidas, URLs indexadas y fecha de último cambio: **N/D**. Hay **dos pares de URLs duplicadas** (`/panama-qualified-investor-visa/` y `-2/`).

**Solapamiento con la web de la promotora:** las IA citan también `glp.com.pa/en/investors/` (6), `glp.com.pa/tu-casa-en-panama-con-glp/` (6) y `glp.com.pa/inversionistas/` (4). La promotora ya tiene páginas para inversionistas; hay que decidir cuál es la principal por consulta.

---

## 4. UNIVERSO DE KEYWORDS (con tendencia)

Pie: `/v3/keywords_data/google_ads/search_volume/live` y `/v3/dataforseo_labs/google/keyword_suggestions/live` · 2840 (en) / 2591, 2484 (es) / 2826 (en) · 2026-10-14. `yoy` = media 12 m ÷ media 12 m previos − 1. **†** = la serie tiene ≥ 2 meses en cero en los 12 meses previos: el `yoy` está inflado.

### 4.1 Mercado de EE. UU. (inglés)

| Keyword | Vol. 12 m | Previo | yoy | Mom. 3 m | Clase |
|---|---|---|---|---|---|
| panama retirement visa | 1.291 | 1.484 | −13 % | 0,61 | Declive |
| **panama pensionado visa** | 933 | 506 | **+85 %** | 2,37 | **Emergente** |
| panama friendly nations visa | 810 | 887 | −9 % | 0,59 | Estable |
| panama visa for us citizens | 633 | 633 | 0 % | 0,72 | Estable |
| move to panama from us | 631 | 764 | −17 % | 0,87 | Declive |
| retire in panama | 514 | 683 | −25 % | 0,58 | Declive |
| panama residency requirements | 279 | 296 | −6 % | 0,87 | Estable (CPC 4,68 USD) |
| panama citizenship by investment | 186 | 280 | **−34 %** | 0,53 | Declive (CPC 6 USD) |
| buy property in panama | 184 | 247 | −25 % | 0,82 | Declive |
| panama golden visa | 170 | 213 | −20 % | 0,36 | Declive (CPC 4,81 USD) |
| panama expat visa † | 152 | 37 | +314 % | 5,54 | Emergente (2 meses en cero) |
| panama permanent residency | 143 | 200 | −29 % | 0,71 | Declive |
| panama property tax | 113 | 145 | −22 % | 0,52 | Declive |
| panama real estate investment | 91 | 292 | **−69 %** | 0,13 | Declive |
| beach houses panama | 81 | 141 | −43 % | 0,86 | Declive |
| can americans buy property in panama | 57 | 55 | +3 % | 1,27 | Estable |
| **panama residency by investment** | 45 | 124 | **−64 %** | 0,36 | Declive |
| glp panama | 18 | 12 | +50 % | 1,4 | Emergente (volumen mínimo) |
| panama residency lawyer † | 17 | 3 | +567 % | 2,67 | Emergente (11 meses en cero) |
| panama residency program | 17 | 43 | −61 % | 0,38 | Declive |

**N/D (sin volumen medible):** `panama qualified investor program`, `panama qualified investor visa`, `panama investor visa`, `panama real estate residency`, `panama residency by real estate`, `buy beach house in panama`, `us veterans retire in panama` (7 de 30 en EE. UU.). **El producto central del sitio, el QIP, no tiene volumen de búsqueda medible en Google Ads.**

**Sub-demanda (Labs, EE. UU.):** `panama residency` y variantes 260/mes · `pensionado visa panama` 1.000 · `panama pensionado visa lawyer` 110 (comercial) · `panama pensionado visa attorney` 20 (transaccional).

### 4.2 Otros mercados

| Mercado | Hallazgo |
|---|---|
| Panamá / español (2591) | 12 de 13 semillas **N/D**; solo `residencia permanente panamá` 6/mes (−30 %). |
| México / español (2484) | 5 de 5 **N/D**: `visa panamá mexicanos`, `residencia panamá mexicanos`, etc. |
| Reino Unido / inglés (2826) | `panama residency by investment` 12/mes (+15 %), `retire in panama` 12/mes (−17 %); 3 de 5 N/D. |

### 4.3 Lecturas

- **La demanda de "residencia por inversión" está en descenso en EE. UU. y es pequeña en el resto.** El sitio apuesta por un tema cuya búsqueda cae; el tema con tracción es el visado de pensionado (+85 %), que **no depende de comprar una propiedad**.
- **La intención de `visa panamá mexicanos` es turística**, no de inversión: la SERP la ocupan consulados y guías de entrada a Panamá (`embamex.sre.gob.mx`, `portales.sre.gob.mx`). La página `/visa-panama-mexicanos/` (pos. 15 en México) atrae a gente que no busca comprar. Lo mismo para `embajada británica en panamá`.
- **Muchas keywords que ya posiciona están fuera de su oferta o más allá de la posición 100** (`panama pensionado program` pos. 96, `retire to panama from us` pos. 109), lo que no genera tráfico.
- **Ruido:** `playa dorada panama` (480/mes) y `grupo los pueblos` aparecen por páginas de proyecto y corporativas copiadas de la promotora.
- **Google Trends no se consultó.**

### 4.4 Score de oportunidad

`volumen` (log, tope 1.500) y `tendencia` de datos; `valor_comercial`, `facilidad` y `encaje_aeo_geo` son **estimaciones mías**, no de API.

| Keyword | Vol. | Clase | Score |
|---|---|---|---|
| panama pensionado visa | 933 | Emergente | 0,76 |
| glp panama | 18 | Emergente | 0,68 |
| panama expat visa † | 152 | Emergente | 0,60 |
| panama friendly nations visa | 810 | Estable | 0,60 |
| panama residency requirements | 279 | Estable | 0,57 |
| can americans buy property in panama | 57 | Estable | 0,55 |
| panama golden visa | 170 | Declive | 0,49 |
| buy property in panama | 184 | Declive | 0,47 |
| panama citizenship by investment | 186 | Declive | 0,45 |
| panama residency by investment | 45 | Declive | 0,43 |
| beach houses panama | 81 | Declive | 0,42 |

**Quick wins (pos. 4–20):** `grupo los pueblos` (12 en EE. UU., 18 en Panamá), `glp panama` (13), `glp properties` (13), `glp brokers` (21). Son búsquedas de marca; el resto del sitio está por debajo de la posición 20.
**Dejar de alimentar:** `panama real estate investment`, `beach houses panama`, `panama residency by investment` como objetivo principal (caen) hasta verificar el contenido.
**Competidores:** son **despachos y consultoras migratorias**, medios y comunidades: `getgoldenvisa.com`, `lincolnglobalpartners.com`, `immigrantinvest.com`, `thelatinvestor.com`, `globalcitizensolutions.com`, `mercan.pa`, `kraemerlaw.com`, `panamasovereign.com`, y medios como `imidaily.com`, `nomadcapitalist.com`, `forbes.com`. **Fuentes oficiales:** `migracion.gob.pa`, `mici.gob.pa`, `embassyofpanama.org`. Backlinks de competidores: N/D.

**Backlinks:** 1.867 backlinks, 1.598 dominios (1.591 principales), rank 281, **spam score 48 (alto)**, primera detección 2019-01-17. Un volumen tan alto de dominios con pocos enlaces por dominio y primera detección en 2019 sugiere **enlaces heredados** (el dominio podría haber tenido otro uso antes). Hay que revisar el historial del dominio.

---

## 5. SERP · AEO · GEO

### 5.1 SERP y AI Overview (15 de 15 resueltas)

Pie: `/v3/serp/google/organic/live/advanced` · 2840 (en) / 2591 y 2484 (es) · desktop · profundidad 20 · 2026-10-14. Una keyword falló con error del servidor y se repitió sin el bloque de AI Overview (`residencia panamá por inversión`).

| Keyword (mercado) | AI Overview | Web en top 20 | Qué gana |
|---|---|---|---|
| panama qualified investor program (US) | sí (sin fuentes) | fuera | `globalcitizensolutions`, `citizenshipinvest`, `mundo.expert`, `mondaq` |
| panama qualified investor visa (US) | sí (sin fuentes) | fuera | `kraemerlaw.com`, `henleyglobal`, `imidaily`, `getgoldenvisa` |
| panama residency by investment (US) | sí (sin fuentes) | fuera | Forbes, YouTube, `jj-associate`, `imidaily` |
| panama golden visa (US) | sí (sin fuentes) | fuera | Reddit, `globalcitizensolutions`, `mondaq`, `imidaily` |
| panama citizenship by investment (US) | sí (sin fuentes) | fuera | `imidaily`, `nomadcapitalist`, Reddit, `passportlegacy` |
| panama pensionado visa (US) | sí (sin fuentes) | fuera | `ndm.com.pa`, `primesls`, YouTube, Yahoo |
| panama friendly nations visa (US) | sí (sin fuentes) | fuera | YouTube, Reddit, `relofirm`, `delvallepanama` |
| panama retirement visa (US) | sí (sin fuentes) | fuera | YouTube, `panamarelocationtours`, `smithstonewalters` |
| panama expat visa (US) | sí (sin fuentes) | fuera | `embassyofpanama.org`, `startabroad`, `taxesforexpats` |
| can americans buy property in panama (US) | sí (sin fuentes) | fuera | `taxesforexpats`, `panamasovereign`, `livinginpanama`, Reddit |
| beach houses in panama (US) | no | **14** | Zillow (Panama City Beach, Florida), Booking, VRBO |
| residencia panamá por inversión (PA, sin AIO por error) | — | fuera | `mici.gob.pa`, `icazalaw.com`, `panamags.com`, `kraemerlaw.com` |
| visa panamá inversionista (PA) | sí (sin fuentes) | fuera | Instagram, `ndm.com.pa`, `propanama.gob.pa` |
| residencia fiscal panamá (PA) | sí (sin fuentes) | fuera | despachos legales (`limitlesslegal`, `legal500`, `anorco`) |
| visa panamá mexicanos (MX) | sí (sin fuentes) | **15** | consulados (`embamex.sre.gob.mx`) |

**AI Overview presente en 14 de 15, sin devolver fuentes en ninguno (N/D).** El sitio solo aparece en el top 20 en 2 búsquedas: `beach houses in panama` (pos. 14, donde gana Panama City Beach de Florida) y `visa panamá mexicanos` (pos. 15, de intención turística).

**Titulares recientes en las SERPs** (leídos de los títulos, **no verificados**): "Panama Scraps Planned Increase for Real Estate…" (`imidaily.com`), "Panama Extends Discount on Qualified Investor Real Estate…" (`imidaily.com`), "Update on Panama's CBI: No citizenship, just residency" (Reddit), "Qualified Investor visa changes in Panama" (`mundo.expert`), "New Qualified Investor Residency Decree In Panama" (`mondaq.com`). **Indican que la norma del programa ha cambiado o está cambiando.** Cualquier cifra del sitio puede estar desactualizada.

**Qué formato crear:** ganan despachos legales, medios especializados y fuentes oficiales. Un sitio comercial solo compite con **contenido revisado por un abogado, con fecha de la norma y enlaces a la fuente oficial**.

### 5.2 GEO — 15 prompts × 4 motores × 3 repeticiones = 180 respuestas

Pie: `/v3/ai_optimization/{chat_gpt,claude,gemini,perplexity}/llm_responses/live` · modelos `gpt-6-sol`, `claude-sonnet-5-5`, `gemini-3.5-flash`, `sonar` · 2026-10-14. Búsqueda web activa en ChatGPT, Gemini y Perplexity; **Claude sin búsqueda**.

**Prompts de marca (3: ¿qué es GLP Panama Residency?, ¿es confiable?, y su versión en español):**

| Motor | Describe a GLP Residency | Cita `glppanamaresidency.com` |
|---|---|---|
| ChatGPT | Sí: "un servicio privado, **no el programa del gobierno**"; para "¿es confiable?" interpreta GLP como Grupo Los Pueblos y advierte que "las cifras son afirmaciones propias de la empresa" | 4 de 9 |
| Perplexity | Sí: "servicio de residencia por inversión asociado con Grupo Los Pueblos y sus asesores socios" | 9 de 9 |
| Gemini | Sí | 0 verificable |
| Claude (sin web) | **No**: "No puedo hablar de GLP Panama Residency… prefiero no adivinar"; ante "¿es confiable?" dice que "GLP" podría ser un despacho, una consultora de reubicación o una inmobiliaria | — |

**Prompts sin nombrar la marca (12 prompts × 3 réplicas = 36 por motor):**

| Motor | Menciona a GLP | Cita la web |
|---|---|---|
| ChatGPT / Gemini / Claude | 0/36 | 0 |
| Perplexity | 0/36 | 2 (solo en "plazos y pasos") |

**No aparece en ninguna de las 12 preguntas** (mejor forma de obtener residencia en EE. UU., cuánto invertir, qué es el QIP y sus requisitos, plazos y pasos, comparación con Friendly Nations y Pensionado, ciudadanía, inversión, propiedades de playa, riesgos de comprar, y las tres en español).

**Quién se cita:** `migracion.gob.pa` 54, `mici.gob.pa` 28, `getgoldenvisa.com` 21, `lincolnglobalpartners.com` 21, `immigrantinvest.com` 18, `jarniascyril.com` 17, `thelatinvestor.com` 15, `gacetaoficial.gob.pa` 14, `mirabelloconsultancy.com` 12, `henleyglobal.com` 12. **Páginas propias más citadas** (casi solo en prompts de marca): `/` (14), `/faqs/` (9), `/services/` (6).

**Lo que dicen las IA sobre montos y condiciones (NO verificado por mí; se contrasta con lo que afirma el sitio):**
- Las respuestas mencionan **US$300.000 y US$500.000** (59 y 51 menciones) y, con menos frecuencia, US$200.000 y US$750.000. Perplexity y ChatGPT distinguen **US$300.000 para primera venta/obra nueva y US$500.000 para reventa**, con reglas que, según una fuente de prensa citada por ChatGPT, **entran en vigor en septiembre de 2026**; Perplexity habla de un aumento "después de octubre". **Las IA no coinciden en la fecha.** Perplexity añade que la inversión debe estar libre de gravámenes y mantenerse **al menos cinco años**.
- El sitio dice, sin esa distinción, "investing $300,000 in real estate".
- Sobre **ciudadanía**, ChatGPT responde "No, no directamente" y Perplexity "Panamá no ofrece ciudadanía directa por inversión". El sitio tiene una página titulada `/panama-citizenship-by-investment/` y la sección "Path to Citizenship".
- **Estos puntos no son un veredicto.** Son contradicciones que un abogado de inmigración debe resolver con la norma vigente (`gacetaoficial.gob.pa`, `migracion.gob.pa`).

**Otros hallazgos:**
- **Las IA piden fuentes oficiales y despachos** para estos temas. Un sitio comercial sin revisor visible no entra.
- **Confusión de entidad:** Claude no sabe si "GLP" es un despacho, una consultora o una inmobiliaria. Hace falta una definición clara de qué es GLP Residency y quién presta cada parte del servicio.
- **Sobre "es confiable":** ChatGPT encuentra el registro de una empresa de administración de GLP, pero aclara que no verifica las finanzas ni los títulos. Es una señal de que **faltan pruebas de confianza visibles**.

---

## 6. AUDITORÍA TÉCNICA

Solo la home pudo rastrearse. Pie: `/v3/on_page/instant_pages` · 2026-10-14. Lo no listado: **N/D**.

| Área | Estado | Evidencia |
|---|---|---|
| Código, HTTPS, canonical | ✔ | home 200, canonical a sí misma |
| Title | ✔ | "Panama Residency by Real Estate Investment \| GLP" |
| Meta description | **⚠ contenido** | "Get permanent Panama residency by investing $300,000 in real estate. GLP handles the property, the visa filing and the legal work for US buyers." Técnicamente correcta; **su contenido legal requiere revisión** (§2). |
| H1 | ✖ | **dos H1**: "Panama Qualified Investor Program" y "From our Blog" |
| Estructura H2/H3 | parcial | H2 duplicados ("Live or invest in a project by Grupo Los Pueblos" x2); H3 con afirmaciones legales ("Instant Permanent Status", "Expedited Processing", "Fiscal Optimization", "Path to Citizenship", "Legal Certainty & Security") |
| Contenido | parcial | 1.946 palabras; flags `low_content_rate` y `low_readability_rate` |
| Meta duplicados | ✖ | flag `duplicate_meta_tags` |
| Imágenes | ✖ | 20 imágenes; flag `no_image_alt` |
| **Schema** | ✖ | `has_micromarkup: false` |
| Rendimiento (medido desde DataForSEO) | parcial | TTFB 2.761 ms; LCP 1.976 ms; flags `high_loading_time` y `has_render_blocking_resources` |
| Open Graph | ✔ | `og:locale` en_US; `og:site_name` "GLP Panama Residency" |
| URLs duplicadas | ✖ | `/panama-qualified-investor-visa/` y `/panama-qualified-investor-visa-2/` |
| Idiomas | N/D | hay versión en español (`/inversionista-calificado-panama/`); hreflang sin verificar |
| `robots.txt`, `llms.txt`, sitemap | **N/D** | sin acceso: no puedo decir si se bloquea a GPTBot, ClaudeBot o PerplexityBot |
| Backlinks | informativo | 1.867 backlinks, 1.591 dominios principales, rank 281, **spam score 48**, primera detección 2019-01-17 |

---

## 7. AUDITORÍA E-E-A-T (YMYL: dinero y estatus migratorio)

Puntuación 0–3 sobre lo observable; "N/D" donde no hay evidencia.

| Pilar | Señal | Punt. | Evidencia |
|---|---|---|---|
| Experience | Casos de clientes reales y procesos completados | N/D | no encontrado en lo rastreado |
| Expertise | **Abogado o despacho identificado que presenta el trámite** | **0** | la meta description dice que GLP "handles the visa filing and the legal work"; **no se ve quién lo ejecuta ni con qué licencia** |
| Expertise | Autores y revisores del contenido legal | **0** | ausentes en lo rastreado |
| Expertise | Fecha de la norma y fuente oficial en las guías | **0** | no visibles; las SERPs muestran que la norma cambia |
| Authoritativeness | Respaldo de la promotora | 2 | asociación con Grupo Los Pueblos; las IA lo mencionan |
| Authoritativeness | Perfil de enlaces | 1 | 1.591 dominios, pero spam 48 y probablemente heredados |
| Trust | Razón social, RUC, dirección, teléfono | N/D | no visible en lo rastreado |
| Trust | Avisos legales y de resultados no garantizados | N/D | no verificado |
| Trust | Honorarios y costos oficiales separados | N/D | no verificado |
| Trust | Afirmaciones absolutas ("instant", "expedited") | **0** | requieren respaldo oficial |

### Qué debe aportar el cliente

1. **Identidad legal del prestador:** razón social, RUC, y el **despacho o abogado de inmigración** que presenta los trámites, con su idoneidad.
2. **Revisión legal** de todas las páginas de residencia, ciudadanía, impuestos y requisitos por un abogado de inmigración panameño, con nombre y fecha.
3. **Fuente oficial y fecha vigente** de cada monto, plazo y condición (`gacetaoficial.gob.pa`, `migracion.gob.pa`).
4. **Honorarios propios frente a tasas oficiales**, separados y fechados.
5. **Casos reales** (con consentimiento) o testimonios verificables; no inventar.
6. **Historial del dominio** (por qué hay 1.591 dominios con primera detección en 2019).
7. **Relación con `glp.com.pa`**: qué páginas de inversionista viven en cada web.
8. Acceso a Search Console y a `robots.txt` / `llms.txt` / sitemap.

---

## 8. MAPA DE CONTENIDO (18 piezas)

**Todas las piezas requieren revisor legal y fuente oficial con fecha. Ninguna debe publicarse con montos o plazos que no estén verificados.** "Insumo" = lo que se pide antes de redactar.

### Pilar A — El programa QIP (con fuente oficial)

| # | Pieza | Dato | Formato | Insumo |
|---|---|---|---|---|
| 1 | **Panama Qualified Investor Program: estado de la norma al [fecha]** | titulares recientes de cambios; AIO presente; 0 visibilidad | página versionada: qué dice la norma hoy, qué cambió y cuándo, con enlace a la fuente oficial | revisor legal |
| 2 | **Requisitos de la inversión inmobiliaria**: tipo de propiedad, condiciones y mantenimiento | las IA mencionan umbrales distintos | solo lo que confirme la norma vigente | revisor legal |
| 3 | **Paso a paso y quién presenta cada trámite** | PAA "How to gain residency in Panama?" | pasos con quién hace qué (cliente, abogado, notaría), sin promesas de plazo si no hay fuente | revisor legal |
| 4 | **Costos: honorarios y tasas oficiales** | PAA "How much does it cost to get residency in Panama?" | tabla con fuente y fecha | tarifas |
| 5 | **Preguntas frecuentes del QIP** (renovar `/faqs/`, citada 9 veces) | | una pregunta = un H2 | revisor legal |

### Pilar B — Comparativas honestas

| # | Pieza | Dato | Formato | Insumo |
|---|---|---|---|---|
| 6 | **QIP vs Friendly Nations vs Pensionado: cuál encaja contigo** | 0 visibilidad; pensionado +85 %, friendly nations 810/mes | tabla de criterios que **incluya los casos en que la inversión no es necesaria** | revisor legal |
| 7 | **Panama Pensionado Visa: ¿para quién es?** | 933/mes, +85 % | guía neutral con fuente oficial | revisor legal |
| 8 | **Friendly Nations Visa: requisitos vigentes** | 810/mes | fuente y fecha | revisor legal |
| 9 | **Residencia migratoria frente a residencia fiscal** (ES; renovar `/residencia-fiscal-panama/`) | SERP dominada por despachos | revisor fiscal y legal | revisor |

### Pilar C — Ciudadanía y expectativas

| # | Pieza | Dato | Formato | Insumo |
|---|---|---|---|---|
| 10 | **¿Se puede obtener la ciudadanía comprando propiedad en Panamá?** (revisar `/panama-citizenship-by-investment/`) | las IA dicen que no directamente; el sitio tiene una página con ese título | respuesta basada en la norma, o retirar la página | revisor legal |

### Pilar D — Propiedad y confianza

| # | Pieza | Dato | Formato | Insumo |
|---|---|---|---|---|
| 11 | **Can Americans buy property in Panama?** (renovar `/investing-in-panama-real-estate/`) | 57/mes estable; AIO presente | pasos, riesgos y fuentes | revisor legal |
| 12 | **Quiénes somos: quién es GLP Panama Residency y quién presta cada servicio** | Claude no la identifica; ChatGPT no verifica | entidad: razón social, abogado socio, relación con Grupo Los Pueblos, `Organization` | datos legales |
| 13 | **¿Es confiable GLP? Cómo verificar a cualquier proveedor de residencia** | ChatGPT: "no compraría solo por su trayectoria" | lista de verificación y documentos disponibles | documentos |
| 14 | **Impuesto a la propiedad en Panamá** | 113/mes, −22 % | solo con fuente de la DGI | revisor fiscal |
| 15 | **GLP Property Management: qué es y cuánto cuesta** | servicio en la home | descripción con tarifas | tarifas |
| 16 | **Propiedades de playa que califican** (renovar `/beach-houses-for-sale-panama-city/`) | `beach house panama for sale` pos. 26; Zillow gana por Panama City Beach, Florida | solo propiedades que cumplan la norma vigente; precios fechados | revisor legal |

### Pilar E — Higiene

| # | Pieza | Formato |
|---|---|---|
| 17 | **Consolidar duplicados**: `/panama-qualified-investor-visa/` y `-2/` | 301 a una URL |
| 18 | **Revisar páginas fuera de oferta** (`/visa-panama-mexicanos/`, `/visa-panama-britanicos/`, `/us-veterans-retire-in-panama/`): intención turística o sin relación con la inversión | reconvertir, fusionar o retirar |

**No perseguir sin revisión legal:** cualquier contenido sobre "ciudadanía por inversión", "estatus permanente instantáneo", "optimización fiscal" o plazos garantizados.

---

## 9. PLAN DE 90 DÍAS

Ordenado por riesgo e impacto ÷ esfuerzo.

| # | Acción | Cuándo | Métrica | Insumo |
|---|---|---|---|---|
| 1 | **Revisión legal inmediata** de la home, la meta description y las páginas de QIP, ciudadanía y residencia: confirmar montos, tipo de propiedad, fechas de entrada en vigor, plazos y condiciones; **corregir o retirar** lo que no se sustente | Sem. 1 | cero afirmaciones legales sin fuente oficial y fecha | abogado de inmigración |
| 2 | Declarar **quién presta el servicio** (razón social, RUC, abogado o despacho con idoneidad) y añadir avisos de que no se garantizan resultados | Sem. 1–2 | datos visibles en todas las páginas | cliente |
| 3 | Acceso a Search Console; revisar `robots.txt`, `llms.txt`, sitemap y hreflang | Sem. 1 | indexación y bots de IA conocidos | cliente |
| 4 | **Revisar el historial del dominio y los enlaces** (spam 48, 1.591 dominios con primera detección en 2019) | Sem. 2 | informe de enlaces y desautorización si procede | cliente |
| 5 | Decidir la relación con `glp.com.pa` (páginas de inversionistas) y consolidar duplicados (`-2/`) | Sem. 2 | una página principal por consulta | cliente |
| 6 | Arreglos on-page: un solo H1, H2 únicos, metas duplicadas, `alt` en 20 imágenes, schema `Organization` y `FAQPage` | Sem. 2–4 | flags en verde | — |
| 7 | Pilar A (piezas 1–5), con fecha de la norma y enlaces oficiales | Sem. 3–8 | menciones en los prompts de requisitos y montos (hoy 0/48) | revisor |
| 8 | Pilar B (6–9): comparativas honestas | Sem. 6–10 | visibilidad en "QIP vs Friendly Nations vs Pensionado" (hoy 0/12) | revisor |
| 9 | Pilar C (10): ciudadanía | Sem. 4 | respuesta alineada con la norma o página retirada | revisor |
| 10 | Pilar D (11–16): entidad, confianza, propiedad | Sem. 6–12 | Claude describe bien a GLP Residency | datos y documentos |
| 11 | Reorientar o retirar páginas fuera de oferta (pieza 18) | Sem. 4 | menos tráfico sin intención | — |
| 12 | **Repetir esta batería de LLM y las 15 SERPs** a 30 y 90 días | Sem. 4, 12 | menciones sin marca > 0/36; aparición en los 12 prompts hoy vacíos | — |

---

## 10. LIMITACIONES

- **No pude abrir el sitio** desde este entorno (política de red). Solo la home se rastreó con contenido real; el resto figura por `ranked_keywords`, `relevant_pages` y las URLs que citan las IA.
- **Este informe no verifica ninguna afirmación legal, migratoria o fiscal.** Los montos (US$300.000, US$500.000 y otros), los plazos, los requisitos y las fechas de entrada en vigor provienen del sitio, de las IA o de titulares de prensa y están **pendientes de verificación** por un abogado de inmigración con la norma vigente.
- **Volumen de búsqueda:** el producto central (`panama qualified investor program`/`visa`) es N/D en Google Ads, y 27 de 53 semillas son N/D. Los mercados de México y Reino Unido casi no tienen datos.
- **Series con meses en cero** (†): `panama expat visa` y `panama residency lawyer`: su `yoy` está inflado.
- **Google Trends no se consultó.**
- **AI Overview:** 14 de 15 SERPs tienen el bloque, pero ninguno devolvió fuentes (N/D). Una SERP se repitió sin el bloque.
- **Gemini:** los enlaces llegan como redirección; el 0 de citas es "no verificable". **Claude se midió sin búsqueda web.**
- **Titulares de prensa** leídos de títulos de las SERPs; no se abrieron los artículos.
- **Relación con `glp.com.pa` y con los despachos socios:** no confirmada.
- **Backlinks de competidores, Core Web Vitals de campo, URLs indexadas y fichas vendidas: no medidos.**
