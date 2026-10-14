# Auditoría SEO · E-E-A-T · AEO · GEO — playacaracolresidences.com (Playa Caracol Residences & Beach Club)

Fecha: 2026-10-14 (UTC) · Prompt: `prompts/seo-auditoria-inmobiliaria-panama.md` (versión con variables de Playa Caracol) · Fuente: DataForSEO + respuestas de ChatGPT, Gemini, Perplexity y Claude vía API.

---

## 1. CONTEXTO

| Parámetro | Valor |
|---|---|
| Web | https://playacaracolresidences.com/ |
| Marca | Playa Caracol (Playa Caracol Residences & Beach Club) |
| Modelo de negocio | **Portal de una comunidad de playa con varios proyectos y servicios** (la variable venía sin rellenar). Por las URLs: proyectos residenciales (The Tides, Seashore, Olas del Mar, Brisas del Mar, Colección del Mar / Villas del Mar, Sky View), club de playa (Vento Beach & Residence Club), hotel (Surfside), Radisson Riviera Panama, spa (Zenter), comercial (Caracol Retail Village), alquileres y una calculadora (`/calculadora/`, `/en/calculator/`). |
| Ubicación | **Playa Caracol, Punta Chame, distrito de Chame, Panamá Oeste.** Las IA dan distancias distintas a la Ciudad de Panamá (ver §5.2). |
| Desarrolladora | ChatGPT y Perplexity la atribuyen a **Grupo Los Pueblos (GLP)** y ChatGPT cita `playacaracolresidences.com/nosotros/` como fuente; la web tiene una página "GLP te espera en su Experience Center en Costa del Este". **Sin confirmar por el cliente.** |
| `ZONAS` de tu archivo | Panamá, Costa del Este, Punta Pacífica, Coronado. **El proyecto está en Chame.** Costa del Este aparece por el Experience Center de GLP (y `villas del mar costa del este`, 260/mes); Coronado es la zona de playa comparable (el centro comercial The Village Coronado figura en keywords); Punta Pacífica: sin relación encontrada. |
| `location_code` | **2591** (Panamá, país); Chame figura como 9247998 (no usado). Serie EN medida también en EE. UU. (2840). |
| Idiomas | `es` y `en`; hay subcarpeta `/en/` (`/en/playa-caracol-en/`, `/en/beachfront-condos-for-sale-panama/`); hreflang: N/D. |
| Dispositivo SERP | desktop |
| Ventana de tendencia | 24 meses (2024-08 → 2026-08) |
| Gasto | ≈ 4,5 USD (saldo 46,40 → 41,94) |

Pie general: `DataForSEO · location_code 2591 · es/en · 2026-10-14`.

**Limitación de acceso, con un hallazgo:** desde este entorno no se pudo abrir el sitio (política de red). Al rastrearlo con `/v3/on_page/instant_pages`, el rastreador de DataForSEO **recibió una pantalla "Robot Challenge Screen"** (`/.well-known/sgcaptcha/`, un desafío anti-bot) en lugar de la home. Solo una de las cuatro URLs consultadas devolvió contenido real. Detalle y riesgo en §6.

---

## 2. RESUMEN EJECUTIVO

1. **Estado:** 228 keywords posicionadas en Panamá (15 en pos. 1, 24 en pos. 2–3, 55 en pos. 4–10, 34 en pos. 11–20) y ~3.646 de tráfico orgánico estimado, más 54 keywords con ~1.110 de tráfico en inglés (EE. UU.). Es la web con más tráfico estimado de las cuatro auditadas. **El 68 % cae en la home (2.494).**
2. **Mayor riesgo:** el **desafío anti-bot**. Si lo reciben también los rastreadores de IA o de búsqueda, la web podría no leerse completa. No lo he podido comprobar con esos bots: hay que verificarlo. Segundo riesgo: **buena parte del tráfico es turístico** (Radisson Riviera, surf, ballenas, Cerro Chame), no de compra.
3. **Mayor oportunidad:** `playa caracol` sube un 51 % (de 3.175 a 4.800/mes; momentum 1,58) y varias marcas de proyecto crecen: `vento beach & residence club` +74 %, `the tides playa caracol` +91 %, `brisas del mar` +46 %, `surfside playa caracol` +56 %.
4. **Brecha E-E-A-T principal:** no pude leer la home ni las páginas de proyecto. Lo observable: hay una página sobre **Golden Visa** (tema legal, sin revisor visible), contenido fuera de tema (`/quien-construyo-canal-de-panama/`) y ningún dato de autores, razón social o licencia en lo rastreado.
5. **Estado en IA:** `playacaracolresidences.com` es el **dominio más citado (24 veces)** en las respuestas sin nombrar la marca, casi todo por Perplexity (12 citas) y ChatGPT (3). Pero **ningún motor nombra "Playa Caracol Residences" en esas respuestas salvo ChatGPT en 3/36**, y en **8 de 12 preguntas no aparece nada**. Claude (sin búsqueda) no conoce el proyecto y lo confunde con otras "Playa Caracol".
6. **Acción única prioritaria:** comprobar que Googlebot y los bots de IA (GPTBot, ClaudeBot, PerplexityBot) **no reciben el desafío anti-bot**, y después ordenar la estructura de dominios (esta web, `glp.com.pa`, `playacaracolrentals.com`, `playacaracol.org`) para que cada consulta tenga una página principal.

