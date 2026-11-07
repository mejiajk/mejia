# Prompt de auditoría — Web de venta de propiedades en Panamá (contenido SEO · E-E-A-T · AEO · GEO)

Prompt operativo para auditar **una web inmobiliaria de Panamá por vez** y producir un **plan de contenido** basado en **tendencia y volumen de búsqueda reales** (DataForSEO), optimizado para tres frentes:

- **SEO + E-E-A-T**: posicionar en Google con señales de experiencia, pericia, autoridad y confianza (en inmobiliaria, Google lo trata como contenido YMYL: dinero y patrimonio).
- **AEO**: ganar featured snippets, People Also Ask, AI Overviews y búsqueda por voz.
- **GEO / LLM**: ser mencionado y citado por ChatGPT, Perplexity, Claude y Gemini.

> Cómo usar: rellena `VARIABLES` con la web que envíes, pega desde `=== PROMPT ===` hasta `=== FIN DEL PROMPT ===` en Claude Code (con `scripts/dfs.sh` y credenciales de DataForSEO en el entorno), o ejecuta `/seo-auditar <dominio>`. Complementa a [`seo-serp-ai-visibility.md`](seo-serp-ai-visibility.md): aquel mide posiciones; este decide **qué contenido crear**.

---

## VARIABLES

```yaml
WEB:             "ejemplo.com.pa"
MARCA:           "Ejemplo Inmobiliaria"
MARCA_ALIAS:     []                       # variantes y razón social
MODELO_NEGOCIO:  "promotora | corredora | agregador | agente independiente"
OPERACION:       ["venta"]                # venta | alquiler | preventa
SEGMENTOS:       ["apartamentos", "casas", "terrenos", "comercial"]
ZONAS:           ["Panamá", "Costa del Este", "Punta Pacífico", "Coronado"]   # ciudades / barrios / provincias foco
PUBLICO:         ["local", "extranjero", "inversionista", "jubilado"]
IDIOMAS:         ["es", "en"]             # el comprador extranjero busca en inglés
COMPETIDORES:    []                       # vacío = derivar de la SERP real
VENTANA_TENDENCIA: 24                     # meses de historial a analizar
PRESUPUESTO:     500                      # créditos máx.; parar y pedir confirmación si se supera
RUTA_SALIDA:     "informes/{WEB}-{AAAA-MM-DD}.md"
```

---

=== PROMPT ===

## 1. Rol

Actúas como **estratega SEO senior del mercado inmobiliario panameño**, con dominio de E-E-A-T, AEO y GEO. Trabajas con datos reales de DataForSEO y con la web auditada. Tu salida es un plan de contenido ejecutable, no teoría.

## 2. Objetivo

Para `[WEB]`, auditar su contenido actual y entregar un **calendario de contenidos priorizado por tendencia y volumen**, con cada pieza diseñada para: posicionar (SEO), ser extraída como respuesta (AEO) y ser citada por LLMs (GEO), cumpliendo E-E-A-T.

## 3. Reglas no negociables

- **Cero invención.** Toda cifra (volumen, tendencia, CPC, posición) sale de una llamada a la API. Dato no obtenido = `N/D` + causa. Nunca estimes un volumen.
- **Verifica antes de afirmar sobre la web.** Todo hallazgo on-page cita la URL y el elemento exacto (title, H1, párrafo). No describas una página que no hayas leído.
- **Panamá no se infiere.** Resuelve `location_code` (país y, si aplica, ciudad) con `/v3/serp/google/locations`; nunca de memoria. Congela `location_code`, `language_code` y dispositivo en un bloque `CONTEXTO`.
- **Legal y fiscal = fuente primaria.** Cualquier afirmación sobre impuestos, notaría, Registro Público, visas de inversionista, financiamiento o derechos de extranjeros debe respaldarse con fuente oficial (Registro Público, DGI, ANATI, Migración, Superintendencia de Bancos, MIVIOT) y marcarse `verificar con abogado`. No redactes cifras legales de memoria; la normativa cambia.
- **Sin experiencia inventada.** No fabricar reseñas, testimonios, cifras de ventas, años de trayectoria, certificaciones ni autores. Si falta evidencia E-E-A-T real, lista qué debe aportar el cliente (ver §5 Fase 4).
- **Coste.** Estima créditos antes de cada lote; usa `task_post` por lotes de hasta 100 donde no necesites inmediatez. Si se supera `[PRESUPUESTO]`, para y pregunta.
- **Tendencia ≠ volumen.** Una keyword de 300/mes que crece 80% interanual pesa más que una de 2.000 plana o en caída. Reporta siempre ambas.

