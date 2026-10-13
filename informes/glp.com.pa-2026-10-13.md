# Auditoría SEO · E-E-A-T · AEO · GEO — glp.com.pa (Grupo Los Pueblos · GLP Properties)

Fecha: 2026-10-13 (UTC) · Prompt: `prompts/seo-auditoria-inmobiliaria-panama.md` (versión con variables de GLP) · Fuente: DataForSEO + respuestas de ChatGPT, Gemini, Perplexity y Claude vía API.

---

## 1. CONTEXTO

| Parámetro | Valor |
|---|---|
| Web | https://glp.com.pa |
| Marca | Grupo Los Pueblos · GLP Properties (el H1 de la home dice "Grupo Los Pueblos \| GLP Properties") |
| Modelo de negocio | **Promotora/desarrolladora con cartera de varios proyectos** (la variable venía sin rellenar). Evidencia en la home: H2 "Líder de la industria de Desarrollo residencial", "Proyectos en venta". Además de vivienda tiene activos comerciales (Federal Mall, Albrook Mall, Santa María Business District). |
| Proyectos en venta en la home | Océana (apartamentos frente al mar) · The Tides (Playa Caracol, Chame) · Armonía (Cinta Costera) · Bosco di Santa María |
| `ZONAS` de tu archivo | Panamá, Costa del Este, Punta Pacífica, Chame. **Chame** corresponde a Playa Caracol / The Tides. **Costa del Este y Punta Pacífica: no encontré en lo rastreado ningún proyecto de GLP asociado** (N/D); las traté como zonas de comparación y de demanda. |
| `location_code` | **2591** (Panamá, país), resuelto con `/v3/serp/google/locations/pa`. Chame figura como 9247998 (no usado). Serie EN medida también con 2840 (EE. UU.) por la config previa. |
| Idiomas | `es` y `en`. Subcarpeta `/en/` confirmada por URLs citadas por las IA (hreflang: N/D). |
| Dispositivo SERP | desktop |
| Ventana de tendencia | 24 meses (2024-08 → 2026-08) |
| Gasto | ≈ 4,9 USD (saldo 55,98 → 51,10) |

Pie general: `DataForSEO · location_code 2591 · es/en · 2026-10-13`.

**Limitación de acceso:** desde este entorno no se pudo abrir `glp.com.pa` (la política de red lo bloquea). Lo on-page viene de `/v3/on_page/instant_pages`, que devolvió solo la home.

---

## 2. RESUMEN EJECUTIVO

1. **Estado:** 522 keywords posicionadas en Panamá (20 en pos. 1, 26 en pos. 2–3, 100 en pos. 4–10, 118 en pos. 11–20) y tráfico orgánico estimado de ~4.720. Es una web fuerte, pero **el tráfico viene de búsquedas de marca y de activos comerciales** (Federal Mall, Los Pueblos, Santa María Business District), no de intención de compra de vivienda.
2. **Mayor riesgo:** la marca se está partiendo en dos. `grupo los pueblos` baja un 36 % (1.190 → 763/mes) mientras `glp properties` sube un 914 % (6 → 59/mes), y las IA a veces confunden el nombre: Claude (sin búsqueda web) responde "no logro identificar con certeza" a la pregunta directa y en una lista lo mezcla como "Pacific Group / Grupo Los Pueblos".
3. **Mayor oportunidad:** `ocean reef islands` (3.742/mes, +32 %) y **Playa Caracol** (4.400/mes; `playa caracol apartamentos` +52 %, Emergente). En las respuestas de IA sobre esos proyectos, **GLP casi no aparece como desarrolladora** y los precios que se citan salen de otros sitios.
4. **Brecha E-E-A-T principal:** sin schema (`has_micromarkup` falso en la home), sin autores en las guías y sin evidencia visible de licencia, razón social y revisión legal en lo rastreado.
5. **Estado en IA:** sobre preguntas de marca ("¿qué es GLP?") ChatGPT y Perplexity responden bien y citan `glp.com.pa` en 8 de 9 y 9 de 9 respuestas de los tres prompts de marca. En las 11 preguntas **sin nombrar la marca**, GLP aparece en 4–8 de 33 respuestas por motor (Perplexity 4, Claude 6, Gemini 7 de 32, ChatGPT 8) y **en 7 de esas 11 preguntas no aparece en ningún motor**: Punta Pacífica vs Costa del Este, precio de Ocean Reef, inversión en playa, proceso de compra (ES y EN), gastos de cierre y condominios frente al mar en inglés. En Playa Caracol solo aparece en 1 de 12 respuestas.
6. **Acción única prioritaria:** convertir cada página de proyecto en una página de **entidad con desarrolladora, ubicación, precios y fechas vigentes** y, sobre esa base, publicar las guías de Playa Caracol/Chame y Ocean Reef, donde la demanda es alta y GLP es invisible en IA.

