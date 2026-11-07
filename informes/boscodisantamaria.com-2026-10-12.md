# Auditoría SEO · E-E-A-T · AEO · GEO — boscodisantamaria.com

Fecha: 2026-10-12 (UTC) · Prompt: `prompts/seo-auditoria-inmobiliaria-panama.md` (versión con variables de Bosco) · Fuente de datos: DataForSEO + respuestas de ChatGPT, Gemini, Perplexity y Claude vía API.

---

## 1. CONTEXTO

| Parámetro | Valor |
|---|---|
| Web | https://boscodisantamaria.com |
| Marca | Bosco di Santa María (og:site_name del sitio: "Bosco Galería Panamá") |
| Modelo de negocio | **Promotora, proyecto único.** *Inferido*, no confirmado: la variable venía sin rellenar. Las respuestas de ChatGPT, Gemini y Perplexity atribuyen el proyecto a GLP / Grupo Los Pueblos, y el H2 de la home dice "Un ícono desarrollado por:". Confirmar con el cliente. |
| Zona real del proyecto | **Santa María (Santa María Norte), Ciudad de Panamá**, dentro de Santa María Golf & Country Club. Tu variable `ZONAS` decía "Panamá, Costa del Este"; Costa del Este es **zona vecina y competidora**, no la ubicación del proyecto. Audité Santa María como zona principal y Costa del Este como zona de comparación. |
| `location_code` | **2591** (Panamá, país), resuelto con `/v3/serp/google/locations/pa` |
| Idiomas | `es` y `en` |
| Dispositivo SERP | desktop (móvil no medido) |
| Ventana de tendencia | 24 meses, de 2024-08 a 2026-08. Septiembre 2026 no estaba disponible en Google Ads. |
| Gasto | ≈ 4,9 USD (saldo 60,99 → ≈ 56,1). Presupuesto del prompt: 500; no se acercó. |

Pie general: `DataForSEO · location_code 2591 · es/en · 2026-10-12`.

---

## 2. RESUMEN EJECUTIVO

1. **Estado:** la web posiciona 54 keywords, casi todas de marca/zona. 47 de las 54 caen en la **home**. Ninguna está en el top 3; una (`panama golf course`) está en la posición 9. Tráfico orgánico estimado: 38 visitas/mes.
2. **Mayor oportunidad emergente:** `santa maria golf and country club` pasa de ~91 a **~1.009 búsquedas/mes (media 12 m)** y llegó a **3.600 en ago-2026**. La web está en la posición 21 con `/ubicacion/`. Es una búsqueda mayormente navegacional (la gente busca el club), así que el objetivo realista es capturar al que investiga vivir ahí, no suplantar al club.
3. **Mayor riesgo:** en las respuestas de LLM **sin nombrar la marca**, Bosco aparece en 8/36 respuestas de ChatGPT y 10/36 de Gemini, y en **0/36 de Perplexity y 0/36 de Claude**. La web **no es citada como fuente en ninguna** de esas respuestas. Quienes se citan son `panamaprop.com`, `encuentra24.com`, `glp.com.pa` y `vacagroup.net`.
4. **Brecha E-E-A-T principal:** la web publica 323 palabras en la home, sin autor, sin schema, con H1/H2 en italiano y **dos erratas en H2** ("estrátegico", "desarollado"). Los temas legales y de compra, donde los LLMs sí citan fuentes, no están cubiertos.
5. **Estado en IA:** Claude (sin búsqueda web) responde "No tengo información confiable sobre Bosco di Santa María", así que la marca no está en su conocimiento base. Con búsqueda, ChatGPT y Perplexity sí la describen y citan la web, pero apoyándose sobre todo en `glp.com.pa` y `vacagroup.net`.
6. **Acción única prioritaria:** crear el contenido de **entidad y zona** (qué es Bosco, Santa María Norte, Santa María Golf & Country Club) con autor, fecha y fuentes, y enlazarlo con `glp.com.pa`, que ya concentra las citas de IA.

---

## 3. INVENTARIO