---

## 3. INVENTARIO

Fuente: `ranked_keywords`, `relevant_pages` (es-PA) y URLs citadas por los LLM. Tráfico estimado (ETV) de DataForSEO, no de Analytics. Pie: `/v3/dataforseo_labs/google/relevant_pages/live` · 2591 · es · 2026-10-14.

| URL | Tipo | Keywords | ETV | Notas |
|---|---|---|---|---|
| `/` | home | 89 | 2.494 | `playa caracol` pos. 5 (BD) · `playa caracol panama` pos. 4 · `playa caracol rentals` pos. 2 |
| `/punta-chame-playa-caracol/` | guía / FAQ | 20 | 233 | **rastreada**: title y H1 "Preguntas Frecuentes sobre Punta Chame y Playa Caracol, Panamá"; 1.636 palabras; `punta chame` pos. 12 |
| `/te-presentamos-el-nuevo-radisson-riviera-panama/` | noticia (hotel) | 11 | 213 | `radisson riviera panama` (3.433/mes) pos. 7 · **turístico** |
| `/vento-beach-and-residence-club/` | club de playa | 11 | 172 | `vento beach & residence club` pos. 4 |
| `/conoces-cerro-chame/` | guía turística | 7 | 142 | `cerro chame` (956/mes) pos. 7–8 |
| `/brisas-del-mar-lista-para-ti-y-tu-familia/` | proyecto | 11 | 131 | `brisas del mar` pos. 6 |
| `/surfside-el-nuevo-hotel-de-playa-caracol/` | noticia (hotel) | 7 | 122 | `hotel playa caracol` pos. 2 |
| `/the-tides/` | proyecto | 3 | 28 | **poco tráfico para un proyecto clave** |
| `/coleccion-del-mar/` | proyecto | 5 | 19 | `villas del mar` pos. 17 |
| `/en/playa-caracol-en/` | home EN | 1 | 39 | `playa caracol residences vacation rental` pos. 4 |
| `/descubre-los-mejores-restaurantes-alrededor-de-playa-caracol-en-panama/`, `/ballenas-a-la-vista/`, `/descubre-las-mejores-playas-para-surfear-.../`, `/conoce-el-nuevo-beer-garden-.../`, `/zenter-spa/` | turismo y servicios | 3–10 | 4–11 | tráfico turístico |
| `/casas-de-playa-en-venta-en-panama-guia-.../` | guía de compra | 5 | 2 | casi sin tráfico |
| `/seashore/`, `/sky-view-playa-caracol/`, `/en/olas-del-mar-lovely-beachfront-condos-in-panama/`, `/un-paraiso-te-espera/` | proyectos | 0–5 | 0–3 | |
| `/golden-visa-panama-vs-otros/` | **legal (YMYL)** | 1 | 1 | sin revisor visible |
| `/quien-construyo-canal-de-panama/` | **fuera de tema** | 7 | 1 | |
| `/glp-te-espera-en-su-experience-center-en-costa-del-este/`, `/conoce-casa-playa-caracol-en-casco-viejo/`, `/10-razones-para-vivir-en-la-riviera-pacifica-de-panama/` | noticias / ventas | 1–4 | 1–4 | |
| `/nosotros/`, `/invertir-playa-caracol/`, `/en/beachfront-condos-for-sale-panama/`, `/en/beachfront-community-panama-with-marina/`, `/alquiler-playa-caracol/`, `/invierte-en-playa-caracol-y-disfruta/`, `/calculadora/`, `/apartamentos-para-comprar-en-panama-con-excelente-ubicacion/`, `/los-mejores-destinos-para-inversion-inmobiliaria-en-panama/` | corporativas, inversión, alquiler | — | — | **citadas por las IA** (3–8 veces); no rastreadas por mí |

Movimiento (es-PA): 125 keywords nuevas, 31 suben, 47 bajan, 43 perdidas. Fichas vendidas, URLs indexadas y fecha de último cambio: **N/D**.

**La mezcla turístico/compra:** entre las 8 páginas con más tráfico, 3 son turismo o noticias de hotel (Radisson, Surfside y Cerro Chame), 1 es la guía de zona (Punta Chame) y 4 son de oferta (la home, Vento, Brisas del Mar y la home en inglés). No es malo: atrae audiencia a la zona, pero hay que conectarla con la oferta de compra.

---

## 4. UNIVERSO DE KEYWORDS (con tendencia)

Pie: `/v3/keywords_data/google_ads/search_volume/live` y `/v3/dataforseo_labs/google/keyword_suggestions/live` · 2591 · es/en · 2026-10-14. `yoy` = media 12 m ÷ media 12 m previos − 1. Clases según el prompt. **†** = la serie tiene ≥ 2 meses en cero en los 12 meses previos: el `yoy` está inflado y debe leerse con cautela.