---

## 3. INVENTARIO

Fuente: `ranked_keywords`, `relevant_pages` (es-PA) y URLs citadas por los LLM. Tráfico estimado (ETV) de DataForSEO, no de Analytics. Pie: `/v3/dataforseo_labs/google/relevant_pages/live` · 2591 · es · 2026-10-13.

| URL | Tipo | Keywords | ETV | Notas |
|---|---|---|---|---|
| `/` | home | 117 | 1.205 | `grupo los pueblos` pos. 1; `los pueblos panama` pos. 5 |
| `/proyecto/santa-maria-business-district/` | proyecto comercial | 44 | 915 | `santa maria business district` pos. 2 |
| `/proyecto/federal-mall/` | proyecto comercial | 15 | 493 | `federal mall` pos. 7 (6.600/mes) |
| `/proyecto/playa-caracol/` | proyecto residencial | 20 | 455 | `playa caracol panama` pos. 8; `playa caracol` pos. 12 |
| `/proyecto/the-reserve/` | proyecto | 23 | 261 | `reserva del norte` (2.400/mes) en pos. 61–64 |
| `/proyecto/playa-dorada/` | proyecto | 13 | 205 | `playa dorada panama` pos. 7 |
| `/proyecto/embassy-club/` | proyecto | 11 | 173 | `residencial embassy club` pos. 5 |
| `/proyecto/coco-place/` | proyecto | 24 | 143 | `ph coco place` pos. 3 |
| `/en/proyecto/ocean-reef-islands/` | proyecto (EN) | 11 | 161 | `ocean reef panama` pos. 12 (3.600/mes) |
| `/proyecto/ipanema/`, `/proyecto/ocean-house/`, `/proyecto/armonia/` | proyectos | 8–14 | 66–116 | `armonía` pos. 13 (1.300/mes) |
| `/proyecto/bosco-di-santa-maria/` | proyecto | 11 | 3 | **casi sin tráfico**; ver §9 (hay otra web del mismo proyecto) |
| `/guia-completa-playa-caracol/` | guía | 7 | 10 | existe, rinde poco |
| `/que-es-un-ph-en-panama/` | guía | 11 | 26 | `que es un ph en panama` +11 % |
| `/mayor-alfredo-aleman-mr-desarrollador/` | corporativa | 5 | 113 | contenido de fundador |
| `/nosotros/`, `/venta-apartamentos-playa/`, `/comprar-propiedad-ciudad-de-panama/`, `/grupo-los-pueblos-desarrollador-inmobiliario/`, `/guia-completa-del-mercado-inmobiliario-de-panama-2025/`, `/mejores-proyectos-inmobiliarios-panama-2026-2027/`, `/cuanto-cuesta-apartamento-panama/`, `/mejores-lugares-para-vivir-en-panama/` | guías/corporativas | — | — | **citadas por las IA** (hasta 14 veces la home y 13 `/nosotros/`); no rastreadas por mí |
| `/en/`, `/en/about-us/`, `/en/projects/`, `/en/buy-property-panama-city/`, `/en/venta-casas-panama/` | EN | — | — | citadas por las IA |

Serie EN medida en EE. UU.: 72 keywords, ETV ≈ 105 (`domain_rank_overview` · 2840 · en). Fichas vendidas, URLs indexadas y fecha de último cambio: **N/D**.

**Movimiento (es-PA):** 274 keywords nuevas, 129 suben, 89 bajan, 153 perdidas. Alta rotación: conviene mirar qué páginas pierden.

---

## 4. UNIVERSO DE KEYWORDS (con tendencia)

Pie: `/v3/keywords_data/google_ads/search_volume/live` y `/v3/dataforseo_labs/google/keyword_suggestions/live` · 2591 · es/en · 2026-10-13. `yoy` = media 12 m ÷ media 12 m previos − 1. Clases según el prompt.

### 4.1 Con tendencia medida

