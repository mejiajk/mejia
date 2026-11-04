# Biblioteca de prompts para diversificar el contenido de GLP Panama Residency

Cómo usarla: copia el **prompt base** una sola vez al inicio de cada conversación con la IA, y luego pega el prompt del formato que necesites. Reemplaza las variables entre `{llaves}`.

---

## 0. Prompt base (pegar primero siempre)

```
Actúa como estratega de contenido SEO, AEO y GEO y redactor especializado en inmigración e inversión inmobiliaria en Panamá.

Marca: GLP Panama Residency (glppanamaresidency.com). Programa principal: residencia permanente por Inversionista Calificado. Rutas relacionadas: Países Amigos y Pensionado.
Público: extranjeros de EE. UU., Canadá, Reino Unido, Europa y Latinoamérica que quieren residir, invertir o jubilarse en Panamá.
Tono: profesional, claro, cercano y prudente. Nunca prometas aprobación garantizada ni plazos fijos.

Reglas obligatorias:
1. No inventes cifras, leyes ni plazos. Si un dato cambia por decreto o las fuentes discrepan, dilo y escribe "verificar con Migración o abogado idóneo".
2. Atribuye cada dato a su fuente cuando exista (decreto, entidad oficial o firma).
3. Incluye al final: autor "[Nombre]", revisión legal "[Abogado idóneo, N.º de idoneidad]" y la fecha de actualización.
4. Añade el aviso: "Contenido informativo, no constituye asesoría legal, fiscal ni de inversión."
5. Responde primero con la respuesta directa (40 a 60 palabras) y luego desarrolla.
6. Evita relleno, frases genéricas y repetir lo que ya dicen los competidores; aporta un ángulo propio.
```

---

## A. Artículos de blog (variantes de formato)

### A1. Guía larga (pilar)

```
Escribe una guía de {1800-2200} palabras sobre "{keyword principal}" en {español/inglés}.
Entrega: title (60 caracteres o menos), meta description (150-158 caracteres), slug, H1, TL;DR de 7-9 puntos, H2/H3 con preguntas reales, una tabla comparativa, errores comunes, sección "Cómo verificamos esta información" y 6 preguntas frecuentes con respuesta directa.
Incluye 5 enlaces internos sugeridos a artículos satélite: {lista}.
```

### A2. Artículo comparativo

```
Compara "{opción A}" vs "{opción B}" para {perfil de lector}.
Formato: tabla de 8 criterios (base legal, requisito, capital, estatus, velocidad, riesgos, ideal para, límites), veredicto por perfil (si eres X elige A; si eres Y elige B) y 5 preguntas frecuentes.
Sé neutral y señala lo que debe verificarse.
```

### A3. Artículo por nacionalidad

```
Escribe una guía de residencia en Panamá para ciudadanos de {país}.
Incluye: rutas disponibles (verificando si {país} figura en Países Amigos), documentos específicos del país y cómo apostillarlos (autoridad y procedimiento), puntos fiscales de salida de {país}, riesgos y 6 preguntas frecuentes propias de esa nacionalidad.
No asumas elegibilidad: indica cómo verificarla.
```

### A4. Artículo por intención de problema

```
Escribe un artículo que resuelva este problema: "{problema, p. ej. mi trámite se retrasó, me piden más documentos, mi país no está en la lista}".
Estructura: síntomas, causas más comunes, qué hacer paso a paso, qué NO hacer, cuándo contratar a un abogado y checklist final.
```

### A5. Caso de estudio (con datos reales de GLP)

```
Con estos datos reales de un cliente (anonimizados): {perfil, nacionalidad, objetivo, ruta elegida, tiempos reales, dificultades, resultado}, redacta un caso de estudio de 900 palabras.
Estructura: situación, decisión, proceso, obstáculos, resultado, lecciones y aviso de que cada caso es distinto.
No inventes ningún dato que no esté en la información que te di.
```

---

## B. Contenido para AEO (respuestas directas)

### B1. Banco de respuestas cortas

```
Genera 30 preguntas reales que una persona haría sobre {tema}. Para cada una, escribe una respuesta de 40-60 palabras, autocontenida y citable por un buscador o asistente de IA, con la cifra y su fuente si existe, o "verificar" si no hay dato firme.
Entrega en tabla: pregunta | respuesta | intención (informativa/comercial) | página sugerida.
```

### B2. Glosario

```
Crea un glosario de 40 términos de inmigración y residencia en Panamá (p. ej. apostilla, idoneidad, residente permanente, Países Amigos, vínculo económico, carné de residente).
Para cada término: definición de 25-40 palabras, ejemplo práctico y enlace sugerido a un artículo relacionado.
```

### B3. Datos estructurados

```
Genera el marcado JSON-LD para esta página: {pegar texto}. Incluye Article, FAQPage con las preguntas del texto y, si aplica, HowTo. Valida que cada respuesta coincida exactamente con el contenido visible.
```

---

## C. Contenido para GEO (que las IA te citen)

### C1. Estudio con datos propios

```
Diseña una encuesta de 12 preguntas para clientes y prospectos de GLP sobre su experiencia con la residencia en Panamá (motivaciones, presupuesto, dudas, tiempos reales, obstáculos).
Luego, con los resultados que te pegaré: {datos}, redacta un informe de 1.000 palabras con 5 hallazgos citables, una tabla y una infografía en texto. No inventes cifras.
```