**Limitación:** desde este entorno **no se pudo abrir el sitio** (la política de red bloqueó el dominio). Todo lo on-page viene del rastreador de DataForSEO (`/v3/on_page/instant_pages`), que devolvió **solo 2 de 14 URLs consultadas** (home y `/ubicacion/`). El resto figura abajo con la fuente por la que se conoce.

| URL | Tipo | Keyword / señal | Posición | Fuente |
|---|---|---|---|---|
| `/` | home | 47 keywords (`santa maria` pos. 23, `apartamentos don bosco` pos. 17…) | 17–74 | on-page + ranked_keywords |
| `/ubicacion/` | zona | `santa maria golf and country club` | 21 | on-page + SERP |
| `/golf-course-condos-panama/` | guía (EN) | `panama golf course` | 9 | ranked_keywords |
| `/avanti/` | tipología/torre | `avanti` | 35 | ranked_keywords |
| `/casa-bosco/` | casas | `casas en don bosco` | 26 | ranked_keywords |
| `/apartamentos-lujo-santa-maria/` | categoría | citada 8 veces por ChatGPT/Perplexity | N/D | citas de LLM |
| `/venta-apartamento-santa-maria/` | categoría | citada 3 veces por Perplexity | N/D | citas de LLM |
| `/apartamentos/`, `/lujo-innovador/` | N/D | citadas por ChatGPT / Perplexity | N/D | citas de LLM |
| `info.boscodisantamaria.com` | subdominio | citado 3 veces por Perplexity | N/D | citas de LLM |

N/D: el rastreador no devolvió contenido de `/apartamentos-lujo-santa-maria/`, `/venta-apartamento-santa-maria/`, `/blog/`, `/en/` ni `/contacto/`. No afirmo que no existan: unas se conocen por citas de IA y de otras no hay evidencia. Fichas vendidas/expiradas, número de URLs indexadas y fecha de último cambio: **N/D**.

---

## 4. UNIVERSO DE KEYWORDS (con tendencia)

Pie: `/v3/keywords_data/google_ads/search_volume/live` y `/v3/dataforseo_labs/google/keyword_suggestions/live` · 2591 · es/en · 2026-10-12. Cálculo de `yoy` = media 12 m (sep-25→ago-26) ÷ media 12 m previa − 1. Clase según las reglas del prompt.

### 4.1 Con tendencia medida

| Keyword | Idioma | Vol. 12 m | Previo | yoy | Mom. 3 m | Clase | Score |
|---|---|---|---|---|---|---|---|
| buy apartment in panama | en | 90 | 55 | +64 % | 2,0 | **Emergente** | 0,74 |
| santa maria golf and country club | es | 1.009 | 91 | +1.011 % | 29 | **Emergente** | 0,67 |
| casas en venta costa del este | es | 108 | 89 | +21 % | 1,16 | Creciente | 0,64 |
| apartamentos en venta costa del este | es | 51 | 45 | +13 % | 1,38 | Creciente | 0,60 |
| casas en venta panamá | es | 34 | 28 | +24 % | 1,11 | Creciente | 0,58 |
| vivir en costa del este | es | 6,7 | 4,2 | +60 % | 2,0 | **Emergente** | 0,57 |
| panama real estate | en | 543 | 549 | −1 % | 1,32 | Estable | 0,57 |
| panama city real estate for sale | en | 20 | 11 | +85 % | 1,0 | Creciente | 0,57 |
| santa maria panama real estate | en | 15 | 12,5 | +20 % | 1,33 | Creciente | 0,56 |
| costa del este panamá | es | 1.375 | 1.400 | −2 % | 1,0 | Estable | 0,56 |
| apartamentos en venta panamá | es | 16 | 14 | +12 % | 1,0 | Creciente | 0,55 |
| apartamentos en venta santa maria | es | 10 | 10 | 0 % | 1,0 | Estable | 0,53 |
| santa maria business district | es | 1.450 | 1.325 | +9 % | 1,31 | Estable | 0,51 |
| proyectos inmobiliarios panamá | es | 104 | 122 | −15 % | 0,92 | **Declive** | 0,41 |