| Keyword | Idioma | Vol. 12 m | Previo | yoy | Mom. 3 m | Clase |
|---|---|---|---|---|---|---|
| ocean reef islands | es/en | 3.742 | 2.825 | +32 % | 1,15 | Creciente |
| playa caracol panama | en | 3.550 | 3.700 | −4 % | 0,85 | Estable |
| playa dorada panamá | es | 967 | 1.013 | −5 % | 1,0 | Estable |
| grupo los pueblos | es | 763 | 1.190 | **−36 %** | 0,58 | **Declive** |
| panama real estate | en | 543 | 549 | −1 % | 1,32 | Estable |
| ocean reef islands panamá | es | 293 | 258 | +13 % | 0,88 | Creciente |
| coco del mar panamá | es | 259 | 268 | −3 % | 1,0 | Estable |
| buy house in panama | en | 127 | 126 | +1 % | 0,85 | Estable |
| casas en venta costa del este | es | 108 | 89 | +21 % | 1,16 | Creciente |
| proyectos inmobiliarios panamá | es | 104 | 123 | −15 % | 0,92 | Declive |
| glp panama | es | 90 | 108 | −17 % | 0,92 | Declive |
| buy apartment in panama | en | 90 | 55 | +64 % | 2,0 | **Emergente** |
| playa caracol panamá | es | 86 | 59 | +45 % | 0,85 | Creciente |
| que es un ph en panama | es | 70 | 63 | +11 % | 1,0 | Creciente |
| **glp properties** | es | 59 | 6 | **+914 %** | 20 | **Emergente** |
| apartamentos en venta costa del este | es | 51 | 45 | +13 % | 1,38 | Creciente |
| chame panamá | es | 50 | 40 | +25 % | 1,56 | Creciente |
| constructoras en panamá | es | 41 | 49 | −17 % | 0,56 | Declive |
| punta pacífica panamá | es | 35 | 48 | −26 % | 0,53 | Declive |
| casas en venta panamá | es | 34 | 28 | +24 % | 1,11 | Creciente |
| retire in panama | en | 32 | 28 | +15 % | 1,25 | Creciente |
| **playa caracol apartamentos** | es | 27 | 18 | +52 % | 1,75 | **Emergente** |
| apartamentos en venta panamá | es | 16 | 14 | +12 % | 1,0 | Creciente |
| punta pacifica apartamentos | es | 13 | 13 | +7 % | 0,75 | Estable |
| vivir en costa del este | es | 6,7 | 4,2 | +60 % | 2,0 | Emergente (volumen mínimo) |

**Sub-demanda de Playa Caracol (Labs, 12 m):** `playa caracol` 4.400 · `playa caracol residences & beach club` 880 · `playa caracol residences vacation rental` 590 · `playa caracol rentals` 480 · `playa caracol chame` 320. Hay demanda de alquiler vacacional además de compra.

### 4.2 Lecturas

- **Marca partida.** `grupo los pueblos` cae mientras `glp properties` crece. Eso coincide con el cambio de nombre comercial de la web. Hay que decidir y unificar. Mientras tanto la web usa ambos en title y H1.
- **El mercado de apartamentos por zona es pequeño en Google Ads.** `apartamentos en venta punta pacífica` y similares dan 10–50/mes; `apartamentos en venta costa del este` 51. El volumen real está en **marcas de proyecto** (Ocean Reef, Playa Caracol) y en **búsquedas de playa**.
- **Punta Pacífica baja** (−26 %). No es una zona donde invertir contenido primero, a menos que GLP tenga un proyecto ahí (N/D).
- **47 de 95 semillas** no tienen volumen en Google Ads (N/D): proceso de compra, gastos de cierre, hipoteca para extranjeros, visa, rentabilidad, `promotora inmobiliaria panamá`, `apartamentos frente al mar panamá` y similares. Aparecen igualmente en PAA y en respuestas de IA, así que se mantienen como temas aunque no se puedan priorizar por volumen.
- **Google Trends** devolvió casi todo 0 para estos términos en Panamá: no es fiable aquí (N/D).

### 4.3 Score de oportunidad

`volumen` (log, tope 1.500) y `tendencia` de datos; `valor_comercial`, `facilidad` y `encaje_aeo_geo` son **estimaciones mías** (no de API). Para ordenar, no para medir.

| Keyword | Vol. | Clase | Score |
|---|---|---|---|
| buy apartment in panama | 90 | Emergente | 0,74 |
| playa caracol apartamentos | 27 | Emergente | 0,65 |
| ocean reef islands | 3.742 | Creciente | 0,63 |
| casas en venta costa del este | 108 | Creciente | 0,64 |
| apartamentos en venta costa del este | 51 | Creciente | 0,60 |
| chame panamá | 50 | Creciente | 0,52 |
| glp properties | 59 | Emergente | no puntuada (marca propia) |

