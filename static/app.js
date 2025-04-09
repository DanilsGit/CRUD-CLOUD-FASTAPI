document.addEventListener("DOMContentLoaded", () => {
  const eventForm = document.getElementById("eventForm");
  const eventsList = document.getElementById("eventsList");

  // Cargar eventos al iniciar
  fetchEvents();

  // Manejar envío del formulario
  eventForm.addEventListener("submit", async (e) => {
    e.preventDefault();

    const title = document.getElementById("title").value;
    const description = document.getElementById("description").value;
    const location = document.getElementById("location").value;
    const start_time = document.getElementById("start_time").value;
    const end_time = document.getElementById("end_time").value;

    const eventData = {
      title,
      description,
      location,
      start_time: new Date(start_time).toISOString(),
      end_time: new Date(end_time).toISOString(),
    };

    try {
      const response = await fetch("/api/events/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(eventData),
      });

      if (!response.ok) throw new Error("Error al crear evento");

      eventForm.reset();
      fetchEvents();
    } catch (error) {
      console.error("Error:", error);
      alert("Error al crear evento");
    }
  });

  // Función para cargar todos los eventos
  async function fetchEvents() {
    try {
      const response = await fetch("/api/events/");
      if (!response.ok) throw new Error("Error al cargar eventos");

      const events = await response.json();

      renderEvents(events);
    } catch (error) {
      console.error("Error:", error);
      eventsList.innerHTML = "<p>Error al cargar eventos</p>";
    }
  }

  // Función para renderizar eventos
  function renderEvents(events) {
    if (events.length === 0) {
      eventsList.innerHTML = "<p>No hay eventos registrados</p>";
      return;
    }

    eventsList.innerHTML = "";
    events.forEach((event) => {
      const eventElement = document.createElement("div");
      eventElement.className = "event-item";
      eventElement.innerHTML = `
                <h3>${event.title}</h3>
                <p>${event.description || "Sin descripción"}</p>
                <p>Lugar: ${event.location || "Sin descripción"}</p>
                <small>Desde: ${new Date(
                  event.start_time
                ).toLocaleString().split(",")[0]}</small>
                <small>Hasta: ${new Date(
                  event.end_time
                ).toLocaleString().split(",")[0]}</small>
                <div class="event-actions">
                    <button class="delete-btn" onclick="deleteEvent(${event.id})">Eliminar</button>
                </div>
            `;
      eventsList.appendChild(eventElement);
    });
  }

  window.deleteEvent = async (id) => {
    if (!confirm("¿Estás seguro de eliminar este evento?")) return;

    try {
      const response = await fetch(`/api/events/${id}`, {
        method: "DELETE",
      });

      if (!response.ok) throw new Error("Error al eliminar evento");

      fetchEvents();
    } catch (error) {
      console.error("Error:", error);
      alert("Error al eliminar evento");
    }
  };
});
