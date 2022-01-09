# finam-quote-loader
Web service  для закачки котировок с Finam.ru

## API
### /timeframe 
Список доступных таймфрэймов
### /markets
Список доступных рынков
### /stock
Загрузить список инструментов  
**Query Parameters**
- market - название рынка
- code - код инструмента
### /quote
Загрузить котировки инструментов  
**Query Parameters**
- market - название рынка
- code - код инструмента
- from - дата с
- till - дата по
- tf - таймфрэйм
