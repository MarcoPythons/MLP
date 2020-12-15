var CACHE_NAME = 'Cashe_MLP'; /* Nombre del Cache*/
var urlsToCache = [/* URLS que se dejaran en el cache */ 
    'home/',
    'static/img/logo.png',
    'static/img/icono.ico',

    ];

self.addEventListener("install", function (event) {
  /* Instalacion */ // Perform install steps
  event.waitUntil(
    caches
      .open(
        CACHE_NAME
      ) /* Apertura del cache definido en la variable CACHE_NAME */
      .then(function (cache) {
        console.log("Opened cache");
        return cache.addAll(
          urlsToCache
        ); /* se agregan todas las urls definidas al cache de la pagina web  */
      })
  );
});

self.addEventListener("fetch", function (event) {  
  /* peticion */ event.respondWith(
      fetch(event.request) /* intercepcion de la peticion*/
      .then(function(result){ 
        return caches.open(CACHE_NAME) /* aca se abre el cashe*/
        .then(function(c){
            c.put(event.request.url, result.clone()) /* aca se ponen todo lo que se guardo en el cache y hacemos una copia para evitar problemas*/
            return result; /* y aca retornamoos todo*/
        })

        })
        .catch(function(e){ /* y si falla la conexion*/
            return caches.match(event.request) /* retornamos todo lo que este en el cache cache*/

        })
      
    
  );
});