### 4.1 Con tendencia medida

| Keyword | Idioma | Vol. 12 m | Previo | yoy | Mom. 3 m | Clase |
|---|---|---|---|---|---|---|
| **playa caracol** | es | 4.800 | 3.175 | **+51 %** | 1,58 | **Emergente** |
| playa caracol panama | en | 3.550 | 3.700 | −4 % | 0,85 | Estable |
| radisson riviera panama † | es | 3.433 | 2.248 | +53 % | 1,19 | Creciente (turístico) |
| punta chame | es | 3.417 | 3.392 | +1 % | 0,75 | Estable |
| casamar panama | es | 1.023 | 796 | +29 % | 1,12 | Creciente (**ruido**: otra comunidad) |
| cerro chame | es | 956 | 691 | +38 % | 1,19 | Creciente (turístico) |
| playa caracol residences & beach club | es | 783 | 1.038 | **−25 %** | 0,55 | **Declive** |
| villas del mar | es | 540 | 473 | +14 % | 1,07 | Creciente |
| playa caracol rentals | es/en | 510 | 499 | +2 % | 0,76 | Estable |
| **vento beach & residence club** | es | 471 | 271 | **+74 %** | 1,44 | **Emergente** |
| playa caracol chame | es | 354 | 316 | +12 % | 1,33 | Creciente |
| brisas del mar | es | 318 | 218 | +46 % | 1,41 | Emergente |
| punta chame panama | en | 301 | 231 | +30 % | 0,95 | Creciente |
| coronado panama real estate | en | 124 | 103 | +20 % | 1,0 | Creciente |
| **the tides playa caracol** | es | 88 | 46 | **+91 %** | 1,32 | **Emergente** |
| playa caracol panamá | es | 86 | 59 | +45 % | 0,85 | Creciente |
| olas del mar playa caracol † | es | 84 | 23 | +274 % | 4,14 | Emergente (2 meses en cero) |
| playa caracol residences | es/en | 64 | 64 | 0 % | 1,17 | Estable |
| dónde queda playa caracol | es | 61 | 108 | −44 % | 0,55 | Declive |
| surfside playa caracol | es | 51 | 33 | +56 % | 1,75 | Emergente |
| airbnb playa caracol † | es | 38 | 10 | +283 % | 3,75 | Emergente (5 meses en cero) |
| **playa caracol apartamentos** | es | 27 | 18 | **+52 %** | 1,75 | **Emergente** |
| playa caracol alquiler | es | 27 | 17 | +60 % | 1,0 | Creciente |
| seashore playa caracol † | es | 24 | 7 | +262 % | 0,83 | Creciente (9 meses en cero) |
| casa de playa panamá | es | 20 | 17 | +20 % | 0,6 | Creciente |
| casas en venta chame | es | 10 | 10 | 0 % | 1,0 | Estable |
| terrenos en punta chame | es | 10 | 9 | +9 % | 1,0 | Estable |
| playa caracol condos for sale | en | 6,7 | 3,3 | +100 % | 2,0 | Emergente (volumen mínimo; CPC 8,47 USD) |

**Sub-demanda de marca (Labs, 12 m):** `playa caracol residences & beach club` 880 · `playa caracol residences vacation rental` 590 (transaccional) · `playa caracol rentals` 480 · `radisson playa caracol` 390 · `playa caracol chame` 320 · `punta chame` 3.600 · `punta chame playa` 1.000 · `punta chame villas` 480. `vento beach club` y `playa caracol vento beach club` son consultas de **pasadía** (day pass), no de compra.

### 4.2 Lecturas

- **El nombre de marca cae, el lugar sube.** `playa caracol residences & beach club` baja un 25 % mientras `playa caracol` sube un 51 %. La gente busca el lugar, no el nombre comercial del proyecto: conviene apuntar a "Playa Caracol" + producto.
- **La demanda de compra explícita es muy pequeña en Google Ads** (`playa caracol apartamentos` 27/mes, `playa caracol condos for sale` 7/mes, `casas en venta chame` 10/mes). El volumen real está en el lugar, el turismo y el alquiler.
- **Hay demanda de alquiler vacacional:** `playa caracol rentals` 510, `playa caracol residences vacation rental` 590, `airbnb playa caracol` +283 %†. La web ya posiciona muy bien ahí (pos. 2–4 y 6 resultados en el top 25 en inglés).
- **Ruido:** `casamar panama` (1.023) es otra comunidad de playa (el SERP lo domina `casamarbeachproperties.com`); `surf`, `avistamiento de ballenas`, `beer pool`, `mall the village coronado`, `bella beach club` y similares atraen audiencia sin intención de compra.
- **32 de 71 semillas son N/D** en Google Ads: compra de apartamento, inversión, vivir en Punta Chame, financiamiento, proceso para extranjeros, gastos de cierre y `golden visa panamá bienes raíces`, entre otras.
- **Google Trends no se consultó** en esta auditoría.

### 4.3 Score de oportunidad

