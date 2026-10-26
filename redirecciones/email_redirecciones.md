**Asunto:** xuss.co – Plan de redirecciones 301 (VTEX → Shopify): qué hacer con el Excel

Hola,

Te comparto el análisis de las URLs antiguas de xuss.co (Search Console + Analytics) cruzado con el crawl de Screaming Frog del sitio nuevo. El sitio anterior era VTEX (`/slug/p`, filtros por talla y color) y el nuevo es Shopify (`/products/`, `/collections/`), así que casi ninguna URL antigua existe igual hoy: de 15.4k rutas, solo 2 coinciden. Sin redirecciones se pierde el tráfico y el posicionamiento histórico.

**Archivos adjuntos**
1. `xuss_redirecciones.xlsx`: análisis completo.
2. `shopify_redirects_alta_media.csv`: 8.729 redirecciones listas para importar.
3. `shopify_redirects_baja_revisar.csv`: 3.242 redirecciones de confianza baja (revisar antes de importar).

**Qué hacer, paso a paso**

1. **Crear lo que falta en Shopify (antes de importar).** Hoja "Colecciones a crear". Lo más importante por tráfico:
   - `/terceras-prendas`: 204k vistas y no existe colección.
   - `/capas-y-kimonos`: 191 clics.
   - `/black-friday` y `/ultimas-tallas`: 112k vistas; hoy apuntan a hot-sale como solución temporal.
   - `/mas-vendidos`: 5k vistas.
   - Gift card (`/bono-regalo`): 46 clics.
   - Opcional: colecciones propias para collares, aretes, anillos, pulseras y blazers.
   Cuando exista cada una, cambia su destino en el CSV (columna "Redirect to") antes de importar.

2. **Confirmar dos decisiones.**
   - `/sale` → `/collections/hot-sale` (392 clics y 1,9M de vistas). ¿Hot Sale cumple el mismo rol que SALE?
   - Qué hacer con productos descontinuados: hoy van a su colección. Alternativa: 410.

3. **Importar el CSV "alta_media".** Shopify Admin → Contenido → Menús → Redirecciones de URL (en versiones recientes: Configuración → Navegación → Redirecciones) → Importar. Son 8.729 filas con columnas `Redirect from` / `Redirect to`.

4. **Revisar el CSV "baja_revisar".** Son productos que ya no existen, filtros de talla/color y categorías padre antiguas. Corrige a mano los que tengan sentido y descarta los de tráfico mínimo (la hoja "Todo" incluye clics y vistas para priorizar). Luego impórtalo.

5. **No redirigir** las URLs de la hoja "Ignorar" (`/checkout`, `/login`, `/account`).

6. **Verificar después de importar.**
   - Probar a mano las 25 URLs con más tráfico (hoja "Redirecciones 301", ordenada por clics y vistas).
   - Rastrear de nuevo con Screaming Frog (modo lista con las URLs antiguas) y confirmar que todas dan 301 → 200 y no hay cadenas ni bucles.
   - En Search Console, vigilar durante 4–8 semanas los informes de Páginas (404 y "Redirección") y el tráfico de las URLs principales.

**Cómo leer el Excel**
- *Resumen*: cuántas URLs hay por tipo y acción.
- *Redirecciones 301*: origen, destino propuesto, confianza (Alta/Media/Baja), nota y tráfico. Ordenada por importancia.
- *Sin equivalente*: URLs sin destino claro; requieren decisión.
- *Colecciones a crear*: lo que hay que construir en Shopify.
- *Ignorar* y *Todo*: referencia completa.

**Ojo**
- No pude verificar el sitio en vivo; todo sale de los Excel (GSC, GA4 y el crawl).
- Las URLs con espacios, tildes o errores (`/pantalón mujer`, `blusas-y--camisas`, `chalechos`) están normalizadas; Shopify puede requerir codificarlas al importar.
- Todo el análisis también está en el PR: https://github.com/mejiajk/mejia/pull/9

Quedo atento para resolver dudas o ajustar los destinos.

Saludos,
