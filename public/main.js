const yearEl = document.getElementById("year");
if (yearEl) yearEl.textContent = String(new Date().getFullYear());

function setText(id, value) {
  const el = document.getElementById(id);
  if (el) el.textContent = value;
}

async function refresh() {
  setText("browserTime", new Date().toLocaleString("ru-RU"));
  try {
    const r = await fetch("/api/status", { cache: "no-store" });
    const d = await r.json();
    setText("title", d.title);
    setText("version", d.version);
    setText("host", d.host);
    setText("system", d.system);
    setText("python", d.python);
    setText("docker", d.in_docker ? "да" : "нет");
    setText("serverTime", d.server_time);
  } catch (e) {
    setText("serverTime", "нет связи с сервером: " + e.message);
  }
}

refresh();
setInterval(refresh, 1000);