**Cómo se calculó el score:** `volumen` (escala log, tope 1.500) y `tendencia` salen de los datos. `valor_comercial`, `facilidad` y `encaje_aeo_geo` son **estimaciones mías** a partir de la intención y de los dominios del top 10 (no son datos de API). Úsalo para ordenar, no como medida exacta.

**Marca y entidad (Google Ads, 12 m):** `bosco di santa maria` 390/mes (serie plana, con un pico de 1.000 hace 12 meses), `grupo los pueblos` 720, `glp panama` 90, `bosco santa maria` 70. `santa maria business district` es un parque comercial, no residencial: trátalo como tráfico de baja relevancia.

**Dos lecturas honestas:**
- **El mercado en Google Ads para Panamá es pequeño.** Casi todas las búsquedas informativas y de proceso (cómo comprar, gastos de cierre, hipoteca para extranjeros, precio por m², visa) devolvieron **N/D**: sin volumen en Google Ads, que no equivale a cero.
- **Google Trends y Google Ads se contradicen** en `santa maria golf & country club`: Trends devuelve 0 en las últimas 107 semanas, mientras Ads muestra el salto y Labs lista variantes con 1.000–1.600/mes. Trataría el salto como real pero **a verificar con Search Console** antes de invertir mucho en él. Puede deberse a una campaña, un evento o un cambio de agrupación de variantes.

### 4.2 Sin volumen medible (N/D)

`preventa apartamentos panamá`, `apartamentos de lujo panamá`, `apartamentos con vista al golf panamá`, `cómo comprar un apartamento en panamá`, `gastos de cierre…`, `impuesto de transferencia…`, `hipoteca para extranjeros…`, `visa por inversión…`, `precio por m²…`, `golf course condos panama`, `panama real estate for foreigners`, `buying property in panama as a foreigner`, entre otras (53 de 84 semillas). Son útiles como temas (aparecen en PAA y en las respuestas de IA) pero **no puedo priorizarlas por volumen**.

### 4.3 Lo que hoy posiciona la web (54 keywords)

- 0 en pos. 1–3 · 2 en pos. 4–10 · 10 en 11–20 · 10 en 21–30 · 32 en 31+.
- Evolución: 30 nuevas, 19 suben, 4 bajan, 8 perdidas.
- **Ruido de entidad:** ≥ 15 keywords son de **Urbanización Don Bosco** (otro barrio: `urbanización don bosco` 590/mes, `villas de don bosco`, `apartamentos don bosco`…). Traen tráfico que no es del proyecto. Además, Claude sugiere "Bosco" = obras salesianas, y `santa maria golf club` mezcla con Marbella (España).
- **Quick wins (pos. 4–20):** `panama golf course` (9, vol. 50), `villas de santa maria` (12, vol. 30), `santa maria panamá` (19, vol. 320), `apartamentos don bosco` (17, ruido).

**Competidores (SERP real):** `compreoalquile.com` (13 apariciones en top 10 de 11 SERPs), `encuentra24.com` (11), `santamariapanama.com` (7, sitio oficial de la comunidad), `realtor.com`, `inmopanama.com`. Son **portales/agregadores**; promotoras directas en SERP: `glp.com.pa` (su propia matriz). Competidores directos de proyecto nombrados por las IA: Greenview, The Woods, Dieci, Avanti (en menor medida). Perfil de backlinks de competidores: **N/D** (no consulté).

---

## 5. SERP · AEO · GEO

### 5.1 SERP y AI Overview (11 de 12 keywords resueltas; 1 falló con error del servidor)

Pie: `/v3/serp/google/organic/live/advanced` · 2591 · desktop · profundidad 20 · 2026-10-12.

