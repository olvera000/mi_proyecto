# Mi Proyecto con Codex CLI y GPT-5

Este es un proyecto de configuración y pruebas con **OpenAI Codex CLI** utilizando el modelo **GPT-5 (High reasoning)**.  
El objetivo es contar con un entorno de trabajo aislado, versionado con Git y conectado a GitHub mediante **SSH**.

## 🚀 Características
- Configuración inicial de **Codex CLI** en Windows 11.  
- Uso de **GPT-5 High** como modelo por defecto.  
- Integración con **GitHub mediante SSH**.  
- Control de versiones con **Git**.  
- `.gitignore` documentado para mantener el repo limpio.  

## 📂 Estructura del proyecto
mi_proyecto/
├── .gitignore
├── README.md
├── src/
│   └── main.py
└── .env.example

## ⚙️ Requisitos
- Windows 11  
- [Git](https://git-scm.com/) instalado  
- Clave SSH configurada en GitHub  
- [Codex CLI](https://www.npmjs.com/package/@openai/codex) instalado  

> Para ejecutar el ejemplo en Python: tener [Python 3.9+](https://www.python.org/) instalado.

## ▶️ Uso
1. Clona el repositorio:
   ```bash
   git clone git@github.com:olvera000/mi_proyecto.git
Ingresa a la carpeta del proyecto:
cd mi_proyecto
Ejecuta Codex CLI:
codex
Ejemplos de uso de Codex CLI

Dentro de Codex podés usar comandos especiales para gestionar tu entorno:
Ver el estado actual:

/status

Muestra el modelo activo, el esfuerzo de razonamiento y la configuración actual.
Cambiar de modelo o esfuerzo de razonamiento:

/model

Te permite elegir entre gpt-5 minimal | low | medium | high.
Inicializar agentes personalizados:

/init
Genera un archivo AGENTS.md en el proyecto para definir agentes con comportamientos específicos.

Crear un archivo nuevo:

/new archivo.py

Codex genera un archivo con la plantilla inicial.
Ejecutar un plan en tu código (cuando te propone pasos):
/run

Salir de Codex:

quit

o presionando Ctrl+C.

---

## 🐍 Aplicación Python (ejemplo)

Pequeño script de ejemplo en `src/main.py` con una función `greet` y un `main()` ejecutable desde la línea de comandos.

### Instalación rápida

```bash
# (Opcional) Crear y activar entorno virtual (Windows PowerShell)
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### Ejecutar

```bash
python src/main.py --name "Mundo"
```

Salida esperada:

```
Hola, Mundo!
```

### Variables de entorno

Usa `.env.example` como referencia para variables de entorno. Crea un archivo `.env` (que está ignorado por Git) si necesitas configurar valores locales.

No hay dependencias externas por ahora; el script usa solo la librería estándar.
