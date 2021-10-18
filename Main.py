from pyautogui import sleep
import ReconocedordeVoz
import sintetizador
import ventana
import subprocess as sp
import controlTecladoyMouse
import time
import threading

duracion = "4" 
modoPrueba = True
menuAyuda = True
tiempo = {"uno":1,"1":1,"dos":2,"2":2,"tres":3,"3":3,"cuatro":4,"4":4,"cinco":5,"5":5,"seis":6,"6":6,"siente":7,"7":7,"ocho":8,"8":8,"nueve":9,"9":9,"diez":10,"10":10}

a = True
sintetizador.hablar("iniciando asistente de voz")

while True:
    try:
        vozUsuario = ""
        vozUsuario = ReconocedordeVoz.reconocer(duracion).lower()

        if ("modo" in vozUsuario and ("desactivar" in vozUsuario or "fin" in vozUsuario)  and "prueba" in vozUsuario):
            modoPrueba = True
        
        elif ("modo" in vozUsuario and ("activar" in vozUsuario or "iniciar" in vozUsuario) and "prueba" in vozUsuario):
            modoPrueba = False

        if (modoPrueba == False):
            sintetizador.hablar("modo de prueba activo, usted dijo: "+vozUsuario)


        if (("ajustar" in vozUsuario or "cambiar" in vozUsuario) and ("tiempo" in vozUsuario or "duracion" in vozUsuario)):
            if (duracion == "Mone"):
                actual = "es automatico por el sistema, a la espera que dejes de hablar,"
            else:
                actual = "es de "+duracion+" segundos,"
           
            sintetizador.hablar("el tiempo actual es de "+actual+" diga el nuevo valor, recuerde que el tiempo esta dado en segundos y debe ser entero, por favor diga un numero entre uno y diez")
            vozUsuario = ReconocedordeVoz.reconocer("2").lower()
            aux2 = str(tiempo[vozUsuario])
            if (int(aux2) > 0 and int(aux2) < 11):
                sintetizador.hablar("el nuevo tiempo de escucha cambio a "+aux2+ " segundos.")
                duracion = aux2
            else:
                sintetizador.hablar("el numero dicho no fue entendido correctamente, queda de finido de forma automatica.")
                duracion = "None"

        if ("modo" in vozUsuario  and "ayuda" in vozUsuario):
            tex = "Este es el modo ayuda, en este usted podrá mirar los diferentes módulos y se le dirán como son los comandos, ¿por favor diga que ayuda necesita?  Puede elegir entre navegación, configuración o escritura."
            sintetizador.hablar(tex)   
            while menuAyuda:
                vozUsuario = ReconocedordeVoz.reconocer("None").lower()
                sintetizador.hablar("muy bien, ")
                if ("navegación" in vozUsuario or "navegacion" in vozUsuario): 
                    tex = "En el módulo de navegación puede realizar las siguientes acciones, como primer comando esta, abrir WhatsApp, que sirve para abrir la aplicación, de igual manera esta el comando, cerrar WhatsApp, que cierra la aplicacion, otra funcionalidad  es ,minimizar, con esta oculta la ventana de la aplicación, si quieres volverla a abrir esta el comando, maximizar, o tembien puedes decir , restaurar, y volverá a aparecer tu ventana de WhatsApp, también están los comandos para hacer scroll los cuales deberá decir, bajar, en caso de querer hacer un scroll hacia abajo, o deberá decir subir, en caso de querer hacer un scroll hacia arriba. ¿Desea preguntar sobre otro modulo? Responde con sí o no."
                    sintetizador.hablar(tex) 
                    vozUsuario = ReconocedordeVoz.reconocer("None").lower()
                    if ("si" in vozUsuario or "sí" in vozUsuario):
                        sintetizador.hablar("muy bien, Puede elegir entre navegación, configuración o escritura") 
                    else:
                        sintetizador.hablar("muy bien, Espero haber sido de ayuda, saliendo del modo")
                        menuAyuda = False
                elif ("configuración" in vozUsuario or "configuracion" in vozUsuario): 
                    tex = "En el módulo de configuración puede realizar las siguientes acciones, como primer comando puedes tener un modo de prueba con el siguiente comando, activar modo de prueba, con este podrás probar el micrófono y dirá todo lo que tú le hables, también  está el comando para cambiar el tiempo de escucha y se activa diciendo, ajustar tiempo de escucha, donde  te pregunta el nuevo valor en segundos de 1 a 10 y lo parametriza. ¿Desea preguntar sobre otro modulo? Responde con sí o no"
                    sintetizador.hablar(tex) 
                    vozUsuario = ReconocedordeVoz.reconocer("None").lower()
                    if ("si" in vozUsuario or "sí" in vozUsuario):
                        sintetizador.hablar("muy bien, Puede elegir entre navegación, configuración o escritura") 
                    else:
                        sintetizador.hablar("muy bien, Espero haber sido de ayuda, saliendo del modo")
                        menuAyuda = False 
                elif ("escritura" in vozUsuario):
                    tex = "En el módulo de escritura básicamente tiene los comandos necesarios para escribir o iniciar un chat nuevo,  como primer comando esta, nuevo, con este abre el panel de los contactos y posteriormente dices el nombre del contacto a buscar luego puedes decir el mensaje que quieres. con el comando, escribir, puedes escribir, estando situado en el chat o contacto luego con el comando, enter o aceptar, si quieres enviar un mensaje a un contacto especifico de manera rápida podrás hacerlo con el siguiente comando, enviar mensaje a, y al final le añades el nombre el contacto, un ejemplo puede ser, enviar mensaje a Alvaro, el aplicativo reconocerá el contacto y luego te pedirá que digas tu mensaje y luego lo enviara. ¿Desea preguntar sobre otro modulo? Responde con sí o no"
                    sintetizador.hablar(tex) 
                    vozUsuario = ReconocedordeVoz.reconocer("None").lower()
                    if ("si" in vozUsuario or "sí" in vozUsuario):
                        sintetizador.hablar("muy bien, Puede elegir entre navegación, configuración o escritura") 
                    else:
                        sintetizador.hablar("muy bien, Espero haber sido de ayuda, saliendo del modo")
                        menuAyuda = False


        if ("abrir" in vozUsuario and modoPrueba):
            aux = "abriendo whatsapp"
            sintetizador.hablar(aux)
            controlTecladoyMouse.abrir()
            
        elif (("bajar" in vozUsuario or "scroll down" in vozUsuario or "scrolldown" in vozUsuario) and modoPrueba) :
            sintetizador.hablar("bajando")
            controlTecladoyMouse.scrollDown()
        
        elif (("abajo" in vozUsuario  or "siguiente" in vozUsuario) and modoPrueba):
            sintetizador.hablar("bajando siguiente chat") 
            controlTecladoyMouse.siguienteChat()   
        
        elif (("arriba" in vozUsuario or "Anterior" in vozUsuario) and modoPrueba):
            sintetizador.hablar("subiendo al siguiente chat") 
            controlTecladoyMouse.anteriorChat()   
        
        elif (("subir" in vozUsuario or "scroll up" in vozUsuario or "scrollup" in vozUsuario) and modoPrueba) :
            sintetizador.hablar("subiendo") 
            controlTecladoyMouse.scrollUp()     
        
        elif ("minimi" in vozUsuario and modoPrueba):
            sintetizador.hablar("minimizando whatsapp")
            controlTecladoyMouse.minimizar()
        
        elif ((("restaurar" in vozUsuario) or ("maximi" in vozUsuario)) and modoPrueba):
            sintetizador.hablar("restaurando whatsapp")
            controlTecladoyMouse.abrir()
        
        elif ((("aumentar" in vozUsuario and  "letra" in vozUsuario) or  "acercar" in vozUsuario) and modoPrueba):
            sintetizador.hablar("aumentando letra")
            controlTecladoyMouse.acercar()
        
        elif ((("reducir" in vozUsuario and  "letra" in vozUsuario) or  "alejar" in vozUsuario) and modoPrueba):
            sintetizador.hablar("reduciendo letra")
            controlTecladoyMouse.alejar()
        
        elif ("nuevo" in vozUsuario and modoPrueba):
            vozUsuario = vozUsuario[vozUsuario.find("nuevo")+10:]
            sintetizador.hablar("creando nuevo chat")
            controlTecladoyMouse.nuevo()
            time.sleep(.5)
            sintetizador.hablar("diga el nombre para el nuevo chat")
            vozUsuario1 = ReconocedordeVoz.reconocer("None").lower()
            controlTecladoyMouse.escribir(vozUsuario1)
            time.sleep(1.5)
            controlTecladoyMouse.enter() 
            time.sleep(.5)
            tex = "que mensaje desea darle a ",vozUsuario1,"?"
            sintetizador.hablar(tex)   
            vozUsuario2 = ReconocedordeVoz.reconocer("None").lower()
            sintetizador.hablar("muy bien, escribiendo mensaje")
            controlTecladoyMouse.escribir(vozUsuario2)
            time.sleep(1.5)
            controlTecladoyMouse.enter()
            time.sleep(.5)
            sintetizador.hablar("mensaje enviado")
            
        elif ("perfil" in vozUsuario and modoPrueba):
            sintetizador.hablar("mostrando perfil")
            controlTecladoyMouse.foto()

        
        elif ("buscar chat" in vozUsuario and modoPrueba):
            vozUsuario = vozUsuario[vozUsuario.find("buscar")+10:]
            sintetizador.hablar("que chat quieres buscar")            
            vozUsuariochat = ReconocedordeVoz.reconocer("None").lower()
            sintetizador.hablar("buscando "+vozUsuariochat)
            controlTecladoyMouse.buscarChat()            
            controlTecladoyMouse.escribir(vozUsuariochat)
            time.sleep(1)
            controlTecladoyMouse.enter()
        
        elif (("atras" in vozUsuario or "atrás" in vozUsuario or "volver" in vozUsuario) and modoPrueba):
            sintetizador.hablar("atrás")
            controlTecladoyMouse.escape()
        
        #agregando funcionamiento falta confirmacion
        elif (("eliminar" in vozUsuario and "conver" in vozUsuario) and modoPrueba):
            sintetizador.hablar("eliminando conversacion")
            controlTecladoyMouse.eliminarChat()
        
        elif (("aceptar" in vozUsuario or "enter" in vozUsuario) and modoPrueba):
            sintetizador.hablar("aceptar")
            controlTecladoyMouse.enter() 
        
        elif ("escribir" in vozUsuario and modoPrueba):
            vozUsuario = vozUsuario[vozUsuario.find("escribir")+9:]
            sintetizador.hablar("claro")
            time.sleep(1)
            sintetizador.hablar("que quieres escribir?")
            vozUsuario = ReconocedordeVoz.reconocer("None").lower()
            controlTecladoyMouse.escribir(vozUsuario)
            sintetizador.hablar("escribiendo")
            time.sleep(1)
            controlTecladoyMouse.enter()
            time.sleep(1)
            
            
        elif (("enviar" in vozUsuario and  "mensaje a" in vozUsuario) and modoPrueba): 
            aux = vozUsuario[vozUsuario.find("mensaje a")+10:]
            tex = "que mensaje desea darle a ",aux,"?"
            sintetizador.hablar(tex)   
            vozUsuario = ReconocedordeVoz.reconocer("None").lower()
            sintetizador.hablar("muy bien, enviando mensaje")
            controlTecladoyMouse.nuevo()
            time.sleep(.5)
            controlTecladoyMouse.escribir(aux)
            time.sleep(1)
            controlTecladoyMouse.enter() 
            time.sleep(1)
            controlTecladoyMouse.escribir(vozUsuario)
            controlTecladoyMouse.enter()
            time.sleep(1)
            sintetizador.hablar("mensaje enviado")
        
        elif (( "chat de" in vozUsuario) and modoPrueba): 
            aux = vozUsuario[vozUsuario.find("chat de")+7:]
            sintetizador.hablar("muy bien")
            controlTecladoyMouse.buscarChat()
            time.sleep(1)
            sintetizador.hablar("dí el nombre del chat a buscar")
            vozUsuario1 = ReconocedordeVoz.reconocer("None").lower()
            controlTecladoyMouse.escribir(vozUsuario1)
            time.sleep(1)
            controlTecladoyMouse.enter()   
            sintetizador.hablar("este es el chat que encontre")


        elif (("ver foto" in vozUsuario) and modoPrueba):
            sintetizador.hablar("mostrando foto")
            controlTecladoyMouse.Verfoto()        

        elif (("eliminar" in vozUsuario and "chat" in vozUsuario) and modoPrueba): 
            controlTecladoyMouse.eliminarChat()
        
        elif (("borrar" in vozUsuario) and modoPrueba): 
            controlTecladoyMouse.borrarTexto()

        elif(("llamar" in vozUsuario)and modoPrueba):
            sintetizador.hablar("se va a realizar una llamada")
            time.sleep(1)
            controlTecladoyMouse.llamada()
        
        elif(("colgar" in vozUsuario)and modoPrueba):
            sintetizador.hablar("se va a colgar la llamada")
            time.sleep(1)
            controlTecladoyMouse.colgarLLamada()
        
        elif(("video" in vozUsuario and "llamada")and modoPrueba):
            sintetizador.hablar("se va a realizar una video llamada")
            time.sleep(1)
            controlTecladoyMouse.videoLLamada()
        
        elif(("finalizar video" in vozUsuario)and modoPrueba):
            sintetizador.hablar("se va a colgar la video llamada")
            time.sleep(1)
            controlTecladoyMouse.colgarVideoLLamada()  
        #se archiva pero no sale      
        elif(("archivar chat" in vozUsuario )and modoPrueba):
            sintetizador.hablar("se esta archivando el chat")
            time.sleep(1)
            controlTecladoyMouse.archivarChat()
        
        #falta implemetar agregar o desagregar contatos, paso siguiente nombre del grupo y posteriormente las reglas 
        elif(("crear grupo" in vozUsuario )and modoPrueba):
            sintetizador.hablar("se esta creando un grupo por favor selecione a los contactos que participaran")
            controlTecladoyMouse.crearGrupo() 
        #falta seleccionar el tiempo de silenciar y luego confirmar o cancelar el silencio
        elif(("silenciar chat" in vozUsuario )and modoPrueba):
            sintetizador.hablar("se va a silencair estes chat")
            time.sleep(1)
            controlTecladoyMouse.silenciarChat()  
        #no esta implementado
        elif(("buscar texto" in vozUsuario)and modoPrueba):
            sintetizador.hablar("diga la palabra a buscar")
            vozUsuario = ReconocedordeVoz.reconocer("None").lower()
            vozUsuario = vozUsuario[vozUsuario.find("buscar")+7:]            
            sintetizador.hablar("buscando "+vozUsuario)
            controlTecladoyMouse.buscarTextoChat()
            controlTecladoyMouse.escribir(aux)
            time.sleep(1)
            controlTecladoyMouse.enter() 
        #no esta implementado 
        elif(("dejar de" in vozUsuario and "buscar texto" in vozUsuario)and modoPrueba):
            sintetizador.hablar("muy bien")
            time.sleep(1)
            controlTecladoyMouse.Verfoto()         
        
        elif(("marcar" in vozUsuario and "como leido" in vozUsuario)and modoPrueba):
            sintetizador.hablar("muy bien")
            time.sleep(1)
            controlTecladoyMouse.marcarMensaje()
        
        elif(("desmarcar" in vozUsuario and "como leido" in vozUsuario)and modoPrueba):
            sintetizador.hablar("muy bien")
            time.sleep(1)
            controlTecladoyMouse.marcarMensaje()
        
        elif(("nota de vo" in vozUsuario or "audio" in vozUsuario) and modoPrueba):
            sintetizador.hablar("se va a mandar un mensaje de voz")
            time.sleep(1)
            controlTecladoyMouse.microfono()
        
        elif(( "enviar audio"in vozUsuario ) and modoPrueba):
            controlTecladoyMouse.microfono()
            time.sleep(1)
            sintetizador.hablar("se a enviado el audio exitosa mente")
        
        elif(("cancelar vo" in vozUsuario or "cancelar audio" in vozUsuario) and modoPrueba):
            controlTecladoyMouse.cancelarAudio()
            time.sleep(1)
            sintetizador.hablar("se cancelo el mensaje de voz")

        elif (("fijar chat" in vozUsuario) and modoPrueba):
            sintetizador.hablar("chat fijado")
            controlTecladoyMouse.fijarChat() 

        elif (("desacer chat" in vozUsuario) and modoPrueba):
            sintetizador.hablar("se ha des fijado el chat")
            controlTecladoyMouse.fijarChat()     

        elif (("cerra foto" in vozUsuario) and modoPrueba):
            sintetizador.hablar("cerrando foto volviendo al chat")
            controlTecladoyMouse.cerrarVerFoto()

        elif (("cerrar" in vozUsuario and "whatsapp") and modoPrueba):
            sintetizador.hablar("cerrando whatsapp")
            controlTecladoyMouse.cerrarVentana()
 

    except Exception as e:
        print("Ocurrio un error", e)
        continue