`volumen` (log, tope 1.500) y `tendencia` de datos; `valor_comercial`, `facilidad` y `encaje_aeo_geo` son **estimaciones mías**, no de API.

| Keyword | Vol. | Clase | Score |
|---|---|---|---|
| playa caracol | 4.800 | Emergente | 0,75 |
| the tides playa caracol | 88 | Emergente | 0,73 |
| vento beach & residence club | 471 | Emergente | 0,72 |
| playa caracol apartamentos | 27 | Emergente | 0,70 |
| olas del mar playa caracol † | 84 | Emergente | 0,68 |
| playa caracol condos for sale (EN) | 7 | Emergente | 0,66 |
| playa caracol rentals | 510 | Estable | 0,60 |
| punta chame | 3.417 | Estable | 0,57 |
| airbnb playa caracol † | 38 | Emergente | 0,56 |
| playa caracol residences & beach club | 783 | Declive | 0,53 |

**Quick wins (pos. 4–20):** `playa caracol` (5 en la base de datos; **fuera del top 20 en la SERP en vivo**, ver §5.1), `playa caracol panama` (4), `playa caracol residences & beach club` (5), `playa caracol chame` (4), `punta chame` (12), `punta chame playa` (10), `cerro chame` (7–8), `brisas del mar` (6), `vento beach club` (4).
**Dejar de alimentar:** `dónde queda playa caracol` (−44 %), `casamar`, `surf`, `avistamiento`, `beer pool`, `quien construyó el canal`.
**Competidores / vecinos:** `playacaracolrentals.com` (alquileres, 9 apariciones en top 10), `metrorealtypanama.com` (9), `panamaequity.com` (8), `househunterspanama.com`, `casasolution.com`, `remax-centralamerica.com`, `glp.com.pa` (pos. 11 en "playa caracol panama"). Relación de `playacaracolrentals.com` y `playacaracol.org` con el proyecto: **N/D**.

**Backlinks:** 4.371 backlinks, 1.615 dominios (1.606 principales), rank 319, spam score 20, primera detección 2023-10-14. Comparación entre las cuatro webs auditadas: GLP 479 dominios (spam 5), Playa Dorada 520 (spam 5), Bosco 1.320 (spam 48), Playa Caracol 1.606 (spam 20).

---

## 5. SERP · AEO · GEO

### 5.1 SERP y AI Overview (17 keywords: 14 nuevas + 3 reutilizadas del mismo día)

Pie: `/v3/serp/google/organic/live/advanced` · 2591 · desktop · profundidad 20 · 2026-10-13/14. Las tres reutilizadas (`apartamentos en venta chame`, `apartamentos frente al mar panamá`, `casas de playa panamá`) vienen de las auditorías de GLP y Playa Dorada.

| Keyword | AI Overview | Web en top 20 | Qué gana |
|---|---|---|---|
| **playa caracol** | no | **fuera** (BD: pos. 5) | Instagram (5, 6), gites.fr, `playacaracolrentals.com` (11), `chamepanama.com`; PAA "¿Qué hoteles hay en Playa Caracol?", "¿Qué hacer…?" |
| playa caracol panama (EN) | no | **4** (GLP en 11) | Instagram, `playacaracolrentals`, `metrorealtypanama`; PAA "¿Quién es el dueño de Playa Caracol?" |
| playa caracol apartamentos | sí (sin fuentes) | **2, 6, 13** | `panamaequity`, `metrorealtypanama`, Instagram; PAA "¿Cuánto cuesta un departamento en Panamá?" |
| the tides playa caracol | sí (sin fuentes) | **4** | `panamaequity` (2), Instagram, `engelvoelkers` |
| olas del mar playa caracol | sí (sin fuentes) | **2, 8** (GLP en 11) | `playacaracolrentals`, `metrorealtypanama`, Instagram |
| vento beach & residence club | no | **4** | Instagram, ofertas de pasadía |
| playa caracol rentals (EN) | sí (sin fuentes) | **3, 5, 10, 12, 18, 23** | `playacaracolrentals.com`; PAA "Is Playa Caracol a good investment?" |
| playa caracol condos for sale (EN) | sí (sin fuentes) | **3** | `remax-centralamerica` (2), `househunterspanama` |
| playa caracol real estate (EN) | no | **5, 6, 9, 15, 21** | `casasolution` (1), `panamaequity`, `househunterspanama` |
| apartamentos en venta chame | sí | **7** (GLP en 18) | portales; **el AIO cita `playacaracolresidences.com`** |
| dónde queda playa caracol | no | **6, 13** | Instagram, `metrorealtypanama`, `residepanama.com` |
| punta chame | sí (sin fuentes) | **10** | Instagram, Wikipedia, Tripadvisor |
| apartamentos frente al mar panamá | no | **9** | Airbnb, `mlsacobir`, `encuentra24` |
| casas de playa panamá | no | 22 | `playadorada.com.pa` (1, 2) |
| airbnb playa caracol | sí (sin fuentes) | fuera | Airbnb |
| golden visa panamá bienes raíces | sí (sin fuentes) | fuera | `immigrantinvest.com`, `natlawreview`, despachos legales |
| casamar panama | sí (sin fuentes) | fuera | Instagram, `casamarbeachproperties.com` |

