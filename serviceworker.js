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
      fetch(event.request)
      .then(function(result){
        return caches.open(CACHE_NAME)
        .then(function(c){
            c.put(event.request.url, result.clone())
            return result;
        })

        })
        .catch(function(e){
            return caches.match(event.request)

        })
      
    
  );
});