**Quick wins (pos. 4–20 con volumen):** `playa caracol panama` (8; 3.600), `playa caracol` (12; 4.400), `ocean reef panama` (12; 3.600), `armonía` (13; 1.300), `playa vacamonte` (20; 1.300), `playa dorada panama` (7; 1.000). Son búsquedas de proyecto con intención mixta.
**Oportunidad por brecha:** `reserva del norte` (2.400/mes) en pos. 61–64 con la página `/proyecto/the-reserve/`.
**Dejar de alimentar:** `proyectos inmobiliarios panamá`, `constructoras en panamá`, `punta pacífica panamá`, `glp panama` (todas en declive).
**Ruido de intención:** `tipos de viviendas` / `vivienda` / `viviendas` (1.900) sobre `/que-tipo-de-casa-quieres/`: términos genéricos de baja intención de compra.

**Competidores directos (nombrados por las IA):** Empresas Bern, RIG, Grupo Roble, Constructora Urbana, Cuatro Cuatro. **Portales:** `encuentra24.com`, `compreoalquile.com`, `icasas.com.pa`, `mlsacobir.com`, `panamaprop.com`. Backlinks de competidores: N/D.

---

## 5. SERP · AEO · GEO

### 5.1 SERP y AI Overview (14 de 14 resueltas)

Pie: `/v3/serp/google/organic/live/advanced` · 2591 · desktop · profundidad 20 · 2026-10-13. Tres keywords fallaron con "Internal Server Error" y se repitieron con una variante (sin tilde / plural); está marcado.

| Keyword | AI Overview | GLP en top 20 | Qué gana |
|---|---|---|---|
| grupo los pueblos | no | **1** | su web, Instagram, LinkedIn; PAA "¿Quién es el dueño de Grupo Los Pueblos?" |
| glp properties | sí (sin fuentes devueltas) | **2, 3, 7, 8, 9, 10…** (10 resultados) | su web ocupa 10 de 20 posiciones |
| ocean reef islands | sí | **4** (`Ocean Reef Park`) | Instagram, `metrorealtypanama`, `panamasovereign`; **el AIO cita `glp.com.pa`** |
| playa caracol | no | fuera de top 20* | `playacaracolresidences.com` (pos. 2), Instagram, `playacaracolrentals`, Booking; PAA "¿Quién es el dueño de Playa Caracol?" |
| apartamentos en venta chame | sí | **18** | `compreoalquile`, `encuentra24`, `icasas`; AIO cita `playacaracolresidences.com` |
| apartamentos en venta costa del este | sí | fuera | portales |
| apartamentos en venta en punta pacifica (variante) | sí | fuera | portales |
| apartamentos frente al mar panamá | no | fuera | Airbnb, `mlsacobir`, `encuentra24`; PAA "¿Cuánto cuesta un apartamento en Playa Caracol?" |
| mejores promotoras inmobiliarias de panama (variante) | sí | fuera | `hauspanama.com`, `primepanama.com`, listas y directorios |
| invertir en bienes raíces en panamá | sí (sin fuentes devueltas) | fuera | `fmm.com.pa`, despachos legales, `gprovivienda.com` |
| requisitos para comprar casa en panamá | sí | fuera | `kraemerlaw.com`, `exteriores.gob.es`, Instagram |
| buy property in panama | sí | fuera | portales; AIO cita `casasolution`, `wise.com` |
| beachfront real estate panama | no | fuera | portales y agencias en inglés |
| best real estate developers in panama (variante) | sí | fuera | agencias y directorios |

\* **Discrepancia a investigar:** la base de `ranked_keywords` indica `playa caracol` en pos. 12 con `/proyecto/playa-caracol/`, pero la SERP en vivo (desktop) no la muestra en el top 20. Puede ser volatilidad o diferencia de dispositivo/momento. Medir con Search Console.

**AI Overview presente en 10 de 14.** GLP es citada en **1** (`ocean reef islands`). **Qué formato crear:** en keywords de zona y compra ganan portales y proyectos con micrositio propio. En proceso/legal ganan despachos legales y fuentes oficiales. En preguntas de empresa ("¿quién es el dueño…?") GLP puede ganar con una página de entidad.

**Posible fragmentación de entidad:** `playacaracolresidences.com` (pos. 2) y `oceanreefmarina.com.pa` aparecen como webs de proyecto/marina. Si son micrositios de GLP, compiten con `glp.com.pa` por las mismas consultas (relación con GLP: **N/D, confirmar**).

