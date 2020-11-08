document.addEventListener('DOMContentLoaded', () => {
    /* Buscamos cada elemento svg con el atributo "src" */
    document.querySelectorAll('svg[data-src]').forEach(svg => {
      /* Cargamos el contenido en su HTML interno */
      fetch(svg.dataset.src)
        .then(respuesta => respuesta.text())
        .then(xml => svg.innerHTML = xml);
    });
  });
  