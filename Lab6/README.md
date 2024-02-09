# Лабораторная работа №6: Деревья решений
[Теория](https://docs.yandex.ru/docs/view?url=ya-browser%3A%2F%2F4DT1uXEPRrJRXlUFoewruIahFDye-c3wQPioFsQt3LKbfd7eQM0EIRLvX5x2D_92fJbQdDfXGxL6Is77aeu15n-rrxyYV9KyZdlOVpQdMnUk1G0bbHJtXFeVXOQ2UYoXJvKE3ZLeQqUcscNU-9V1CA%3D%3D%3Fsign%3D0j9chAXI0HwAtPAp4dBpUpVMeQuEvOaqFvI2pzjyC9I%3D&name=Дерево%20решений.docx)

Спонсор понимания: [Данный парень](https://www.youtube.com/watch?v=FeGe35iYTXU&t=452s)
### ТЗ:

1. Для студентов с четным порядковым номером в группе – датасет с [классификацией грибов](https://archive.ics.uci.edu/ml/datasets/Mushroom), а нечетным – [датасет с данными про оценки студентов инженерного и педагогического факультетов](https://archive.ics.uci.edu/dataset/856/higher+education+students+performance+evaluation) (для данного датасета нужно ввести метрику: студент успешный/неуспешный на основании грейда)
2. Отобрать **случайным** образом sqrt(n) признаков
3. Реализовать без использования сторонних библиотек построение дерева решений (numpy и pandas использовать можно, использовать списки для реализации  дерева - нельзя)
4. Провести оценку реализованного алгоритма с использованием Accuracy, precision и recall
5. Построить AUC-ROC и AUC-PR (в пунктах 4 и 5 использовать библиотеки нельзя)