### 5.2 GEO — 15 prompts × 4 motores × 3 repeticiones = 180 (179 con respuesta)

Pie: `/v3/ai_optimization/{chat_gpt,claude,gemini,perplexity}/llm_responses/live` · modelos `gpt-6-sol`, `claude-sonnet-5-5`, `gemini-3.5-flash`, `sonar` · 2026-10-13. Búsqueda web activa en ChatGPT, Gemini y Perplexity; **Claude sin búsqueda** (mide conocimiento base). Una réplica de Gemini no devolvió resultado (N/D).

**Prompts de marca (4):** ¿qué es GLP? (ES y EN), ¿es confiable? y ¿es buena inversión Ocean Reef Islands?

| Motor | Responde correctamente quién es GLP | Cita `glp.com.pa` |
|---|---|---|
| ChatGPT | Sí (fundada en 1985, Ocean Reef Islands, Santa María, Playa Caracol, Albrook Mall) | 8 de 9 en los 3 prompts de GLP; 0 en Ocean Reef |
| Perplexity | Sí | 9 de 9 en los 3 prompts de GLP; 0 en Ocean Reef |
| Gemini | Sí (menciona al fundador Mayor Alfredo Alemán) | 0 verificable (enlaces como redirección) |
| Claude (sin web) | **No**: "no logro identificar con certeza… prefiero no inventar" (ES), y "no tengo información confiable" ante "¿es confiable?" | — |

**Prompts sin nombrar la marca (11 prompts × 3 réplicas = 33 por motor):**

| Motor | Menciona a GLP | Cita la web |
|---|---|---|
| ChatGPT | 8/33 (24 %) | 7 |
| Gemini | 7/32 (22 %) | 0 verificable |
| Claude (sin web) | 6/33 (18 %) | — |
| Perplexity | 4/33 (12 %) | 6 |

Dónde aparece: *mejores promotoras* (ChatGPT 3/3, Claude 3/3, Gemini 3/3, Perplexity 1/3), *Best real estate developers in Panama* (3/3 en los cuatro), *proyectos frente al mar* (ChatGPT 2/3; Perplexity cita la web en 3/3 sin nombrarla). **No aparece en ningún motor en 7 de las 11 preguntas:** Punta Pacífica vs Costa del Este, precio en Ocean Reef Islands, inversión en playa, proceso de compra para extranjeros (ES), gastos de cierre e impuestos, condominios frente al mar para extranjeros (EN) y proceso de compra (EN). En *¿vale la pena comprar en Playa Caracol?* solo aparece Gemini, en 1 de 3 réplicas.

**Hallazgos de contenido:**
- **GLP no se asocia con sus proyectos en las respuestas de zona.** Ante "¿cuánto cuesta una propiedad en Ocean Reef Islands?" ChatGPT cita `oceanreefislandpanamaforsale.com` y Perplexity da rangos (desde ~US$900.000–1,05 millones; unidades de lujo hasta US$10–12 millones o más) sin nombrar a GLP. Ante Playa Caracol, hablan del lugar sin la desarrolladora. **Son cifras de terceros, no verificadas**: GLP debería publicar las suyas, fechadas.
- **Claude confunde la marca.** En una lista de promotoras la presenta como "Pacific Group / Grupo Los Pueblos". Un dato incorrecto que una página de entidad corrige.
- **Quién se cita en respuestas sin marca** (enlaces): `panamaprop.com` 49, **`glp.com.pa` 19**, `dgi.mef.gob.pa` 17, `panamarealestate.org` 16, `wise.com` 15, `mundo.expert` 15, `encuentra24.com` 13, **`registro-publico.gob.pa` 13**, `tulugar.com` 12, `acodeco.gob.pa` 7. Para los temas legales, las IA citan **fuentes oficiales**: sin enlazarlas y sin revisor legal, una guía de proceso no entra.
- **URLs de GLP más citadas:** `/` (14), `/nosotros/` (13), `/en/` (8), `/en/about-us/` (8), `/venta-apartamentos-playa/` (7), `/comprar-propiedad-ciudad-de-panama/` (6), `/grupo-los-pueblos-desarrollador-inmobiliario/` (6). Las IA ya usan las páginas corporativas y de guía; los proyectos concretos no.
- **ChatGPT, sobre confiabilidad,** responde "parece ser una promotora establecida, pero no compraría basándome solo en su trayectoria" y menciona un aviso de operación de *Inmobiliaria Los Pueblos Towers, S.A.* Es una señal de que **faltan pruebas de confianza visibles** en la web (documentos, proyectos entregados, garantías).