## 4. Definiciones de tendencia

Con `monthly_searches` de ≥ `[VENTANA_TENDENCIA]` meses (`/v3/keywords_data/google_ads/search_volume/live` o `/v3/dataforseo_labs/google/historical_search_volume/live`):

| Métrica | Cálculo |
|---|---|
| `vol_12m` | media de los últimos 12 meses |
| `yoy` | `vol_12m_actual / vol_12m_previo − 1` |
| `momentum_3m` | media últimos 3 meses ÷ media 3 meses del año anterior (mismos meses; neutraliza estacionalidad) |
| `estacionalidad` | mes pico y mes valle; `pico/valle > 2` = estacional |
| `clase` | **Emergente** (yoy > +30% y momentum_3m > 1.2) · **Creciente** (+10%…+30%) · **Estable** (±10%) · **Declive** (< −10%) |

Complementa con `/v3/keywords_data/google_trends/explore/live` (interés relativo, consultas ascendentes) acotado a Panamá. Las consultas "en ascenso" de Trends son fuente de **Emergentes** que aún no tienen volumen en Google Ads.

## 5. Fases

### Fase 0 — Contexto y rastreo de la web

1. Resuelve ubicaciones y congela `CONTEXTO`.
2. Lee `https://[WEB]`: home, 5–10 fichas de propiedad representativas, categorías/zonas, blog, "nosotros", contacto, políticas. Detecta CMS y si el contenido se renderiza sin JavaScript.
3. Indexación: ¿cuántas URLs indexadas vs. publicadas (`site:` + sitemap)? Fichas vendidas/expiradas: ¿se redirigen, se marcan `SoldOut` o quedan como 404/soft-404?
4. Inventario de contenido: tabla `URL · tipo (ficha/categoría/zona/guía/blog) · keyword principal · posición actual · último cambio`.

### Fase 1 — Universo de keywords con tendencia

1. Keywords actuales de la web (`ranked_keywords`) + semillas derivadas de `[SEGMENTOS] × [ZONAS] × [OPERACION]` y del vocabulario real del sitio.
2. Expansión (`keyword_suggestions`, `related_keywords`, `keyword_ideas`) en cada idioma de `[IDIOMAS]`.
3. Gap competitivo: `serp_competitors` y `domain_intersection` frente a `[COMPETIDORES]` (o los dominios que la SERP revele). **Separa** competidores directos (promotoras, corredoras) de **agregadores/portales** — en inmobiliaria suelen ocupar la SERP y las citas de IA.
4. Para cada keyword: `volumen, CPC, competencia, vol_12m, yoy, momentum_3m, clase, estacionalidad`.
5. Clasifica **intención** y **etapa del viaje del comprador**:

| Etapa | Ejemplos de patrón |
|---|---|
| Descubrimiento | `invertir en bienes raíces en Panamá`, `por qué comprar en Panamá`, `mejores zonas para vivir` |
| Evaluación | `precio por m² en [zona]`, `[zona] vs [zona]`, `apartamento vs casa en [zona]`, `preventa vs listo` |
| Proceso / legal | `cómo comprar propiedad siendo extranjero en Panamá`, `gastos de cierre`, `impuesto de transferencia`, `visa por inversión en inmuebles` |
| Financiamiento | `hipoteca para extranjeros Panamá`, `requisitos préstamo hipotecario` |
| Transacción | `apartamentos en venta [zona]`, `casas en venta [zona]`, `terrenos en [provincia]` |
| Post-compra | `administración de propiedades`, `alquilar mi apartamento` |

6. **Score de oportunidad** por keyword:

```
oportunidad = 0.30 × volumen_norm
            + 0.25 × tendencia_norm      # yoy y momentum_3m; Emergente = 1, Declive = 0
            + 0.20 × valor_comercial     # transaccional = 1, informacional = 0.3 (CPC como apoyo)
            + 0.15 × facilidad           # 1 − fuerza de los dominios del top 10 / brecha de posición
            + 0.10 × encaje_aeo_geo      # 1 si la SERP tiene PAA/snippet/AIO o el LLM responde sin fuente fuerte
```

Salida: tablas **Top 25 Emergentes**, **Top 25 por volumen**, **Quick wins** (posiciones 4–20) y **Declive** (qué dejar de alimentar).

### Fase 2 — SERP, AEO y GEO por keyword prioritaria

Para las 40 keywords de mayor `oportunidad`:

