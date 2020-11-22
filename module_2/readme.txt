Анализ и подготовка данных для построения модели, предсказывающей баллы за экзамен по математике среди учеников
EDA for create model which predictions exam-score of Math
Описание исходных данных:
  - представлены данные об условиях жизни и учебы 395 учеников 
  - в датасете 3 числовых признака (age - возраст, score - баллы по госэкзамену по математике , absences - количество пропущенных занятий)
    и 27 категориальных признаков
Description of the initial data:
  - data's about the living and learning 395 students
  - there are 3 numerical variables (age, score - points on the state exam in Math, absences - the number of missed classes)
    and 27 categorical variables      
Цель:
 - Подготовить данные для создания модели
Destination:
 - Prepare data for create prediction-model
Задачи:
 - Импортировать необходимые библиотеки и файл с данными
 - Создать блок с функциями, необходимыми для универсальной обработки данных
 - Осмотреть имеющиеся данные, выявить и устранить явные ошибочные данные
 - Найти и отбросить данные, выходящие за пределы IQR более, чем на 1,5 IQR
 - Провести коррелляционный анализ количественных переменных и сделать промежуточные выводы
 - Провести анализ номинативных переменных, удалить не влияющие на оценку данные, сделать промежуточные    выводы
 - Сделать выводы
Ways:
 - Import libraries and DataFrame
 - Create func() for preparation different columns of DataFrame
 - View DataFrame and fix mistakes
 - Find and drop data which is in over range more than 1.5 IQR from IQR
 - Apply corelation-analysis into DataFrame for quantitative variables and write pre-conclusion
 - Apply view-analysis into DataFrame for nominative variables, drop useless columns and write pre-        conclusion
 - Write conclusion