---

## 6. AUDITORÍA TÉCNICA

Solo la home pudo rastrearse. Pie: `/v3/on_page/instant_pages` · 2026-10-13. Lo no listado: **N/D**.

| Área | Estado | Evidencia |
|---|---|---|
| Código, HTTPS, canonical | ✔ | home 200, https, canonical a sí misma |
| Title | ✖ largo | "Grupo Los Pueblos, GLP Properties \| Proyectos Inmobiliarios Panamá" (flag `title_too_long`) |
| H1 | ✔ | "Grupo Los Pueblos \| GLP Properties" (un H1); no contiene keyword de producto |
| Estructura H2 | parcial | 22 H2 con repeticiones (Océana, The Tides, Armonía, Bosco x2–3 por carrusel); "Panama" como H2 suelto |
| Contenido | parcial | 1.229 palabras; flags `low_content_rate` y `low_readability_rate` |
| Meta duplicados | ✖ | flag `duplicate_meta_tags` |
| Imágenes | ✖ | 6 imágenes; flag `no_image_alt` |
| **Schema** | ✖ | `has_micromarkup: false` en la home |
| Rendimiento (medido desde DataForSEO) | ✔ | TTFB 796 ms, LCP 508 ms; recursos que bloquean el render (`has_render_blocking_resources`) |
| Open Graph / idioma | parcial | `og:locale` es_ES con alternate en_US; twitter:card `summary` sin `twitter:site`; imagen OG es el logo (1999×555) |
| Idiomas | N/D | `/en/` existe por citas de IA; hreflang sin verificar |
| `robots.txt`, `llms.txt`, sitemap | **N/D** | sin acceso; no puedo decir si se bloquea a GPTBot, ClaudeBot o PerplexityBot |
| On-page score (API) | 92,32 | home |
| Backlinks | informativo | 12.440 backlinks, 487 dominios (479 principales), rank 351, spam score 5, primera detección 2019-02-23 |

**Comparación útil:** la web de Bosco tiene más dominios que GLP (1.320 principales) pero con spam score 48 frente a 5, y mucho menos tráfico. GLP tiene el perfil más sano.

---

## 7. AUDITORÍA E-E-A-T

Puntuación 0–3 sobre lo observable; "N/D" donde no hay evidencia.

| Pilar | Señal | Punt. | Evidencia |
|---|---|---|---|
| Experience | Proyectos entregados verificables | 2 | las IA citan Albrook Mall, Ocean Reef Islands, Santa María; la home dice "Cuatro décadas construyendo el futuro de Panamá"; documentación en la web: N/D |
| Experience | Fotos/vídeo propios, casos | N/D | solo 6 imágenes en la home |
| Expertise | Autores con bio en las guías | N/D | no verificado en las guías |
| Expertise | Revisión legal de contenido de compra | N/D | las guías de proceso existen (`/comprar-propiedad-ciudad-de-panama/`); no se vio revisor |
| Authoritativeness | Respaldo de fundador y trayectoria | 2 | página `/mayor-alfredo-aleman-mr-desarrollador/`; 1985 según ChatGPT citando `/nosotros/` (no verificado por mí) |
| Authoritativeness | Backlinks | 2 | 479 dominios principales, spam 5 |
| Trust | Razón social / RUC / dirección | N/D | no visible en lo rastreado; ChatGPT cita un aviso de operación |
| Trust | Calidad de marca | 1 | marca partida entre "Grupo Los Pueblos" y "GLP Properties" |
| Trust | Precios y fechas citables | 0 | las IA dan cifras de terceros |

### Qué debe aportar el cliente

1. Decisión de **nombre de marca principal** (Grupo Los Pueblos vs GLP Properties) y razón social, RUC, dirección y teléfono.
2. **Lista oficial de precios, tipologías y fechas** por proyecto, con fecha de vigencia.
3. Lista de **proyectos entregados** (nombre, año, unidades) que se puedan demostrar.
4. Autores y revisores nombrados (legal, fiscal) con bio.
5. Confirmar si `playacaracolresidences.com`, `oceanreefmarina.com.pa`, `seascape.oceanreefislands.com` y `boscodisantamaria.com` son micrositios de GLP.
6. Acceso a Search Console y a `robots.txt` / `llms.txt` / sitemap.
7. Fotos y vídeos propios de obra y entregas.

---

## 8. MAPA DE CONTENIDO (18 piezas)

Datos de §4. "Insumo" = lo que se pide antes de redactar. Las piezas legales llevan fuente oficial y revisor.