**AI Overview presente en 10 de 17**, y **cita a la web solo en 1** (`apartamentos en venta chame`). En 9 de los 10 el bloque no devolvió fuentes (N/D).

**Discrepancia importante:** la base de `ranked_keywords` da pos. 5 para `playa caracol` (4.800/mes), pero en la SERP en vivo la web no aparece en el top 20 orgánico y arriba hay Instagram, vídeos cortos, imágenes y anuncios. **Es la keyword más valiosa y hay que medirla con Search Console.**

**Qué formato crear:** en las búsquedas del lugar ganan redes sociales y alquileres; en las de compra, corredoras (`metrorealtypanama`, `panamaequity`, `househunterspanama`). La web ya está bien en el top 10 en búsquedas de proyecto y de alquiler. El hueco son las preguntas ("¿Quién es el dueño de Playa Caracol?", "¿Cuánto cuesta un apartamento?", "¿Es una buena inversión?"), que aparecen en PAA.

### 5.2 GEO — 15 prompts × 4 motores × 3 repeticiones = 180 respuestas

Pie: `/v3/ai_optimization/{chat_gpt,claude,gemini,perplexity}/llm_responses/live` · modelos `gpt-6-sol`, `claude-sonnet-5-5`, `gemini-3.5-flash`, `sonar` · 2026-10-14. Búsqueda web activa en ChatGPT, Gemini y Perplexity; **Claude sin búsqueda** (conocimiento base).

**Prompts de marca (3: ¿qué es Playa Caracol Residences?, ¿vale la pena comprar un apartamento en Playa Caracol?, y su versión en inglés):**

| Motor | Describe el proyecto | Cita `playacaracolresidences.com` |
|---|---|---|
| ChatGPT | Sí; **"La desarrolla Grupo Los Pueblos (GLP)"**, citando `/nosotros/` | 4 de 6 en los dos prompts de "¿qué es?"; 0 de 3 en "¿vale la pena?" |
| Perplexity | Sí; "desarrollado y operado por GLP… más de tres décadas de experiencia" | 9 de 9 |
| Gemini | Sí; "a unos 75 km (1 h 15 min) de la Ciudad de Panamá" | 0 verificable |
| Claude (sin web) | **No**: "No tengo información confiable sobre un proyecto llamado exactamente…"; ante "¿vale la pena?" pregunta a cuál Playa Caracol te refieres (México, otros países) | — |

**Prompts sin nombrar la marca (12 prompts × 3 réplicas = 36 por motor).** "Menciona" = nombra *Playa Caracol Residences*:

| Motor | Menciona | Cita la web |
|---|---|---|
| ChatGPT | 3/36 | 3 |
| Perplexity | 0/36 | **12** |
| Gemini | 0/36 | 0 verificable |
| Claude (sin web) | 0/36 | — |

Los otros prompts nombran "Playa Caracol" a secas, así que miro si el motor conoce al proyecto o cita su web. **No aparece nada en ningún motor en 8 de las 12 preguntas:** vivir en Punta Chame, precio de un apartamento, comparación con Coronado, proceso de compra para extranjeros, gastos de cierre e impuestos, *Best beachfront condos near Panama City*, *Can I rent a condo on Airbnb?* y *Can foreigners buy a beachfront condo?*. Perplexity cita la web (sin nombrar el proyecto) en: mejores proyectos de playa, dónde queda y cómo llegar, alquiler como inversión y *Is Playa Caracol a good place to buy a condo?*.

**Quién se cita en respuestas sin marca:** **`playacaracolresidences.com` 24**, `panamaprop.com` 23, `airbnb.com` 23, `homes.com` 15, **`registro-publico.gob.pa` 15**, `panamaequity.com` 13, `revisa24.com` 13, **`dgi.mef.gob.pa` 13**, **`glp.com.pa` 12**, `primepanama.com` 12, `directoriodigitaldecoronado.com` 12, `playacaracolrentals.com` 10, `playacaracol.org` 9. **Páginas propias más citadas:** `/nosotros/` (8), `/invertir-playa-caracol/` (7), `/en/beachfront-condos-for-sale-panama/` (6), `/en/beachfront-community-panama-with-marina/` (3), `/alquiler-playa-caracol/` (3), `/calculadora/` (3).