| Keyword | AI Overview | Web en top 20 | Qué gana |
|---|---|---|---|
| santa maria golf and country club | no | **21** (`/ubicacion/`) | sitios del club y de la comunidad, Instagram, Marriott; **PAA**: "¿Cuánto cuesta la membresía…?", "¿Dónde queda Santa María?" |
| santa maria panama | no | fuera | `santamariapanama.com`, Marriott, `thepanamalink.com` (guía inmobiliaria); PAA "¿Qué proyectos hay en Santa María?" |
| apartamentos en venta santa maria | **sí** | fuera | `encuentra24`, `compreoalquile`; **AIO cita `glp.com.pa`** |
| apartamentos en venta costa del este | no | fuera | portales (`encuentra24`, `icasas`, `compreoalquile`) |
| apartamentos de lujo en venta panamá | sí (sin fuentes devueltas) | fuera | `properstar`, `compreoalquile`, `jamesedition` |
| apartamentos con vista al golf panamá | **sí** | fuera | `compreoalquile`, `encuentra24` |
| vivir en costa del este | **sí** | fuera | Reddit, `thepanamalink`, Instagram, TikTok |
| buy apartment in panama | sí (sin fuentes devueltas) | fuera | `panacrypto`, `realtor.com`; PAA "Can a foreigner purchase property in Panama?" |
| golf course condos panama | **sí** | **13** | **AIO cita `boscodisantamaria.com`** junto a `panamaequity` y `casasolution` |
| panama real estate for foreigners | sí | fuera | `metrorealtypanama`, `escapeartist`; PAA sobre extranjeros |
| santa maria panama real estate | no | fuera | `compreoalquile`, `panama-real-estate.com` |
| cómo comprar un apartamento en panamá | **N/D** | N/D | error del servidor en dos intentos |

**AI Overview presente en 7 de 11.** La web es citada en **1** (`golf course condos panama`). Eso es una señal buena y concreta: la página `/golf-course-condos-panama/` extrae bien aunque solo rankee 13.

**Qué formato debes crear:** en keywords de zona y de compra ganan **portales y guías**. No compitas con una página de listado: compite con **guías con datos propios** (precio por m² de tu proyecto, planos, fechas, amenidades) y con **respuestas directas** a las PAA.

### 5.2 GEO — 15 prompts × 4 motores × 3 repeticiones = 180 respuestas

Pie: `/v3/ai_optimization/{chat_gpt,claude,gemini,perplexity}/llm_responses/live` · modelos `gpt-6-sol`, `claude-sonnet-5-5`, `gemini-3.5-flash`, `sonar` · 2026-10-12. Búsqueda web activada en ChatGPT, Gemini y Perplexity. **Claude se ejecutó sin búsqueda web** (con ella la API devolvió una respuesta interrumpida), así que mide **conocimiento base**, no citas.

**Prompts de marca (3 prompts × 3 réplicas, 9 por motor).** Que el motor repita el nombre no cuenta: lo relevante es si lo conoce.

| Motor | ¿Conoce y describe el proyecto? | Cita `boscodisantamaria.com` |
|---|---|---|
| ChatGPT | Sí, 9/9 (GLP, 5 edificios, diseño italiano) | **6 de 9** |
| Perplexity | Sí, 9/9 | **6 de 9** (ES), 0 de 3 en inglés |
| Gemini | Sí, 9/9 | 0 (sus enlaces vienen como redirecciones `vertexaisearch`, dominio no verificable) |
| Claude (sin web) | **No** ("No tengo información confiable") | — |

**Prompts sin nombrar la marca (12 prompts × 3 réplicas = 36 respuestas por motor):**

| Motor | Menciona a Bosco | Cita la web |
|---|---|---|
| ChatGPT | 8/36 (22 %) | 0 |
| Gemini | 10/36 (28 %) | 0 verificable |
| Perplexity | 0/36 | 0 |
| Claude (sin web) | 0/36 | — |

Dónde aparece: *mejores proyectos de lujo en preventa* (ES y EN: ChatGPT y Gemini 3/3), *proyectos nuevos en Santa María* (Gemini 3/3, ChatGPT 2/3) y *golf course condos* (Gemini 1/3). **En 8 de los 12 prompts no aparece en ningún motor:** precio en Santa María Golf & Country Club, Santa María vs Costa del Este, vista al golf, proceso de compra para extranjeros, gastos de cierre, rentabilidad de alquiler, calidad de la zona.