### C2. Página "Hechos clave" (fuente citable)

```
Crea una página de "Hechos clave sobre la residencia en Panamá" con 25 afirmaciones concretas, cada una con: dato, fuente oficial, fecha de verificación y nivel de certeza (confirmado / reportado por firmas / discrepante).
```

### C3. Pasajes autocontenidos

```
Reescribe este texto en bloques de 80-120 palabras que se entiendan sin el contexto del resto de la página, cada uno bajo un encabezado con forma de pregunta. Mantén cifras, fechas y fuentes. Texto: {pegar}.
```

### C4. Prueba de visibilidad en IA

```
Actúa como un usuario que consulta un asistente de IA. Genera 25 consultas reales sobre residencia en Panamá (informativas, comparativas, de costo y de abogados) para medir cada mes si ChatGPT, Gemini, Perplexity y Copilot citan a glppanamaresidency.com.
Devuelve una tabla para registrar: consulta | asistente | ¿nos cita? | fuente citada | acción.
```

---

## D. Otros formatos y canales

### D1. Guion de video (YouTube o Shorts)

```
Escribe el guion de un video de {60 segundos / 6 minutos} sobre "{tema}".
Incluye: gancho de 5 segundos, desarrollo en 3-5 puntos, llamado a la acción, texto en pantalla, título (60 caracteres), descripción con palabras clave y 10 etiquetas. Evita promesas garantizadas.
```

### D2. Hilo de LinkedIn / X

```
Convierte este artículo en un hilo de 8 publicaciones para LinkedIn orientado a inversionistas: {pegar}.
Primera línea con gancho, un dato por publicación, lenguaje sencillo y cierre con pregunta para generar comentarios. Sin hashtags excesivos (máximo 3).
```

### D3. Publicaciones para Instagram o Facebook

```
Crea 10 ideas de publicaciones (carrusel, reel, mito vs realidad, checklist) sobre {tema}. Para cada una: formato, texto de cada lámina o escena, pie de foto de 40-60 palabras y llamado a la acción.
```

### D4. Boletín por correo

```
Redacta un boletín mensual de 400 palabras con: novedad normativa (a verificar), una pregunta del mes con respuesta, un caso breve, un enlace a un recurso y un llamado a agendar consulta. Asunto con 3 variantes A/B.
```

### D5. Imán de leads (checklist o e-book)

```
Crea un checklist descargable de "Documentos para tu residencia en Panamá según tu ruta" con casillas, plazos orientativos de apostilla y errores a evitar. Entrega el texto de la página de descarga, el correo de bienvenida y 3 correos de seguimiento.
```

### D6. Respuestas para foros (Reddit, expatriados, Quora)

```
Redacta una respuesta útil, honesta y no promocional a esta pregunta: "{pregunta de foro}".
Aporta pasos concretos, reconoce incertidumbres y cita fuentes. Menciona a GLP solo si es relevante y al final, de forma transparente.
```

### D7. Guion de presentación o webinar

```
Diseña un webinar de 45 minutos "Residencia en Panamá: qué ruta me conviene". Incluye agenda por minutos, 10 diapositivas con texto, 5 preguntas para interacción, sesión de preguntas frecuentes y un llamado a la acción suave.
```

---

## E. Planificación y mantenimiento

### E1. Calendario editorial de 6 meses

```
Con estas keywords: {lista} y este ritmo de {8-12} piezas al mes, crea un calendario de 6 meses.
Tabla: mes | semana | formato | keyword | intención | idioma | enlace interno | canal de difusión. Alterna español e inglés y varía formatos (guía, comparativa, caso, FAQ, video, boletín).
```

### E2. Brechas frente a competidores

```
Analiza estas URLs de competidores: {lista}. Identifica 20 temas que cubren y que nosotros no, 10 en los que podemos ser más profundos y 10 ángulos nuevos que nadie cubre bien. Devuelve prioridad por impacto y dificultad.
```

### E3. Reutilización (1 pieza → 8 formatos)

```
Toma este artículo: {pegar} y conviértelo en: 1 hilo de LinkedIn, 3 publicaciones cortas, 1 guion de video, 1 boletín, 5 preguntas para un banco de respuestas, 1 infografía en texto, 1 respuesta para foro y 3 títulos alternativos A/B.
```

### E4. Actualización de contenido existente

```
Revisa este artículo: {pegar} y devuelve: datos que deben verificarse (cifras, decretos, listas), secciones obsoletas, preguntas nuevas que añadir, mejoras de title y meta, y un resumen de cambios para mostrar como "Actualizado el {fecha}".
```

### E5. Control de calidad antes de publicar

```
Audita este borrador: {pegar}. Revisa: cifras sin fuente, promesas de aprobación o plazos garantizados, afirmaciones legales sin respaldo, canibalización con estas páginas {lista}, E-E-A-T (autor, revisor, fecha), longitud de title y meta, y claridad de la respuesta directa. Entrega una lista de correcciones priorizadas.
```

---

## Reglas de oro para todos los prompts

- Nunca publiques cifras o listas de países sin verificarlas con Migración o con un abogado idóneo.
- Añade siempre experiencia propia (casos, tiempos reales, fotos, testimonios con permiso). Es lo que la IA no puede inventar y lo que más pesa en E-E-A-T.
- Revisa cada pieza con una persona antes de publicar.
- Mide: Search Console para SEO, y la prueba mensual de consultas para AEO y GEO.