**Hallazgos de contenido:**
- **Datos que cambian de una respuesta a otra.** Distancia a la ciudad: Gemini dice 75 km (1 h 15 min); ChatGPT, citando la página `/the-tides/`, dice "unos 16 km desde la salida hacia Punta Chame… alrededor de 1 h 30 min" (el 16 km es el tramo final, no el total); un resultado de Instagram habla de "90 minutos". Precios: Perplexity da "US$199.900 a US$408.139" por apartamentos y ChatGPT "US$249.000 a US$375.000" (precios de anuncio de terceros). **Nada de eso está verificado por mí**: la web necesita publicar sus cifras, fechadas, y medir el trayecto.
- **Sobre rentabilidad por alquiler**, Perplexity dice que se puede ganar dinero con alquiler de corta estancia y el programa de *property management* del complejo, y advierte que la rentabilidad depende de varios factores. Hay que respaldar con datos propios o no prometer.
- **Confusión de entidad.** Claude lo asocia a Playa Caracol de México y otros países; la SERP mezcla `casamar`, `playa escondida` y otras. La página de entidad debe nombrar país, distrito y provincia en la primera frase.
- **Inconsistencia de trayectoria de GLP:** una respuesta dice "más de tres décadas" y otras "cuatro décadas". Un detalle para la página corporativa.
- **Fuentes oficiales:** para temas legales las IA citan `registro-publico.gob.pa` (15) y `dgi.mef.gob.pa` (13); el sitio no está en esas respuestas.

---

## 6. AUDITORÍA TÉCNICA

Pie: `/v3/on_page/instant_pages` · 2026-10-14. Lo no listado: **N/D**.

| Área | Estado | Evidencia |
|---|---|---|
| **Acceso del rastreador** | **✖ riesgo alto** | La home devolvió `https://playacaracolresidences.com/.well-known/sgcaptcha/…` con título **"Robot Challenge Screen"**, 27 palabras y H1 "playacaracolresidences.com". Es un desafío anti-bot (`sgcaptcha`) que se sirve a ciertos visitantes automatizados. |
| Qué no se sabe | N/D | Si el desafío se aplica a **Googlebot**, **GPTBot**, **ClaudeBot**, **PerplexityBot** u otros. Las IA y Google sí leen la web (la citan y la posicionan), así que al menos esos bots llegan al contenido real; el riesgo es que no todos lo hagan, o que lo hagan de forma intermitente. |
| Resto de URLs | N/D | De cuatro URLs consultadas, solo `/punta-chame-playa-caracol/` devolvió contenido real. `/the-tides/` y `/en/playa-caracol-en/` no devolvieron resultado. |
| `/punta-chame-playa-caracol/` | parcial | title y H1 "Preguntas Frecuentes sobre Punta Chame y Playa Caracol, Panamá"; 1.636 palabras; on-page score 87,1; sin datos estructurados (`has_micromarkup: false`) |
| Home: title, H1, meta, schema, rendimiento, imágenes | **N/D** | bloqueado por el desafío |
| Idiomas | N/D | `/en/` existe; hreflang sin verificar |
| `robots.txt`, `llms.txt`, sitemap | N/D | sin acceso |
| Backlinks | informativo | 4.371 backlinks, 1.606 dominios principales, rank 319, spam score 20 |

**Qué hacer:** pedir al hosting (el desafío proviene de SiteGround Security) que **excluya de `sgcaptcha`** a Googlebot, Bingbot y a los user-agents de los bots de IA que el cliente quiera permitir, y verificarlo con Search Console (Inspección de URL en vivo) y con los registros del servidor.

---

## 7. AUDITORÍA E-E-A-T

Puntuación 0–3 sobre lo observable; "N/D" donde no hay evidencia.

| Pilar | Señal | Punt. | Evidencia |
|---|---|---|---|
| Experience | Club de playa, hotel, spa, restaurantes en la comunidad | 2 | páginas `/vento-beach-and-residence-club/`, `/surfside-el-nuevo-hotel-de-playa-caracol/`, `/zenter-spa/`; autenticidad de las fotos: N/D |
| Experience | Casos o clientes reales | N/D | no encontrado |
| Expertise | Autores con bio | N/D | no verificado |
| Expertise | Revisión legal de contenido de compra y visa | 0 | `/golden-visa-panama-vs-otros/` existe sin revisor visible |
| Authoritativeness | Perfil de enlaces | 2 | 1.606 dominios principales; spam score 20 (moderado) |
| Authoritativeness | Respaldo de desarrolladora | 1 | las IA lo atribuyen a GLP, citando `/nosotros/`; el contenido de la página: N/D |
| Trust | Razón social, RUC, dirección, teléfono | N/D | no visible en lo rastreado |
| Trust | Calidad editorial | 1 | contenido fuera de tema (`/quien-construyo-canal-de-panama/`) |
| Trust | Precios y fechas citables | 0 | las IA citan precios y distancias de terceros |

### Qué debe aportar el cliente

1. **Confirmación de la desarrolladora** (razón social, RUC) y del papel de GLP en la comunidad, el hotel, el club y los alquileres.
2. **Lista oficial de precios, tipologías y fechas** por proyecto (The Tides, Seashore, Olas del Mar, Brisas del Mar, Colección del Mar, Sky View), con fecha de vigencia.
3. **Estructura de dominios**: relación de `glp.com.pa`, `playacaracolrentals.com`, `playacaracol.org` y `playacaracolresidences.com`.
4. **Datos del programa de alquiler / property management** (qué incluye, cuántas unidades, resultados que se puedan demostrar).
5. **Hoja de supuestos de la calculadora** (`/calculadora/`) y quién la revisó.
6. **Autores y revisores** (legal, fiscal, inmigración).
7. **Acceso a Search Console, a los registros del servidor y a la configuración de seguridad** (desafío anti-bot).

