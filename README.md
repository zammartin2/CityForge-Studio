# Кузнец умных потоков (SityFactory Studio)

Интерактивная среда для визуального проектирования и исполнения потоков данных.  
Позволяет создавать, соединять и конфигурировать узлы, а затем запускать и тестировать сценарии.

## ✨ Особенности

- **Модульная архитектура** узлов и плагинов  
- **Drag & drop** по канвасу, зум и панорамирование  
- **Интерактивное соединение** узлов с «липнущей» линией  
- **Авто-выравнивание** (auto layout)  
- **Grid & Snap to Grid** для точного позиционирования  
- **Inspector** для редактирования свойств узлов  
- **Расширяемость**: плагины (history, IO, layout и др.)  
- **Темная тема** с настраиваемой топбар-панелью

## 🚀 Быстрый старт

1. **Клонируйте репозиторий**  
   ```bash
   git clone https://github.com/yourname/sityfactory-studio.git
   cd sityfactory-studio

python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows

pip install -r requirements.txt

```
├── main.py
├── core/
│   ├── graph.py
│   ├── node.py
│   └── connection.py
├── nodes/
│   ├── start_node.py
│   ├── http_node.py
│   ├── delay_node.py
│   └── play_node.py
├── plugins/
│   ├── history_plugin.py
│   ├── io_plugin.py
│   └── layout_plugin.py
├── ui/
│   ├── main_window.py
│   ├── canvas_view.py
│   ├── inspector.py
│   └── dialogs.py
├── utils/
│   ├── config.py
│   └── path_utils.py
├── docs/
│   └── logo.png
├── requirements.txt
└── README.md
```

⚙️ Конфигурация
Все константы (размеры узлов, цвета, шаг сетки) вынесены в utils/config.py:
GRID_SIZE = 20
GRID_COLOR = (200, 200, 200, 30)
NODE_WIDTH = 120
NODE_HEIGHT = 50
NODE_FILL_COLOR = "#2c2c2c"
NODE_BORDER_COLOR = "#555"

