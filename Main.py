#importacion de modulos 
import speechRecognition
import voiceSynthesizer
import controllers
import time

duracion = "3" 
modoPrueba = True
menuAyuda = True
tiempo = {"uno":1,"1":1,"dos":2,"2":2,"tres":3,"3":3,"cuatro":4,"4":4,"cinco":5,"5":5,"seis":6,"6":6,"siente":7,"7":7,"ocho":8,"8":8,"nueve":9,"9":9,"diez":10,"10":10}


voiceSynthesizer.hablar("iniciando asistente de voz")

while True:
    try:
        #inicio de reconocimineto de voz 
        vozUsuario = ""
        vozUsuario = speechRecognition.reconocer(duracion).lower()
        #modo de prueba para el microfono 
        if ("modo" in vozUsuario and ("desactivar" in vozUsuario or "fin" in vozUsuario)  and "prueba" in vozUsuario):
            modoPrueba = True
        
        elif ("modo" in vozUsuario and ("activar" in vozUsuario or "iniciar" in vozUsuario) and "prueba" in vozUsuario):
            modoPrueba = False

        if (modoPrueba == False):
            voiceSynthesizer.hablar("modo de prueba activo, usted dijo: "+vozUsuario)

        #cambio de tiempo para que escuche el sistema 
        if (("ajustar" in vozUsuario or "cambiar" in vozUsuario) and ("tiempo" in vozUsuario or "duracion" in vozUsuario)):
            if (duracion == "Mone"):
                actual = "es automatico por el sistema, a la espera que dejes de hablar,"
            else:
                actual = "es de "+duracion+" segundos,"
           
            voiceSynthesizer.hablar("el tiempo actual es de "+actual+" diga el nuevo valor, recuerde que el tiempo esta dado en segundos y debe ser entero, por favor diga un numero entre uno y diez")
            vozUsuario = speechRecognition.reconocer("2").lower()
            aux2 = str(tiempo[vozUsuario])
            if (int(aux2) > 0 and int(aux2) < 11):
                voiceSynthesizer.hablar("el nuevo tiempo de escucha cambio a "+aux2+ " segundos.")
                duracion = aux2
            else:
                voiceSynthesizer.hablar("el numero dicho no fue entendido correctamente, queda de finido de forma automatica.")
                duracion = "None"
        #menu de ayuda para aprender a utilizar los comandos de voz
        if ("modo" in vozUsuario  and "ayuda" in vozUsuario):
            tex = "Este es el modo ayuda, en este usted podrá mirar los diferentes módulos y se le dirán como son los comandos, ¿por favor diga que ayuda necesita?  Puede elegir entre navegación, configuración o escritura."
            voiceSynthesizer.hablar(tex)   
            
            while menuAyuda:
                vozUsuario = speechRecognition.reconocer("None").lower()
                voiceSynthesizer.hablar("muy bien, ")
                if ("navegación" in vozUsuario or "navegacion" in vozUsuario): 
                    tex = "En el módulo de navegación puede realizar las siguientes acciones, como primer comando esta, abrir WhatsApp, que sirve para abrir la aplicación, de igual manera esta el comando, cerrar WhatsApp, que cierra la aplicacion, otra funcionalidad  es ,minimizar, con esta oculta la ventana de la aplicación, si quieres volverla a abrir esta el comando, maximizar, o tembien puedes decir , restaurar, y volverá a aparecer tu ventana de WhatsApp, también están los comandos para hacer scroll los cuales deberá decir, bajar, en caso de querer hacer un scroll hacia abajo, o deberá decir subir, en caso de querer hacer un scroll hacia arriba. ¿Desea preguntar sobre otro modulo? Responde con sí o no."
                    voiceSynthesizer.hablar(tex) 
                    vozUsuario = speechRecognition.reconocer("None").lower()
                    if ("si" in vozUsuario or "sí" in vozUsuario):
                        voiceSynthesizer.hablar("muy bien, Puede elegir entre navegación, configuración o escritura") 
                    else:
                        voiceSynthesizer.hablar("muy bien, Espero haber sido de ayuda, saliendo del modo")
                        menuAyuda = False
                elif ("configuración" in vozUsuario or "configuracion" in vozUsuario): 
                    tex = "En el módulo de configuración puede realizar las siguientes acciones, como primer comando puedes tener un modo de prueba con el siguiente comando, activar modo de prueba, con este podrás probar el micrófono y dirá todo lo que tú le hables, también  está el comando para cambiar el tiempo de escucha y se activa diciendo, ajustar tiempo de escucha, donde  te pregunta el nuevo valor en segundos de 1 a 10 y lo parametriza. ¿Desea preguntar sobre otro modulo? Responde con sí o no"
                    voiceSynthesizer.hablar(tex) 
                    vozUsuario = speechRecognition.reconocer("None").lower()
                    if ("si" in vozUsuario or "sí" in vozUsuario):
                        voiceSynthesizer.hablar("muy bien, Puede elegir entre navegación, configuración o escritura") 
                    else:
                        voiceSynthesizer.hablar("muy bien, Espero haber sido de ayuda, saliendo del modo")
                        menuAyuda = False 
                elif ("escritura" in vozUsuario):
                    tex = "En el módulo de escritura básicamente tiene los comandos necesarios para escribir o iniciar un chat nuevo,  como primer comando esta, nuevo, con este abre el panel de los contactos y posteriormente dices el nombre del contacto a buscar luego puedes decir el mensaje que quieres. con el comando, escribir, puedes escribir, estando situado en el chat o contacto luego con el comando, enter o aceptar, si quieres enviar un mensaje a un contacto especifico de manera rápida podrás hacerlo con el siguiente comando, enviar mensaje a, y al final le añades el nombre el contacto, un ejemplo puede ser, enviar mensaje a Alvaro, el aplicativo reconocerá el contacto y luego te pedirá que digas tu mensaje y luego lo enviara. ¿Desea preguntar sobre otro modulo? Responde con sí o no"
                    voiceSynthesizer.hablar(tex) 
                    vozUsuario = speechRecognition.reconocer("None").lower()
                    if ("si" in vozUsuario or "sí" in vozUsuario):
                        voiceSynthesizer.hablar("muy bien, Puede elegir entre navegación, configuración o escritura") 
                    else:
                        voiceSynthesizer.hablar("muy bien, Espero haber sido de ayuda, saliendo del modo")
                        menuAyuda = False

        #comandos 
        if ("abrir" in vozUsuario and modoPrueba):
            aux = "abriendo whatsapp"
            voiceSynthesizer.hablar(aux)
            controllers.abrir()
       #movimiento del scroll del mouse     
        elif (("bajar" in vozUsuario or "scroll down" in vozUsuario or "scrolldown" in vozUsuario) and modoPrueba) :
            voiceSynthesizer.hablar("bajando")
            controllers.scrollDown()

        elif (("subir" in vozUsuario or "scroll up" in vozUsuario or "scrollup" in vozUsuario) and modoPrueba) :
            voiceSynthesizer.hablar("subiendo") 
            controllers.scrollUp()     
        #movilizarce en la seccion de chats 
        elif (("abajo" in vozUsuario  or "siguiente" in vozUsuario) and modoPrueba):
            voiceSynthesizer.hablar("bajando siguiente chat") 
            controllers.siguienteChat()   
        
        elif (("arriba" in vozUsuario or "Anterior" in vozUsuario) and modoPrueba):
            voiceSynthesizer.hablar("subiendo al siguiente chat") 
            controllers.anteriorChat()   
       
        elif (("hacer cli" in vozUsuario) and modoPrueba):
            voiceSynthesizer.hablar("hacionando clik")
            controllers.hacerclik()

        elif ("minimi" in vozUsuario and modoPrueba):
            voiceSynthesizer.hablar("minimizando whatsapp")
            controllers.minimizar()
        
        elif ((("restaurar" in vozUsuario) or ("maximi" in vozUsuario)) and modoPrueba):
            voiceSynthesizer.hablar("restaurando whatsapp")
            controllers.abrir()
        
        elif ((("aumentar" in vozUsuario and  "letra" in vozUsuario) or  "acercar" in vozUsuario) and modoPrueba):
            voiceSynthesizer.hablar("aumentando letra")
            controllers.acercar()
        
        elif ((("reducir" in vozUsuario and  "letra" in vozUsuario) or  "alejar" in vozUsuario) and modoPrueba):
            voiceSynthesizer.hablar("reduciendo letra")
            controllers.alejar()
        
        elif ("nuevo" in vozUsuario and modoPrueba):
            vozUsuario = vozUsuario[vozUsuario.find("nuevo")+10:]
            voiceSynthesizer.hablar("creando nuevo chat")
            controllers.nuevo()
            time.sleep(.5)
            voiceSynthesizer.hablar("diga el nombre para el nuevo chat")
            vozUsuario1 = speechRecognition.reconocer("None").lower()
            controllers.escribir(vozUsuario1)
            time.sleep(1.5)
            controllers.enter() 
            time.sleep(.5)
            tex = "que mensaje desea darle a ",vozUsuario1,"?"
            voiceSynthesizer.hablar(tex)   
            vozUsuario2 = speechRecognition.reconocer("None").lower()
            voiceSynthesizer.hablar("muy bien, escribiendo mensaje")
            controllers.escribir(vozUsuario2)
            time.sleep(1.5)
            controllers.enter()
            time.sleep(.5)
            voiceSynthesizer.hablar("mensaje enviado")
            
        elif ("perfil" in vozUsuario and modoPrueba):
            voiceSynthesizer.hablar("mostrando perfil")
            controllers.foto()

        elif ("buscar chat" in vozUsuario and modoPrueba):
            vozUsuario = vozUsuario[vozUsuario.find("buscar")+10:]
            voiceSynthesizer.hablar("que chat quieres buscar")            
            vozUsuariochat = speechRecognition.reconocer("None").lower()
            voiceSynthesizer.hablar("buscando "+vozUsuariochat)
            controllers.buscarChat()            
            controllers.escribir(vozUsuariochat)
            voiceSynthesizer.hablar("este es el chat que en contre")
            time.sleep(1)
            controllers.enter()
        
        elif (("atras" in vozUsuario or "atrás" in vozUsuario or "volver" in vozUsuario) and modoPrueba):
            voiceSynthesizer.hablar("atrás")
            controllers.escape()
        
        #se debe confirmar con el mouse
        elif (("eliminar" in vozUsuario and "conver" in vozUsuario) and modoPrueba):
            voiceSynthesizer.hablar("eliminando conversacion")
            controllers.eliminarChat()
        
        elif (("aceptar" in vozUsuario or "enter" in vozUsuario) and modoPrueba):
            voiceSynthesizer.hablar("aceptar")
            controllers.enter() 
        
        elif ("escribir" in vozUsuario and modoPrueba):
            vozUsuario = vozUsuario[vozUsuario.find("escribir")+9:]
            voiceSynthesizer.hablar("claro")
            time.sleep(1)
            voiceSynthesizer.hablar("que quieres escribir?")
            vozUsuario = speechRecognition.reconocer("None").lower()
            controllers.escribir(vozUsuario)
            voiceSynthesizer.hablar("escribiendo")
            time.sleep(1)
            controllers.enter()
            time.sleep(1)
            
            
        elif (("enviar" in vozUsuario and  "mensaje a" in vozUsuario) and modoPrueba): 
            aux = vozUsuario[vozUsuario.find("mensaje a")+10:]
            tex = "que mensaje desea darle a ",aux,"?"
            voiceSynthesizer.hablar(tex)   
            vozUsuario = speechRecognition.reconocer("None").lower()
            voiceSynthesizer.hablar("muy bien, enviando mensaje")
            controllers.nuevo()
            time.sleep(.5)
            controllers.escribir(aux)
            time.sleep(1)
            controllers.enter() 
            time.sleep(1)
            controllers.escribir(vozUsuario)
            controllers.enter()
            time.sleep(1)
            voiceSynthesizer.hablar("mensaje enviado")
        
        elif (( "chat de" in vozUsuario) and modoPrueba): 
            aux = vozUsuario[vozUsuario.find("chat de")+7:]
            voiceSynthesizer.hablar("muy bien")
            controllers.buscarChat()
            time.sleep(1)
            voiceSynthesizer.hablar("dí el nombre del chat a buscar")
            vozUsuario1 = speechRecognition.reconocer("None").lower()
            controllers.escribir(vozUsuario1)
            time.sleep(1)
            controllers.enter()   
            voiceSynthesizer.hablar("este es el chat que encontre")


        elif (("ver foto" in vozUsuario) and modoPrueba):
            voiceSynthesizer.hablar("mostrando foto")
            controllers.Verfoto()        

        elif (("eliminar" in vozUsuario and "chat" in vozUsuario) and modoPrueba): 
            controllers.eliminarChat()
        
        elif (("borrar" in vozUsuario) and modoPrueba): 
            controllers.borrarTexto()

        elif(("llamar" in vozUsuario)and modoPrueba):
            voiceSynthesizer.hablar("se va a realizar una llamada")
            time.sleep(1)
            controllers.llamada()
        
        elif(("colgar" in vozUsuario)and modoPrueba):
            voiceSynthesizer.hablar("se va a colgar la llamada")
            time.sleep(1)
            controllers.colgarLLamada()
        
        elif(("video" in vozUsuario and "llamada")and modoPrueba):
            voiceSynthesizer.hablar("se va a realizar una video llamada")
            time.sleep(1)
            controllers.videoLLamada()
        
        elif(("finalizar video" in vozUsuario)and modoPrueba):
            voiceSynthesizer.hablar("se va a colgar la video llamada")
            time.sleep(1)
            controllers.colgarVideoLLamada()  
        
        elif(("archivar chat" in vozUsuario )and modoPrueba):
            voiceSynthesizer.hablar("se esta archivando el chat")
            time.sleep(1)
            controllers.archivarChat()
        
        elif(("crear grupo" in vozUsuario )and modoPrueba):
            voiceSynthesizer.hablar("se esta creando un grupo por favor selecione a los contactos que participaran")
            controllers.crearGrupo()

        elif(("silenciar chat" in vozUsuario )and modoPrueba):
            voiceSynthesizer.hablar("se va a silencair estes chat")
            time.sleep(1)
            controllers.silenciarChat()  
       
        elif(("marcar" in vozUsuario and "como leido" in vozUsuario)and modoPrueba):
            voiceSynthesizer.hablar("muy bien")
            time.sleep(1)
            controllers.marcarMensaje()
        
        elif(("desmarcar" in vozUsuario and "como leido" in vozUsuario)and modoPrueba):
            voiceSynthesizer.hablar("muy bien")
            time.sleep(1)
            controllers.marcarMensaje()
        
        elif(("nota de vo" in vozUsuario) and modoPrueba):
            voiceSynthesizer.hablar("se va a mandar un mensaje de voz")
            time.sleep(1)
            controllers.microfono()
        
        elif(( "enviar au"in vozUsuario ) and modoPrueba):
            controllers.microfono()
            time.sleep(1)
            voiceSynthesizer.hablar("se a enviado el audio")
        
        elif(("cancelar au" in vozUsuario or "cancelar audio" in vozUsuario) and modoPrueba):
            controllers.cancelarAudio()
            time.sleep(1)
            voiceSynthesizer.hablar("se cancelo el mensaje de voz")

        elif (("fijar chat" in vozUsuario) and modoPrueba):
            voiceSynthesizer.hablar("chat fijado")
            controllers.fijarChat() 

        elif (("desacer chat" in vozUsuario) and modoPrueba):
            voiceSynthesizer.hablar("se ha des fijado el chat")
            controllers.fijarChat()     

        elif (("cerrar" in vozUsuario and "whatsapp") and modoPrueba):
            voiceSynthesizer.hablar("cerrando whatsapp")
            controllers.cerrarVentana()
 

    except Exception as e:
        print("Ocurrio un error", e)
        continue