**Share of Model:** no lo calculo como cociente porque no conté las menciones de todas las marcas competidoras; lo que sí puedo dar es la tasa de presencia de arriba. Como referencia, en las respuestas sin marca se nombra **Santa María** 139 veces y **Costa del Este** 76 veces; los proyectos rivales aparecen mucho menos (Greenview 7, The Woods 3, Dieci 3).

**Quién se cita en las respuestas sin marca** (conteo de enlaces): `panamaprop.com` 51, `encuentra24.com` 39, **`glp.com.pa` 19**, **`vacagroup.net` 18**, `panama-real-estate.com` 17, `arenasrealtor.com` 15, **`dgi.mef.gob.pa` 13**, `inmopluspanama.com` 12.

**Qué implica:**
- **`glp.com.pa` es tu activo GEO más fuerte.** Sus guías (`/mejores-proyectos-inmobiliarios-panama-2026-2027/`, `/cuanto-cuesta-apartamento-panama/`, `/en/best-real-estate-projects-panama/`, `/en/bosco-di-santa-maria-glps-new-icon-in-panama/`) se citan más que la propia web de Bosco. Hay que decidir qué contenido vive en cada dominio y enlazarlos.
- **Para temas fiscales/legales, los LLMs citan `dgi.mef.gob.pa` (fuente oficial).** Un artículo de gastos de cierre sin fuente oficial no competirá.
- **Datos que cambian de una respuesta a otra:** la entrega aparece como "2029", "2030" y "2029–2030"; los precios "desde US$484.000–498.000" y "desde ~US$738.000" dependen del tamaño. Hay que **contrastarlo con la lista de precios y fechas oficial del cliente** y publicar una página con esas cifras vigentes y fechadas. Es el hueco de contenido más claro.
- **Google AI Overview sí cita a Bosco** (`golf course condos panama`) pese a rankear 13: la página en inglés está bien construida para extracción.

---

## 6. AUDITORÍA TÉCNICA

Fuente: `instant_pages` de la home y `/ubicacion/`. La mayoría de áreas no se pudieron comprobar (ver §3). Pie: `/v3/on_page/instant_pages` · 2026-10-12.

| Área | Estado | Evidencia |
|---|---|---|
| Código HTTP, HTTPS, canonical | ✔ | home 200, https, canonical a sí misma |
| Title | ✖ demasiado largo | "Bosco di Santa María \| Apartamentos de Lujo en Santa María Golf & Country Club Panamá" (flag `title_too_long`) |
| Meta description | ✔ presente, relevante | 197 caracteres, incluye CTA |
| **H1 / H2 en italiano** | ✖ | H1 home: "Vive la vita naturale"; H2: "Ricchezza Residenziale"; H1 `/ubicacion/`: "Connessioni Strategiche". No contienen ninguna keyword de búsqueda. |
| **Erratas en H2** | ✖ | "Un destino **estrátegico** de inversión", "Un ícono **desarollado** por:" |
| Contenido | ✖ | home 323 palabras; flags `low_content_rate` y `low_readability_rate` |
| Meta duplicados | ✖ | flag `duplicate_meta_tags` |
| Imágenes | ✖ | 31 imágenes; flag `no_image_alt` y `no_image_title` |
| **Schema (datos estructurados)** | ✖ | `has_micromarkup: false` en la home |
| Rendimiento | ✖ | TTFB 2.959 ms, LCP 3.116 ms (medidos desde DataForSEO, no de campo); flags `high_loading_time`, `has_render_blocking_resources`. `total_dom_size` = 16.370.039 según la API: **unidad no confirmada, verificar con Lighthouse** |
| Open Graph | ✖ | `og:title` = "Inicio", `og:locale` = es_MX, `og:site_name` = "Bosco Galería Panamá" |
| Sitemap | ✖ / N/D | la home figura `from_sitemap: false`; `sitemap.xml` no devolvió contenido |
| robots.txt / llms.txt | **N/D** | `robots.txt` existe (975 bytes) pero **no pude leer su contenido**; `llms.txt` no devolvió resultado. **No puedo decir si se bloquea GPTBot, ClaudeBot o PerplexityBot.** |
| hreflang / versión EN | **N/D** | la IA cita `/golf-course-condos-panama/` (EN) y `info.boscodisantamaria.com`; estructura de idiomas sin verificar |
| Backlinks | informativo | 1.731 backlinks, 1.320 dominios, rank 276, `backlinks_spam_score` 48 (a revisar), primera detección 2025-08-22. Sin comparación con competidores. |