### Pilar A — Entidad y marca

| # | Pieza | Dato | Formato / bloque AEO-GEO | Insumo |
|---|---|---|---|---|
| 1 | **Quiénes somos: Grupo Los Pueblos (GLP Properties)** (actualizar `/nosotros/`) | marca partida; PAA "¿Quién es el dueño…?" | Definición en 1 frase, línea de tiempo con fechas, tabla de proyectos; `Organization` con `alternateName` | historia y cifras demostrables |
| 2 | **¿Es confiable GLP? Cómo verificar a una promotora** | ChatGPT duda; Claude no la conoce | Lista de verificación, documentos públicos y proyectos entregados | documentos y entregas |
| 3 | **Todo proyecto lleva la frase "Un proyecto de Grupo Los Pueblos (GLP)"** en una tabla de datos | las IA no asocian proyecto y desarrolladora | Plantilla de ficha con desarrolladora, ubicación, precios y fecha | datos oficiales por proyecto |

### Pilar B — Playa y Chame (mayor demanda)

| # | Pieza | Dato | Formato | Insumo |
|---|---|---|---|---|
| 4 | **Playa Caracol: guía completa** (rehacer `/guia-completa-playa-caracol/`) | 4.400/mes; PAA "¿Dónde queda…?", "¿Quién es el dueño…?", "¿Cuánto cuesta un apartamento…?" | Respuestas directas por pregunta, tabla de datos fechada | precios y titularidad |
| 5 | **Vivir e invertir en Chame** (hub de zona) | `chame panamá` +25 % | Hub con transporte, servicios, proyectos | datos medidos |
| 6 | **Playa Caracol: alquiler vacacional vs. uso propio** | 590 + 480/mes en variantes de alquiler | Comparativa con reglas de alquiler | reglas del proyecto |
| 7 | **Apartamentos frente al mar en Panamá: guía de compra** | PAA "¿cuál es la mejor zona de playa?" | Guía neutral con criterios | datos propios |
| 8 | **Beachfront condos in Panama for foreign buyers** (EN) | 0 visibilidad en IA | Guía con "Can foreigners own beachfront property?" y fuentes oficiales | revisor legal |

### Pilar C — Ocean Reef Islands

| # | Pieza | Dato | Formato | Insumo |
|---|---|---|---|---|
| 9 | **Ocean Reef Islands: qué es, quién lo desarrolla y precios vigentes** (ES) | 3.742/mes; precios de terceros en las IA | Ficha con cifras oficiales y fecha | lista oficial |
| 10 | **Is Ocean Reef Islands a good investment?** (EN) | 0 menciones de GLP | Análisis equilibrado: riesgos, liquidez, costos | datos de reventa |

### Pilar D — Ciudad

| # | Pieza | Dato | Formato | Insumo |
|---|---|---|---|---|
| 11 | **Punta Pacífica vs Costa del Este** | 0 visibilidad en IA | Tabla de criterios, sin cifras sin fuente | precios por m² con fuente |
| 12 | **Armonía en Cinta Costera: guía del proyecto y la zona** | `armonía` 1.300/mes en pos. 13 | Página de entidad del proyecto | datos oficiales |

### Pilar E — Proceso y legal (con fuente oficial)

| # | Pieza | Dato | Formato | Insumo |
|---|---|---|---|---|
| 13 | **Cómo comprar propiedad en Panamá siendo extranjero** (renovar `/comprar-propiedad-ciudad-de-panama/`) | 6 citas de IA; fuentes oficiales dominan | Pasos, enlaces a Registro Público/DGI, revisor | revisor legal |
| 14 | **Can foreigners buy property in Panama?** (EN) (renovar `/en/buy-property-panama-city/`) | 0 menciones | Misma estructura con fuentes | revisor legal |
| 15 | **Gastos de cierre e impuestos al comprar** | 0 menciones; `dgi.mef.gob.pa` 17 citas | Cifras solo con fuente y fecha | revisor fiscal |
| 16 | **Qué es un PH en Panamá** (ampliar) | +11 % | Definición, derechos y deberes | revisor legal |

### Pilar F — Mercado y decisión

| # | Pieza | Formato | Insumo |
|---|---|---|---|
| 17 | **Informe trimestral de mercado** (convertir `/guia-completa-del-mercado-inmobiliario-de-panama-2025/`) | Datos propios de precios y ventas, fechados | datos de ventas |
| 18 | **Cómo elegir una promotora en Panamá** (criterios) | Lista de verificación; `mejores promotoras` sin volumen medible pero con AIO | proyectos entregados |