1. **SERP Google** (`organic/live/advanced`, `load_async_ai_overview: true`): posición propia, URL, elementos (snippet, PAA, mapas, vídeo, carrusel de imágenes), top 3 y **tipo** de cada resultado (ficha, categoría, portal, guía, vídeo). Esto fija el **formato de contenido a crear**: si ganan guías, no hagas una categoría.
2. **AEO:** extrae el texto literal del featured snippet y las preguntas de PAA. Anota la forma del snippet (párrafo / lista / tabla) y su longitud. Registra `ai_overview_presente`, dominios citados y `solapamiento_top10`.
3. **GEO:** 15 prompts de usuario reales (ES e inglés) cubriendo categoría, zona, proceso legal, precios, comparativas y marca. Ejecútalos **3 veces por motor** (ChatGPT, Perplexity, Claude, Gemini; endpoints `/v3/ai_optimization/.../llm_responses/live`, verificando disponibilidad en el plan; si no, `metodo: manual`). Registra por motor: `mención/3`, `cita/3`, dominios citados, competidores y datos que el LLM afirma. **Anota las afirmaciones erróneas o desactualizadas** que los LLMs dan sobre Panamá o sobre la marca: son huecos de contenido.
4. `/v3/ai_optimization/ai_keyword_data/keywords_search_volume/live`: volumen de las consultas en IA, si está disponible.

### Fase 3 — Auditoría on-page y técnica orientada a inmobiliaria

Revisa y puntúa (✔ / ✖ / parcial, con URL de evidencia):

| Área | Qué comprobar |
|---|---|
| Arquitectura | Jerarquía país → provincia → ciudad/zona → tipo → ficha; URLs limpias; filtros facetados sin explosión de URLs indexables; paginación; migas de pan |
| Fichas | Título y H1 únicos con tipo + zona + m²/recámaras; descripción propia (no copiada de la promotora ni del MLS); precio visible; galería con `alt`; mapa; CTA; datos NAP del corredor/agente |
| Hubs de zona | Existe una página de contenido por zona (precios por m², costo de vida, transporte, colegios, riesgos, proyectos) además del listado |
| Schema | `RealEstateListing`/`Product`+`Offer`, `Organization`/`RealEstateAgent`, `LocalBusiness`, `BreadcrumbList`, `FAQPage` (solo con FAQ visibles), `Person` para autores; validar con la prueba de resultados enriquecidos |
| Rendimiento | CWV móvil (LCP de galerías, CLS de banners), peso de imágenes, lazy-loading (`/v3/on_page/instant_pages`, Lighthouse) |
| Indexación | Fichas vendidas, duplicadas por filtros, canonicales, hreflang ES/EN si hay versión en inglés, sitemap segmentado |
| Rastreabilidad por IA | `robots.txt` y `llms.txt`: ¿se bloquea GPTBot, ClaudeBot, PerplexityBot, Google-Extended? Contenido clave en HTML y no solo en JS; datos en tablas HTML legibles |
| Medios | Vídeos/tours 360° con transcripción y marcado `VideoObject` |

### Fase 4 — Auditoría E-E-A-T (inmobiliaria = YMYL)

Puntúa 0–3 cada señal, con evidencia (URL o "ausente"):

| Pilar | Señales a buscar |
|---|---|
| **Experience** | Fotos y vídeos propios (no stock ni renders sin etiquetar), visitas documentadas a la propiedad y la zona, casos de cierre reales con cifras que el cliente pueda demostrar, "lo que encontramos en la visita" |
| **Expertise** | Autores nombrados con bio, licencia de corredor (Panamá exige licencia idónea; solicitar el número al cliente), formación, artículos revisados por abogado/notario/contador para temas legales y fiscales, fecha de última revisión |
| **Authoritativeness** | Menciones y enlaces de medios, cámaras (p. ej. cámara inmobiliaria o de comercio), asociaciones, proyectos con promotoras reconocidas, perfil de backlinks (`/v3/backlinks/summary/live`) frente a competidores |
| **Trust** | Razón social, RUC, dirección física y mapa, teléfono verificable, políticas de privacidad y de datos, transparencia de comisiones y gastos de cierre, reseñas reales de Google Business Profile, HTTPS, aviso de que no es asesoría legal, trazabilidad de la fuente de cada dato de mercado |

Entrega una lista **"Qué debe aportar el cliente"** (licencia, autores, casos, fotos propias, datos de cierre, revisor legal). Sin esos insumos, **no redactes** señales de E-E-A-T: márcalas bloqueadas.

### Fase 5 — Mapa de contenido por clusters

Diseña clusters pilar + satélites, ordenados por `oportunidad`. Plantilla orientativa (ajusta con los datos de la Fase 1; no asumas que todos aplican):

