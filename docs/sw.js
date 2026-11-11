// Service worker : garde en mémoire l'écran de démarrage et les icônes (l'appli s'ouvre même avec un réseau lent).
// Le contenu des révisions vient toujours du site en direct : il n'est jamais mis en cache ici.
// Change le numéro de version quand tu modifies index.html, pour que les téléphones prennent la nouvelle version.
const VERSION = "ciel-v2";
const FICHIERS = ["./", "index.html", "manifest.webmanifest", "icons/icon-192.png", "icons/icon-512.png", "icons/apple-touch-icon.png"];

self.addEventListener("install", (e) => {
  e.waitUntil(caches.open(VERSION).then((c) => c.addAll(FICHIERS)));
  self.skipWaiting();
});

self.addEventListener("activate", (e) => {
  e.waitUntil(caches.keys().then((cles) => Promise.all(cles.filter((k) => k !== VERSION).map((k) => caches.delete(k)))));
  self.clients.claim();
});

self.addEventListener("fetch", (e) => {
  const url = new URL(e.request.url);
  if (url.origin !== location.origin || e.request.method !== "GET") return;   // le site Streamlit passe directement
  // Réseau d'abord (toujours la dernière version), mémoire si pas de réseau
  e.respondWith(
    fetch(e.request)
      .then((rep) => { const copie = rep.clone(); caches.open(VERSION).then((c) => c.put(e.request, copie)); return rep; })
      .catch(() => caches.match(e.request, { ignoreSearch: true }).then((r) => r || caches.match("index.html")))
  );
});