On-page score de la API: 85,27 para ambas páginas rastreadas.

---

## 7. AUDITORÍA E-E-A-T

Puntuación 0–3 sobre lo que **se pudo observar**; "N/D" donde no hay evidencia.

| Pilar | Señal | Punt. | Evidencia |
|---|---|---|---|
| Experience | Fotos/vídeos propios | N/D | 31 imágenes en home, sin `alt`; no verificable si son renders o fotos reales |
| Experience | Visitas/casos de cierre | 0 | no hay evidencia |
| Expertise | Autor con bio | 0 | ausente en home y `/ubicacion/` |
| Expertise | Licencia de corredor | N/D | no visible en lo rastreado |
| Expertise | Revisión legal de temas fiscales/compra | 0 | no hay contenido de ese tipo en la web |
| Authoritativeness | Respaldo de GLP | 2 | las IA lo atribuyen a GLP; la home dice "desarrollado por" |
| Authoritativeness | Menciones/backlinks | 1 | 1.320 dominios, pero calidad no evaluada, spam score 48 |
| Trust | Datos de empresa (razón social, RUC, dirección) | N/D | no verificado |
| Trust | Calidad editorial | 1 | erratas en H2, H1 en italiano, OG title "Inicio" |
| Trust | Precios y fechas con fuente y vigencia | 0 | datos de IA inconsistentes, la web no los publica de forma citable |

### Qué debe aportar el cliente (sin esto no se redacta)

1. Lista oficial de **precios, tipologías y fechas de entrega**, con fecha de vigencia.
2. Razón social, RUC, dirección, teléfono y **número de licencia** del corredor/promotora.
3. Nombres, cargos y bio de **autores y revisores** (abogado/notario para legal; contador para fiscal).
4. **Fotos y vídeos propios** de obra, zona y unidad piloto; etiquetar los renders.
5. Casos reales de clientes o hitos de obra **que se puedan demostrar**.
6. Datos de plan de pagos y condiciones de preventa, y su respaldo legal (fiduciario, garantías).
7. Acceso a **Search Console** y al `robots.txt` / `llms.txt` / sitemap para cerrar los N/D.
8. Decisión sobre qué contenido vive en `glp.com.pa` y cuál en la web de Bosco.

---

## 8. MAPA DE CONTENIDO (16 piezas)

Convenciones: **AEO** = respuesta directa de 40–60 palabras bajo un H2 en forma de pregunta; **GEO** = hecho + fuente + fecha; **Insumo** = lo que hay que pedir antes de redactar. Todas llevan autor y revisor nombrados y fecha de revisión. Volúmenes y tendencias de §4; "N/D" = sin volumen medible.

### Pilar A — Entidad y zona (prioridad 1)