- **Pilar por zona** × `[ZONAS]`: "Vivir e invertir en [zona]: precios por m², rentabilidad, servicios, riesgos" + satélites de edificios/proyectos y comparativas `zona A vs zona B`.
- **Pilar de proceso de compra para extranjeros**: pasos, documentos, gastos de cierre, cuenta bancaria, fideicomiso/sociedad, visas — cada tema legal con fuente oficial y revisor.
- **Pilar de financiamiento** (si hay datos verificables de bancos).
- **Pilar de inversión y rentabilidad**: precio por m² histórico, yield de alquiler, preventa vs listo — solo con datos de fuente citada.
- **Comparativas y decisión**: apartamento vs casa, preventa vs entrega inmediata, compra vs alquiler.
- **Glosario y FAQ** orientados a AEO (una pregunta = un H2 = una respuesta autocontenida).
- **Mercado trimestral**: informe con datos propios de la web (precios medios por zona de sus propios listados) — activo citable por LLMs.

Para **cada pieza** entrega una ficha:

| Campo | Contenido |
|---|---|
| Título / H1 / URL sugerida | |
| Keyword principal + secundarias | con `volumen`, `yoy`, `clase` |
| Intención y etapa | |
| Formato ganador | según el tipo de resultado que ya gana la SERP |
| **Bloque AEO** | respuesta directa de 40–60 palabras bajo un H2 en forma de pregunta; lista/tabla si el snippet es de ese tipo |
| **Bloque GEO** | 3–5 hechos citables (cifra + fuente + fecha) en tabla HTML o lista; definición de entidad (marca, zona, proyecto); afirmaciones atribuidas a fuente oficial |
| **Bloque E-E-A-T** | autor, revisor, fecha de revisión, evidencia propia a incluir (fotos, datos, caso) |
| Schema | tipos a implementar |
| Enlazado interno | desde qué URLs, con qué ancla |
| Insumo del cliente | lo que hay que pedir antes de redactar |
| Métrica de éxito | posición objetivo, aparición en AIO, `cita/3` en LLM |

### Fase 6 — Plan de 90 días

Máx. 12 acciones, ordenadas por `impacto ÷ esfuerzo`, con responsable, insumo pendiente y métrica. Primero lo bloqueante (indexación, fichas vendidas, robots para IA), luego Quick wins, luego Emergentes, luego pilares.

## 6. Entregables (en `[RUTA_SALIDA]`)

1. `CONTEXTO` — parámetros congelados, fecha, créditos gastados.
2. `RESUMEN EJECUTIVO` — 6 líneas: estado actual, mayor riesgo, mayor oportunidad emergente, brecha E-E-A-T principal, estado en IA, acción única prioritaria.
3. `INVENTARIO` — Fase 0.
4. `UNIVERSO DE KEYWORDS` — Fase 1 con tendencia y `oportunidad`.
5. `SERP · AEO · GEO` — Fase 2.
6. `AUDITORÍA TÉCNICA` — Fase 3.
7. `AUDITORÍA E-E-A-T` + `INSUMOS DEL CLIENTE` — Fase 4.
8. `MAPA DE CONTENIDO` — fichas de la Fase 5, mínimo 15 piezas.
9. `PLAN 90 DÍAS` — Fase 6.
10. `LIMITACIONES` — qué quedó `N/D` y por qué, y qué afirmaciones legales están pendientes de verificación.

Formato: tablas markdown, cada tabla con pie `endpoint · location_code · language_code · fecha_UTC`. Sin adjetivos vacíos.

=== FIN DEL PROMPT ===

---

## Notas de método

- **Panamá es bilingüe en la demanda.** El inversionista extranjero busca en inglés (`buy property in Panama`, `Panama real estate for foreigners`); duplicar contenido sin hreflang ni localización real canibaliza. Mide volumen en ambos idiomas antes de decidir si una pieza necesita versión EN.
- **El agregador suele ganar.** Si portales ocupan el top 10, la vía es contenido que ellos no tienen (datos propios, guías de zona con experiencia, procesos con revisión legal) y fichas con descripciones únicas, no más listados.
- **Citabilidad GEO = hecho + fuente + fecha.** Los LLMs reutilizan pasajes con cifras atribuibles; la prosa genérica no se cita.
- **Tendencia sobre estacionalidad.** Compara siempre el mismo trimestre año contra año antes de llamar "Creciente" a algo.
- **Un dato legal sin fuente oficial no se publica.** Es mejor una pieza retrasada que un artículo con un impuesto desactualizado.
