import datetime # Importa el módulo para trabajar con fechas y horas
class Logger:   # Clase Logger con patrón Singleton
    _instancia = None                  # Única instancia (inicia en None)
    def __new__(cls):                  # Controla la creación del objeto
        if cls._instancia is None:     # Si no existe instancia...
            cls._instancia= super().__new__(cls)  # ...la crea una sola vez
            cls._instancia._logs= []   # Lista vacía de logs
        return cls._instancia          # Siempre devuelve la misma instancia     
    def _registrar(self, nivel, mensaje):                         # Guarda un mensaje en el log
        hora=datetime.datetime.now().strftime("%H:%M:%S") # Hora actual
        entrada={"hora" :hora,"nivel" : nivel, "msg":mensaje}  # Diccionario con los datos
        self._logs.append(entrada)  # Agrega a la lista
    
    def info(self, msg): self._registrar("INFO",    msg)  # Registra nivel INFO
    def warning(self, msg): self._registrar("WARNING", msg)  # Registra nivel WARNING
    def error(self, msg):   self._registrar("ERROR",   msg)  # Registra nivel ERROR
      
    def mostrar_logs(self):     
        print(f"\n=== HISTORIAL DEL SISTEMA ({len(self._logs)} eventos) ===")
        for log in self._logs: # Recorre cada entrada
            print(f"  [{log['hora']}] {log['nivel']:7} | {log['msg']}") # Imprime con formato
              
    #-------------------------------------------         
    def limpiar(self):
        self._logs.clear()
        print("OK Historial de logs limpiado.")