**No perseguir sin inventario propio:** `casas en venta costa del este` (108/mes, +21 %) y `apartamentos en venta costa del este`, porque no se encontró un proyecto de GLP ahí.

---

## 9. PLAN DE 90 DÍAS

Ordenado por impacto ÷ esfuerzo.

| # | Acción | Cuándo | Métrica | Insumo |
|---|---|---|---|---|
| 1 | Acceso a Search Console; revisar `robots.txt`, `llms.txt`, sitemap y hreflang; **cerrar los N/D** | Sem. 1 | indexación y bots de IA conocidos | cliente |
| 2 | **Decidir el nombre de marca** y unificarlo (title, H1, schema, redes) | Sem. 1–2 | `glp properties` y `grupo los pueblos` convergen | cliente |
| 3 | Resolver la **relación entre `glp.com.pa` y los sitios de proyecto** (Bosco, Playa Caracol, Ocean Reef): mapa de qué contenido vive dónde, canonicales y enlaces cruzados | Sem. 2 | sin competencia entre dominios por la misma consulta | cliente |
| 4 | Arreglos on-page: title, metas duplicadas, `alt` en imágenes, H2 repetidos | Sem. 2 | flags en verde | — |
| 5 | Schema: `Organization` (+ `alternateName`, `sameAs`), `BreadcrumbList`, `Product`+`Offer` por proyecto | Sem. 2–4 | `has_micromarkup` verdadero | datos de empresa |
| 6 | Ficha estándar por proyecto (desarrolladora, ubicación, precio desde, fecha, entrega) + página de **precios vigentes** | Sem. 3–5 | las IA citan las cifras oficiales | listas oficiales |
| 7 | Piezas 1–3 (entidad y confianza) | Sem. 3–6 | Claude y Perplexity describen bien la marca; 0 errores de atribución | documentos |
| 8 | Pilar B: piezas 4–5, luego 6–8 | Sem. 4–10 | `playa caracol` a top 10; GLP citada en prompts de Playa Caracol | precios, titularidad |
| 9 | Pilar C: piezas 9–10 | Sem. 5–9 | GLP citada en "precio de Ocean Reef" (hoy 0/12) | lista oficial |
| 10 | Pilar E con revisor legal: 13–16 | Sem. 6–12 | menciones en los 3 prompts legales (hoy 0) | revisor |
| 11 | Rescatar `reserva del norte` (2.400/mes en pos. 61–64): reescribir `/proyecto/the-reserve/` | Sem. 6–8 | subir de pos. 61 a top 20 | datos del proyecto |
| 12 | **Repetir esta batería de LLM y las 14 SERPs** a 30 y 90 días | Sem. 4, 12 | menciones sin marca > 24 % (ChatGPT); presencia en los 7 prompts hoy vacíos | — |

---

## 10. LIMITACIONES

- **No pude abrir `glp.com.pa`** (política de red del entorno). Lo on-page cubre solo la home. Para el resto hay que permitir el dominio en *Network access → Allowed domains* o aportar una exportación.
- **Sin contenido de `robots.txt`, `llms.txt`, sitemap, schema del resto de páginas ni hreflang.** Estado de bots de IA: **N/D**.
- **Volumen de búsqueda:** 47 de 95 semillas son N/D en Google Ads. No priorizo por volumen los temas de proceso, legales y de inversión.
- **Google Trends** devolvió casi todo 0: no fiable para estos términos.
- **AI Overview:** en 3 SERPs se detectó el bloque pero sin fuentes devueltas. Tres keywords se midieron con una variante tras un error del servidor.
- **Discrepancia** de posición de `playa caracol` entre `ranked_keywords` (pos. 12) y la SERP en vivo (fuera del top 20).
- **Gemini:** los enlaces llegan como redirección; el 0 de citas es "no verificable". Una réplica sin resultado.
- **Claude se midió sin búsqueda web.**
- **Cifras de precio, fechas y la fundación en 1985** provienen de respuestas de IA y de lo que citan; no están verificadas por mí frente a documentos del cliente.
- **Backlinks de competidores, Core Web Vitals de campo, fichas vendidas y URLs indexadas: no medidos.**
- **Afirmaciones legales/fiscales:** el informe no contiene ninguna cifra legal; cada pieza del Pilar E necesita fuente oficial y revisión de un abogado panameño.
- **Relación entre GLP y otros dominios** (`playacaracolresidences.com`, `oceanreefmarina.com.pa`, `boscodisantamaria.com`): no confirmada.
