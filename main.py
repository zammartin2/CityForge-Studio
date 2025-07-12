#!/usr/bin/env python3
import sys
from PySide6.QtWidgets import QApplication, QStyleFactory
from PySide6.QtGui import QPalette, QColor
from core.graph import Graph
from core.plugin_manager import PluginManager
from ui.main_window import MainWindow
import nodes  # чтобы получить список доступных типов узлов

def apply_dark_theme(app: QApplication):
    # Используем Fusion-стиль и тёмную палитру
    app.setStyle(QStyleFactory.create("Fusion"))
    p = QPalette()
    p.setColor(QPalette.Window,        QColor(30,  30,  30))
    p.setColor(QPalette.Base,          QColor(25,  25,  25))
    p.setColor(QPalette.AlternateBase, QColor(45,  45,  45))
    p.setColor(QPalette.WindowText,    QColor(220, 220, 220))
    p.setColor(QPalette.Text,          QColor(220, 220, 220))
    p.setColor(QPalette.ToolTipBase,   QColor(220, 220, 220))
    p.setColor(QPalette.ToolTipText,   QColor(30,  30,  30))
    p.setColor(QPalette.Button,        QColor(45,  45,  45))
    p.setColor(QPalette.ButtonText,    QColor(220, 220, 220))
    p.setColor(QPalette.Highlight,     QColor(80,  150, 255))
    p.setColor(QPalette.HighlightedText, QColor(30,  30,  30))
    app.setPalette(p)

def main():
    app = QApplication(sys.argv)
    apply_dark_theme(app)

    # Создаём модель графа
    graph = Graph()

    # Регистрируем все типы узлов из пакета nodes
    for cls_name in nodes.__all__:
        cls = getattr(nodes, cls_name)
        graph.register_node_type(cls)

    # Загружаем плагины
    plugin_manager = PluginManager(graph)
    plugin_manager.load_all()

    # Создаём и показываем главное окно
    window = MainWindow(graph)
    window.show()

    # Запуск цикла событий
    exit_code = app.exec()

    # При выходе выгружаем плагины
    plugin_manager.unload_all()
    sys.exit(exit_code)

if __name__ == "__main__":
    main()