---

## 8. MAPA DE CONTENIDO (19 piezas)

Datos de §4. "Insumo" = lo que se pide antes de redactar. Las piezas legales llevan fuente oficial y revisor.

### Pilar A — Entidad y estructura de la comunidad

| # | Pieza | Dato | Formato | Insumo |
|---|---|---|---|---|
| 1 | **Playa Caracol Residences & Beach Club: qué es, dónde está y quién lo desarrolla** (renovar `/nosotros/`, citada 8 veces) | marca −25 %; Claude no la conoce; PAA "¿Quién es el dueño…?" | Definición con país, distrito y provincia en la 1.ª frase; tabla de datos; `Organization` | datos oficiales |
| 2 | **Playa Caracol, Panama: what it is and who develops it** (EN) | EN 3.550/mes | versión EN con hreflang | datos oficiales |
| 3 | **Hub "Proyectos y colecciones"**: The Tides, Seashore, Olas del Mar, Brisas del Mar, Colección del Mar, Sky View | marcas de proyecto +46 % a +91 % | tabla comparable: tipología, m², precio desde, entrega, fecha | lista oficial |

### Pilar B — Compra

| # | Pieza | Dato | Formato | Insumo |
|---|---|---|---|---|
| 4 | **Apartamentos en venta en Playa Caracol** | `playa caracol apartamentos` +52 %; pos. 2, 6, 13 | categoría con oferta | precios y disponibilidad |
| 5 | **Beachfront condos for sale in Playa Caracol** (EN; renovar `/en/beachfront-condos-for-sale-panama/`, 6 citas) | EN condos +100 % (volumen mínimo, CPC 8,47 USD) | landing con oferta | precios |
| 6 | **The Tides: villas y townhouses frente al mar** | `the tides playa caracol` +91 % | ficha de proyecto | planos y precios |
| 7 | **Olas del Mar** y **Brisas del Mar** (una ficha cada una) | `olas del mar` +274 %†; `brisas del mar` +46 % | fichas | planos y precios |

### Pilar C — Precio

| # | Pieza | Dato | Formato | Insumo |
|---|---|---|---|---|
| 8 | **¿Cuánto cuesta un apartamento en Playa Caracol?** | 0 visibilidad; las IA citan cifras de terceros que difieren (US$199.900–408.139 vs US$249.000–375.000) | tabla oficial fechada | lista de precios |
| 9 | **Calculadora** (renovar `/calculadora/` y `/en/calculator/`) | citada 3 veces | supuestos visibles y fecha | hoja de supuestos |

### Pilar D — Alquiler e inversión (sin prometer rentabilidades)

| # | Pieza | Dato | Formato | Insumo |
|---|---|---|---|---|
| 10 | **Invertir en Playa Caracol** (renovar `/invertir-playa-caracol/`, 7 citas) | PAA "Is Playa Caracol a good investment?" | análisis equilibrado: costos, riesgos, liquidez | datos reales |
| 11 | **Alquilar tu apartamento: cómo funciona el programa de property management** (renovar `/alquiler-playa-caracol/`) | `playa caracol rentals` 510; 0 menciones en el prompt de Airbnb (EN) | proceso, costos y reglas | contrato tipo |

### Pilar E — Zona y acceso

| # | Pieza | Dato | Formato | Insumo |
|---|---|---|---|---|
| 12 | **Cómo llegar a Playa Caracol desde la Ciudad de Panamá** | las IA dan 75 km/1 h 15, 1 h 30 y "90 min" | rutas con tiempos **medidos** y fecha | mediciones |
| 13 | **Vivir en Punta Chame** | `punta chame` 3.417; 0 visibilidad | hub de zona: servicios, accesos, vida diaria | visita |
| 14 | **Playa Caracol vs Coronado: dónde comprar** | 0 visibilidad | tabla de criterios | precios por m² con fuente |
| 15 | **Punta Chame y Playa Caracol: preguntas frecuentes** (ya rastreada, 233 ETV) | `punta chame` pos. 12 | mantener; añadir fecha y fuentes | — |

### Pilar F — Proceso y legal (con fuente oficial)

| # | Pieza | Dato | Formato | Insumo |
|---|---|---|---|---|
| 16 | **Cómo comprar un apartamento de playa en Panamá siendo extranjero** | 0 visibilidad; `registro-publico.gob.pa` 15 citas | pasos y enlaces oficiales | revisor legal |
| 17 | **Can foreigners buy a beachfront condo in Panama?** (EN) | 0 visibilidad | misma estructura | revisor legal |
| 18 | **Gastos de cierre e impuestos** | 0 visibilidad; `dgi.mef.gob.pa` 13 citas | cifras solo con fuente y fecha | revisor fiscal |
| 19 | **Golden Visa y bienes raíces: qué dice la norma vigente** (revisar `/golden-visa-panama-vs-otros/`) | AIO presente; ganan despachos legales | contenido revisado por abogado de inmigración o retirarlo | revisor |