| # | Pieza | Keyword / dato | Formato / bloque AEO-GEO | Insumo |
|---|---|---|---|---|
| 1 | **Qué es Bosco di Santa María** (página de entidad) | `bosco di santa maria` 390/mes; Claude no lo conoce | Definición en 1 frase; tabla de datos (ubicación, promotora, nº de torres, entrega con fecha); `Organization` + `RealEstateAgent` + `sameAs` a GLP; aclarar que **no es Urbanización Don Bosco** | datos oficiales del proyecto |
| 2 | **Santa María Golf & Country Club: guía para quien quiere vivir ahí** | `santa maria golf and country club` ~1.009/mes, +1.011 % | Responder PAA ("¿Dónde queda?", "¿Qué hay dentro?"); **no** publicar costo de membresía sin fuente del club | datos y permiso del club |
| 3 | **Vivir e invertir en Santa María Norte** (hub de zona) | `santa maria panama` (pos. >20), PAA de zona | Transporte, servicios, riesgos, precios; enlaza a todo | datos propios de zona |
| 4 | **Proyectos de apartamentos nuevos en Santa María: comparativa** | prompt de IA donde ChatGPT/Gemini ya te nombran; PAA "¿Qué proyectos hay en Santa María?" | Tabla comparativa honesta (incluye rivales); se actualiza trimestralmente | datos públicos de rivales |
| 5 | **Santa María vs Costa del Este: dónde comprar** | `costa del este panamá` 1.375/mes; `vivir en costa del este` +60 % | Tabla de decisión; 8/12 prompts de IA no te nombran aquí | datos de precios por m² con fuente |

### Pilar B — Proceso de compra (extranjeros), con fuente oficial

| # | Pieza | Keyword / dato | Notas | Insumo |
|---|---|---|---|---|
| 6 | **Buy an apartment in Panama as a foreigner: step by step** (EN) | `buy apartment in panama` 90/mes, +64 %, **Emergente** · PAA "Can a foreigner purchase property in Panama?" | AEO sobre PAA; GEO con enlace a fuentes oficiales; marcar `verificar con abogado` | revisor legal |
| 7 | **Cómo comprar un apartamento en preventa en Panamá siendo extranjero** (ES) | N/D volumen; aparece en prompts de IA | versión ES de la anterior; no copiar | revisor legal |
| 8 | **Gastos de cierre e impuestos al comprar** | N/D; `dgi.mef.gob.pa` es citada 13 veces | **todas las cifras con enlace a DGI/Registro Público y fecha**; no usar cifras de memoria | revisor fiscal |
| 9 | **Preventa vs apartamento listo** | N/D | árbol de decisión; riesgos reales de preventa | datos del fideicomiso |
| 10 | **Plan de pagos de preventa en Bosco** | N/D | tabla con porcentajes y fechas **vigentes** | condiciones oficiales |

### Pilar C — Producto

| # | Pieza | Keyword / dato | Notas | Insumo |
|---|---|---|---|---|
| 11 | **Golf course condos in Panama** (reforzar la existente) | AIO ya cita la web; pos. 13 | añadir tabla comparativa, fecha, FAQ visible, `VideoObject` | datos y fotos propias |
| 12 | **Apartamentos con vista al golf en Panamá** (ES) | N/D; AIO presente | versión ES; hoy no rankea | fotos de vista reales |
| 13 | **Páginas por tipología** (2, 3, 4 recámaras, penthouse) | N/D | una URL por tipología, H1 con tipo + zona + m², `Product`+`Offer` | planos, m², precios |
| 14 | **Precios y fechas vigentes** (página de datos citable) | hueco detectado: las IA dan cifras distintas | tabla HTML con fecha de actualización | lista oficial |

### Pilar D — Datos propios y AEO

| # | Pieza | Notas | Insumo |
|---|---|---|---|
| 15 | **Informe trimestral de mercado de Santa María** | solo con datos propios y fuentes; activo citable por LLMs | datos de ventas/precios reales |
| 16 | **Hub de preguntas frecuentes** (una pregunta = un H2) | preguntas de PAA reales de §5.1; `FAQPage` solo con FAQ visibles | respuestas verificadas |

**No perseguir sin inventario propio:** `casas en venta costa del este` (108/mes, +21 %) y `casas en venta panamá` son las keywords transaccionales más fuertes de la lista, pero son de **otra oferta**. Solo tienen sentido si el cliente vende casas ahí; si no, se capturan indirectamente con la pieza 5.

---

## 9. PLAN DE 90 DÍAS

Ordenado por impacto ÷ esfuerzo. Responsable orientativo.

