# ⏰ Time API (FastAPI + Azure)

Este proyecto es una **API simple en FastAPI** que devuelve la hora actual en UTC (y con zona horaria local si está disponible).  
Se despliega automáticamente en **Azure App Service (Linux, Contenedor)** usando **GitHub Actions + Azure Container Registry (ACR)**.

---

## 🚀 Endpoints disponibles

- **`/api/health`** → Verifica si la API está viva.
- **`/api/time`** → Devuelve la hora actual en UTC (ISO y epoch).
- **`/docs`** → Documentación interactiva (Swagger UI).
- **`/`** → Página raíz con los enlaces a los endpoints.

Ejemplo del deploy en Azure:  
👉 [`https://time-api-py-agustin.azurewebsites.net`](https://time-api-py-agustin.azurewebsites.net)

---

## 🛠️ Inicialización local

1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/AgustinB123/Desafio1.git
   cd Desafio1
   Crear y activar entorno virtual
   ```

bash
Copiar
Editar
python -m venv .venv
source .venv/bin/activate # En Linux/Mac
.venv\Scripts\activate # En Windows
Instalar dependencias

bash
Copiar
Editar
pip install -r requirements.txt
Levantar servidor local (con Uvicorn)

bash
Copiar
Editar
uvicorn app.main:app --reload --port 8080
Ahora podés entrar en 👉 http://127.0.0.1:8080

☁️ Deploy automático en Azure
Cada vez que hacés push a la rama main, GitHub Actions:

Corre los tests con pytest.

Construye la imagen Docker.

Publica la imagen en Azure Container Registry (ACR).

Actualiza el Azure Web App con el nuevo contenedor.

Podés monitorear el workflow en la pestaña Actions de GitHub.

📴 Apagar o desactivar la máquina virtual (App Service)
Aunque Azure App Service no es una VM tradicional, podés detener el servicio para no consumir créditos:

Ir al portal 👉 Azure Portal

Buscar tu recurso: time-api-py-agustin

Hacer clic en Detener (arriba en la barra de acciones).

El estado pasará de En ejecución a Detenido.

La URL (.azurewebsites.net) dejará de estar disponible hasta que la reinicies.

Para volver a encenderlo, simplemente hacé clic en Iniciar.

📚 Tecnologías
FastAPI

Uvicorn

Docker

Azure App Service

GitHub Actions

👨‍💻 Proyecto creado por Agustín Brites para práctica de Despliegue en la Nube (Azure).