**Gobernanza del contenido turístico:** mantener Radisson, surf, ballenas y Cerro Chame (atraen audiencia), pero en una categoría "Vivir en la zona" que enlace a la oferta; evaluar retirar o `noindex` lo que no tiene relación (`/quien-construyo-canal-de-panama/`).

---

## 9. PLAN DE 90 DÍAS

Ordenado por impacto ÷ esfuerzo.

| # | Acción | Cuándo | Métrica | Insumo |
|---|---|---|---|---|
| 1 | **Probar el desafío anti-bot** con Googlebot, GPTBot, ClaudeBot y PerplexityBot (Inspección de URL en vivo, registros del servidor) y **excluirlos de `sgcaptcha`** si se aplica | Sem. 1 | los bots reciben el contenido real | hosting |
| 2 | Acceso a Search Console; revisar `robots.txt`, `llms.txt`, sitemap y hreflang; **medir `playa caracol`** (BD pos. 5 frente a fuera del top 20 en vivo) | Sem. 1 | posición real conocida | cliente |
| 3 | **Mapa de dominios**: qué vive en cada uno (`glp.com.pa`, `playacaracolresidences.com`, `playacaracolrentals.com`, `playacaracol.org`), canonicales y enlaces cruzados | Sem. 1–2 | una página principal por consulta | cliente |
| 4 | Repetir la auditoría on-page de la home y de los proyectos cuando el rastreo sea posible | Sem. 2 | schema, H1, rendimiento y `alt` medidos | — |
| 5 | Página de entidad ES/EN (piezas 1 y 2) con país, distrito y desarrolladora en la primera frase | Sem. 2–4 | Claude describe bien el proyecto | datos oficiales |
| 6 | **Precios y disponibilidad fechados** por proyecto (piezas 3, 8) | Sem. 3–5 | las IA citan las cifras oficiales | lista de precios |
| 7 | **Tiempos de trayecto medidos** (pieza 12) | Sem. 2–3 | una cifra coherente en la web | mediciones |
| 8 | Fichas de proyecto (piezas 4–7) | Sem. 4–8 | `the tides playa caracol`, `playa caracol apartamentos` en top 3 | planos y precios |
| 9 | Alquiler e inversión (10–11) con datos reales, sin prometer rentabilidad | Sem. 5–8 | presencia en los prompts de Airbnb/inversión (hoy 0/12 y 1/12) | datos |
| 10 | Pilar F con revisor legal (16–19); revisar o retirar Golden Visa | Sem. 6–12 | menciones en los 3 prompts legales (hoy 0) | revisor |
| 11 | Zona y comparativas (13–15) | Sem. 6–10 | visibilidad en "vivir en Punta Chame" y "vs Coronado" (hoy 0) | visita |
| 12 | **Repetir esta batería de LLM y las 17 SERPs** a 30 y 90 días | Sem. 4, 12 | menciones por nombre en ChatGPT > 3/36; aparición en los 8 prompts hoy vacíos | — |

---

## 10. LIMITACIONES

- **No pude abrir el sitio** desde este entorno (política de red). Además, el rastreador de DataForSEO **recibió un desafío anti-bot** en la home: title, H1, meta, schema, rendimiento e imágenes de la home son **N/D**. Solo una subpágina se rastreó con contenido real.
- **No sé si el desafío afecta a Googlebot o a los bots de IA.** Las IA citan la web, lo cual indica que al menos algunos sí acceden.
- **Sin contenido de `robots.txt`, `llms.txt`, sitemap ni hreflang.** Estado de bots de IA: N/D.
- **Volumen de búsqueda:** 32 de 71 semillas son N/D en Google Ads. Los temas de compra, inversión, proceso legal y financiamiento no se pueden priorizar por volumen.
- **Series con meses en cero** (†): `radisson riviera panama`, `olas del mar playa caracol`, `airbnb playa caracol`, `seashore playa caracol`: su `yoy` está inflado.
- **Discrepancia de posición** entre `ranked_keywords` y la SERP en vivo para `playa caracol` (pos. 5 frente a fuera del top 20).
- **AI Overview:** en 9 de 10 SERPs con bloque no se devolvieron fuentes. Tres SERPs se reutilizaron de otras auditorías del mismo día.
- **Gemini:** los enlaces llegan como redirección; el 0 de citas es "no verificable". **Claude se midió sin búsqueda web.**
- **Distancias y precios** que citan las IA no están verificados por mí; el 16 km de ChatGPT es el último tramo, no el trayecto total.
- **Relación con GLP** y con `playacaracolrentals.com` / `playacaracol.org`: no confirmada.
- **Google Trends no se consultó.** Backlinks de competidores, Core Web Vitals de campo, fichas vendidas y URLs indexadas: no medidos.
- **Afirmaciones legales/fiscales:** el informe no contiene ninguna cifra legal; cada pieza del Pilar F necesita fuente oficial y revisión de un abogado panameño.
