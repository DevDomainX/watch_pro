#!/usr/bin/env python3
#created by : Hans saldias
import os as kay
from time import sleep as xpa

def python():
    kay.system('termux-open https://www.youtube.com/watch?v=G2FCfQj-9ig&list=PLU8oAlHdN5BlvPxziopYZRd55pdqFwkeS')

def android():
    kay.system('termux-open https://www.youtube.com/watch?v=pdYkmCcQFd8&list=PLU8oAlHdN5Bkn-KS1sRFlSEnXXcAtAJ9P')

def larabel():
    kay.system('termux-open https://www.youtube.com/watch?v=0sHSrqyZCnM&list=PLU8oAlHdN5Bk-qkvjER90g2c_jVmpAHBh')

def java():
    kay.system('termux-open https://www.youtube.com/watch?v=U709qY6S9rA&list=PLU8oAlHdN5BktAXdEVCLUYzvDyqRQJ2lk')

def php():
    kay.system('termux-open https://www.youtube.com/watch?v=U709qY6S9rA&list=PLU8oAlHdN5BktAXdEVCLUYzvDyqRQJ2lk')

def exel():
    kay.system('termux-open https://www.youtube.com/watch?v=XlCQGjcPIiA&list=PLU8oAlHdN5BkCs-P-AnQhxsSyxSxv9jfI')



if __name__ == '__main__':
    kay.system("clear")
    title = """
    =========================================================
    ||         Created by: 1LugarParaProgramar              ||
    ||                                                      ||
    ||         Author Script: Hans saldias                  ||
    ||                                                      ||
    || script para aprender a programar desde contenido     ||
    || gratis lo cual ase que este sea mas divertido.       ||
    || Este contenido contiene cursos completos de progra  -||
    || macion desde cero asta lo mas complejo desde ya      ||
    || comentar que desde este medio aprendi a programar    ||
    || desde estos mismos curso desde ya darle gracias a    ||
    ||        Don JUAN DIAS por su contenido                ||
    ||        "ya que sin el no ubiera podido"              ||
    ||                                                      ||
    || NOTA: descargo del contenido ya que no me pertenece  ||
    || solo lo automatize para su uso ya que es muy bueno   ||
    || pertenece a canal de youtube pildoras informaticas   ||
    ||     les dejo el link para su revision                || 
    ||  url:https://www.youtube.com/@pildorasinformaticas   ||
    ==========================================================

    $ 1  Curso desde cero python

    $ 2  Curso desde cero android

    $ 3 Curso desde cero laravel

    $ 4 Curso desde cero java

    $ 5 Curso desde cero exel 2010

    $ 00 salir...
    \n\n"""
    print(title)
    try:
        op = int(input("Ingrese opcion:"))
        if op == 1:
            python()
        elif op == 2:
            android()
        elif op == 3:
            larabel()
        elif op == 4:
            java()
        elif op == 5:
            php()
        elif op == 6:
            exel()
        elif op == 00:
            exit()
        else:
            print("opcion ingresa no valida, intente nuevamente")
    except ValueError:
        print("opcion no valida, intenta nuevamnte")            
