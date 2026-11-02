# ♞ Ajedrez Cristal 3D

Tablero de ajedrez 3D interactivo con piezas de cristal originales. Un solo `index.html` (three.js por CDN, sin compilar).

**Diseño Vibe Coding por Ing. Hernán Quiroz**

## Qué incluye
- Piezas 3D facetadas con núcleo luminoso (cada tipo tiene su propia animación).
- Juega contra la IA (4 niveles), 2 jugadores en el mismo dispositivo, o en línea con un código de sala.
- Rotación 3D libre (arriba, abajo, izquierda, derecha, incluso por debajo del tablero), zoom, panel de flechas y teclado.
- Vista plana 2D con fichas y símbolos.
- Dibujo de estrategias sobre el tablero: lápiz libre, flechas y casillas marcadas. Funciona con dedo, mouse y lápiz óptico.
- Reglas completas: enroque, al paso, promoción, jaque mate, ahogado, 50 movimientos, repetición y material insuficiente.

## Publicar en GitHub Pages
1. Crea un repositorio y sube `index.html`.
2. En *Settings → Pages* elige la rama `main` y la carpeta `/ (root)`.
3. Tu tablero queda en `https://TU-USUARIO.github.io/TU-REPO/`.

Para incrustarlo en otra página:

```html
<iframe src="https://TU-USUARIO.github.io/TU-REPO/" width="100%" height="720"
        style="border:0" allow="fullscreen"></iframe>
```

## Desplegar en Streamlit
1. Sube al mismo repositorio `app.py`, `requirements.txt` e `index.html`.
2. En [share.streamlit.io](https://share.streamlit.io) elige *New app*, apunta al repositorio y usa `app.py` como archivo principal.
3. En local: `pip install -r requirements.txt` y `streamlit run app.py`.

## Notas
- Se necesita internet para cargar three.js (y PeerJS si usas el modo en línea).
- El modo en línea usa WebRTC con el servicio público de PeerJS: el anfitrión crea la sala y comparte el código de 5 letras.
- Si va lento en un dispositivo modesto, desactiva las sombras en el menú ☰.