| # | Acción | Cuándo | Métrica | Insumo pendiente |
|---|---|---|---|---|
| 1 | Dar acceso a Search Console y compartir `robots.txt`, `llms.txt`, sitemap; **cerrar los N/D** | Sem. 1 | indexación conocida; bots de IA permitidos | cliente |
| 2 | Corregir H1/H2 (italiano → español con keyword), erratas, title, `og:title`, metas duplicadas, `alt` en 31 imágenes | Sem. 1–2 | flags de `instant_pages` en verde | — |
| 3 | Publicar la **página de precios y fechas vigentes** (pieza 14) | Sem. 2 | las IA dejan de dar cifras contradictorias | lista oficial |
| 4 | Implementar schema: `Organization`, `RealEstateAgent`, `BreadcrumbList`, `Product`+`Offer` | Sem. 2–3 | `has_micromarkup` verdadero, resultados enriquecidos válidos | datos de empresa |
| 5 | Página de entidad (pieza 1) + enlaces cruzados con `glp.com.pa` | Sem. 3 | Claude/Perplexity describen la marca sin errores | datos oficiales |
| 6 | Reducir TTFB (2,9 s) y LCP; quitar recursos que bloquean el render | Sem. 3–5 | LCP < 2,5 s en Lighthouse | desarrollo web |
| 7 | Pilar A: piezas 2, 3, 4, 5 | Sem. 4–8 | `santa maria golf and country club` de pos. 21 a top 10; Bosco citado en prompts de zona | datos de zona |
| 8 | Pilar B: piezas 6–8 con revisor legal | Sem. 5–10 | aparición en PAA de extranjeros; `cita/3` en ChatGPT/Perplexity | revisor |
| 9 | Reforzar `/golf-course-condos-panama/` (pieza 11) y crear la versión ES (12) | Sem. 6–8 | mantener cita en AIO; subir de pos. 13 | fotos/datos |
| 10 | Páginas por tipología (pieza 13) | Sem. 8–10 | URL por tipología indexada | planos |
| 11 | Decidir reparto de contenido entre `glp.com.pa` y Bosco para evitar canibalización | Sem. 2 | sin duplicados | cliente |
| 12 | **Repetir esta batería de LLM y las 11 SERPs** a los 30 y 90 días y comparar con esta línea base | Sem. 4, 12 | menciones sin marca > 22 % (ChatGPT) y > 0 en Perplexity | — |

---

## 10. LIMITACIONES

- **No pude abrir el sitio** desde este entorno (política de red). Todo lo on-page proviene de `instant_pages` de DataForSEO y cubre solo la home y `/ubicacion/`. Para completar la auditoría de las demás URLs hay que **permitir `boscodisantamaria.com` en el acceso de red del entorno** (Edit del entorno → Network access → Allowed domains) o pasar capturas/exportación.
- **Sin contenido de `robots.txt`, `llms.txt`, sitemap, schema del resto de páginas ni hreflang.**
- **Volumen de búsqueda:** casi todas las búsquedas informativas y de proceso son N/D en Google Ads para Panamá. Eso limita la priorización de los pilares B y D; se han incluido porque aparecen en PAA y en respuestas de IA.
- **Google Trends** devolvió 0 para `santa maria golf & country club`, en contradicción con Ads/Labs.
- **AI Overview:** en 2 SERPs se detectó el bloque pero sin fuentes devueltas; 1 SERP falló (`cómo comprar un apartamento en panamá`).
- **Gemini:** los enlaces llegan como redirecciones `vertexaisearch`; no se puede confirmar si cita tu dominio. El 0 de citas de Gemini es "no verificable", no "no cita".
- **Claude se midió sin búsqueda web**; no es comparable con los otros tres en citas.
- **SERP solo en desktop**, sin móvil ni grid local.
- **Backlinks de competidores, Core Web Vitals de campo y fichas/URLs indexadas: no medidos.**
- **Afirmaciones legales/fiscales:** este informe no contiene ninguna cifra legal. Cualquier pieza de los pilares B debe redactarse con fuente oficial y revisión de abogado.
- **Datos del proyecto** (precios, fechas, número de torres) provienen de respuestas de IA y **no están verificados** contra el cliente.
